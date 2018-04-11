""" Cisco_IOS_XR_l2vpn_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR l2vpn package configuration.

This module contains definitions
for the following management objects\:
  l2vpn\: L2VPN configuration
  generic\-interface\-lists\: generic interface lists
  evpn\: evpn

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
modules with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BackupDisable(Enum):
    """
    BackupDisable (Enum Class)

    Backup disable

    .. data:: never = 0

    	Never

    .. data:: delay = 1

    	Delay seconds

    """

    never = Enum.YLeaf(0, "never")

    delay = Enum.YLeaf(1, "delay")


class BdmacLearn(Enum):
    """
    BdmacLearn (Enum Class)

    Bdmac learn

    .. data:: disable_learning = 2

    	Disable Learning

    """

    disable_learning = Enum.YLeaf(2, "disable-learning")


class BgpRouteDistinguisher(Enum):
    """
    BgpRouteDistinguisher (Enum Class)

    Bgp route distinguisher

    .. data:: auto = 1

    	RD automatically assigned

    .. data:: two_byte_as = 2

    	RD in 2 byte AS:nn format

    .. data:: four_byte_as = 3

    	RD in 4 byte AS:nn format

    .. data:: ipv4_address = 4

    	RD in IpV4address

    """

    auto = Enum.YLeaf(1, "auto")

    two_byte_as = Enum.YLeaf(2, "two-byte-as")

    four_byte_as = Enum.YLeaf(3, "four-byte-as")

    ipv4_address = Enum.YLeaf(4, "ipv4-address")


class BgpRouteTarget(Enum):
    """
    BgpRouteTarget (Enum Class)

    Bgp route target

    .. data:: no_stitching = 0

    	RT is default type

    .. data:: stitching = 1

    	RT is for stitching (Golf-L2)

    """

    no_stitching = Enum.YLeaf(0, "no-stitching")

    stitching = Enum.YLeaf(1, "stitching")


class BgpRouteTargetFormat(Enum):
    """
    BgpRouteTargetFormat (Enum Class)

    Bgp route target format

    .. data:: none = 0

    	No route target

    .. data:: two_byte_as = 1

    	2 Byte AS:nn format

    .. data:: four_byte_as = 2

    	4 byte AS:nn format

    .. data:: ipv4_address = 3

    	IP:nn format

    .. data:: es_import = 1538

    	a.a.i format

    """

    none = Enum.YLeaf(0, "none")

    two_byte_as = Enum.YLeaf(1, "two-byte-as")

    four_byte_as = Enum.YLeaf(2, "four-byte-as")

    ipv4_address = Enum.YLeaf(3, "ipv4-address")

    es_import = Enum.YLeaf(1538, "es-import")


class BgpRouteTargetRole(Enum):
    """
    BgpRouteTargetRole (Enum Class)

    Bgp route target role

    .. data:: both = 0

    	Both Import and export roles

    .. data:: import_ = 1

    	Import role

    .. data:: export = 2

    	Export role

    """

    both = Enum.YLeaf(0, "both")

    import_ = Enum.YLeaf(1, "import")

    export = Enum.YLeaf(2, "export")


class BridgeDomainTransportMode(Enum):
    """
    BridgeDomainTransportMode (Enum Class)

    Bridge domain transport mode

    .. data:: vlan_passthrough = 3

    	Vlan tagged passthrough mode

    """

    vlan_passthrough = Enum.YLeaf(3, "vlan-passthrough")


class ControlWord(Enum):
    """
    ControlWord (Enum Class)

    Control word

    .. data:: enable = 1

    	Enable control word

    .. data:: disable = 2

    	Disable control word

    """

    enable = Enum.YLeaf(1, "enable")

    disable = Enum.YLeaf(2, "disable")


class ErpPort(Enum):
    """
    ErpPort (Enum Class)

    Erp port

    .. data:: none = 1

    	ERP port type none

    .. data:: virtual = 2

    	ERP port type virtual

    .. data:: interface = 3

    	ERP port type interface

    """

    none = Enum.YLeaf(1, "none")

    virtual = Enum.YLeaf(2, "virtual")

    interface = Enum.YLeaf(3, "interface")


class ErpPort1(Enum):
    """
    ErpPort1 (Enum Class)

    Erp port1

    .. data:: port0 = 0

    	ERP main port 0

    .. data:: port1 = 1

    	ERP main port 1

    """

    port0 = Enum.YLeaf(0, "port0")

    port1 = Enum.YLeaf(1, "port1")


class Erpaps(Enum):
    """
    Erpaps (Enum Class)

    Erpaps

    .. data:: interface = 1

    	ERP APS type interface

    .. data:: bridge_domain = 2

    	ERP APS type bridge domain

    .. data:: xconnect = 3

    	ERP APS type xconnect

    .. data:: none = 4

    	ERP APS type none

    """

    interface = Enum.YLeaf(1, "interface")

    bridge_domain = Enum.YLeaf(2, "bridge-domain")

    xconnect = Enum.YLeaf(3, "xconnect")

    none = Enum.YLeaf(4, "none")


class EthernetSegmentIdentifier(Enum):
    """
    EthernetSegmentIdentifier (Enum Class)

    Ethernet segment identifier

    .. data:: type0 = 0

    	ESI type 0

    .. data:: legacy = 128

    	Legacy ESI type

    .. data:: override = 129

    	Override ESI type

    """

    type0 = Enum.YLeaf(0, "type0")

    legacy = Enum.YLeaf(128, "legacy")

    override = Enum.YLeaf(129, "override")


class EvpnEncapsulation(Enum):
    """
    EvpnEncapsulation (Enum Class)

    Evpn encapsulation

    .. data:: evpn_encapsulationvxlan = 8

    	VXLAN Encapsulation

    .. data:: evpn_encapsulation_mpls = 10

    	MPLS Encapsulation

    """

    evpn_encapsulationvxlan = Enum.YLeaf(8, "evpn-encapsulationvxlan")

    evpn_encapsulation_mpls = Enum.YLeaf(10, "evpn-encapsulation-mpls")


class EvpnSide(Enum):
    """
    EvpnSide (Enum Class)

    Evpn side

    .. data:: evpn_side_stitching = 2

    	EVPN Instance side defined as stitching

    """

    evpn_side_stitching = Enum.YLeaf(2, "evpn-side-stitching")


class FlowLabelLoadBalance(Enum):
    """
    FlowLabelLoadBalance (Enum Class)

    Flow label load balance

    .. data:: off = 0

    	Flow Label load balance is off

    .. data:: receive = 1

    	Delete Flow Label on receive side

    .. data:: transmit = 2

    	Insert Flow Label on transmit side

    .. data:: both = 3

    	Insert/Delete  Flow Label on transmit/receive

    	side

    """

    off = Enum.YLeaf(0, "off")

    receive = Enum.YLeaf(1, "receive")

    transmit = Enum.YLeaf(2, "transmit")

    both = Enum.YLeaf(3, "both")


class FlowLabelTlvCode(Enum):
    """
    FlowLabelTlvCode (Enum Class)

    Flow label tlv code

    .. data:: Y_17 = 4

    	Set Flow Label Legacy TLV code (DEPRECATED)

    .. data:: disable = 8

    	Disable Sending Flow Label Legacy TLV

    """

    Y_17 = Enum.YLeaf(4, "17")

    disable = Enum.YLeaf(8, "disable")


class InterfaceProfile(Enum):
    """
    InterfaceProfile (Enum Class)

    Interface profile

    .. data:: snoop = 1

    	Set the snooping

    .. data:: dhcp_protocol = 2

    	disable DHCP protocol

    """

    snoop = Enum.YLeaf(1, "snoop")

    dhcp_protocol = Enum.YLeaf(2, "dhcp-protocol")


class InterfaceTrafficFlood(Enum):
    """
    InterfaceTrafficFlood (Enum Class)

    Interface traffic flood

    .. data:: traffic_flooding = 0

    	Traffic flooding

    .. data:: enable_flooding = 1

    	Enable Flooding

    .. data:: disable_flooding = 2

    	Disable flooding

    """

    traffic_flooding = Enum.YLeaf(0, "traffic-flooding")

    enable_flooding = Enum.YLeaf(1, "enable-flooding")

    disable_flooding = Enum.YLeaf(2, "disable-flooding")


class Interworking(Enum):
    """
    Interworking (Enum Class)

    Interworking

    .. data:: ethernet = 1

    	Ethernet interworking

    .. data:: ipv4 = 3

    	IPv4 interworking

    """

    ethernet = Enum.YLeaf(1, "ethernet")

    ipv4 = Enum.YLeaf(3, "ipv4")


class L2Encapsulation(Enum):
    """
    L2Encapsulation (Enum Class)

    L2 encapsulation

    .. data:: vlan = 4

    	Vlan tagged mode

    .. data:: ethernet = 5

    	Ethernet port mode

    """

    vlan = Enum.YLeaf(4, "vlan")

    ethernet = Enum.YLeaf(5, "ethernet")


class L2tpCookieSize(Enum):
    """
    L2tpCookieSize (Enum Class)

    L2tp cookie size

    .. data:: zero = 0

    	Cookie size is zero bytes

    .. data:: four = 4

    	Cookie size is four bytes

    .. data:: eight = 8

    	Cookie size is eight bytes

    """

    zero = Enum.YLeaf(0, "zero")

    four = Enum.YLeaf(4, "four")

    eight = Enum.YLeaf(8, "eight")


class L2tpSignalingProtocol(Enum):
    """
    L2tpSignalingProtocol (Enum Class)

    L2tp signaling protocol

    .. data:: none = 1

    	No signaling

    .. data:: l2tpv3 = 2

    	L2TPv3

    """

    none = Enum.YLeaf(1, "none")

    l2tpv3 = Enum.YLeaf(2, "l2tpv3")


class L2tpv3Sequencing(Enum):
    """
    L2tpv3Sequencing (Enum Class)

    L2tpv3 sequencing

    .. data:: off = 0

    	Sequencing is off

    .. data:: both = 4

    	Sequencing on both transmit and receive side

    """

    off = Enum.YLeaf(0, "off")

    both = Enum.YLeaf(4, "both")


class L2vpnCapabilityMode(Enum):
    """
    L2vpnCapabilityMode (Enum Class)

    L2vpn capability mode

    .. data:: high_mode = 1

    	Compute global capability as the highest node

    	capability

    .. data:: single_mode = 2

    	Disable global capability re-computation

    """

    high_mode = Enum.YLeaf(1, "high-mode")

    single_mode = Enum.YLeaf(2, "single-mode")


class L2vpnLogging(Enum):
    """
    L2vpnLogging (Enum Class)

    L2vpn logging

    .. data:: enable = 1

    	enable logging

    .. data:: disable = 2

    	disable logging

    """

    enable = Enum.YLeaf(1, "enable")

    disable = Enum.YLeaf(2, "disable")


class L2vpnVerification(Enum):
    """
    L2vpnVerification (Enum Class)

    L2vpn verification

    .. data:: enable = 1

    	enable verification

    .. data:: disable = 2

    	disable verification

    """

    enable = Enum.YLeaf(1, "enable")

    disable = Enum.YLeaf(2, "disable")


class LdpVplsId(Enum):
    """
    LdpVplsId (Enum Class)

    Ldp vpls id

    .. data:: two_byte_as = 10

    	VPLS-ID in 2 byte AS:nn format

    .. data:: ipv4_address = 266

    	VPLS-ID in IPv4 IP:nn format

    """

    two_byte_as = Enum.YLeaf(10, "two-byte-as")

    ipv4_address = Enum.YLeaf(266, "ipv4-address")


class LoadBalance(Enum):
    """
    LoadBalance (Enum Class)

    Load balance

    .. data:: source_dest_mac = 1

    	Source and Destination MAC hashing

    .. data:: source_dest_ip = 2

    	Source and Destination IP hashing

    .. data:: pseudowire_label = 4

    	PW Label hashing

    """

    source_dest_mac = Enum.YLeaf(1, "source-dest-mac")

    source_dest_ip = Enum.YLeaf(2, "source-dest-ip")

    pseudowire_label = Enum.YLeaf(4, "pseudowire-label")


class MacAging(Enum):
    """
    MacAging (Enum Class)

    Mac aging

    .. data:: absolute = 1

    	Absolute aging type

    .. data:: inactivity = 2

    	Inactivity aging type

    """

    absolute = Enum.YLeaf(1, "absolute")

    inactivity = Enum.YLeaf(2, "inactivity")


class MacFlushMode(Enum):
    """
    MacFlushMode (Enum Class)

    Mac flush mode

    .. data:: mvrp = 1

    	MVRP MAC Flushing

    """

    mvrp = Enum.YLeaf(1, "mvrp")


class MacLearn(Enum):
    """
    MacLearn (Enum Class)

    Mac learn

    .. data:: default_learning = 0

    	Mac Learning

    .. data:: enable_learning = 1

    	Enable Learning

    .. data:: disable_learning = 2

    	Disable Learning

    """

    default_learning = Enum.YLeaf(0, "default-learning")

    enable_learning = Enum.YLeaf(1, "enable-learning")

    disable_learning = Enum.YLeaf(2, "disable-learning")


class MacLimitAction(Enum):
    """
    MacLimitAction (Enum Class)

    Mac limit action

    .. data:: none = 0

    	No action

    .. data:: flood = 1

    	Flood Mac Limit Action

    .. data:: no_flood = 2

    	NoFlood Mac Limit Action

    .. data:: shutdown = 3

    	Shutdown Mac Limit Action

    """

    none = Enum.YLeaf(0, "none")

    flood = Enum.YLeaf(1, "flood")

    no_flood = Enum.YLeaf(2, "no-flood")

    shutdown = Enum.YLeaf(3, "shutdown")


class MacNotification(Enum):
    """
    MacNotification (Enum Class)

    Mac notification

    .. data:: no_notif = 0

    	No_Notification Trap

    .. data:: syslog = 1

    	syslog message

    .. data:: trap = 2

    	Snmp Trap

    .. data:: syslog_snmp = 3

    	Syslog_snmp Trap

    """

    no_notif = Enum.YLeaf(0, "no-notif")

    syslog = Enum.YLeaf(1, "syslog")

    trap = Enum.YLeaf(2, "trap")

    syslog_snmp = Enum.YLeaf(3, "syslog-snmp")


class MacSecureAction(Enum):
    """
    MacSecureAction (Enum Class)

    Mac secure action

    .. data:: restrict = 1

    	MAC Secure Action Restrict

    .. data:: none = 2

    	No Action

    .. data:: shutdown = 3

    	MAC Secure Action Shutdown

    """

    restrict = Enum.YLeaf(1, "restrict")

    none = Enum.YLeaf(2, "none")

    shutdown = Enum.YLeaf(3, "shutdown")


class MacWithdrawBehavior(Enum):
    """
    MacWithdrawBehavior (Enum Class)

    Mac withdraw behavior

    .. data:: legacy = 1

    	MAC Withdrawal sent on state-down (legacy)

    .. data:: optimized = 2

    	Optimized MAC Withdrawal

    """

    legacy = Enum.YLeaf(1, "legacy")

    optimized = Enum.YLeaf(2, "optimized")


class MplsSequencing(Enum):
    """
    MplsSequencing (Enum Class)

    Mpls sequencing

    .. data:: off = 0

    	Sequencing is off

    .. data:: transmit = 1

    	Sequencing on transmit side

    .. data:: receive = 2

    	Sequencing on receive side

    .. data:: both = 4

    	Sequencing on both transmit and receive side

    """

    off = Enum.YLeaf(0, "off")

    transmit = Enum.YLeaf(1, "transmit")

    receive = Enum.YLeaf(2, "receive")

    both = Enum.YLeaf(4, "both")


class MplsSignalingProtocol(Enum):
    """
    MplsSignalingProtocol (Enum Class)

    Mpls signaling protocol

    .. data:: none = 1

    	No signaling

    .. data:: ldp = 4

    	LDP

    """

    none = Enum.YLeaf(1, "none")

    ldp = Enum.YLeaf(4, "ldp")


class PortDownFlush(Enum):
    """
    PortDownFlush (Enum Class)

    Port down flush

    .. data:: port_down_flush = 0

    	MAC Port Down Flush

    .. data:: enable_port_down_flush = 1

    	Enable Port Down Flush

    .. data:: disable_port_down_flush = 2

    	Disable Port Down Flush

    """

    port_down_flush = Enum.YLeaf(0, "port-down-flush")

    enable_port_down_flush = Enum.YLeaf(1, "enable-port-down-flush")

    disable_port_down_flush = Enum.YLeaf(2, "disable-port-down-flush")


class PreferredPath(Enum):
    """
    PreferredPath (Enum Class)

    Preferred path

    .. data:: te_tunnel = 2

    	TE Tunnel

    .. data:: ip_tunnel = 3

    	IP Tunnel

    .. data:: tp_tunnel = 4

    	TP Tunnel

    .. data:: sr_te_policy = 5

    	SR TE Policy

    """

    te_tunnel = Enum.YLeaf(2, "te-tunnel")

    ip_tunnel = Enum.YLeaf(3, "ip-tunnel")

    tp_tunnel = Enum.YLeaf(4, "tp-tunnel")

    sr_te_policy = Enum.YLeaf(5, "sr-te-policy")


class PwSwitchingPointTlv(Enum):
    """
    PwSwitchingPointTlv (Enum Class)

    Pw switching point tlv

    .. data:: hide = 2

    	Hide TLV

    """

    hide = Enum.YLeaf(2, "hide")


class RplRole(Enum):
    """
    RplRole (Enum Class)

    Rpl role

    .. data:: owner = 1

    	ERP RPL owner

    .. data:: neighbor = 2

    	ERP RPL neighbor

    .. data:: next_neighbor = 3

    	ERP RPL next neighbor

    """

    owner = Enum.YLeaf(1, "owner")

    neighbor = Enum.YLeaf(2, "neighbor")

    next_neighbor = Enum.YLeaf(3, "next-neighbor")


class StormControl(Enum):
    """
    StormControl (Enum Class)

    Storm control

    .. data:: unicast = 1

    	Unknown-unicast Storm Control

    .. data:: multicast = 2

    	Multicast Storm Control

    .. data:: broadcast = 4

    	Broadcast Storm Control

    """

    unicast = Enum.YLeaf(1, "unicast")

    multicast = Enum.YLeaf(2, "multicast")

    broadcast = Enum.YLeaf(4, "broadcast")


class TransportMode(Enum):
    """
    TransportMode (Enum Class)

    Transport mode

    .. data:: ethernet = 1

    	Ethernet port mode

    .. data:: vlan = 2

    	Vlan tagged mode

    .. data:: vlan_passthrough = 3

    	Vlan tagged passthrough mode

    """

    ethernet = Enum.YLeaf(1, "ethernet")

    vlan = Enum.YLeaf(2, "vlan")

    vlan_passthrough = Enum.YLeaf(3, "vlan-passthrough")


class TypeOfServiceMode(Enum):
    """
    TypeOfServiceMode (Enum Class)

    Type of service mode

    .. data:: none = 0

    	Do not reflect the type of service

    .. data:: reflect = 1

    	Reflect the type of service

    """

    none = Enum.YLeaf(0, "none")

    reflect = Enum.YLeaf(1, "reflect")


class VccvVerification(Enum):
    """
    VccvVerification (Enum Class)

    Vccv verification

    .. data:: none = 0

    	No connectivity verification over VCCV

    .. data:: lsp_ping = 2

    	LSP Ping over VCCV

    """

    none = Enum.YLeaf(0, "none")

    lsp_ping = Enum.YLeaf(2, "lsp-ping")



class L2Vpn(Entity):
    """
    L2VPN configuration
    
    .. attribute:: pw_routing
    
    	Pseudowire\-routing attributes
    	**type**\:  :py:class:`PwRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.PwRouting>`
    
    .. attribute:: neighbor
    
    	L2VPN neighbor submode
    	**type**\:  :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Neighbor>`
    
    .. attribute:: database
    
    	L2VPN databases
    	**type**\:  :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database>`
    
    .. attribute:: pbb
    
    	L2VPN PBB Global
    	**type**\:  :py:class:`Pbb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Pbb>`
    
    .. attribute:: auto_discovery
    
    	Global auto\-discovery attributes
    	**type**\:  :py:class:`AutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.AutoDiscovery>`
    
    .. attribute:: utility
    
    	L2VPN utilities
    	**type**\:  :py:class:`Utility <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Utility>`
    
    .. attribute:: snmp
    
    	SNMP related configuration
    	**type**\:  :py:class:`Snmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Snmp>`
    
    .. attribute:: nsr
    
    	Enable Non\-Stop Routing
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: mtu_mismatch_ignore
    
    	Ignore MTU Mismatch for XCs
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: tcn_propagation
    
    	Topology change notification propagation
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: pwoam_refresh
    
    	Configure PW OAM refresh interval
    	**type**\: int
    
    	**range:** 1..4095
    
    	**units**\: second
    
    .. attribute:: load_balance
    
    	Enable flow load balancing on l2vpn bridges
    	**type**\:  :py:class:`LoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.LoadBalance>`
    
    .. attribute:: mspw_description
    
    	MS\-PW global description
    	**type**\: str
    
    	**length:** 1..64
    
    .. attribute:: mac_limit_threshold
    
    	Configure MAC limit threshold percent
    	**type**\: int
    
    	**range:** 1..100
    
    	**units**\: percentage
    
    .. attribute:: pw_status_disable
    
    	Disable PW status
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: enable
    
    	Enable L2VPN feature
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: pw_grouping
    
    	Enable PW grouping
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: capability
    
    	L2VPN Capability Mode
    	**type**\:  :py:class:`L2vpnCapabilityMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnCapabilityMode>`
    
    .. attribute:: l2vpn_router_id
    
    	Global L2VPN Router ID
    	**type**\: str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    

    """

    _prefix = 'l2vpn-cfg'
    _revision = '2017-06-26'

    def __init__(self):
        super(L2Vpn, self).__init__()
        self._top_entity = None

        self.yang_name = "l2vpn"
        self.yang_parent_name = "Cisco-IOS-XR-l2vpn-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("pw-routing", ("pw_routing", L2Vpn.PwRouting)), ("neighbor", ("neighbor", L2Vpn.Neighbor)), ("database", ("database", L2Vpn.Database)), ("pbb", ("pbb", L2Vpn.Pbb)), ("auto-discovery", ("auto_discovery", L2Vpn.AutoDiscovery)), ("utility", ("utility", L2Vpn.Utility)), ("snmp", ("snmp", L2Vpn.Snmp))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('nsr', YLeaf(YType.empty, 'nsr')),
            ('mtu_mismatch_ignore', YLeaf(YType.empty, 'mtu-mismatch-ignore')),
            ('tcn_propagation', YLeaf(YType.empty, 'tcn-propagation')),
            ('pwoam_refresh', YLeaf(YType.uint32, 'pwoam-refresh')),
            ('load_balance', YLeaf(YType.enumeration, 'load-balance')),
            ('mspw_description', YLeaf(YType.str, 'mspw-description')),
            ('mac_limit_threshold', YLeaf(YType.uint32, 'mac-limit-threshold')),
            ('pw_status_disable', YLeaf(YType.empty, 'pw-status-disable')),
            ('enable', YLeaf(YType.empty, 'enable')),
            ('pw_grouping', YLeaf(YType.empty, 'pw-grouping')),
            ('capability', YLeaf(YType.enumeration, 'capability')),
            ('l2vpn_router_id', YLeaf(YType.str, 'l2vpn-router-id')),
        ])
        self.nsr = None
        self.mtu_mismatch_ignore = None
        self.tcn_propagation = None
        self.pwoam_refresh = None
        self.load_balance = None
        self.mspw_description = None
        self.mac_limit_threshold = None
        self.pw_status_disable = None
        self.enable = None
        self.pw_grouping = None
        self.capability = None
        self.l2vpn_router_id = None

        self.pw_routing = L2Vpn.PwRouting()
        self.pw_routing.parent = self
        self._children_name_map["pw_routing"] = "pw-routing"
        self._children_yang_names.add("pw-routing")

        self.neighbor = L2Vpn.Neighbor()
        self.neighbor.parent = self
        self._children_name_map["neighbor"] = "neighbor"
        self._children_yang_names.add("neighbor")

        self.database = L2Vpn.Database()
        self.database.parent = self
        self._children_name_map["database"] = "database"
        self._children_yang_names.add("database")

        self.pbb = L2Vpn.Pbb()
        self.pbb.parent = self
        self._children_name_map["pbb"] = "pbb"
        self._children_yang_names.add("pbb")

        self.auto_discovery = L2Vpn.AutoDiscovery()
        self.auto_discovery.parent = self
        self._children_name_map["auto_discovery"] = "auto-discovery"
        self._children_yang_names.add("auto-discovery")

        self.utility = L2Vpn.Utility()
        self.utility.parent = self
        self._children_name_map["utility"] = "utility"
        self._children_yang_names.add("utility")

        self.snmp = L2Vpn.Snmp()
        self.snmp.parent = self
        self._children_name_map["snmp"] = "snmp"
        self._children_yang_names.add("snmp")
        self._segment_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn"

    def __setattr__(self, name, value):
        self._perform_setattr(L2Vpn, ['nsr', 'mtu_mismatch_ignore', 'tcn_propagation', 'pwoam_refresh', 'load_balance', 'mspw_description', 'mac_limit_threshold', 'pw_status_disable', 'enable', 'pw_grouping', 'capability', 'l2vpn_router_id'], name, value)


    class PwRouting(Entity):
        """
        Pseudowire\-routing attributes
        
        .. attribute:: pw_routing_bgp
        
        	Enable Autodiscovery BGP Pseudowire\-routing BGP
        	**type**\:  :py:class:`PwRoutingBgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.PwRouting.PwRoutingBgp>`
        
        .. attribute:: pw_routing_global_id
        
        	Pseudowire\-routing Global ID
        	**type**\: int
        
        	**range:** 1..4294967295
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(L2Vpn.PwRouting, self).__init__()

            self.yang_name = "pw-routing"
            self.yang_parent_name = "l2vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("pw-routing-bgp", ("pw_routing_bgp", L2Vpn.PwRouting.PwRoutingBgp))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('pw_routing_global_id', YLeaf(YType.uint32, 'pw-routing-global-id')),
            ])
            self.pw_routing_global_id = None

            self.pw_routing_bgp = L2Vpn.PwRouting.PwRoutingBgp()
            self.pw_routing_bgp.parent = self
            self._children_name_map["pw_routing_bgp"] = "pw-routing-bgp"
            self._children_yang_names.add("pw-routing-bgp")
            self._segment_path = lambda: "pw-routing"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Vpn.PwRouting, ['pw_routing_global_id'], name, value)


        class PwRoutingBgp(Entity):
            """
            Enable Autodiscovery BGP Pseudowire\-routing BGP
            
            .. attribute:: enable
            
            	Enable Autodiscovery BGP
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: evpn_route_distinguisher
            
            	Route Distinguisher
            	**type**\:  :py:class:`EvpnRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.PwRouting.PwRoutingBgp, self).__init__()

                self.yang_name = "pw-routing-bgp"
                self.yang_parent_name = "pw-routing"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("evpn-route-distinguisher", ("evpn_route_distinguisher", L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', YLeaf(YType.empty, 'enable')),
                ])
                self.enable = None

                self.evpn_route_distinguisher = L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher()
                self.evpn_route_distinguisher.parent = self
                self._children_name_map["evpn_route_distinguisher"] = "evpn-route-distinguisher"
                self._children_yang_names.add("evpn-route-distinguisher")
                self._segment_path = lambda: "pw-routing-bgp"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/pw-routing/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.PwRouting.PwRoutingBgp, ['enable'], name, value)


            class EvpnRouteDistinguisher(Entity):
                """
                Route Distinguisher
                
                .. attribute:: type
                
                	Router Distinguisher Type
                	**type**\:  :py:class:`BgpRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher>`
                
                .. attribute:: as_
                
                	Two byte or 4 byte AS number
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: as_index
                
                	AS\:nn (hex or decimal format)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: address
                
                	IPV4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: addr_index
                
                	Addr index
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher, self).__init__()

                    self.yang_name = "evpn-route-distinguisher"
                    self.yang_parent_name = "pw-routing-bgp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', YLeaf(YType.enumeration, 'type')),
                        ('as_', YLeaf(YType.uint32, 'as')),
                        ('as_index', YLeaf(YType.uint32, 'as-index')),
                        ('address', YLeaf(YType.str, 'address')),
                        ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                    ])
                    self.type = None
                    self.as_ = None
                    self.as_index = None
                    self.address = None
                    self.addr_index = None
                    self._segment_path = lambda: "evpn-route-distinguisher"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/pw-routing/pw-routing-bgp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher, ['type', 'as_', 'as_index', 'address', 'addr_index'], name, value)


    class Neighbor(Entity):
        """
        L2VPN neighbor submode
        
        .. attribute:: ldp_flap
        
        	Enable targetted LDP session flap action
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(L2Vpn.Neighbor, self).__init__()

            self.yang_name = "neighbor"
            self.yang_parent_name = "l2vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ldp_flap', YLeaf(YType.empty, 'ldp-flap')),
            ])
            self.ldp_flap = None
            self._segment_path = lambda: "neighbor"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Vpn.Neighbor, ['ldp_flap'], name, value)


    class Database(Entity):
        """
        L2VPN databases
        
        .. attribute:: g8032_rings
        
        	List of G8032 Ring
        	**type**\:  :py:class:`G8032Rings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings>`
        
        .. attribute:: xconnect_groups
        
        	List of xconnect groups
        	**type**\:  :py:class:`XconnectGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups>`
        
        .. attribute:: bridge_domain_groups
        
        	List of bridge  groups
        	**type**\:  :py:class:`BridgeDomainGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups>`
        
        .. attribute:: pseudowire_classes
        
        	List of pseudowire classes
        	**type**\:  :py:class:`PseudowireClasses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses>`
        
        .. attribute:: flexible_xconnect_service_table
        
        	List of Flexible XConnect Services
        	**type**\:  :py:class:`FlexibleXconnectServiceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable>`
        
        .. attribute:: redundancy
        
        	Redundancy groups
        	**type**\:  :py:class:`Redundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.Redundancy>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(L2Vpn.Database, self).__init__()

            self.yang_name = "database"
            self.yang_parent_name = "l2vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("g8032-rings", ("g8032_rings", L2Vpn.Database.G8032Rings)), ("xconnect-groups", ("xconnect_groups", L2Vpn.Database.XconnectGroups)), ("bridge-domain-groups", ("bridge_domain_groups", L2Vpn.Database.BridgeDomainGroups)), ("pseudowire-classes", ("pseudowire_classes", L2Vpn.Database.PseudowireClasses)), ("flexible-xconnect-service-table", ("flexible_xconnect_service_table", L2Vpn.Database.FlexibleXconnectServiceTable)), ("redundancy", ("redundancy", L2Vpn.Database.Redundancy))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.g8032_rings = L2Vpn.Database.G8032Rings()
            self.g8032_rings.parent = self
            self._children_name_map["g8032_rings"] = "g8032-rings"
            self._children_yang_names.add("g8032-rings")

            self.xconnect_groups = L2Vpn.Database.XconnectGroups()
            self.xconnect_groups.parent = self
            self._children_name_map["xconnect_groups"] = "xconnect-groups"
            self._children_yang_names.add("xconnect-groups")

            self.bridge_domain_groups = L2Vpn.Database.BridgeDomainGroups()
            self.bridge_domain_groups.parent = self
            self._children_name_map["bridge_domain_groups"] = "bridge-domain-groups"
            self._children_yang_names.add("bridge-domain-groups")

            self.pseudowire_classes = L2Vpn.Database.PseudowireClasses()
            self.pseudowire_classes.parent = self
            self._children_name_map["pseudowire_classes"] = "pseudowire-classes"
            self._children_yang_names.add("pseudowire-classes")

            self.flexible_xconnect_service_table = L2Vpn.Database.FlexibleXconnectServiceTable()
            self.flexible_xconnect_service_table.parent = self
            self._children_name_map["flexible_xconnect_service_table"] = "flexible-xconnect-service-table"
            self._children_yang_names.add("flexible-xconnect-service-table")

            self.redundancy = L2Vpn.Database.Redundancy()
            self.redundancy.parent = self
            self._children_name_map["redundancy"] = "redundancy"
            self._children_yang_names.add("redundancy")
            self._segment_path = lambda: "database"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/%s" % self._segment_path()


        class G8032Rings(Entity):
            """
            List of G8032 Ring
            
            .. attribute:: g8032_ring
            
            	G8032 Ring
            	**type**\: list of  		 :py:class:`G8032Ring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Database.G8032Rings, self).__init__()

                self.yang_name = "g8032-rings"
                self.yang_parent_name = "database"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("g8032-ring", ("g8032_ring", L2Vpn.Database.G8032Rings.G8032Ring))])
                self._leafs = OrderedDict()

                self.g8032_ring = YList(self)
                self._segment_path = lambda: "g8032-rings"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.Database.G8032Rings, [], name, value)


            class G8032Ring(Entity):
                """
                G8032 Ring
                
                .. attribute:: g8032_ring_name  (key)
                
                	Name of the G8032 ring
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: erp_port0s
                
                	Ethernet ring protection port0
                	**type**\:  :py:class:`ErpPort0S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S>`
                
                .. attribute:: erp_instances
                
                	List of ethernet ring protection instance
                	**type**\:  :py:class:`ErpInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances>`
                
                .. attribute:: erp_port1s
                
                	Ethernet ring protection port0
                	**type**\:  :py:class:`ErpPort1S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S>`
                
                .. attribute:: open_ring
                
                	Specify the G.8032 instance as open ring
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: exclusion_list
                
                	Vlan IDs in the format of a\-b,c,d,e\-f,g ,untagged
                	**type**\: str
                
                .. attribute:: erp_provider_bridge
                
                	Ethernet ring protection provider bridge
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.G8032Rings.G8032Ring, self).__init__()

                    self.yang_name = "g8032-ring"
                    self.yang_parent_name = "g8032-rings"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['g8032_ring_name']
                    self._child_container_classes = OrderedDict([("erp-port0s", ("erp_port0s", L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S)), ("erp-instances", ("erp_instances", L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances)), ("erp-port1s", ("erp_port1s", L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('g8032_ring_name', YLeaf(YType.str, 'g8032-ring-name')),
                        ('open_ring', YLeaf(YType.empty, 'open-ring')),
                        ('exclusion_list', YLeaf(YType.str, 'exclusion-list')),
                        ('erp_provider_bridge', YLeaf(YType.empty, 'erp-provider-bridge')),
                    ])
                    self.g8032_ring_name = None
                    self.open_ring = None
                    self.exclusion_list = None
                    self.erp_provider_bridge = None

                    self.erp_port0s = L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S()
                    self.erp_port0s.parent = self
                    self._children_name_map["erp_port0s"] = "erp-port0s"
                    self._children_yang_names.add("erp-port0s")

                    self.erp_instances = L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances()
                    self.erp_instances.parent = self
                    self._children_name_map["erp_instances"] = "erp-instances"
                    self._children_yang_names.add("erp-instances")

                    self.erp_port1s = L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S()
                    self.erp_port1s.parent = self
                    self._children_name_map["erp_port1s"] = "erp-port1s"
                    self._children_yang_names.add("erp-port1s")
                    self._segment_path = lambda: "g8032-ring" + "[g8032-ring-name='" + str(self.g8032_ring_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/g8032-rings/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring, ['g8032_ring_name', 'open_ring', 'exclusion_list', 'erp_provider_bridge'], name, value)


                class ErpPort0S(Entity):
                    """
                    Ethernet ring protection port0
                    
                    .. attribute:: erp_port0
                    
                    	Configure ERP main port0
                    	**type**\: list of  		 :py:class:`ErpPort0 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S, self).__init__()

                        self.yang_name = "erp-port0s"
                        self.yang_parent_name = "g8032-ring"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("erp-port0", ("erp_port0", L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0))])
                        self._leafs = OrderedDict()

                        self.erp_port0 = YList(self)
                        self._segment_path = lambda: "erp-port0s"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S, [], name, value)


                    class ErpPort0(Entity):
                        """
                        Configure ERP main port0
                        
                        .. attribute:: interface_name  (key)
                        
                        	Port0 interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: monitor
                        
                        	Ethernet ring protection port0 monitor
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0, self).__init__()

                            self.yang_name = "erp-port0"
                            self.yang_parent_name = "erp-port0s"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ('monitor', YLeaf(YType.str, 'monitor')),
                            ])
                            self.interface_name = None
                            self.monitor = None
                            self._segment_path = lambda: "erp-port0" + "[interface-name='" + str(self.interface_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0, ['interface_name', 'monitor'], name, value)


                class ErpInstances(Entity):
                    """
                    List of ethernet ring protection instance
                    
                    .. attribute:: erp_instance
                    
                    	Ethernet ring protection instance
                    	**type**\: list of  		 :py:class:`ErpInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances, self).__init__()

                        self.yang_name = "erp-instances"
                        self.yang_parent_name = "g8032-ring"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("erp-instance", ("erp_instance", L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance))])
                        self._leafs = OrderedDict()

                        self.erp_instance = YList(self)
                        self._segment_path = lambda: "erp-instances"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances, [], name, value)


                    class ErpInstance(Entity):
                        """
                        Ethernet ring protection instance
                        
                        .. attribute:: erp_instance_id  (key)
                        
                        	ERP instance number
                        	**type**\: int
                        
                        	**range:** 1..2
                        
                        .. attribute:: rpl
                        
                        	Ring protection link
                        	**type**\:  :py:class:`Rpl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl>`
                        
                        .. attribute:: aps
                        
                        	Automatic protection switching
                        	**type**\:  :py:class:`Aps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps>`
                        
                        .. attribute:: description
                        
                        	Ethernet ring protection instance description
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: inclusion_list
                        
                        	Associates a set of VLAN IDs with the G .8032 instance
                        	**type**\: str
                        
                        .. attribute:: profile
                        
                        	Ethernet ring protection instance profile
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance, self).__init__()

                            self.yang_name = "erp-instance"
                            self.yang_parent_name = "erp-instances"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['erp_instance_id']
                            self._child_container_classes = OrderedDict([("rpl", ("rpl", L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl)), ("aps", ("aps", L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('erp_instance_id', YLeaf(YType.uint32, 'erp-instance-id')),
                                ('description', YLeaf(YType.str, 'description')),
                                ('inclusion_list', YLeaf(YType.str, 'inclusion-list')),
                                ('profile', YLeaf(YType.str, 'profile')),
                            ])
                            self.erp_instance_id = None
                            self.description = None
                            self.inclusion_list = None
                            self.profile = None

                            self.rpl = L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl()
                            self.rpl.parent = self
                            self._children_name_map["rpl"] = "rpl"
                            self._children_yang_names.add("rpl")

                            self.aps = L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps()
                            self.aps.parent = self
                            self._children_name_map["aps"] = "aps"
                            self._children_yang_names.add("aps")
                            self._segment_path = lambda: "erp-instance" + "[erp-instance-id='" + str(self.erp_instance_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance, ['erp_instance_id', 'description', 'inclusion_list', 'profile'], name, value)


                        class Rpl(Entity):
                            """
                            Ring protection link
                            
                            .. attribute:: port
                            
                            	ERP main port number
                            	**type**\:  :py:class:`ErpPort1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.ErpPort1>`
                            
                            .. attribute:: role
                            
                            	RPL role
                            	**type**\:  :py:class:`RplRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.RplRole>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl, self).__init__()

                                self.yang_name = "rpl"
                                self.yang_parent_name = "erp-instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('port', YLeaf(YType.enumeration, 'port')),
                                    ('role', YLeaf(YType.enumeration, 'role')),
                                ])
                                self.port = None
                                self.role = None
                                self._segment_path = lambda: "rpl"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl, ['port', 'role'], name, value)


                        class Aps(Entity):
                            """
                            Automatic protection switching
                            
                            .. attribute:: port1
                            
                            	APS channel for ERP port1
                            	**type**\:  :py:class:`Port1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1>`
                            
                            .. attribute:: port0
                            
                            	Port0 APS channel in the format of InterfaceName
                            	**type**\: str
                            
                            .. attribute:: enable
                            
                            	Enable automatic protection switching
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: level
                            
                            	Automatic protection switching level
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps, self).__init__()

                                self.yang_name = "aps"
                                self.yang_parent_name = "erp-instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("port1", ("port1", L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('port0', YLeaf(YType.str, 'port0')),
                                    ('enable', YLeaf(YType.empty, 'enable')),
                                    ('level', YLeaf(YType.uint32, 'level')),
                                ])
                                self.port0 = None
                                self.enable = None
                                self.level = None

                                self.port1 = L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1()
                                self.port1.parent = self
                                self._children_name_map["port1"] = "port1"
                                self._children_yang_names.add("port1")
                                self._segment_path = lambda: "aps"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps, ['port0', 'enable', 'level'], name, value)


                            class Port1(Entity):
                                """
                                APS channel for ERP port1
                                
                                .. attribute:: aps_type
                                
                                	Port1 APS type
                                	**type**\:  :py:class:`Erpaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Erpaps>`
                                
                                .. attribute:: aps_channel
                                
                                	Port1 APS channel in the format of InterfaceName, BDName or XconnectName
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1, self).__init__()

                                    self.yang_name = "port1"
                                    self.yang_parent_name = "aps"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('aps_type', YLeaf(YType.enumeration, 'aps-type')),
                                        ('aps_channel', YLeaf(YType.str, 'aps-channel')),
                                    ])
                                    self.aps_type = None
                                    self.aps_channel = None
                                    self._segment_path = lambda: "port1"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1, ['aps_type', 'aps_channel'], name, value)


                class ErpPort1S(Entity):
                    """
                    Ethernet ring protection port0
                    
                    .. attribute:: erp_port1
                    
                    	Ethernet ring protection port1
                    	**type**\: list of  		 :py:class:`ErpPort1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S, self).__init__()

                        self.yang_name = "erp-port1s"
                        self.yang_parent_name = "g8032-ring"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("erp-port1", ("erp_port1", L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1))])
                        self._leafs = OrderedDict()

                        self.erp_port1 = YList(self)
                        self._segment_path = lambda: "erp-port1s"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S, [], name, value)


                    class ErpPort1(Entity):
                        """
                        Ethernet ring protection port1
                        
                        .. attribute:: erp_port_type  (key)
                        
                        	Port1 type
                        	**type**\:  :py:class:`ErpPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.ErpPort>`
                        
                        .. attribute:: none_or_virtual
                        
                        	none or virtual
                        	**type**\:  :py:class:`NoneOrVirtual <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: interface
                        
                        	interface
                        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1, self).__init__()

                            self.yang_name = "erp-port1"
                            self.yang_parent_name = "erp-port1s"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['erp_port_type']
                            self._child_container_classes = OrderedDict([("none-or-virtual", ("none_or_virtual", L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual))])
                            self._child_list_classes = OrderedDict([("interface", ("interface", L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface))])
                            self._leafs = OrderedDict([
                                ('erp_port_type', YLeaf(YType.enumeration, 'erp-port-type')),
                            ])
                            self.erp_port_type = None

                            self.none_or_virtual = None
                            self._children_name_map["none_or_virtual"] = "none-or-virtual"
                            self._children_yang_names.add("none-or-virtual")

                            self.interface = YList(self)
                            self._segment_path = lambda: "erp-port1" + "[erp-port-type='" + str(self.erp_port_type) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1, ['erp_port_type'], name, value)


                        class NoneOrVirtual(Entity):
                            """
                            none or virtual
                            
                            .. attribute:: monitor
                            
                            	Ethernet ring protection port1 monitor
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual, self).__init__()

                                self.yang_name = "none-or-virtual"
                                self.yang_parent_name = "erp-port1"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('monitor', YLeaf(YType.str, 'monitor')),
                                ])
                                self.monitor = None
                                self._segment_path = lambda: "none-or-virtual"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual, ['monitor'], name, value)


                        class Interface(Entity):
                            """
                            interface
                            
                            .. attribute:: interface_name  (key)
                            
                            	Port1 interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: monitor
                            
                            	Ethernet ring protection port1 monitor
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "erp-port1"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('monitor', YLeaf(YType.str, 'monitor')),
                                ])
                                self.interface_name = None
                                self.monitor = None
                                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface, ['interface_name', 'monitor'], name, value)


        class XconnectGroups(Entity):
            """
            List of xconnect groups
            
            .. attribute:: xconnect_group
            
            	Xconnect group
            	**type**\: list of  		 :py:class:`XconnectGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Database.XconnectGroups, self).__init__()

                self.yang_name = "xconnect-groups"
                self.yang_parent_name = "database"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("xconnect-group", ("xconnect_group", L2Vpn.Database.XconnectGroups.XconnectGroup))])
                self._leafs = OrderedDict()

                self.xconnect_group = YList(self)
                self._segment_path = lambda: "xconnect-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.Database.XconnectGroups, [], name, value)


            class XconnectGroup(Entity):
                """
                Xconnect group
                
                .. attribute:: name  (key)
                
                	Name of the xconnect group
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: p2p_xconnects
                
                	List of point to point xconnects
                	**type**\:  :py:class:`P2PXconnects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects>`
                
                .. attribute:: mp2mp_xconnects
                
                	List of multi point to multi point xconnects
                	**type**\:  :py:class:`Mp2MpXconnects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.XconnectGroups.XconnectGroup, self).__init__()

                    self.yang_name = "xconnect-group"
                    self.yang_parent_name = "xconnect-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([("p2p-xconnects", ("p2p_xconnects", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects)), ("mp2mp-xconnects", ("mp2mp_xconnects", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                    ])
                    self.name = None

                    self.p2p_xconnects = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects()
                    self.p2p_xconnects.parent = self
                    self._children_name_map["p2p_xconnects"] = "p2p-xconnects"
                    self._children_yang_names.add("p2p-xconnects")

                    self.mp2mp_xconnects = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects()
                    self.mp2mp_xconnects.parent = self
                    self._children_name_map["mp2mp_xconnects"] = "mp2mp-xconnects"
                    self._children_yang_names.add("mp2mp-xconnects")
                    self._segment_path = lambda: "xconnect-group" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/xconnect-groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup, ['name'], name, value)


                class P2PXconnects(Entity):
                    """
                    List of point to point xconnects
                    
                    .. attribute:: p2p_xconnect
                    
                    	Point to point xconnect
                    	**type**\: list of  		 :py:class:`P2PXconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects, self).__init__()

                        self.yang_name = "p2p-xconnects"
                        self.yang_parent_name = "xconnect-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("p2p-xconnect", ("p2p_xconnect", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect))])
                        self._leafs = OrderedDict()

                        self.p2p_xconnect = YList(self)
                        self._segment_path = lambda: "p2p-xconnects"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects, [], name, value)


                    class P2PXconnect(Entity):
                        """
                        Point to point xconnect
                        
                        .. attribute:: name  (key)
                        
                        	Name of the point to point xconnect
                        	**type**\: str
                        
                        	**length:** 1..38
                        
                        .. attribute:: backup_attachment_circuits
                        
                        	List of backup attachment circuits
                        	**type**\:  :py:class:`BackupAttachmentCircuits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits>`
                        
                        .. attribute:: pseudowire_evpns
                        
                        	List of EVPN Services
                        	**type**\:  :py:class:`PseudowireEvpns <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns>`
                        
                        .. attribute:: pseudowires
                        
                        	List of pseudowires
                        	**type**\:  :py:class:`Pseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires>`
                        
                        .. attribute:: monitor_sessions
                        
                        	List of Monitor session segments
                        	**type**\:  :py:class:`MonitorSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions>`
                        
                        .. attribute:: pseudowire_routeds
                        
                        	List of pseudowire\-routed
                        	**type**\:  :py:class:`PseudowireRouteds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds>`
                        
                        .. attribute:: attachment_circuits
                        
                        	List of attachment circuits
                        	**type**\:  :py:class:`AttachmentCircuits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits>`
                        
                        .. attribute:: p2p_description
                        
                        	cross connect description Name
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: interworking
                        
                        	Interworking
                        	**type**\:  :py:class:`Interworking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Interworking>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect, self).__init__()

                            self.yang_name = "p2p-xconnect"
                            self.yang_parent_name = "p2p-xconnects"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_container_classes = OrderedDict([("backup-attachment-circuits", ("backup_attachment_circuits", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits)), ("pseudowire-evpns", ("pseudowire_evpns", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns)), ("pseudowires", ("pseudowires", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires)), ("monitor-sessions", ("monitor_sessions", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions)), ("pseudowire-routeds", ("pseudowire_routeds", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds)), ("attachment-circuits", ("attachment_circuits", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', YLeaf(YType.str, 'name')),
                                ('p2p_description', YLeaf(YType.str, 'p2p-description')),
                                ('interworking', YLeaf(YType.enumeration, 'interworking')),
                            ])
                            self.name = None
                            self.p2p_description = None
                            self.interworking = None

                            self.backup_attachment_circuits = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits()
                            self.backup_attachment_circuits.parent = self
                            self._children_name_map["backup_attachment_circuits"] = "backup-attachment-circuits"
                            self._children_yang_names.add("backup-attachment-circuits")

                            self.pseudowire_evpns = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns()
                            self.pseudowire_evpns.parent = self
                            self._children_name_map["pseudowire_evpns"] = "pseudowire-evpns"
                            self._children_yang_names.add("pseudowire-evpns")

                            self.pseudowires = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires()
                            self.pseudowires.parent = self
                            self._children_name_map["pseudowires"] = "pseudowires"
                            self._children_yang_names.add("pseudowires")

                            self.monitor_sessions = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions()
                            self.monitor_sessions.parent = self
                            self._children_name_map["monitor_sessions"] = "monitor-sessions"
                            self._children_yang_names.add("monitor-sessions")

                            self.pseudowire_routeds = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds()
                            self.pseudowire_routeds.parent = self
                            self._children_name_map["pseudowire_routeds"] = "pseudowire-routeds"
                            self._children_yang_names.add("pseudowire-routeds")

                            self.attachment_circuits = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits()
                            self.attachment_circuits.parent = self
                            self._children_name_map["attachment_circuits"] = "attachment-circuits"
                            self._children_yang_names.add("attachment-circuits")
                            self._segment_path = lambda: "p2p-xconnect" + "[name='" + str(self.name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect, ['name', 'p2p_description', 'interworking'], name, value)


                        class BackupAttachmentCircuits(Entity):
                            """
                            List of backup attachment circuits
                            
                            .. attribute:: backup_attachment_circuit
                            
                            	Backup attachment circuit
                            	**type**\: list of  		 :py:class:`BackupAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits, self).__init__()

                                self.yang_name = "backup-attachment-circuits"
                                self.yang_parent_name = "p2p-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("backup-attachment-circuit", ("backup_attachment_circuit", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit))])
                                self._leafs = OrderedDict()

                                self.backup_attachment_circuit = YList(self)
                                self._segment_path = lambda: "backup-attachment-circuits"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits, [], name, value)


                            class BackupAttachmentCircuit(Entity):
                                """
                                Backup attachment circuit
                                
                                .. attribute:: interface_name  (key)
                                
                                	Name of the attachment circuit interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit, self).__init__()

                                    self.yang_name = "backup-attachment-circuit"
                                    self.yang_parent_name = "backup-attachment-circuits"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ])
                                    self.interface_name = None
                                    self._segment_path = lambda: "backup-attachment-circuit" + "[interface-name='" + str(self.interface_name) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit, ['interface_name'], name, value)


                        class PseudowireEvpns(Entity):
                            """
                            List of EVPN Services
                            
                            .. attribute:: pseudowire_evpn
                            
                            	EVPN P2P Service Configuration
                            	**type**\: list of  		 :py:class:`PseudowireEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns, self).__init__()

                                self.yang_name = "pseudowire-evpns"
                                self.yang_parent_name = "p2p-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("pseudowire-evpn", ("pseudowire_evpn", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn))])
                                self._leafs = OrderedDict()

                                self.pseudowire_evpn = YList(self)
                                self._segment_path = lambda: "pseudowire-evpns"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns, [], name, value)


                            class PseudowireEvpn(Entity):
                                """
                                EVPN P2P Service Configuration
                                
                                .. attribute:: eviid  (key)
                                
                                	Ethernet VPN ID
                                	**type**\: int
                                
                                	**range:** 1..65534
                                
                                .. attribute:: remote_acid  (key)
                                
                                	Remote AC ID
                                	**type**\: int
                                
                                	**range:** 1..16777215
                                
                                .. attribute:: source_acid  (key)
                                
                                	Source AC ID
                                	**type**\: int
                                
                                	**range:** 1..16777215
                                
                                .. attribute:: class_
                                
                                	Name of the pseudowire class
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn, self).__init__()

                                    self.yang_name = "pseudowire-evpn"
                                    self.yang_parent_name = "pseudowire-evpns"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['eviid','remote_acid','source_acid']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('eviid', YLeaf(YType.uint32, 'eviid')),
                                        ('remote_acid', YLeaf(YType.uint32, 'remote-acid')),
                                        ('source_acid', YLeaf(YType.uint32, 'source-acid')),
                                        ('class_', YLeaf(YType.str, 'class')),
                                    ])
                                    self.eviid = None
                                    self.remote_acid = None
                                    self.source_acid = None
                                    self.class_ = None
                                    self._segment_path = lambda: "pseudowire-evpn" + "[eviid='" + str(self.eviid) + "']" + "[remote-acid='" + str(self.remote_acid) + "']" + "[source-acid='" + str(self.source_acid) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn, ['eviid', 'remote_acid', 'source_acid', 'class_'], name, value)


                        class Pseudowires(Entity):
                            """
                            List of pseudowires
                            
                            .. attribute:: pseudowire
                            
                            	Pseudowire configuration
                            	**type**\: list of  		 :py:class:`Pseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires, self).__init__()

                                self.yang_name = "pseudowires"
                                self.yang_parent_name = "p2p-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("pseudowire", ("pseudowire", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire))])
                                self._leafs = OrderedDict()

                                self.pseudowire = YList(self)
                                self._segment_path = lambda: "pseudowires"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires, [], name, value)


                            class Pseudowire(Entity):
                                """
                                Pseudowire configuration
                                
                                .. attribute:: pseudowire_id  (key)
                                
                                	Pseudowire ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: neighbor
                                
                                	keys\: neighbor
                                	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor>`
                                
                                .. attribute:: pseudowire_address
                                
                                	keys\: pseudowire\-address
                                	**type**\: list of  		 :py:class:`PseudowireAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire, self).__init__()

                                    self.yang_name = "pseudowire"
                                    self.yang_parent_name = "pseudowires"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['pseudowire_id']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("neighbor", ("neighbor", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor)), ("pseudowire-address", ("pseudowire_address", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress))])
                                    self._leafs = OrderedDict([
                                        ('pseudowire_id', YLeaf(YType.uint32, 'pseudowire-id')),
                                    ])
                                    self.pseudowire_id = None

                                    self.neighbor = YList(self)
                                    self.pseudowire_address = YList(self)
                                    self._segment_path = lambda: "pseudowire" + "[pseudowire-id='" + str(self.pseudowire_id) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire, ['pseudowire_id'], name, value)


                                class Neighbor(Entity):
                                    """
                                    keys\: neighbor
                                    
                                    .. attribute:: neighbor  (key)
                                    
                                    	Pseudowire IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: mpls_static_labels
                                    
                                    	MPLS static labels
                                    	**type**\:  :py:class:`MplsStaticLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels>`
                                    
                                    .. attribute:: backup_pseudowires
                                    
                                    	List of pseudowires
                                    	**type**\:  :py:class:`BackupPseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires>`
                                    
                                    .. attribute:: l2tp_static_attributes
                                    
                                    	L2TP Static Attributes
                                    	**type**\:  :py:class:`L2TpStaticAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes>`
                                    
                                    .. attribute:: l2tp_static
                                    
                                    	Pseudowire L2TPv3 static configuration
                                    	**type**\:  :py:class:`L2TpStatic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic>`
                                    
                                    .. attribute:: tag_impose
                                    
                                    	Tag Impose vlan tagged mode
                                    	**type**\: int
                                    
                                    	**range:** 1..4094
                                    
                                    .. attribute:: class_
                                    
                                    	Name of the pseudowire class
                                    	**type**\: str
                                    
                                    	**length:** 1..32
                                    
                                    .. attribute:: source_address
                                    
                                    	Value of the Pseudowire source address. Must be IPv6 only
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: bandwidth
                                    
                                    	Pseudowire Bandwidth
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor, self).__init__()

                                        self.yang_name = "neighbor"
                                        self.yang_parent_name = "pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['neighbor']
                                        self._child_container_classes = OrderedDict([("mpls-static-labels", ("mpls_static_labels", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels)), ("backup-pseudowires", ("backup_pseudowires", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires)), ("l2tp-static-attributes", ("l2tp_static_attributes", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes)), ("l2tp-static", ("l2tp_static", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('neighbor', YLeaf(YType.str, 'neighbor')),
                                            ('tag_impose', YLeaf(YType.uint32, 'tag-impose')),
                                            ('class_', YLeaf(YType.str, 'class')),
                                            ('source_address', YLeaf(YType.str, 'source-address')),
                                            ('bandwidth', YLeaf(YType.uint32, 'bandwidth')),
                                        ])
                                        self.neighbor = None
                                        self.tag_impose = None
                                        self.class_ = None
                                        self.source_address = None
                                        self.bandwidth = None

                                        self.mpls_static_labels = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels()
                                        self.mpls_static_labels.parent = self
                                        self._children_name_map["mpls_static_labels"] = "mpls-static-labels"
                                        self._children_yang_names.add("mpls-static-labels")

                                        self.backup_pseudowires = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires()
                                        self.backup_pseudowires.parent = self
                                        self._children_name_map["backup_pseudowires"] = "backup-pseudowires"
                                        self._children_yang_names.add("backup-pseudowires")

                                        self.l2tp_static_attributes = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes()
                                        self.l2tp_static_attributes.parent = self
                                        self._children_name_map["l2tp_static_attributes"] = "l2tp-static-attributes"
                                        self._children_yang_names.add("l2tp-static-attributes")

                                        self.l2tp_static = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic()
                                        self.l2tp_static.parent = self
                                        self._children_name_map["l2tp_static"] = "l2tp-static"
                                        self._children_yang_names.add("l2tp-static")
                                        self._segment_path = lambda: "neighbor" + "[neighbor='" + str(self.neighbor) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor, ['neighbor', 'tag_impose', 'class_', 'source_address', 'bandwidth'], name, value)


                                    class MplsStaticLabels(Entity):
                                        """
                                        MPLS static labels
                                        
                                        .. attribute:: local_static_label
                                        
                                        	Pseudowire local static label
                                        	**type**\: int
                                        
                                        	**range:** 16..1048575
                                        
                                        .. attribute:: remote_static_label
                                        
                                        	Pseudowire remote static label
                                        	**type**\: int
                                        
                                        	**range:** 16..1048575
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels, self).__init__()

                                            self.yang_name = "mpls-static-labels"
                                            self.yang_parent_name = "neighbor"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('local_static_label', YLeaf(YType.uint32, 'local-static-label')),
                                                ('remote_static_label', YLeaf(YType.uint32, 'remote-static-label')),
                                            ])
                                            self.local_static_label = None
                                            self.remote_static_label = None
                                            self._segment_path = lambda: "mpls-static-labels"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels, ['local_static_label', 'remote_static_label'], name, value)


                                    class BackupPseudowires(Entity):
                                        """
                                        List of pseudowires
                                        
                                        .. attribute:: backup_pseudowire
                                        
                                        	Backup pseudowire for the cross connect
                                        	**type**\: list of  		 :py:class:`BackupPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires, self).__init__()

                                            self.yang_name = "backup-pseudowires"
                                            self.yang_parent_name = "neighbor"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("backup-pseudowire", ("backup_pseudowire", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire))])
                                            self._leafs = OrderedDict()

                                            self.backup_pseudowire = YList(self)
                                            self._segment_path = lambda: "backup-pseudowires"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires, [], name, value)


                                        class BackupPseudowire(Entity):
                                            """
                                            Backup pseudowire for the cross connect
                                            
                                            .. attribute:: neighbor  (key)
                                            
                                            	Neighbor IP address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: pseudowire_id  (key)
                                            
                                            	Pseudowire ID
                                            	**type**\: int
                                            
                                            	**range:** 1..4294967295
                                            
                                            .. attribute:: backup_mpls_static_labels
                                            
                                            	MPLS static labels
                                            	**type**\:  :py:class:`BackupMplsStaticLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels>`
                                            
                                            .. attribute:: backup_pw_class
                                            
                                            	PW class template name to use for the backup PW
                                            	**type**\: str
                                            
                                            	**length:** 1..32
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire, self).__init__()

                                                self.yang_name = "backup-pseudowire"
                                                self.yang_parent_name = "backup-pseudowires"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['neighbor','pseudowire_id']
                                                self._child_container_classes = OrderedDict([("backup-mpls-static-labels", ("backup_mpls_static_labels", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('neighbor', YLeaf(YType.str, 'neighbor')),
                                                    ('pseudowire_id', YLeaf(YType.uint32, 'pseudowire-id')),
                                                    ('backup_pw_class', YLeaf(YType.str, 'backup-pw-class')),
                                                ])
                                                self.neighbor = None
                                                self.pseudowire_id = None
                                                self.backup_pw_class = None

                                                self.backup_mpls_static_labels = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels()
                                                self.backup_mpls_static_labels.parent = self
                                                self._children_name_map["backup_mpls_static_labels"] = "backup-mpls-static-labels"
                                                self._children_yang_names.add("backup-mpls-static-labels")
                                                self._segment_path = lambda: "backup-pseudowire" + "[neighbor='" + str(self.neighbor) + "']" + "[pseudowire-id='" + str(self.pseudowire_id) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire, ['neighbor', 'pseudowire_id', 'backup_pw_class'], name, value)


                                            class BackupMplsStaticLabels(Entity):
                                                """
                                                MPLS static labels
                                                
                                                .. attribute:: local_static_label
                                                
                                                	Pseudowire local static label
                                                	**type**\: int
                                                
                                                	**range:** 16..1048575
                                                
                                                .. attribute:: remote_static_label
                                                
                                                	Pseudowire remote static label
                                                	**type**\: int
                                                
                                                	**range:** 16..1048575
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2017-06-26'

                                                def __init__(self):
                                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels, self).__init__()

                                                    self.yang_name = "backup-mpls-static-labels"
                                                    self.yang_parent_name = "backup-pseudowire"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('local_static_label', YLeaf(YType.uint32, 'local-static-label')),
                                                        ('remote_static_label', YLeaf(YType.uint32, 'remote-static-label')),
                                                    ])
                                                    self.local_static_label = None
                                                    self.remote_static_label = None
                                                    self._segment_path = lambda: "backup-mpls-static-labels"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels, ['local_static_label', 'remote_static_label'], name, value)


                                    class L2TpStaticAttributes(Entity):
                                        """
                                        L2TP Static Attributes
                                        
                                        .. attribute:: l2tp_remote_cookie
                                        
                                        	L2TP remote cookie
                                        	**type**\:  :py:class:`L2TpRemoteCookie <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie>`
                                        
                                        .. attribute:: l2tp_secondary_local_cookie
                                        
                                        	L2TP secondary local cookie
                                        	**type**\:  :py:class:`L2TpSecondaryLocalCookie <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie>`
                                        
                                        .. attribute:: l2tp_local_cookie
                                        
                                        	L2TP local cookie
                                        	**type**\:  :py:class:`L2TpLocalCookie <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie>`
                                        
                                        .. attribute:: l2tp_remote_session_id
                                        
                                        	L2TP remote session ID
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: l2tp_local_session_id
                                        
                                        	L2TP local session ID
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes, self).__init__()

                                            self.yang_name = "l2tp-static-attributes"
                                            self.yang_parent_name = "neighbor"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("l2tp-remote-cookie", ("l2tp_remote_cookie", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie)), ("l2tp-secondary-local-cookie", ("l2tp_secondary_local_cookie", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie)), ("l2tp-local-cookie", ("l2tp_local_cookie", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('l2tp_remote_session_id', YLeaf(YType.uint32, 'l2tp-remote-session-id')),
                                                ('l2tp_local_session_id', YLeaf(YType.uint32, 'l2tp-local-session-id')),
                                            ])
                                            self.l2tp_remote_session_id = None
                                            self.l2tp_local_session_id = None

                                            self.l2tp_remote_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie()
                                            self.l2tp_remote_cookie.parent = self
                                            self._children_name_map["l2tp_remote_cookie"] = "l2tp-remote-cookie"
                                            self._children_yang_names.add("l2tp-remote-cookie")

                                            self.l2tp_secondary_local_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie()
                                            self.l2tp_secondary_local_cookie.parent = self
                                            self._children_name_map["l2tp_secondary_local_cookie"] = "l2tp-secondary-local-cookie"
                                            self._children_yang_names.add("l2tp-secondary-local-cookie")

                                            self.l2tp_local_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie()
                                            self.l2tp_local_cookie.parent = self
                                            self._children_name_map["l2tp_local_cookie"] = "l2tp-local-cookie"
                                            self._children_yang_names.add("l2tp-local-cookie")
                                            self._segment_path = lambda: "l2tp-static-attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes, ['l2tp_remote_session_id', 'l2tp_local_session_id'], name, value)


                                        class L2TpRemoteCookie(Entity):
                                            """
                                            L2TP remote cookie
                                            
                                            .. attribute:: size
                                            
                                            	Remote cookie size
                                            	**type**\:  :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower remote cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher remote cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie, self).__init__()

                                                self.yang_name = "l2tp-remote-cookie"
                                                self.yang_parent_name = "l2tp-static-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('size', YLeaf(YType.enumeration, 'size')),
                                                    ('lower_value', YLeaf(YType.uint32, 'lower-value')),
                                                    ('higher_value', YLeaf(YType.uint32, 'higher-value')),
                                                ])
                                                self.size = None
                                                self.lower_value = None
                                                self.higher_value = None
                                                self._segment_path = lambda: "l2tp-remote-cookie"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie, ['size', 'lower_value', 'higher_value'], name, value)


                                        class L2TpSecondaryLocalCookie(Entity):
                                            """
                                            L2TP secondary local cookie
                                            
                                            .. attribute:: size
                                            
                                            	Local cookie size
                                            	**type**\:  :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie, self).__init__()

                                                self.yang_name = "l2tp-secondary-local-cookie"
                                                self.yang_parent_name = "l2tp-static-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('size', YLeaf(YType.enumeration, 'size')),
                                                    ('lower_value', YLeaf(YType.uint32, 'lower-value')),
                                                    ('higher_value', YLeaf(YType.uint32, 'higher-value')),
                                                ])
                                                self.size = None
                                                self.lower_value = None
                                                self.higher_value = None
                                                self._segment_path = lambda: "l2tp-secondary-local-cookie"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie, ['size', 'lower_value', 'higher_value'], name, value)


                                        class L2TpLocalCookie(Entity):
                                            """
                                            L2TP local cookie
                                            
                                            .. attribute:: size
                                            
                                            	Local cookie size
                                            	**type**\:  :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie, self).__init__()

                                                self.yang_name = "l2tp-local-cookie"
                                                self.yang_parent_name = "l2tp-static-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('size', YLeaf(YType.enumeration, 'size')),
                                                    ('lower_value', YLeaf(YType.uint32, 'lower-value')),
                                                    ('higher_value', YLeaf(YType.uint32, 'higher-value')),
                                                ])
                                                self.size = None
                                                self.lower_value = None
                                                self.higher_value = None
                                                self._segment_path = lambda: "l2tp-local-cookie"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie, ['size', 'lower_value', 'higher_value'], name, value)


                                    class L2TpStatic(Entity):
                                        """
                                        Pseudowire L2TPv3 static configuration
                                        
                                        .. attribute:: enable
                                        
                                        	Enable pseudowire L2TPv3 static configuration
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic, self).__init__()

                                            self.yang_name = "l2tp-static"
                                            self.yang_parent_name = "neighbor"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', YLeaf(YType.empty, 'enable')),
                                            ])
                                            self.enable = None
                                            self._segment_path = lambda: "l2tp-static"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic, ['enable'], name, value)


                                class PseudowireAddress(Entity):
                                    """
                                    keys\: pseudowire\-address
                                    
                                    .. attribute:: pseudowire_address  (key)
                                    
                                    	Pseudowire IPv6 address. A pseudowire can have only one address\: IPv4 or IPv6
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: mpls_static_labels
                                    
                                    	MPLS static labels
                                    	**type**\:  :py:class:`MplsStaticLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels>`
                                    
                                    .. attribute:: backup_pseudowires
                                    
                                    	List of pseudowires
                                    	**type**\:  :py:class:`BackupPseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires>`
                                    
                                    .. attribute:: l2tp_static_attributes
                                    
                                    	L2TP Static Attributes
                                    	**type**\:  :py:class:`L2TpStaticAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes>`
                                    
                                    .. attribute:: l2tp_static
                                    
                                    	Pseudowire L2TPv3 static configuration
                                    	**type**\:  :py:class:`L2TpStatic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic>`
                                    
                                    .. attribute:: tag_impose
                                    
                                    	Tag Impose vlan tagged mode
                                    	**type**\: int
                                    
                                    	**range:** 1..4094
                                    
                                    .. attribute:: class_
                                    
                                    	Name of the pseudowire class
                                    	**type**\: str
                                    
                                    	**length:** 1..32
                                    
                                    .. attribute:: source_address
                                    
                                    	Value of the Pseudowire source address. Must be IPv6 only
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: bandwidth
                                    
                                    	Pseudowire Bandwidth
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress, self).__init__()

                                        self.yang_name = "pseudowire-address"
                                        self.yang_parent_name = "pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['pseudowire_address']
                                        self._child_container_classes = OrderedDict([("mpls-static-labels", ("mpls_static_labels", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels)), ("backup-pseudowires", ("backup_pseudowires", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires)), ("l2tp-static-attributes", ("l2tp_static_attributes", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes)), ("l2tp-static", ("l2tp_static", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('pseudowire_address', YLeaf(YType.str, 'pseudowire-address')),
                                            ('tag_impose', YLeaf(YType.uint32, 'tag-impose')),
                                            ('class_', YLeaf(YType.str, 'class')),
                                            ('source_address', YLeaf(YType.str, 'source-address')),
                                            ('bandwidth', YLeaf(YType.uint32, 'bandwidth')),
                                        ])
                                        self.pseudowire_address = None
                                        self.tag_impose = None
                                        self.class_ = None
                                        self.source_address = None
                                        self.bandwidth = None

                                        self.mpls_static_labels = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels()
                                        self.mpls_static_labels.parent = self
                                        self._children_name_map["mpls_static_labels"] = "mpls-static-labels"
                                        self._children_yang_names.add("mpls-static-labels")

                                        self.backup_pseudowires = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires()
                                        self.backup_pseudowires.parent = self
                                        self._children_name_map["backup_pseudowires"] = "backup-pseudowires"
                                        self._children_yang_names.add("backup-pseudowires")

                                        self.l2tp_static_attributes = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes()
                                        self.l2tp_static_attributes.parent = self
                                        self._children_name_map["l2tp_static_attributes"] = "l2tp-static-attributes"
                                        self._children_yang_names.add("l2tp-static-attributes")

                                        self.l2tp_static = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic()
                                        self.l2tp_static.parent = self
                                        self._children_name_map["l2tp_static"] = "l2tp-static"
                                        self._children_yang_names.add("l2tp-static")
                                        self._segment_path = lambda: "pseudowire-address" + "[pseudowire-address='" + str(self.pseudowire_address) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress, ['pseudowire_address', 'tag_impose', 'class_', 'source_address', 'bandwidth'], name, value)


                                    class MplsStaticLabels(Entity):
                                        """
                                        MPLS static labels
                                        
                                        .. attribute:: local_static_label
                                        
                                        	Pseudowire local static label
                                        	**type**\: int
                                        
                                        	**range:** 16..1048575
                                        
                                        .. attribute:: remote_static_label
                                        
                                        	Pseudowire remote static label
                                        	**type**\: int
                                        
                                        	**range:** 16..1048575
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels, self).__init__()

                                            self.yang_name = "mpls-static-labels"
                                            self.yang_parent_name = "pseudowire-address"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('local_static_label', YLeaf(YType.uint32, 'local-static-label')),
                                                ('remote_static_label', YLeaf(YType.uint32, 'remote-static-label')),
                                            ])
                                            self.local_static_label = None
                                            self.remote_static_label = None
                                            self._segment_path = lambda: "mpls-static-labels"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels, ['local_static_label', 'remote_static_label'], name, value)


                                    class BackupPseudowires(Entity):
                                        """
                                        List of pseudowires
                                        
                                        .. attribute:: backup_pseudowire
                                        
                                        	Backup pseudowire for the cross connect
                                        	**type**\: list of  		 :py:class:`BackupPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires, self).__init__()

                                            self.yang_name = "backup-pseudowires"
                                            self.yang_parent_name = "pseudowire-address"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("backup-pseudowire", ("backup_pseudowire", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire))])
                                            self._leafs = OrderedDict()

                                            self.backup_pseudowire = YList(self)
                                            self._segment_path = lambda: "backup-pseudowires"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires, [], name, value)


                                        class BackupPseudowire(Entity):
                                            """
                                            Backup pseudowire for the cross connect
                                            
                                            .. attribute:: neighbor  (key)
                                            
                                            	Neighbor IP address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: pseudowire_id  (key)
                                            
                                            	Pseudowire ID
                                            	**type**\: int
                                            
                                            	**range:** 1..4294967295
                                            
                                            .. attribute:: backup_mpls_static_labels
                                            
                                            	MPLS static labels
                                            	**type**\:  :py:class:`BackupMplsStaticLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels>`
                                            
                                            .. attribute:: backup_pw_class
                                            
                                            	PW class template name to use for the backup PW
                                            	**type**\: str
                                            
                                            	**length:** 1..32
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire, self).__init__()

                                                self.yang_name = "backup-pseudowire"
                                                self.yang_parent_name = "backup-pseudowires"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['neighbor','pseudowire_id']
                                                self._child_container_classes = OrderedDict([("backup-mpls-static-labels", ("backup_mpls_static_labels", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('neighbor', YLeaf(YType.str, 'neighbor')),
                                                    ('pseudowire_id', YLeaf(YType.uint32, 'pseudowire-id')),
                                                    ('backup_pw_class', YLeaf(YType.str, 'backup-pw-class')),
                                                ])
                                                self.neighbor = None
                                                self.pseudowire_id = None
                                                self.backup_pw_class = None

                                                self.backup_mpls_static_labels = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels()
                                                self.backup_mpls_static_labels.parent = self
                                                self._children_name_map["backup_mpls_static_labels"] = "backup-mpls-static-labels"
                                                self._children_yang_names.add("backup-mpls-static-labels")
                                                self._segment_path = lambda: "backup-pseudowire" + "[neighbor='" + str(self.neighbor) + "']" + "[pseudowire-id='" + str(self.pseudowire_id) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire, ['neighbor', 'pseudowire_id', 'backup_pw_class'], name, value)


                                            class BackupMplsStaticLabels(Entity):
                                                """
                                                MPLS static labels
                                                
                                                .. attribute:: local_static_label
                                                
                                                	Pseudowire local static label
                                                	**type**\: int
                                                
                                                	**range:** 16..1048575
                                                
                                                .. attribute:: remote_static_label
                                                
                                                	Pseudowire remote static label
                                                	**type**\: int
                                                
                                                	**range:** 16..1048575
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2017-06-26'

                                                def __init__(self):
                                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels, self).__init__()

                                                    self.yang_name = "backup-mpls-static-labels"
                                                    self.yang_parent_name = "backup-pseudowire"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('local_static_label', YLeaf(YType.uint32, 'local-static-label')),
                                                        ('remote_static_label', YLeaf(YType.uint32, 'remote-static-label')),
                                                    ])
                                                    self.local_static_label = None
                                                    self.remote_static_label = None
                                                    self._segment_path = lambda: "backup-mpls-static-labels"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels, ['local_static_label', 'remote_static_label'], name, value)


                                    class L2TpStaticAttributes(Entity):
                                        """
                                        L2TP Static Attributes
                                        
                                        .. attribute:: l2tp_remote_cookie
                                        
                                        	L2TP remote cookie
                                        	**type**\:  :py:class:`L2TpRemoteCookie <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie>`
                                        
                                        .. attribute:: l2tp_secondary_local_cookie
                                        
                                        	L2TP secondary local cookie
                                        	**type**\:  :py:class:`L2TpSecondaryLocalCookie <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie>`
                                        
                                        .. attribute:: l2tp_local_cookie
                                        
                                        	L2TP local cookie
                                        	**type**\:  :py:class:`L2TpLocalCookie <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie>`
                                        
                                        .. attribute:: l2tp_remote_session_id
                                        
                                        	L2TP remote session ID
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: l2tp_local_session_id
                                        
                                        	L2TP local session ID
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes, self).__init__()

                                            self.yang_name = "l2tp-static-attributes"
                                            self.yang_parent_name = "pseudowire-address"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("l2tp-remote-cookie", ("l2tp_remote_cookie", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie)), ("l2tp-secondary-local-cookie", ("l2tp_secondary_local_cookie", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie)), ("l2tp-local-cookie", ("l2tp_local_cookie", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('l2tp_remote_session_id', YLeaf(YType.uint32, 'l2tp-remote-session-id')),
                                                ('l2tp_local_session_id', YLeaf(YType.uint32, 'l2tp-local-session-id')),
                                            ])
                                            self.l2tp_remote_session_id = None
                                            self.l2tp_local_session_id = None

                                            self.l2tp_remote_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie()
                                            self.l2tp_remote_cookie.parent = self
                                            self._children_name_map["l2tp_remote_cookie"] = "l2tp-remote-cookie"
                                            self._children_yang_names.add("l2tp-remote-cookie")

                                            self.l2tp_secondary_local_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie()
                                            self.l2tp_secondary_local_cookie.parent = self
                                            self._children_name_map["l2tp_secondary_local_cookie"] = "l2tp-secondary-local-cookie"
                                            self._children_yang_names.add("l2tp-secondary-local-cookie")

                                            self.l2tp_local_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie()
                                            self.l2tp_local_cookie.parent = self
                                            self._children_name_map["l2tp_local_cookie"] = "l2tp-local-cookie"
                                            self._children_yang_names.add("l2tp-local-cookie")
                                            self._segment_path = lambda: "l2tp-static-attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes, ['l2tp_remote_session_id', 'l2tp_local_session_id'], name, value)


                                        class L2TpRemoteCookie(Entity):
                                            """
                                            L2TP remote cookie
                                            
                                            .. attribute:: size
                                            
                                            	Remote cookie size
                                            	**type**\:  :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower remote cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher remote cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie, self).__init__()

                                                self.yang_name = "l2tp-remote-cookie"
                                                self.yang_parent_name = "l2tp-static-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('size', YLeaf(YType.enumeration, 'size')),
                                                    ('lower_value', YLeaf(YType.uint32, 'lower-value')),
                                                    ('higher_value', YLeaf(YType.uint32, 'higher-value')),
                                                ])
                                                self.size = None
                                                self.lower_value = None
                                                self.higher_value = None
                                                self._segment_path = lambda: "l2tp-remote-cookie"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie, ['size', 'lower_value', 'higher_value'], name, value)


                                        class L2TpSecondaryLocalCookie(Entity):
                                            """
                                            L2TP secondary local cookie
                                            
                                            .. attribute:: size
                                            
                                            	Local cookie size
                                            	**type**\:  :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie, self).__init__()

                                                self.yang_name = "l2tp-secondary-local-cookie"
                                                self.yang_parent_name = "l2tp-static-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('size', YLeaf(YType.enumeration, 'size')),
                                                    ('lower_value', YLeaf(YType.uint32, 'lower-value')),
                                                    ('higher_value', YLeaf(YType.uint32, 'higher-value')),
                                                ])
                                                self.size = None
                                                self.lower_value = None
                                                self.higher_value = None
                                                self._segment_path = lambda: "l2tp-secondary-local-cookie"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie, ['size', 'lower_value', 'higher_value'], name, value)


                                        class L2TpLocalCookie(Entity):
                                            """
                                            L2TP local cookie
                                            
                                            .. attribute:: size
                                            
                                            	Local cookie size
                                            	**type**\:  :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie, self).__init__()

                                                self.yang_name = "l2tp-local-cookie"
                                                self.yang_parent_name = "l2tp-static-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('size', YLeaf(YType.enumeration, 'size')),
                                                    ('lower_value', YLeaf(YType.uint32, 'lower-value')),
                                                    ('higher_value', YLeaf(YType.uint32, 'higher-value')),
                                                ])
                                                self.size = None
                                                self.lower_value = None
                                                self.higher_value = None
                                                self._segment_path = lambda: "l2tp-local-cookie"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie, ['size', 'lower_value', 'higher_value'], name, value)


                                    class L2TpStatic(Entity):
                                        """
                                        Pseudowire L2TPv3 static configuration
                                        
                                        .. attribute:: enable
                                        
                                        	Enable pseudowire L2TPv3 static configuration
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic, self).__init__()

                                            self.yang_name = "l2tp-static"
                                            self.yang_parent_name = "pseudowire-address"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', YLeaf(YType.empty, 'enable')),
                                            ])
                                            self.enable = None
                                            self._segment_path = lambda: "l2tp-static"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic, ['enable'], name, value)


                        class MonitorSessions(Entity):
                            """
                            List of Monitor session segments
                            
                            .. attribute:: monitor_session
                            
                            	Monitor session segment
                            	**type**\: list of  		 :py:class:`MonitorSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions, self).__init__()

                                self.yang_name = "monitor-sessions"
                                self.yang_parent_name = "p2p-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("monitor-session", ("monitor_session", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession))])
                                self._leafs = OrderedDict()

                                self.monitor_session = YList(self)
                                self._segment_path = lambda: "monitor-sessions"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions, [], name, value)


                            class MonitorSession(Entity):
                                """
                                Monitor session segment
                                
                                .. attribute:: name  (key)
                                
                                	Name of the monitor session
                                	**type**\: str
                                
                                	**length:** 1..64
                                
                                .. attribute:: enable
                                
                                	Enable monitor session segment 
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession, self).__init__()

                                    self.yang_name = "monitor-session"
                                    self.yang_parent_name = "monitor-sessions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['name']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('name', YLeaf(YType.str, 'name')),
                                        ('enable', YLeaf(YType.empty, 'enable')),
                                    ])
                                    self.name = None
                                    self.enable = None
                                    self._segment_path = lambda: "monitor-session" + "[name='" + str(self.name) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession, ['name', 'enable'], name, value)


                        class PseudowireRouteds(Entity):
                            """
                            List of pseudowire\-routed
                            
                            .. attribute:: pseudowire_routed
                            
                            	Pseudowire configuration
                            	**type**\: list of  		 :py:class:`PseudowireRouted <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds, self).__init__()

                                self.yang_name = "pseudowire-routeds"
                                self.yang_parent_name = "p2p-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("pseudowire-routed", ("pseudowire_routed", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted))])
                                self._leafs = OrderedDict()

                                self.pseudowire_routed = YList(self)
                                self._segment_path = lambda: "pseudowire-routeds"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds, [], name, value)


                            class PseudowireRouted(Entity):
                                """
                                Pseudowire configuration
                                
                                .. attribute:: global_id  (key)
                                
                                	Target Global ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: prefix  (key)
                                
                                	Target Prefix
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: acid  (key)
                                
                                	Target AC ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: sacid  (key)
                                
                                	Source AC ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: tag_impose
                                
                                	Tag Impose vlan tagged mode
                                	**type**\: int
                                
                                	**range:** 1..4094
                                
                                .. attribute:: class_
                                
                                	Name of the pseudowire class
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted, self).__init__()

                                    self.yang_name = "pseudowire-routed"
                                    self.yang_parent_name = "pseudowire-routeds"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['global_id','prefix','acid','sacid']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('global_id', YLeaf(YType.uint32, 'global-id')),
                                        ('prefix', YLeaf(YType.str, 'prefix')),
                                        ('acid', YLeaf(YType.uint32, 'acid')),
                                        ('sacid', YLeaf(YType.uint32, 'sacid')),
                                        ('tag_impose', YLeaf(YType.uint32, 'tag-impose')),
                                        ('class_', YLeaf(YType.str, 'class')),
                                    ])
                                    self.global_id = None
                                    self.prefix = None
                                    self.acid = None
                                    self.sacid = None
                                    self.tag_impose = None
                                    self.class_ = None
                                    self._segment_path = lambda: "pseudowire-routed" + "[global-id='" + str(self.global_id) + "']" + "[prefix='" + str(self.prefix) + "']" + "[acid='" + str(self.acid) + "']" + "[sacid='" + str(self.sacid) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted, ['global_id', 'prefix', 'acid', 'sacid', 'tag_impose', 'class_'], name, value)


                        class AttachmentCircuits(Entity):
                            """
                            List of attachment circuits
                            
                            .. attribute:: attachment_circuit
                            
                            	Attachment circuit interface
                            	**type**\: list of  		 :py:class:`AttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits, self).__init__()

                                self.yang_name = "attachment-circuits"
                                self.yang_parent_name = "p2p-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("attachment-circuit", ("attachment_circuit", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit))])
                                self._leafs = OrderedDict()

                                self.attachment_circuit = YList(self)
                                self._segment_path = lambda: "attachment-circuits"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits, [], name, value)


                            class AttachmentCircuit(Entity):
                                """
                                Attachment circuit interface
                                
                                .. attribute:: name  (key)
                                
                                	Name of the attachment circuit interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: enable
                                
                                	Enable attachment circuit interface
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit, self).__init__()

                                    self.yang_name = "attachment-circuit"
                                    self.yang_parent_name = "attachment-circuits"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['name']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('name', YLeaf(YType.str, 'name')),
                                        ('enable', YLeaf(YType.empty, 'enable')),
                                    ])
                                    self.name = None
                                    self.enable = None
                                    self._segment_path = lambda: "attachment-circuit" + "[name='" + str(self.name) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit, ['name', 'enable'], name, value)


                class Mp2MpXconnects(Entity):
                    """
                    List of multi point to multi point xconnects
                    
                    .. attribute:: mp2mp_xconnect
                    
                    	Multi point to multi point xconnect
                    	**type**\: list of  		 :py:class:`Mp2MpXconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects, self).__init__()

                        self.yang_name = "mp2mp-xconnects"
                        self.yang_parent_name = "xconnect-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("mp2mp-xconnect", ("mp2mp_xconnect", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect))])
                        self._leafs = OrderedDict()

                        self.mp2mp_xconnect = YList(self)
                        self._segment_path = lambda: "mp2mp-xconnects"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects, [], name, value)


                    class Mp2MpXconnect(Entity):
                        """
                        Multi point to multi point xconnect
                        
                        .. attribute:: name  (key)
                        
                        	Name of the multi point to multi point xconnect
                        	**type**\: str
                        
                        	**length:** 1..26
                        
                        .. attribute:: mp2mp_auto_discovery
                        
                        	auto\-discovery in this MP2MP
                        	**type**\:  :py:class:`Mp2MpAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery>`
                        
                        .. attribute:: mp2mpmtu
                        
                        	Maximum transmission unit for this MP2MP VPWS instance
                        	**type**\: int
                        
                        	**range:** 64..65535
                        
                        	**units**\: byte
                        
                        .. attribute:: mp2mp_control_word
                        
                        	Disable control word
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: mp2mpl2_encapsulation
                        
                        	Configure Layer 2 Encapsulation
                        	**type**\:  :py:class:`L2Encapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Encapsulation>`
                        
                        .. attribute:: mp2mp_interworking
                        
                        	Interworking
                        	**type**\:  :py:class:`Interworking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Interworking>`
                        
                        .. attribute:: mp2mp_shutdown
                        
                        	shutdown this MP2MP VPWS instance
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: mp2mpvpn_id
                        
                        	VPN Identifier
                        	**type**\: int
                        
                        	**range:** 1..4294967295
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect, self).__init__()

                            self.yang_name = "mp2mp-xconnect"
                            self.yang_parent_name = "mp2mp-xconnects"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_container_classes = OrderedDict([("mp2mp-auto-discovery", ("mp2mp_auto_discovery", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', YLeaf(YType.str, 'name')),
                                ('mp2mpmtu', YLeaf(YType.uint32, 'mp2mpmtu')),
                                ('mp2mp_control_word', YLeaf(YType.empty, 'mp2mp-control-word')),
                                ('mp2mpl2_encapsulation', YLeaf(YType.enumeration, 'mp2mpl2-encapsulation')),
                                ('mp2mp_interworking', YLeaf(YType.enumeration, 'mp2mp-interworking')),
                                ('mp2mp_shutdown', YLeaf(YType.empty, 'mp2mp-shutdown')),
                                ('mp2mpvpn_id', YLeaf(YType.uint32, 'mp2mpvpn-id')),
                            ])
                            self.name = None
                            self.mp2mpmtu = None
                            self.mp2mp_control_word = None
                            self.mp2mpl2_encapsulation = None
                            self.mp2mp_interworking = None
                            self.mp2mp_shutdown = None
                            self.mp2mpvpn_id = None

                            self.mp2mp_auto_discovery = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery()
                            self.mp2mp_auto_discovery.parent = self
                            self._children_name_map["mp2mp_auto_discovery"] = "mp2mp-auto-discovery"
                            self._children_yang_names.add("mp2mp-auto-discovery")
                            self._segment_path = lambda: "mp2mp-xconnect" + "[name='" + str(self.name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect, ['name', 'mp2mpmtu', 'mp2mp_control_word', 'mp2mpl2_encapsulation', 'mp2mp_interworking', 'mp2mp_shutdown', 'mp2mpvpn_id'], name, value)


                        class Mp2MpAutoDiscovery(Entity):
                            """
                            auto\-discovery in this MP2MP
                            
                            .. attribute:: route_distinguisher
                            
                            	Route Distinguisher
                            	**type**\:  :py:class:`RouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher>`
                            
                            .. attribute:: mp2mp_route_policy
                            
                            	Route policy
                            	**type**\:  :py:class:`Mp2MpRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy>`
                            
                            .. attribute:: mp2mp_route_targets
                            
                            	Route Target
                            	**type**\:  :py:class:`Mp2MpRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets>`
                            
                            .. attribute:: mp2mp_signaling_protocol
                            
                            	signaling protocol in this MP2MP
                            	**type**\:  :py:class:`Mp2MpSignalingProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol>`
                            
                            .. attribute:: enable
                            
                            	Enable auto\-discovery
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery, self).__init__()

                                self.yang_name = "mp2mp-auto-discovery"
                                self.yang_parent_name = "mp2mp-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("route-distinguisher", ("route_distinguisher", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher)), ("mp2mp-route-policy", ("mp2mp_route_policy", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy)), ("mp2mp-route-targets", ("mp2mp_route_targets", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets)), ("mp2mp-signaling-protocol", ("mp2mp_signaling_protocol", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enable', YLeaf(YType.empty, 'enable')),
                                ])
                                self.enable = None

                                self.route_distinguisher = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher()
                                self.route_distinguisher.parent = self
                                self._children_name_map["route_distinguisher"] = "route-distinguisher"
                                self._children_yang_names.add("route-distinguisher")

                                self.mp2mp_route_policy = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy()
                                self.mp2mp_route_policy.parent = self
                                self._children_name_map["mp2mp_route_policy"] = "mp2mp-route-policy"
                                self._children_yang_names.add("mp2mp-route-policy")

                                self.mp2mp_route_targets = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets()
                                self.mp2mp_route_targets.parent = self
                                self._children_name_map["mp2mp_route_targets"] = "mp2mp-route-targets"
                                self._children_yang_names.add("mp2mp-route-targets")

                                self.mp2mp_signaling_protocol = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol()
                                self.mp2mp_signaling_protocol.parent = self
                                self._children_name_map["mp2mp_signaling_protocol"] = "mp2mp-signaling-protocol"
                                self._children_yang_names.add("mp2mp-signaling-protocol")
                                self._segment_path = lambda: "mp2mp-auto-discovery"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery, ['enable'], name, value)


                            class RouteDistinguisher(Entity):
                                """
                                Route Distinguisher
                                
                                .. attribute:: type
                                
                                	Router distinguisher type
                                	**type**\:  :py:class:`BgpRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher>`
                                
                                .. attribute:: as_
                                
                                	Two byte or 4 byte AS number
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: as_index
                                
                                	AS\:nn (hex or decimal format)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: address
                                
                                	IPV4 address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: addr_index
                                
                                	Addr index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher, self).__init__()

                                    self.yang_name = "route-distinguisher"
                                    self.yang_parent_name = "mp2mp-auto-discovery"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('type', YLeaf(YType.enumeration, 'type')),
                                        ('as_', YLeaf(YType.uint32, 'as')),
                                        ('as_index', YLeaf(YType.uint32, 'as-index')),
                                        ('address', YLeaf(YType.str, 'address')),
                                        ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                                    ])
                                    self.type = None
                                    self.as_ = None
                                    self.as_index = None
                                    self.address = None
                                    self.addr_index = None
                                    self._segment_path = lambda: "route-distinguisher"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher, ['type', 'as_', 'as_index', 'address', 'addr_index'], name, value)


                            class Mp2MpRoutePolicy(Entity):
                                """
                                Route policy
                                
                                .. attribute:: export
                                
                                	Export route policy
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy, self).__init__()

                                    self.yang_name = "mp2mp-route-policy"
                                    self.yang_parent_name = "mp2mp-auto-discovery"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('export', YLeaf(YType.str, 'export')),
                                    ])
                                    self.export = None
                                    self._segment_path = lambda: "mp2mp-route-policy"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy, ['export'], name, value)


                            class Mp2MpRouteTargets(Entity):
                                """
                                Route Target
                                
                                .. attribute:: mp2mp_route_target
                                
                                	Name of the Route Target
                                	**type**\: list of  		 :py:class:`Mp2MpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets, self).__init__()

                                    self.yang_name = "mp2mp-route-targets"
                                    self.yang_parent_name = "mp2mp-auto-discovery"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("mp2mp-route-target", ("mp2mp_route_target", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget))])
                                    self._leafs = OrderedDict()

                                    self.mp2mp_route_target = YList(self)
                                    self._segment_path = lambda: "mp2mp-route-targets"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets, [], name, value)


                                class Mp2MpRouteTarget(Entity):
                                    """
                                    Name of the Route Target
                                    
                                    .. attribute:: role  (key)
                                    
                                    	Role of the router target type
                                    	**type**\:  :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                                    
                                    .. attribute:: format  (key)
                                    
                                    	Format of the route target
                                    	**type**\:  :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                                    
                                    .. attribute:: two_byte_as_or_four_byte_as
                                    
                                    	two byte as or four byte as
                                    	**type**\: list of  		 :py:class:`TwoByteAsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	ipv4 address
                                    	**type**\: list of  		 :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget, self).__init__()

                                        self.yang_name = "mp2mp-route-target"
                                        self.yang_parent_name = "mp2mp-route-targets"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['role','format']
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("two-byte-as-or-four-byte-as", ("two_byte_as_or_four_byte_as", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs)), ("ipv4-address", ("ipv4_address", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address))])
                                        self._leafs = OrderedDict([
                                            ('role', YLeaf(YType.enumeration, 'role')),
                                            ('format', YLeaf(YType.enumeration, 'format')),
                                        ])
                                        self.role = None
                                        self.format = None

                                        self.two_byte_as_or_four_byte_as = YList(self)
                                        self.ipv4_address = YList(self)
                                        self._segment_path = lambda: "mp2mp-route-target" + "[role='" + str(self.role) + "']" + "[format='" + str(self.format) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget, ['role', 'format'], name, value)


                                    class TwoByteAsOrFourByteAs(Entity):
                                        """
                                        two byte as or four byte as
                                        
                                        .. attribute:: as_  (key)
                                        
                                        	Two byte or 4 byte AS number
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: as_index  (key)
                                        
                                        	AS\:nn (hex or decimal format)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs, self).__init__()

                                            self.yang_name = "two-byte-as-or-four-byte-as"
                                            self.yang_parent_name = "mp2mp-route-target"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['as_','as_index']
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('as_', YLeaf(YType.uint32, 'as')),
                                                ('as_index', YLeaf(YType.uint32, 'as-index')),
                                            ])
                                            self.as_ = None
                                            self.as_index = None
                                            self._segment_path = lambda: "two-byte-as-or-four-byte-as" + "[as='" + str(self.as_) + "']" + "[as-index='" + str(self.as_index) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs, ['as_', 'as_index'], name, value)


                                    class Ipv4Address(Entity):
                                        """
                                        ipv4 address
                                        
                                        .. attribute:: address  (key)
                                        
                                        	IPV4 address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: addr_index  (key)
                                        
                                        	Addr index
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address, self).__init__()

                                            self.yang_name = "ipv4-address"
                                            self.yang_parent_name = "mp2mp-route-target"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['address','addr_index']
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('address', YLeaf(YType.str, 'address')),
                                                ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                                            ])
                                            self.address = None
                                            self.addr_index = None
                                            self._segment_path = lambda: "ipv4-address" + "[address='" + str(self.address) + "']" + "[addr-index='" + str(self.addr_index) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address, ['address', 'addr_index'], name, value)


                            class Mp2MpSignalingProtocol(Entity):
                                """
                                signaling protocol in this MP2MP
                                
                                .. attribute:: flow_label_load_balance
                                
                                	Enable Flow Label based load balancing
                                	**type**\:  :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance>`
                                
                                .. attribute:: ceids
                                
                                	Local Customer Edge Identifier Table
                                	**type**\:  :py:class:`Ceids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids>`
                                
                                .. attribute:: ce_range
                                
                                	Local Customer Edge Identifier
                                	**type**\: int
                                
                                	**range:** 11..100
                                
                                .. attribute:: enable
                                
                                	Enable signaling protocol
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol, self).__init__()

                                    self.yang_name = "mp2mp-signaling-protocol"
                                    self.yang_parent_name = "mp2mp-auto-discovery"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("flow-label-load-balance", ("flow_label_load_balance", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance)), ("ceids", ("ceids", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ce_range', YLeaf(YType.uint32, 'ce-range')),
                                        ('enable', YLeaf(YType.empty, 'enable')),
                                    ])
                                    self.ce_range = None
                                    self.enable = None

                                    self.flow_label_load_balance = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance()
                                    self.flow_label_load_balance.parent = self
                                    self._children_name_map["flow_label_load_balance"] = "flow-label-load-balance"
                                    self._children_yang_names.add("flow-label-load-balance")

                                    self.ceids = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids()
                                    self.ceids.parent = self
                                    self._children_name_map["ceids"] = "ceids"
                                    self._children_yang_names.add("ceids")
                                    self._segment_path = lambda: "mp2mp-signaling-protocol"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol, ['ce_range', 'enable'], name, value)


                                class FlowLabelLoadBalance(Entity):
                                    """
                                    Enable Flow Label based load balancing
                                    
                                    .. attribute:: flow_label
                                    
                                    	Flow Label load balance type
                                    	**type**\:  :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalance>`
                                    
                                    .. attribute:: static
                                    
                                    	Static Flow Label
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance, self).__init__()

                                        self.yang_name = "flow-label-load-balance"
                                        self.yang_parent_name = "mp2mp-signaling-protocol"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('flow_label', YLeaf(YType.enumeration, 'flow-label')),
                                            ('static', YLeaf(YType.empty, 'static')),
                                        ])
                                        self.flow_label = None
                                        self.static = None
                                        self._segment_path = lambda: "flow-label-load-balance"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance, ['flow_label', 'static'], name, value)


                                class Ceids(Entity):
                                    """
                                    Local Customer Edge Identifier Table
                                    
                                    .. attribute:: ceid
                                    
                                    	Local Customer Edge Identifier 
                                    	**type**\: list of  		 :py:class:`Ceid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids, self).__init__()

                                        self.yang_name = "ceids"
                                        self.yang_parent_name = "mp2mp-signaling-protocol"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("ceid", ("ceid", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid))])
                                        self._leafs = OrderedDict()

                                        self.ceid = YList(self)
                                        self._segment_path = lambda: "ceids"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids, [], name, value)


                                    class Ceid(Entity):
                                        """
                                        Local Customer Edge Identifier 
                                        
                                        .. attribute:: ce_id  (key)
                                        
                                        	Local Customer Edge Identifier
                                        	**type**\: int
                                        
                                        	**range:** 1..16384
                                        
                                        .. attribute:: remote_ceid_attachment_circuits
                                        
                                        	AC And Remote Customer Edge Identifier Table
                                        	**type**\:  :py:class:`RemoteCeidAttachmentCircuits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid, self).__init__()

                                            self.yang_name = "ceid"
                                            self.yang_parent_name = "ceids"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['ce_id']
                                            self._child_container_classes = OrderedDict([("remote-ceid-attachment-circuits", ("remote_ceid_attachment_circuits", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('ce_id', YLeaf(YType.uint32, 'ce-id')),
                                            ])
                                            self.ce_id = None

                                            self.remote_ceid_attachment_circuits = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits()
                                            self.remote_ceid_attachment_circuits.parent = self
                                            self._children_name_map["remote_ceid_attachment_circuits"] = "remote-ceid-attachment-circuits"
                                            self._children_yang_names.add("remote-ceid-attachment-circuits")
                                            self._segment_path = lambda: "ceid" + "[ce-id='" + str(self.ce_id) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid, ['ce_id'], name, value)


                                        class RemoteCeidAttachmentCircuits(Entity):
                                            """
                                            AC And Remote Customer Edge Identifier
                                            Table
                                            
                                            .. attribute:: remote_ceid_attachment_circuit
                                            
                                            	AC And Remote Customer Edge Identifier
                                            	**type**\: list of  		 :py:class:`RemoteCeidAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits, self).__init__()

                                                self.yang_name = "remote-ceid-attachment-circuits"
                                                self.yang_parent_name = "ceid"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([("remote-ceid-attachment-circuit", ("remote_ceid_attachment_circuit", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit))])
                                                self._leafs = OrderedDict()

                                                self.remote_ceid_attachment_circuit = YList(self)
                                                self._segment_path = lambda: "remote-ceid-attachment-circuits"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits, [], name, value)


                                            class RemoteCeidAttachmentCircuit(Entity):
                                                """
                                                AC And Remote Customer Edge Identifier
                                                
                                                .. attribute:: name  (key)
                                                
                                                	The name of the Attachment Circuit
                                                	**type**\: str
                                                
                                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                                
                                                .. attribute:: remote_ce_id  (key)
                                                
                                                	Remote Customer Edge Identifier
                                                	**type**\: int
                                                
                                                	**range:** 1..16384
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2017-06-26'

                                                def __init__(self):
                                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit, self).__init__()

                                                    self.yang_name = "remote-ceid-attachment-circuit"
                                                    self.yang_parent_name = "remote-ceid-attachment-circuits"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['name','remote_ce_id']
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('name', YLeaf(YType.str, 'name')),
                                                        ('remote_ce_id', YLeaf(YType.uint32, 'remote-ce-id')),
                                                    ])
                                                    self.name = None
                                                    self.remote_ce_id = None
                                                    self._segment_path = lambda: "remote-ceid-attachment-circuit" + "[name='" + str(self.name) + "']" + "[remote-ce-id='" + str(self.remote_ce_id) + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit, ['name', 'remote_ce_id'], name, value)


        class BridgeDomainGroups(Entity):
            """
            List of bridge  groups
            
            .. attribute:: bridge_domain_group
            
            	Bridge group
            	**type**\: list of  		 :py:class:`BridgeDomainGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Database.BridgeDomainGroups, self).__init__()

                self.yang_name = "bridge-domain-groups"
                self.yang_parent_name = "database"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("bridge-domain-group", ("bridge_domain_group", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup))])
                self._leafs = OrderedDict()

                self.bridge_domain_group = YList(self)
                self._segment_path = lambda: "bridge-domain-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups, [], name, value)


            class BridgeDomainGroup(Entity):
                """
                Bridge group
                
                .. attribute:: name  (key)
                
                	Name of the Bridge group
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: bridge_domains
                
                	List of Bridge Domain
                	**type**\:  :py:class:`BridgeDomains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup, self).__init__()

                    self.yang_name = "bridge-domain-group"
                    self.yang_parent_name = "bridge-domain-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([("bridge-domains", ("bridge_domains", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                    ])
                    self.name = None

                    self.bridge_domains = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains()
                    self.bridge_domains.parent = self
                    self._children_name_map["bridge_domains"] = "bridge-domains"
                    self._children_yang_names.add("bridge-domains")
                    self._segment_path = lambda: "bridge-domain-group" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/bridge-domain-groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup, ['name'], name, value)


                class BridgeDomains(Entity):
                    """
                    List of Bridge Domain
                    
                    .. attribute:: bridge_domain
                    
                    	bridge domain
                    	**type**\: list of  		 :py:class:`BridgeDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains, self).__init__()

                        self.yang_name = "bridge-domains"
                        self.yang_parent_name = "bridge-domain-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("bridge-domain", ("bridge_domain", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain))])
                        self._leafs = OrderedDict()

                        self.bridge_domain = YList(self)
                        self._segment_path = lambda: "bridge-domains"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains, [], name, value)


                    class BridgeDomain(Entity):
                        """
                        bridge domain
                        
                        .. attribute:: name  (key)
                        
                        	Name of the bridge domain
                        	**type**\: str
                        
                        	**length:** 1..27
                        
                        .. attribute:: bd_storm_controls
                        
                        	Storm Control
                        	**type**\:  :py:class:`BdStormControls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls>`
                        
                        .. attribute:: member_vnis
                        
                        	Bridge Domain VxLAN Network Identifier Table
                        	**type**\:  :py:class:`MemberVnis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis>`
                        
                        .. attribute:: bridge_domain_mac
                        
                        	MAC configuration commands
                        	**type**\:  :py:class:`BridgeDomainMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac>`
                        
                        .. attribute:: nv_satellite
                        
                        	nV Satellite
                        	**type**\:  :py:class:`NvSatellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite>`
                        
                        .. attribute:: bridge_domain_pbb
                        
                        	Bridge Domain PBB
                        	**type**\:  :py:class:`BridgeDomainPbb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb>`
                        
                        .. attribute:: bridge_domain_evis
                        
                        	Bridge Domain EVI Table
                        	**type**\:  :py:class:`BridgeDomainEvis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis>`
                        
                        .. attribute:: access_vfis
                        
                        	Specify the access virtual forwarding interface name
                        	**type**\:  :py:class:`AccessVfis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis>`
                        
                        .. attribute:: bd_pseudowires
                        
                        	List of pseudowires
                        	**type**\:  :py:class:`BdPseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires>`
                        
                        .. attribute:: vfis
                        
                        	Specify the virtual forwarding interface name
                        	**type**\:  :py:class:`Vfis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis>`
                        
                        .. attribute:: bd_attachment_circuits
                        
                        	Attachment Circuit table
                        	**type**\:  :py:class:`BdAttachmentCircuits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits>`
                        
                        .. attribute:: bd_pseudowire_evpns
                        
                        	List of EVPN pseudowires
                        	**type**\:  :py:class:`BdPseudowireEvpns <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns>`
                        
                        .. attribute:: ip_source_guard
                        
                        	IP Source Guard
                        	**type**\:  :py:class:`IpSourceGuard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard>`
                        
                        .. attribute:: dai
                        
                        	Dynamic ARP Inspection
                        	**type**\:  :py:class:`Dai <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai>`
                        
                        .. attribute:: routed_interfaces
                        
                        	Bridge Domain Routed Interface Table
                        	**type**\:  :py:class:`RoutedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces>`
                        
                        .. attribute:: coupled_mode
                        
                        	Coupled\-mode configuration
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: shutdown
                        
                        	shutdown the Bridge Domain
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: flooding_unknown_unicast
                        
                        	Disable Unknown Unicast flooding
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: igmp_snooping_disable
                        
                        	Disable IGMP Snooping
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: transport_mode
                        
                        	Bridge Domain Transport mode
                        	**type**\:  :py:class:`BridgeDomainTransportMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BridgeDomainTransportMode>`
                        
                        .. attribute:: mld_snooping
                        
                        	Attach MLD Snooping Profile Name
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: bridge_domain_mtu
                        
                        	Maximum transmission unit for this Bridge Domain
                        	**type**\: int
                        
                        	**range:** 46..65535
                        
                        	**units**\: byte
                        
                        .. attribute:: dhcp
                        
                        	DHCPv4 Snooping profile name
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: bridge_description
                        
                        	Bridge\-domain description Name
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: igmp_snooping
                        
                        	Attach IGMP Snooping Profile Name
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: flooding
                        
                        	Disable flooding
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain, self).__init__()

                            self.yang_name = "bridge-domain"
                            self.yang_parent_name = "bridge-domains"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_container_classes = OrderedDict([("bd-storm-controls", ("bd_storm_controls", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls)), ("member-vnis", ("member_vnis", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis)), ("bridge-domain-mac", ("bridge_domain_mac", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac)), ("nv-satellite", ("nv_satellite", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite)), ("bridge-domain-pbb", ("bridge_domain_pbb", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb)), ("bridge-domain-evis", ("bridge_domain_evis", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis)), ("access-vfis", ("access_vfis", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis)), ("bd-pseudowires", ("bd_pseudowires", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires)), ("vfis", ("vfis", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis)), ("bd-attachment-circuits", ("bd_attachment_circuits", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits)), ("bd-pseudowire-evpns", ("bd_pseudowire_evpns", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns)), ("ip-source-guard", ("ip_source_guard", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard)), ("dai", ("dai", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai)), ("routed-interfaces", ("routed_interfaces", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', YLeaf(YType.str, 'name')),
                                ('coupled_mode', YLeaf(YType.empty, 'coupled-mode')),
                                ('shutdown', YLeaf(YType.empty, 'shutdown')),
                                ('flooding_unknown_unicast', YLeaf(YType.empty, 'flooding-unknown-unicast')),
                                ('igmp_snooping_disable', YLeaf(YType.empty, 'igmp-snooping-disable')),
                                ('transport_mode', YLeaf(YType.enumeration, 'transport-mode')),
                                ('mld_snooping', YLeaf(YType.str, 'mld-snooping')),
                                ('bridge_domain_mtu', YLeaf(YType.uint32, 'bridge-domain-mtu')),
                                ('dhcp', YLeaf(YType.str, 'dhcp')),
                                ('bridge_description', YLeaf(YType.str, 'bridge-description')),
                                ('igmp_snooping', YLeaf(YType.str, 'igmp-snooping')),
                                ('flooding', YLeaf(YType.empty, 'flooding')),
                            ])
                            self.name = None
                            self.coupled_mode = None
                            self.shutdown = None
                            self.flooding_unknown_unicast = None
                            self.igmp_snooping_disable = None
                            self.transport_mode = None
                            self.mld_snooping = None
                            self.bridge_domain_mtu = None
                            self.dhcp = None
                            self.bridge_description = None
                            self.igmp_snooping = None
                            self.flooding = None

                            self.bd_storm_controls = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls()
                            self.bd_storm_controls.parent = self
                            self._children_name_map["bd_storm_controls"] = "bd-storm-controls"
                            self._children_yang_names.add("bd-storm-controls")

                            self.member_vnis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis()
                            self.member_vnis.parent = self
                            self._children_name_map["member_vnis"] = "member-vnis"
                            self._children_yang_names.add("member-vnis")

                            self.bridge_domain_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac()
                            self.bridge_domain_mac.parent = self
                            self._children_name_map["bridge_domain_mac"] = "bridge-domain-mac"
                            self._children_yang_names.add("bridge-domain-mac")

                            self.nv_satellite = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite()
                            self.nv_satellite.parent = self
                            self._children_name_map["nv_satellite"] = "nv-satellite"
                            self._children_yang_names.add("nv-satellite")

                            self.bridge_domain_pbb = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb()
                            self.bridge_domain_pbb.parent = self
                            self._children_name_map["bridge_domain_pbb"] = "bridge-domain-pbb"
                            self._children_yang_names.add("bridge-domain-pbb")

                            self.bridge_domain_evis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis()
                            self.bridge_domain_evis.parent = self
                            self._children_name_map["bridge_domain_evis"] = "bridge-domain-evis"
                            self._children_yang_names.add("bridge-domain-evis")

                            self.access_vfis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis()
                            self.access_vfis.parent = self
                            self._children_name_map["access_vfis"] = "access-vfis"
                            self._children_yang_names.add("access-vfis")

                            self.bd_pseudowires = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires()
                            self.bd_pseudowires.parent = self
                            self._children_name_map["bd_pseudowires"] = "bd-pseudowires"
                            self._children_yang_names.add("bd-pseudowires")

                            self.vfis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis()
                            self.vfis.parent = self
                            self._children_name_map["vfis"] = "vfis"
                            self._children_yang_names.add("vfis")

                            self.bd_attachment_circuits = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits()
                            self.bd_attachment_circuits.parent = self
                            self._children_name_map["bd_attachment_circuits"] = "bd-attachment-circuits"
                            self._children_yang_names.add("bd-attachment-circuits")

                            self.bd_pseudowire_evpns = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns()
                            self.bd_pseudowire_evpns.parent = self
                            self._children_name_map["bd_pseudowire_evpns"] = "bd-pseudowire-evpns"
                            self._children_yang_names.add("bd-pseudowire-evpns")

                            self.ip_source_guard = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard()
                            self.ip_source_guard.parent = self
                            self._children_name_map["ip_source_guard"] = "ip-source-guard"
                            self._children_yang_names.add("ip-source-guard")

                            self.dai = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai()
                            self.dai.parent = self
                            self._children_name_map["dai"] = "dai"
                            self._children_yang_names.add("dai")

                            self.routed_interfaces = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces()
                            self.routed_interfaces.parent = self
                            self._children_name_map["routed_interfaces"] = "routed-interfaces"
                            self._children_yang_names.add("routed-interfaces")
                            self._segment_path = lambda: "bridge-domain" + "[name='" + str(self.name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain, ['name', 'coupled_mode', 'shutdown', 'flooding_unknown_unicast', 'igmp_snooping_disable', 'transport_mode', 'mld_snooping', 'bridge_domain_mtu', 'dhcp', 'bridge_description', 'igmp_snooping', 'flooding'], name, value)


                        class BdStormControls(Entity):
                            """
                            Storm Control
                            
                            .. attribute:: bd_storm_control
                            
                            	Storm Control Type
                            	**type**\: list of  		 :py:class:`BdStormControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls, self).__init__()

                                self.yang_name = "bd-storm-controls"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("bd-storm-control", ("bd_storm_control", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl))])
                                self._leafs = OrderedDict()

                                self.bd_storm_control = YList(self)
                                self._segment_path = lambda: "bd-storm-controls"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls, [], name, value)


                            class BdStormControl(Entity):
                                """
                                Storm Control Type
                                
                                .. attribute:: sctype  (key)
                                
                                	Storm Control Type
                                	**type**\:  :py:class:`StormControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.StormControl>`
                                
                                .. attribute:: storm_control_unit
                                
                                	Specify units for Storm Control Configuration
                                	**type**\:  :py:class:`StormControlUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl, self).__init__()

                                    self.yang_name = "bd-storm-control"
                                    self.yang_parent_name = "bd-storm-controls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['sctype']
                                    self._child_container_classes = OrderedDict([("storm-control-unit", ("storm_control_unit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('sctype', YLeaf(YType.enumeration, 'sctype')),
                                    ])
                                    self.sctype = None

                                    self.storm_control_unit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit()
                                    self.storm_control_unit.parent = self
                                    self._children_name_map["storm_control_unit"] = "storm-control-unit"
                                    self._children_yang_names.add("storm-control-unit")
                                    self._segment_path = lambda: "bd-storm-control" + "[sctype='" + str(self.sctype) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl, ['sctype'], name, value)


                                class StormControlUnit(Entity):
                                    """
                                    Specify units for Storm Control Configuration
                                    
                                    .. attribute:: kbits_per_sec
                                    
                                    	Kilobits Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                    	**type**\: int
                                    
                                    	**range:** 64..1280000
                                    
                                    	**units**\: kbit/s
                                    
                                    .. attribute:: pkts_per_sec
                                    
                                    	Packets Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                    	**type**\: int
                                    
                                    	**range:** 1..160000
                                    
                                    	**units**\: packet/s
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit, self).__init__()

                                        self.yang_name = "storm-control-unit"
                                        self.yang_parent_name = "bd-storm-control"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('kbits_per_sec', YLeaf(YType.uint32, 'kbits-per-sec')),
                                            ('pkts_per_sec', YLeaf(YType.uint32, 'pkts-per-sec')),
                                        ])
                                        self.kbits_per_sec = None
                                        self.pkts_per_sec = None
                                        self._segment_path = lambda: "storm-control-unit"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit, ['kbits_per_sec', 'pkts_per_sec'], name, value)


                        class MemberVnis(Entity):
                            """
                            Bridge Domain VxLAN Network Identifier
                            Table
                            
                            .. attribute:: member_vni
                            
                            	Bridge Domain Member VxLAN Network Identifier 
                            	**type**\: list of  		 :py:class:`MemberVni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis, self).__init__()

                                self.yang_name = "member-vnis"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("member-vni", ("member_vni", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni))])
                                self._leafs = OrderedDict()

                                self.member_vni = YList(self)
                                self._segment_path = lambda: "member-vnis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis, [], name, value)


                            class MemberVni(Entity):
                                """
                                Bridge Domain Member VxLAN Network
                                Identifier 
                                
                                .. attribute:: vni  (key)
                                
                                	VxLAN Network Identifier number
                                	**type**\: int
                                
                                	**range:** 1..16777215
                                
                                .. attribute:: member_vni_static_mac_addresses
                                
                                	Static Mac Address Table
                                	**type**\:  :py:class:`MemberVniStaticMacAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni, self).__init__()

                                    self.yang_name = "member-vni"
                                    self.yang_parent_name = "member-vnis"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['vni']
                                    self._child_container_classes = OrderedDict([("member-vni-static-mac-addresses", ("member_vni_static_mac_addresses", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('vni', YLeaf(YType.uint32, 'vni')),
                                    ])
                                    self.vni = None

                                    self.member_vni_static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses()
                                    self.member_vni_static_mac_addresses.parent = self
                                    self._children_name_map["member_vni_static_mac_addresses"] = "member-vni-static-mac-addresses"
                                    self._children_yang_names.add("member-vni-static-mac-addresses")
                                    self._segment_path = lambda: "member-vni" + "[vni='" + str(self.vni) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni, ['vni'], name, value)


                                class MemberVniStaticMacAddresses(Entity):
                                    """
                                    Static Mac Address Table
                                    
                                    .. attribute:: member_vni_static_mac_address
                                    
                                    	Static Mac Address Configuration
                                    	**type**\: list of  		 :py:class:`MemberVniStaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses, self).__init__()

                                        self.yang_name = "member-vni-static-mac-addresses"
                                        self.yang_parent_name = "member-vni"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("member-vni-static-mac-address", ("member_vni_static_mac_address", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress))])
                                        self._leafs = OrderedDict()

                                        self.member_vni_static_mac_address = YList(self)
                                        self._segment_path = lambda: "member-vni-static-mac-addresses"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses, [], name, value)


                                    class MemberVniStaticMacAddress(Entity):
                                        """
                                        Static Mac Address Configuration
                                        
                                        .. attribute:: mac_address  (key)
                                        
                                        	Static MAC address
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        .. attribute:: next_hop_ip
                                        
                                        	Enable Static Mac Address Configuration
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress, self).__init__()

                                            self.yang_name = "member-vni-static-mac-address"
                                            self.yang_parent_name = "member-vni-static-mac-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['mac_address']
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mac_address', YLeaf(YType.str, 'mac-address')),
                                                ('next_hop_ip', YLeaf(YType.str, 'next-hop-ip')),
                                            ])
                                            self.mac_address = None
                                            self.next_hop_ip = None
                                            self._segment_path = lambda: "member-vni-static-mac-address" + "[mac-address='" + str(self.mac_address) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress, ['mac_address', 'next_hop_ip'], name, value)


                        class BridgeDomainMac(Entity):
                            """
                            MAC configuration commands
                            
                            .. attribute:: bd_mac_limit
                            
                            	MAC\-Limit configuration commands
                            	**type**\:  :py:class:`BdMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit>`
                            
                            .. attribute:: bd_mac_filters
                            
                            	Filter Mac Address
                            	**type**\:  :py:class:`BdMacFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters>`
                            
                            .. attribute:: mac_secure
                            
                            	MAC Secure
                            	**type**\:  :py:class:`MacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure>`
                            
                            .. attribute:: bd_mac_aging
                            
                            	MAC\-Aging configuration commands
                            	**type**\:  :py:class:`BdMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging>`
                            
                            .. attribute:: bd_mac_withdraw_relay
                            
                            	Mac withdraw sent from access PW to access PW
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bd_mac_withdraw_access_pw_disable
                            
                            	MAC withdraw on Access PW
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bd_mac_port_down_flush
                            
                            	Disable MAC Flush when Port goes Down
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bd_mac_withdraw
                            
                            	Disable Mac Withdraw
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bd_mac_withdraw_behavior
                            
                            	MAC withdraw sent on bridge port down
                            	**type**\:  :py:class:`MacWithdrawBehavior <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacWithdrawBehavior>`
                            
                            .. attribute:: bd_mac_learn
                            
                            	Mac Learning Type
                            	**type**\:  :py:class:`BdmacLearn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BdmacLearn>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac, self).__init__()

                                self.yang_name = "bridge-domain-mac"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("bd-mac-limit", ("bd_mac_limit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit)), ("bd-mac-filters", ("bd_mac_filters", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters)), ("mac-secure", ("mac_secure", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure)), ("bd-mac-aging", ("bd_mac_aging", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('bd_mac_withdraw_relay', YLeaf(YType.empty, 'bd-mac-withdraw-relay')),
                                    ('bd_mac_withdraw_access_pw_disable', YLeaf(YType.empty, 'bd-mac-withdraw-access-pw-disable')),
                                    ('bd_mac_port_down_flush', YLeaf(YType.empty, 'bd-mac-port-down-flush')),
                                    ('bd_mac_withdraw', YLeaf(YType.empty, 'bd-mac-withdraw')),
                                    ('bd_mac_withdraw_behavior', YLeaf(YType.enumeration, 'bd-mac-withdraw-behavior')),
                                    ('bd_mac_learn', YLeaf(YType.enumeration, 'bd-mac-learn')),
                                ])
                                self.bd_mac_withdraw_relay = None
                                self.bd_mac_withdraw_access_pw_disable = None
                                self.bd_mac_port_down_flush = None
                                self.bd_mac_withdraw = None
                                self.bd_mac_withdraw_behavior = None
                                self.bd_mac_learn = None

                                self.bd_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit()
                                self.bd_mac_limit.parent = self
                                self._children_name_map["bd_mac_limit"] = "bd-mac-limit"
                                self._children_yang_names.add("bd-mac-limit")

                                self.bd_mac_filters = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters()
                                self.bd_mac_filters.parent = self
                                self._children_name_map["bd_mac_filters"] = "bd-mac-filters"
                                self._children_yang_names.add("bd-mac-filters")

                                self.mac_secure = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure()
                                self.mac_secure.parent = self
                                self._children_name_map["mac_secure"] = "mac-secure"
                                self._children_yang_names.add("mac-secure")

                                self.bd_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging()
                                self.bd_mac_aging.parent = self
                                self._children_name_map["bd_mac_aging"] = "bd-mac-aging"
                                self._children_yang_names.add("bd-mac-aging")
                                self._segment_path = lambda: "bridge-domain-mac"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac, ['bd_mac_withdraw_relay', 'bd_mac_withdraw_access_pw_disable', 'bd_mac_port_down_flush', 'bd_mac_withdraw', 'bd_mac_withdraw_behavior', 'bd_mac_learn'], name, value)


                            class BdMacLimit(Entity):
                                """
                                MAC\-Limit configuration commands
                                
                                .. attribute:: bd_mac_limit_action
                                
                                	MAC address limit enforcement action
                                	**type**\:  :py:class:`MacLimitAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction>`
                                
                                .. attribute:: bd_mac_limit_notif
                                
                                	Mac Address Limit Notification
                                	**type**\:  :py:class:`MacNotification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotification>`
                                
                                .. attribute:: bd_mac_limit_max
                                
                                	Number of MAC addresses after which MAC limit action is taken
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit, self).__init__()

                                    self.yang_name = "bd-mac-limit"
                                    self.yang_parent_name = "bridge-domain-mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('bd_mac_limit_action', YLeaf(YType.enumeration, 'bd-mac-limit-action')),
                                        ('bd_mac_limit_notif', YLeaf(YType.enumeration, 'bd-mac-limit-notif')),
                                        ('bd_mac_limit_max', YLeaf(YType.uint32, 'bd-mac-limit-max')),
                                    ])
                                    self.bd_mac_limit_action = None
                                    self.bd_mac_limit_notif = None
                                    self.bd_mac_limit_max = None
                                    self._segment_path = lambda: "bd-mac-limit"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit, ['bd_mac_limit_action', 'bd_mac_limit_notif', 'bd_mac_limit_max'], name, value)


                            class BdMacFilters(Entity):
                                """
                                Filter Mac Address
                                
                                .. attribute:: bd_mac_filter
                                
                                	Static MAC address
                                	**type**\: list of  		 :py:class:`BdMacFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters, self).__init__()

                                    self.yang_name = "bd-mac-filters"
                                    self.yang_parent_name = "bridge-domain-mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("bd-mac-filter", ("bd_mac_filter", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter))])
                                    self._leafs = OrderedDict()

                                    self.bd_mac_filter = YList(self)
                                    self._segment_path = lambda: "bd-mac-filters"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters, [], name, value)


                                class BdMacFilter(Entity):
                                    """
                                    Static MAC address
                                    
                                    .. attribute:: address  (key)
                                    
                                    	Static MAC address
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    .. attribute:: drop
                                    
                                    	MAC address for filtering
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter, self).__init__()

                                        self.yang_name = "bd-mac-filter"
                                        self.yang_parent_name = "bd-mac-filters"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['address']
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', YLeaf(YType.str, 'address')),
                                            ('drop', YLeaf(YType.empty, 'drop')),
                                        ])
                                        self.address = None
                                        self.drop = None
                                        self._segment_path = lambda: "bd-mac-filter" + "[address='" + str(self.address) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter, ['address', 'drop'], name, value)


                            class MacSecure(Entity):
                                """
                                MAC Secure
                                
                                .. attribute:: logging
                                
                                	MAC Secure Logging
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: action
                                
                                	MAC secure enforcement action
                                	**type**\:  :py:class:`MacSecureAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacSecureAction>`
                                
                                .. attribute:: enable
                                
                                	Enable MAC Secure
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: threshold
                                
                                	MAC Secure Threshold
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure, self).__init__()

                                    self.yang_name = "mac-secure"
                                    self.yang_parent_name = "bridge-domain-mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('logging', YLeaf(YType.empty, 'logging')),
                                        ('action', YLeaf(YType.enumeration, 'action')),
                                        ('enable', YLeaf(YType.empty, 'enable')),
                                        ('threshold', YLeaf(YType.empty, 'threshold')),
                                    ])
                                    self.logging = None
                                    self.action = None
                                    self.enable = None
                                    self.threshold = None
                                    self._segment_path = lambda: "mac-secure"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure, ['logging', 'action', 'enable', 'threshold'], name, value)


                            class BdMacAging(Entity):
                                """
                                MAC\-Aging configuration commands
                                
                                .. attribute:: bd_mac_aging_type
                                
                                	MAC address aging type
                                	**type**\:  :py:class:`MacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAging>`
                                
                                .. attribute:: bd_mac_aging_time
                                
                                	Mac Aging Time
                                	**type**\: int
                                
                                	**range:** 300..30000
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging, self).__init__()

                                    self.yang_name = "bd-mac-aging"
                                    self.yang_parent_name = "bridge-domain-mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('bd_mac_aging_type', YLeaf(YType.enumeration, 'bd-mac-aging-type')),
                                        ('bd_mac_aging_time', YLeaf(YType.uint32, 'bd-mac-aging-time')),
                                    ])
                                    self.bd_mac_aging_type = None
                                    self.bd_mac_aging_time = None
                                    self._segment_path = lambda: "bd-mac-aging"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging, ['bd_mac_aging_type', 'bd_mac_aging_time'], name, value)


                        class NvSatellite(Entity):
                            """
                            nV Satellite
                            
                            .. attribute:: offload_ipv4_multicast_enable
                            
                            	Enable IPv4 Multicast Offload to Satellite Nodes
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: enable
                            
                            	Enable nV Satellite Settings
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite, self).__init__()

                                self.yang_name = "nv-satellite"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('offload_ipv4_multicast_enable', YLeaf(YType.empty, 'offload-ipv4-multicast-enable')),
                                    ('enable', YLeaf(YType.empty, 'enable')),
                                ])
                                self.offload_ipv4_multicast_enable = None
                                self.enable = None
                                self._segment_path = lambda: "nv-satellite"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite, ['offload_ipv4_multicast_enable', 'enable'], name, value)


                        class BridgeDomainPbb(Entity):
                            """
                            Bridge Domain PBB
                            
                            .. attribute:: pbb_edges
                            
                            	PBB Edge
                            	**type**\:  :py:class:`PbbEdges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges>`
                            
                            .. attribute:: pbb_core
                            
                            	PBB Core
                            	**type**\:  :py:class:`PbbCore <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb, self).__init__()

                                self.yang_name = "bridge-domain-pbb"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("pbb-edges", ("pbb_edges", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges)), ("pbb-core", ("pbb_core", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.pbb_edges = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges()
                                self.pbb_edges.parent = self
                                self._children_name_map["pbb_edges"] = "pbb-edges"
                                self._children_yang_names.add("pbb-edges")

                                self.pbb_core = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore()
                                self.pbb_core.parent = self
                                self._children_name_map["pbb_core"] = "pbb-core"
                                self._children_yang_names.add("pbb-core")
                                self._segment_path = lambda: "bridge-domain-pbb"


                            class PbbEdges(Entity):
                                """
                                PBB Edge
                                
                                .. attribute:: pbb_edge
                                
                                	Configure BD as PBB Edge with ISID and associated PBB Core BD
                                	**type**\: list of  		 :py:class:`PbbEdge <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges, self).__init__()

                                    self.yang_name = "pbb-edges"
                                    self.yang_parent_name = "bridge-domain-pbb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("pbb-edge", ("pbb_edge", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge))])
                                    self._leafs = OrderedDict()

                                    self.pbb_edge = YList(self)
                                    self._segment_path = lambda: "pbb-edges"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges, [], name, value)


                                class PbbEdge(Entity):
                                    """
                                    Configure BD as PBB Edge with ISID and
                                    associated PBB Core BD
                                    
                                    .. attribute:: isid  (key)
                                    
                                    	ISID
                                    	**type**\: int
                                    
                                    	**range:** 256..16777214
                                    
                                    .. attribute:: core_bd_name  (key)
                                    
                                    	Core BD Name
                                    	**type**\: str
                                    
                                    	**length:** 1..27
                                    
                                    .. attribute:: pbb_edge_split_horizon_group
                                    
                                    	Split Horizon Group
                                    	**type**\:  :py:class:`PbbEdgeSplitHorizonGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup>`
                                    
                                    .. attribute:: pbb_static_mac_mappings
                                    
                                    	PBB Static Mac Address Mapping Table
                                    	**type**\:  :py:class:`PbbStaticMacMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings>`
                                    
                                    .. attribute:: pbb_edge_dhcp_profile
                                    
                                    	Attach a DHCP profile
                                    	**type**\:  :py:class:`PbbEdgeDhcpProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile>`
                                    
                                    .. attribute:: pbb_edge_mac
                                    
                                    	MAC configuration commands
                                    	**type**\:  :py:class:`PbbEdgeMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac>`
                                    
                                    .. attribute:: pbb_edge_igmp_profile
                                    
                                    	Attach a IGMP Snooping profile
                                    	**type**\: str
                                    
                                    	**length:** 1..32
                                    
                                    .. attribute:: unknown_unicast_bmac
                                    
                                    	Configure Unknown Unicast BMAC address for PBB Edge Port
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge, self).__init__()

                                        self.yang_name = "pbb-edge"
                                        self.yang_parent_name = "pbb-edges"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['isid','core_bd_name']
                                        self._child_container_classes = OrderedDict([("pbb-edge-split-horizon-group", ("pbb_edge_split_horizon_group", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup)), ("pbb-static-mac-mappings", ("pbb_static_mac_mappings", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings)), ("pbb-edge-dhcp-profile", ("pbb_edge_dhcp_profile", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile)), ("pbb-edge-mac", ("pbb_edge_mac", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('isid', YLeaf(YType.uint32, 'isid')),
                                            ('core_bd_name', YLeaf(YType.str, 'core-bd-name')),
                                            ('pbb_edge_igmp_profile', YLeaf(YType.str, 'pbb-edge-igmp-profile')),
                                            ('unknown_unicast_bmac', YLeaf(YType.str, 'unknown-unicast-bmac')),
                                        ])
                                        self.isid = None
                                        self.core_bd_name = None
                                        self.pbb_edge_igmp_profile = None
                                        self.unknown_unicast_bmac = None

                                        self.pbb_edge_split_horizon_group = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup()
                                        self.pbb_edge_split_horizon_group.parent = self
                                        self._children_name_map["pbb_edge_split_horizon_group"] = "pbb-edge-split-horizon-group"
                                        self._children_yang_names.add("pbb-edge-split-horizon-group")

                                        self.pbb_static_mac_mappings = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings()
                                        self.pbb_static_mac_mappings.parent = self
                                        self._children_name_map["pbb_static_mac_mappings"] = "pbb-static-mac-mappings"
                                        self._children_yang_names.add("pbb-static-mac-mappings")

                                        self.pbb_edge_dhcp_profile = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile()
                                        self.pbb_edge_dhcp_profile.parent = self
                                        self._children_name_map["pbb_edge_dhcp_profile"] = "pbb-edge-dhcp-profile"
                                        self._children_yang_names.add("pbb-edge-dhcp-profile")

                                        self.pbb_edge_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac()
                                        self.pbb_edge_mac.parent = self
                                        self._children_name_map["pbb_edge_mac"] = "pbb-edge-mac"
                                        self._children_yang_names.add("pbb-edge-mac")
                                        self._segment_path = lambda: "pbb-edge" + "[isid='" + str(self.isid) + "']" + "[core-bd-name='" + str(self.core_bd_name) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge, ['isid', 'core_bd_name', 'pbb_edge_igmp_profile', 'unknown_unicast_bmac'], name, value)


                                    class PbbEdgeSplitHorizonGroup(Entity):
                                        """
                                        Split Horizon Group
                                        
                                        .. attribute:: disable
                                        
                                        	Disable split horizon group
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup, self).__init__()

                                            self.yang_name = "pbb-edge-split-horizon-group"
                                            self.yang_parent_name = "pbb-edge"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('disable', YLeaf(YType.empty, 'disable')),
                                            ])
                                            self.disable = None
                                            self._segment_path = lambda: "pbb-edge-split-horizon-group"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup, ['disable'], name, value)


                                    class PbbStaticMacMappings(Entity):
                                        """
                                        PBB Static Mac Address Mapping Table
                                        
                                        .. attribute:: pbb_static_mac_mapping
                                        
                                        	PBB Static Mac Address Mapping Configuration
                                        	**type**\: list of  		 :py:class:`PbbStaticMacMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings, self).__init__()

                                            self.yang_name = "pbb-static-mac-mappings"
                                            self.yang_parent_name = "pbb-edge"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("pbb-static-mac-mapping", ("pbb_static_mac_mapping", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping))])
                                            self._leafs = OrderedDict()

                                            self.pbb_static_mac_mapping = YList(self)
                                            self._segment_path = lambda: "pbb-static-mac-mappings"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings, [], name, value)


                                        class PbbStaticMacMapping(Entity):
                                            """
                                            PBB Static Mac Address Mapping
                                            Configuration
                                            
                                            .. attribute:: address  (key)
                                            
                                            	Static MAC address
                                            	**type**\: str
                                            
                                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                            
                                            .. attribute:: pbb_static_mac_mapping_bmac
                                            
                                            	Static backbone MAC address to map with
                                            	**type**\: str
                                            
                                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping, self).__init__()

                                                self.yang_name = "pbb-static-mac-mapping"
                                                self.yang_parent_name = "pbb-static-mac-mappings"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['address']
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('address', YLeaf(YType.str, 'address')),
                                                    ('pbb_static_mac_mapping_bmac', YLeaf(YType.str, 'pbb-static-mac-mapping-bmac')),
                                                ])
                                                self.address = None
                                                self.pbb_static_mac_mapping_bmac = None
                                                self._segment_path = lambda: "pbb-static-mac-mapping" + "[address='" + str(self.address) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping, ['address', 'pbb_static_mac_mapping_bmac'], name, value)


                                    class PbbEdgeDhcpProfile(Entity):
                                        """
                                        Attach a DHCP profile
                                        
                                        .. attribute:: profile_id
                                        
                                        	Set the snooping profile
                                        	**type**\:  :py:class:`InterfaceProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile>`
                                        
                                        .. attribute:: dhcp_snooping_id
                                        
                                        	Disable DHCP snooping
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile, self).__init__()

                                            self.yang_name = "pbb-edge-dhcp-profile"
                                            self.yang_parent_name = "pbb-edge"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('profile_id', YLeaf(YType.enumeration, 'profile-id')),
                                                ('dhcp_snooping_id', YLeaf(YType.str, 'dhcp-snooping-id')),
                                            ])
                                            self.profile_id = None
                                            self.dhcp_snooping_id = None
                                            self._segment_path = lambda: "pbb-edge-dhcp-profile"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile, ['profile_id', 'dhcp_snooping_id'], name, value)


                                    class PbbEdgeMac(Entity):
                                        """
                                        MAC configuration commands
                                        
                                        .. attribute:: pbb_edge_mac_limit
                                        
                                        	MAC\-Limit configuration commands
                                        	**type**\:  :py:class:`PbbEdgeMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit>`
                                        
                                        .. attribute:: pbb_edge_mac_aging
                                        
                                        	MAC\-Aging configuration commands
                                        	**type**\:  :py:class:`PbbEdgeMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging>`
                                        
                                        .. attribute:: pbb_edge_mac_secure
                                        
                                        	MAC Secure
                                        	**type**\:  :py:class:`PbbEdgeMacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure>`
                                        
                                        .. attribute:: pbb_edge_mac_learning
                                        
                                        	Enable Mac Learning
                                        	**type**\:  :py:class:`MacLearn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLearn>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac, self).__init__()

                                            self.yang_name = "pbb-edge-mac"
                                            self.yang_parent_name = "pbb-edge"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("pbb-edge-mac-limit", ("pbb_edge_mac_limit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit)), ("pbb-edge-mac-aging", ("pbb_edge_mac_aging", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging)), ("pbb-edge-mac-secure", ("pbb_edge_mac_secure", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('pbb_edge_mac_learning', YLeaf(YType.enumeration, 'pbb-edge-mac-learning')),
                                            ])
                                            self.pbb_edge_mac_learning = None

                                            self.pbb_edge_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit()
                                            self.pbb_edge_mac_limit.parent = self
                                            self._children_name_map["pbb_edge_mac_limit"] = "pbb-edge-mac-limit"
                                            self._children_yang_names.add("pbb-edge-mac-limit")

                                            self.pbb_edge_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging()
                                            self.pbb_edge_mac_aging.parent = self
                                            self._children_name_map["pbb_edge_mac_aging"] = "pbb-edge-mac-aging"
                                            self._children_yang_names.add("pbb-edge-mac-aging")

                                            self.pbb_edge_mac_secure = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure()
                                            self.pbb_edge_mac_secure.parent = self
                                            self._children_name_map["pbb_edge_mac_secure"] = "pbb-edge-mac-secure"
                                            self._children_yang_names.add("pbb-edge-mac-secure")
                                            self._segment_path = lambda: "pbb-edge-mac"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac, ['pbb_edge_mac_learning'], name, value)


                                        class PbbEdgeMacLimit(Entity):
                                            """
                                            MAC\-Limit configuration commands
                                            
                                            .. attribute:: pbb_edge_mac_limit_action
                                            
                                            	MAC address limit enforcement action
                                            	**type**\:  :py:class:`MacLimitAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction>`
                                            
                                            .. attribute:: pbb_edge_mac_limit_max
                                            
                                            	Number of MAC addresses after which MAC limit action is taken
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: pbb_edge_mac_limit_notif
                                            
                                            	MAC address limit notification action
                                            	**type**\:  :py:class:`MacNotification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotification>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit, self).__init__()

                                                self.yang_name = "pbb-edge-mac-limit"
                                                self.yang_parent_name = "pbb-edge-mac"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('pbb_edge_mac_limit_action', YLeaf(YType.enumeration, 'pbb-edge-mac-limit-action')),
                                                    ('pbb_edge_mac_limit_max', YLeaf(YType.uint32, 'pbb-edge-mac-limit-max')),
                                                    ('pbb_edge_mac_limit_notif', YLeaf(YType.enumeration, 'pbb-edge-mac-limit-notif')),
                                                ])
                                                self.pbb_edge_mac_limit_action = None
                                                self.pbb_edge_mac_limit_max = None
                                                self.pbb_edge_mac_limit_notif = None
                                                self._segment_path = lambda: "pbb-edge-mac-limit"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit, ['pbb_edge_mac_limit_action', 'pbb_edge_mac_limit_max', 'pbb_edge_mac_limit_notif'], name, value)


                                        class PbbEdgeMacAging(Entity):
                                            """
                                            MAC\-Aging configuration commands
                                            
                                            .. attribute:: pbb_edge_mac_aging_type
                                            
                                            	MAC address aging type
                                            	**type**\:  :py:class:`MacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAging>`
                                            
                                            .. attribute:: pbb_edge_mac_aging_time
                                            
                                            	Mac Aging Time
                                            	**type**\: int
                                            
                                            	**range:** 300..30000
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging, self).__init__()

                                                self.yang_name = "pbb-edge-mac-aging"
                                                self.yang_parent_name = "pbb-edge-mac"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('pbb_edge_mac_aging_type', YLeaf(YType.enumeration, 'pbb-edge-mac-aging-type')),
                                                    ('pbb_edge_mac_aging_time', YLeaf(YType.uint32, 'pbb-edge-mac-aging-time')),
                                                ])
                                                self.pbb_edge_mac_aging_type = None
                                                self.pbb_edge_mac_aging_time = None
                                                self._segment_path = lambda: "pbb-edge-mac-aging"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging, ['pbb_edge_mac_aging_type', 'pbb_edge_mac_aging_time'], name, value)


                                        class PbbEdgeMacSecure(Entity):
                                            """
                                            MAC Secure
                                            
                                            .. attribute:: logging
                                            
                                            	MAC Secure Logging
                                            	**type**\:  :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                            
                                            .. attribute:: disable
                                            
                                            	Disable Virtual instance port MAC Secure
                                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                            
                                            .. attribute:: action
                                            
                                            	MAC secure enforcement action
                                            	**type**\:  :py:class:`MacSecureAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacSecureAction>`
                                            
                                            .. attribute:: enable
                                            
                                            	Enable MAC Secure
                                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                            
                                            .. attribute:: accept_shutdown
                                            
                                            	Accept Virtual instance port to be shutdown on mac violation
                                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure, self).__init__()

                                                self.yang_name = "pbb-edge-mac-secure"
                                                self.yang_parent_name = "pbb-edge-mac"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('logging', YLeaf(YType.enumeration, 'logging')),
                                                    ('disable', YLeaf(YType.empty, 'disable')),
                                                    ('action', YLeaf(YType.enumeration, 'action')),
                                                    ('enable', YLeaf(YType.empty, 'enable')),
                                                    ('accept_shutdown', YLeaf(YType.empty, 'accept-shutdown')),
                                                ])
                                                self.logging = None
                                                self.disable = None
                                                self.action = None
                                                self.enable = None
                                                self.accept_shutdown = None
                                                self._segment_path = lambda: "pbb-edge-mac-secure"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure, ['logging', 'disable', 'action', 'enable', 'accept_shutdown'], name, value)


                            class PbbCore(Entity):
                                """
                                PBB Core
                                
                                .. attribute:: pbb_core_mac
                                
                                	MAC configuration commands
                                	**type**\:  :py:class:`PbbCoreMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac>`
                                
                                .. attribute:: pbb_core_evis
                                
                                	PBB Core EVI Table
                                	**type**\:  :py:class:`PbbCoreEvis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis>`
                                
                                .. attribute:: pbb_core_dhcp_profile
                                
                                	Attach a DHCP profile
                                	**type**\:  :py:class:`PbbCoreDhcpProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile>`
                                
                                .. attribute:: pbb_core_mmrp_flood_optimization
                                
                                	Enabling MMRP PBB\-VPLS Flood Optimization
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN ID to push
                                	**type**\: int
                                
                                	**range:** 1..4094
                                
                                .. attribute:: pbb_core_igmp_profile
                                
                                	Attach a IGMP Snooping profile
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                .. attribute:: enable
                                
                                	Enable Bridge Domain PBB Core Configuration
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore, self).__init__()

                                    self.yang_name = "pbb-core"
                                    self.yang_parent_name = "bridge-domain-pbb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("pbb-core-mac", ("pbb_core_mac", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac)), ("pbb-core-evis", ("pbb_core_evis", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis)), ("pbb-core-dhcp-profile", ("pbb_core_dhcp_profile", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('pbb_core_mmrp_flood_optimization', YLeaf(YType.empty, 'pbb-core-mmrp-flood-optimization')),
                                        ('vlan_id', YLeaf(YType.uint32, 'vlan-id')),
                                        ('pbb_core_igmp_profile', YLeaf(YType.str, 'pbb-core-igmp-profile')),
                                        ('enable', YLeaf(YType.empty, 'enable')),
                                    ])
                                    self.pbb_core_mmrp_flood_optimization = None
                                    self.vlan_id = None
                                    self.pbb_core_igmp_profile = None
                                    self.enable = None

                                    self.pbb_core_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac()
                                    self.pbb_core_mac.parent = self
                                    self._children_name_map["pbb_core_mac"] = "pbb-core-mac"
                                    self._children_yang_names.add("pbb-core-mac")

                                    self.pbb_core_evis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis()
                                    self.pbb_core_evis.parent = self
                                    self._children_name_map["pbb_core_evis"] = "pbb-core-evis"
                                    self._children_yang_names.add("pbb-core-evis")

                                    self.pbb_core_dhcp_profile = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile()
                                    self.pbb_core_dhcp_profile.parent = self
                                    self._children_name_map["pbb_core_dhcp_profile"] = "pbb-core-dhcp-profile"
                                    self._children_yang_names.add("pbb-core-dhcp-profile")
                                    self._segment_path = lambda: "pbb-core"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore, ['pbb_core_mmrp_flood_optimization', 'vlan_id', 'pbb_core_igmp_profile', 'enable'], name, value)


                                class PbbCoreMac(Entity):
                                    """
                                    MAC configuration commands
                                    
                                    .. attribute:: pbb_core_mac_aging
                                    
                                    	MAC\-Aging configuration commands
                                    	**type**\:  :py:class:`PbbCoreMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging>`
                                    
                                    .. attribute:: pbb_core_mac_limit
                                    
                                    	MAC\-Limit configuration commands
                                    	**type**\:  :py:class:`PbbCoreMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit>`
                                    
                                    .. attribute:: pbb_core_mac_learning
                                    
                                    	Enable Mac Learning
                                    	**type**\:  :py:class:`MacLearn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLearn>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac, self).__init__()

                                        self.yang_name = "pbb-core-mac"
                                        self.yang_parent_name = "pbb-core"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("pbb-core-mac-aging", ("pbb_core_mac_aging", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging)), ("pbb-core-mac-limit", ("pbb_core_mac_limit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('pbb_core_mac_learning', YLeaf(YType.enumeration, 'pbb-core-mac-learning')),
                                        ])
                                        self.pbb_core_mac_learning = None

                                        self.pbb_core_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging()
                                        self.pbb_core_mac_aging.parent = self
                                        self._children_name_map["pbb_core_mac_aging"] = "pbb-core-mac-aging"
                                        self._children_yang_names.add("pbb-core-mac-aging")

                                        self.pbb_core_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit()
                                        self.pbb_core_mac_limit.parent = self
                                        self._children_name_map["pbb_core_mac_limit"] = "pbb-core-mac-limit"
                                        self._children_yang_names.add("pbb-core-mac-limit")
                                        self._segment_path = lambda: "pbb-core-mac"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac, ['pbb_core_mac_learning'], name, value)


                                    class PbbCoreMacAging(Entity):
                                        """
                                        MAC\-Aging configuration commands
                                        
                                        .. attribute:: pbb_core_mac_aging_type
                                        
                                        	MAC address aging type
                                        	**type**\:  :py:class:`MacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAging>`
                                        
                                        .. attribute:: pbb_core_mac_aging_time
                                        
                                        	Mac Aging Time
                                        	**type**\: int
                                        
                                        	**range:** 300..30000
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging, self).__init__()

                                            self.yang_name = "pbb-core-mac-aging"
                                            self.yang_parent_name = "pbb-core-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('pbb_core_mac_aging_type', YLeaf(YType.enumeration, 'pbb-core-mac-aging-type')),
                                                ('pbb_core_mac_aging_time', YLeaf(YType.uint32, 'pbb-core-mac-aging-time')),
                                            ])
                                            self.pbb_core_mac_aging_type = None
                                            self.pbb_core_mac_aging_time = None
                                            self._segment_path = lambda: "pbb-core-mac-aging"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging, ['pbb_core_mac_aging_type', 'pbb_core_mac_aging_time'], name, value)


                                    class PbbCoreMacLimit(Entity):
                                        """
                                        MAC\-Limit configuration commands
                                        
                                        .. attribute:: pbb_core_mac_limit_max
                                        
                                        	Number of MAC addresses after which MAC limit action is taken
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pbb_core_mac_limit_notif
                                        
                                        	MAC address limit notification action
                                        	**type**\:  :py:class:`MacNotification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotification>`
                                        
                                        .. attribute:: pbb_core_mac_limit_action
                                        
                                        	MAC address limit enforcement action
                                        	**type**\:  :py:class:`MacLimitAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit, self).__init__()

                                            self.yang_name = "pbb-core-mac-limit"
                                            self.yang_parent_name = "pbb-core-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('pbb_core_mac_limit_max', YLeaf(YType.uint32, 'pbb-core-mac-limit-max')),
                                                ('pbb_core_mac_limit_notif', YLeaf(YType.enumeration, 'pbb-core-mac-limit-notif')),
                                                ('pbb_core_mac_limit_action', YLeaf(YType.enumeration, 'pbb-core-mac-limit-action')),
                                            ])
                                            self.pbb_core_mac_limit_max = None
                                            self.pbb_core_mac_limit_notif = None
                                            self.pbb_core_mac_limit_action = None
                                            self._segment_path = lambda: "pbb-core-mac-limit"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit, ['pbb_core_mac_limit_max', 'pbb_core_mac_limit_notif', 'pbb_core_mac_limit_action'], name, value)


                                class PbbCoreEvis(Entity):
                                    """
                                    PBB Core EVI Table
                                    
                                    .. attribute:: pbb_core_evi
                                    
                                    	PBB Core EVI
                                    	**type**\: list of  		 :py:class:`PbbCoreEvi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis, self).__init__()

                                        self.yang_name = "pbb-core-evis"
                                        self.yang_parent_name = "pbb-core"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("pbb-core-evi", ("pbb_core_evi", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi))])
                                        self._leafs = OrderedDict()

                                        self.pbb_core_evi = YList(self)
                                        self._segment_path = lambda: "pbb-core-evis"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis, [], name, value)


                                    class PbbCoreEvi(Entity):
                                        """
                                        PBB Core EVI
                                        
                                        .. attribute:: eviid  (key)
                                        
                                        	Ethernet VPN ID
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi, self).__init__()

                                            self.yang_name = "pbb-core-evi"
                                            self.yang_parent_name = "pbb-core-evis"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['eviid']
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('eviid', YLeaf(YType.uint32, 'eviid')),
                                            ])
                                            self.eviid = None
                                            self._segment_path = lambda: "pbb-core-evi" + "[eviid='" + str(self.eviid) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi, ['eviid'], name, value)


                                class PbbCoreDhcpProfile(Entity):
                                    """
                                    Attach a DHCP profile
                                    
                                    .. attribute:: profile_id
                                    
                                    	Set the snooping profile
                                    	**type**\:  :py:class:`InterfaceProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile>`
                                    
                                    .. attribute:: dhcp_snooping_id
                                    
                                    	Disable DHCP snooping
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile, self).__init__()

                                        self.yang_name = "pbb-core-dhcp-profile"
                                        self.yang_parent_name = "pbb-core"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('profile_id', YLeaf(YType.enumeration, 'profile-id')),
                                            ('dhcp_snooping_id', YLeaf(YType.str, 'dhcp-snooping-id')),
                                        ])
                                        self.profile_id = None
                                        self.dhcp_snooping_id = None
                                        self._segment_path = lambda: "pbb-core-dhcp-profile"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile, ['profile_id', 'dhcp_snooping_id'], name, value)


                        class BridgeDomainEvis(Entity):
                            """
                            Bridge Domain EVI Table
                            
                            .. attribute:: bridge_domain_evi
                            
                            	Bridge Domain EVI
                            	**type**\: list of  		 :py:class:`BridgeDomainEvi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis, self).__init__()

                                self.yang_name = "bridge-domain-evis"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("bridge-domain-evi", ("bridge_domain_evi", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi))])
                                self._leafs = OrderedDict()

                                self.bridge_domain_evi = YList(self)
                                self._segment_path = lambda: "bridge-domain-evis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis, [], name, value)


                            class BridgeDomainEvi(Entity):
                                """
                                Bridge Domain EVI
                                
                                .. attribute:: eviid  (key)
                                
                                	Ethernet VPN ID
                                	**type**\: int
                                
                                	**range:** 1..65534
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi, self).__init__()

                                    self.yang_name = "bridge-domain-evi"
                                    self.yang_parent_name = "bridge-domain-evis"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['eviid']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('eviid', YLeaf(YType.uint32, 'eviid')),
                                    ])
                                    self.eviid = None
                                    self._segment_path = lambda: "bridge-domain-evi" + "[eviid='" + str(self.eviid) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi, ['eviid'], name, value)


                        class AccessVfis(Entity):
                            """
                            Specify the access virtual forwarding
                            interface name
                            
                            .. attribute:: access_vfi
                            
                            	Name of the Acess Virtual Forwarding Interface
                            	**type**\: list of  		 :py:class:`AccessVfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis, self).__init__()

                                self.yang_name = "access-vfis"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("access-vfi", ("access_vfi", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi))])
                                self._leafs = OrderedDict()

                                self.access_vfi = YList(self)
                                self._segment_path = lambda: "access-vfis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis, [], name, value)


                            class AccessVfi(Entity):
                                """
                                Name of the Acess Virtual Forwarding
                                Interface
                                
                                .. attribute:: name  (key)
                                
                                	Name of the AccessVirtual Forwarding Interface
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                .. attribute:: access_vfi_pseudowires
                                
                                	List of pseudowires
                                	**type**\:  :py:class:`AccessVfiPseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires>`
                                
                                .. attribute:: access_vfi_shutdown
                                
                                	shutdown the AccessVfi
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi, self).__init__()

                                    self.yang_name = "access-vfi"
                                    self.yang_parent_name = "access-vfis"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['name']
                                    self._child_container_classes = OrderedDict([("access-vfi-pseudowires", ("access_vfi_pseudowires", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('name', YLeaf(YType.str, 'name')),
                                        ('access_vfi_shutdown', YLeaf(YType.empty, 'access-vfi-shutdown')),
                                    ])
                                    self.name = None
                                    self.access_vfi_shutdown = None

                                    self.access_vfi_pseudowires = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires()
                                    self.access_vfi_pseudowires.parent = self
                                    self._children_name_map["access_vfi_pseudowires"] = "access-vfi-pseudowires"
                                    self._children_yang_names.add("access-vfi-pseudowires")
                                    self._segment_path = lambda: "access-vfi" + "[name='" + str(self.name) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi, ['name', 'access_vfi_shutdown'], name, value)


                                class AccessVfiPseudowires(Entity):
                                    """
                                    List of pseudowires
                                    
                                    .. attribute:: access_vfi_pseudowire
                                    
                                    	Pseudowire configuration
                                    	**type**\: list of  		 :py:class:`AccessVfiPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires, self).__init__()

                                        self.yang_name = "access-vfi-pseudowires"
                                        self.yang_parent_name = "access-vfi"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("access-vfi-pseudowire", ("access_vfi_pseudowire", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire))])
                                        self._leafs = OrderedDict()

                                        self.access_vfi_pseudowire = YList(self)
                                        self._segment_path = lambda: "access-vfi-pseudowires"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires, [], name, value)


                                    class AccessVfiPseudowire(Entity):
                                        """
                                        Pseudowire configuration
                                        
                                        .. attribute:: neighbor  (key)
                                        
                                        	Neighbor IP address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: pseudowire_id  (key)
                                        
                                        	Pseudowire ID
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: access_vfi_pseudowire_static_mac_addresses
                                        
                                        	Static Mac Address Table
                                        	**type**\:  :py:class:`AccessVfiPseudowireStaticMacAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses>`
                                        
                                        .. attribute:: access_vfi_pw_class
                                        
                                        	Pseudowire class template name to use for this pseudowire
                                        	**type**\: str
                                        
                                        	**length:** 1..32
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire, self).__init__()

                                            self.yang_name = "access-vfi-pseudowire"
                                            self.yang_parent_name = "access-vfi-pseudowires"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['neighbor','pseudowire_id']
                                            self._child_container_classes = OrderedDict([("access-vfi-pseudowire-static-mac-addresses", ("access_vfi_pseudowire_static_mac_addresses", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('neighbor', YLeaf(YType.str, 'neighbor')),
                                                ('pseudowire_id', YLeaf(YType.uint32, 'pseudowire-id')),
                                                ('access_vfi_pw_class', YLeaf(YType.str, 'access-vfi-pw-class')),
                                            ])
                                            self.neighbor = None
                                            self.pseudowire_id = None
                                            self.access_vfi_pw_class = None

                                            self.access_vfi_pseudowire_static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses()
                                            self.access_vfi_pseudowire_static_mac_addresses.parent = self
                                            self._children_name_map["access_vfi_pseudowire_static_mac_addresses"] = "access-vfi-pseudowire-static-mac-addresses"
                                            self._children_yang_names.add("access-vfi-pseudowire-static-mac-addresses")
                                            self._segment_path = lambda: "access-vfi-pseudowire" + "[neighbor='" + str(self.neighbor) + "']" + "[pseudowire-id='" + str(self.pseudowire_id) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire, ['neighbor', 'pseudowire_id', 'access_vfi_pw_class'], name, value)


                                        class AccessVfiPseudowireStaticMacAddresses(Entity):
                                            """
                                            Static Mac Address Table
                                            
                                            .. attribute:: access_vfi_pseudowire_static_mac_address
                                            
                                            	Static Mac Address Configuration
                                            	**type**\: list of  		 :py:class:`AccessVfiPseudowireStaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses, self).__init__()

                                                self.yang_name = "access-vfi-pseudowire-static-mac-addresses"
                                                self.yang_parent_name = "access-vfi-pseudowire"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([("access-vfi-pseudowire-static-mac-address", ("access_vfi_pseudowire_static_mac_address", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress))])
                                                self._leafs = OrderedDict()

                                                self.access_vfi_pseudowire_static_mac_address = YList(self)
                                                self._segment_path = lambda: "access-vfi-pseudowire-static-mac-addresses"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses, [], name, value)


                                            class AccessVfiPseudowireStaticMacAddress(Entity):
                                                """
                                                Static Mac Address Configuration
                                                
                                                .. attribute:: address  (key)
                                                
                                                	Static MAC address
                                                	**type**\: str
                                                
                                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2017-06-26'

                                                def __init__(self):
                                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress, self).__init__()

                                                    self.yang_name = "access-vfi-pseudowire-static-mac-address"
                                                    self.yang_parent_name = "access-vfi-pseudowire-static-mac-addresses"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['address']
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('address', YLeaf(YType.str, 'address')),
                                                    ])
                                                    self.address = None
                                                    self._segment_path = lambda: "access-vfi-pseudowire-static-mac-address" + "[address='" + str(self.address) + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress, ['address'], name, value)


                        class BdPseudowires(Entity):
                            """
                            List of pseudowires
                            
                            .. attribute:: bd_pseudowire
                            
                            	Pseudowire configuration
                            	**type**\: list of  		 :py:class:`BdPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires, self).__init__()

                                self.yang_name = "bd-pseudowires"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("bd-pseudowire", ("bd_pseudowire", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire))])
                                self._leafs = OrderedDict()

                                self.bd_pseudowire = YList(self)
                                self._segment_path = lambda: "bd-pseudowires"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires, [], name, value)


                            class BdPseudowire(Entity):
                                """
                                Pseudowire configuration
                                
                                .. attribute:: neighbor  (key)
                                
                                	Neighbor IP address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: pseudowire_id  (key)
                                
                                	Pseudowire ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: pseudowire_dai
                                
                                	Access Pseudowire Dynamic ARP Inspection
                                	**type**\:  :py:class:`PseudowireDai <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai>`
                                
                                .. attribute:: bdpw_storm_control_types
                                
                                	Storm Control
                                	**type**\:  :py:class:`BdpwStormControlTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes>`
                                
                                .. attribute:: pseudowire_profile
                                
                                	Attach a DHCP profile
                                	**type**\:  :py:class:`PseudowireProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile>`
                                
                                .. attribute:: bd_pw_static_mac_addresses
                                
                                	Static Mac Address Table
                                	**type**\:  :py:class:`BdPwStaticMacAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses>`
                                
                                .. attribute:: pseudowire_ip_source_guard
                                
                                	IP Source Guard
                                	**type**\:  :py:class:`PseudowireIpSourceGuard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard>`
                                
                                .. attribute:: pseudowire_mac
                                
                                	Bridge\-domain Pseudowire MAC configuration commands
                                	**type**\:  :py:class:`PseudowireMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac>`
                                
                                .. attribute:: bd_pw_split_horizon
                                
                                	Split Horizon
                                	**type**\:  :py:class:`BdPwSplitHorizon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon>`
                                
                                .. attribute:: bd_pw_mpls_static_labels
                                
                                	MPLS static labels
                                	**type**\:  :py:class:`BdPwMplsStaticLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels>`
                                
                                .. attribute:: bridge_domain_backup_pseudowires
                                
                                	List of pseudowires
                                	**type**\:  :py:class:`BridgeDomainBackupPseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires>`
                                
                                .. attribute:: pseudowire_mld_snoop
                                
                                	Attach a MLD Snooping profile
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                .. attribute:: pseudowire_igmp_snoop
                                
                                	Attach a IGMP Snooping profile
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                .. attribute:: pseudowire_flooding
                                
                                	Bridge\-domain Pseudowire flooding
                                	**type**\:  :py:class:`InterfaceTrafficFlood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFlood>`
                                
                                .. attribute:: bd_pw_class
                                
                                	PW class template name to use for this pseudowire
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                .. attribute:: pseudowire_flooding_unknown_unicast
                                
                                	Bridge\-domain Pseudowire flooding Unknown Unicast
                                	**type**\:  :py:class:`InterfaceTrafficFlood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFlood>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire, self).__init__()

                                    self.yang_name = "bd-pseudowire"
                                    self.yang_parent_name = "bd-pseudowires"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['neighbor','pseudowire_id']
                                    self._child_container_classes = OrderedDict([("pseudowire-dai", ("pseudowire_dai", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai)), ("bdpw-storm-control-types", ("bdpw_storm_control_types", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes)), ("pseudowire-profile", ("pseudowire_profile", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile)), ("bd-pw-static-mac-addresses", ("bd_pw_static_mac_addresses", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses)), ("pseudowire-ip-source-guard", ("pseudowire_ip_source_guard", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard)), ("pseudowire-mac", ("pseudowire_mac", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac)), ("bd-pw-split-horizon", ("bd_pw_split_horizon", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon)), ("bd-pw-mpls-static-labels", ("bd_pw_mpls_static_labels", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels)), ("bridge-domain-backup-pseudowires", ("bridge_domain_backup_pseudowires", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('neighbor', YLeaf(YType.str, 'neighbor')),
                                        ('pseudowire_id', YLeaf(YType.uint32, 'pseudowire-id')),
                                        ('pseudowire_mld_snoop', YLeaf(YType.str, 'pseudowire-mld-snoop')),
                                        ('pseudowire_igmp_snoop', YLeaf(YType.str, 'pseudowire-igmp-snoop')),
                                        ('pseudowire_flooding', YLeaf(YType.enumeration, 'pseudowire-flooding')),
                                        ('bd_pw_class', YLeaf(YType.str, 'bd-pw-class')),
                                        ('pseudowire_flooding_unknown_unicast', YLeaf(YType.enumeration, 'pseudowire-flooding-unknown-unicast')),
                                    ])
                                    self.neighbor = None
                                    self.pseudowire_id = None
                                    self.pseudowire_mld_snoop = None
                                    self.pseudowire_igmp_snoop = None
                                    self.pseudowire_flooding = None
                                    self.bd_pw_class = None
                                    self.pseudowire_flooding_unknown_unicast = None

                                    self.pseudowire_dai = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai()
                                    self.pseudowire_dai.parent = self
                                    self._children_name_map["pseudowire_dai"] = "pseudowire-dai"
                                    self._children_yang_names.add("pseudowire-dai")

                                    self.bdpw_storm_control_types = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes()
                                    self.bdpw_storm_control_types.parent = self
                                    self._children_name_map["bdpw_storm_control_types"] = "bdpw-storm-control-types"
                                    self._children_yang_names.add("bdpw-storm-control-types")

                                    self.pseudowire_profile = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile()
                                    self.pseudowire_profile.parent = self
                                    self._children_name_map["pseudowire_profile"] = "pseudowire-profile"
                                    self._children_yang_names.add("pseudowire-profile")

                                    self.bd_pw_static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses()
                                    self.bd_pw_static_mac_addresses.parent = self
                                    self._children_name_map["bd_pw_static_mac_addresses"] = "bd-pw-static-mac-addresses"
                                    self._children_yang_names.add("bd-pw-static-mac-addresses")

                                    self.pseudowire_ip_source_guard = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard()
                                    self.pseudowire_ip_source_guard.parent = self
                                    self._children_name_map["pseudowire_ip_source_guard"] = "pseudowire-ip-source-guard"
                                    self._children_yang_names.add("pseudowire-ip-source-guard")

                                    self.pseudowire_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac()
                                    self.pseudowire_mac.parent = self
                                    self._children_name_map["pseudowire_mac"] = "pseudowire-mac"
                                    self._children_yang_names.add("pseudowire-mac")

                                    self.bd_pw_split_horizon = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon()
                                    self.bd_pw_split_horizon.parent = self
                                    self._children_name_map["bd_pw_split_horizon"] = "bd-pw-split-horizon"
                                    self._children_yang_names.add("bd-pw-split-horizon")

                                    self.bd_pw_mpls_static_labels = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels()
                                    self.bd_pw_mpls_static_labels.parent = self
                                    self._children_name_map["bd_pw_mpls_static_labels"] = "bd-pw-mpls-static-labels"
                                    self._children_yang_names.add("bd-pw-mpls-static-labels")

                                    self.bridge_domain_backup_pseudowires = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires()
                                    self.bridge_domain_backup_pseudowires.parent = self
                                    self._children_name_map["bridge_domain_backup_pseudowires"] = "bridge-domain-backup-pseudowires"
                                    self._children_yang_names.add("bridge-domain-backup-pseudowires")
                                    self._segment_path = lambda: "bd-pseudowire" + "[neighbor='" + str(self.neighbor) + "']" + "[pseudowire-id='" + str(self.pseudowire_id) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire, ['neighbor', 'pseudowire_id', 'pseudowire_mld_snoop', 'pseudowire_igmp_snoop', 'pseudowire_flooding', 'bd_pw_class', 'pseudowire_flooding_unknown_unicast'], name, value)


                                class PseudowireDai(Entity):
                                    """
                                    Access Pseudowire Dynamic ARP Inspection
                                    
                                    .. attribute:: pseudowire_dai_address_validation
                                    
                                    	Address Validation
                                    	**type**\:  :py:class:`PseudowireDaiAddressValidation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation>`
                                    
                                    .. attribute:: logging
                                    
                                    	Logging Type
                                    	**type**\:  :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                    
                                    .. attribute:: disable
                                    
                                    	Disable Dynamic ARP Inspection
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable Access Pseudowire Dynamic ARP Inspection
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai, self).__init__()

                                        self.yang_name = "pseudowire-dai"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("pseudowire-dai-address-validation", ("pseudowire_dai_address_validation", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('logging', YLeaf(YType.enumeration, 'logging')),
                                            ('disable', YLeaf(YType.empty, 'disable')),
                                            ('enable', YLeaf(YType.empty, 'enable')),
                                        ])
                                        self.logging = None
                                        self.disable = None
                                        self.enable = None

                                        self.pseudowire_dai_address_validation = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation()
                                        self.pseudowire_dai_address_validation.parent = self
                                        self._children_name_map["pseudowire_dai_address_validation"] = "pseudowire-dai-address-validation"
                                        self._children_yang_names.add("pseudowire-dai-address-validation")
                                        self._segment_path = lambda: "pseudowire-dai"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai, ['logging', 'disable', 'enable'], name, value)


                                    class PseudowireDaiAddressValidation(Entity):
                                        """
                                        Address Validation
                                        
                                        .. attribute:: ipv4_verification
                                        
                                        	IPv4 Verification
                                        	**type**\:  :py:class:`L2vpnVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification>`
                                        
                                        .. attribute:: destination_mac_verification
                                        
                                        	Destination MAC Verification
                                        	**type**\:  :py:class:`L2vpnVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification>`
                                        
                                        .. attribute:: source_mac_verification
                                        
                                        	Source MAC Verification
                                        	**type**\:  :py:class:`L2vpnVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation, self).__init__()

                                            self.yang_name = "pseudowire-dai-address-validation"
                                            self.yang_parent_name = "pseudowire-dai"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('ipv4_verification', YLeaf(YType.enumeration, 'ipv4-verification')),
                                                ('destination_mac_verification', YLeaf(YType.enumeration, 'destination-mac-verification')),
                                                ('source_mac_verification', YLeaf(YType.enumeration, 'source-mac-verification')),
                                            ])
                                            self.ipv4_verification = None
                                            self.destination_mac_verification = None
                                            self.source_mac_verification = None
                                            self._segment_path = lambda: "pseudowire-dai-address-validation"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation, ['ipv4_verification', 'destination_mac_verification', 'source_mac_verification'], name, value)


                                class BdpwStormControlTypes(Entity):
                                    """
                                    Storm Control
                                    
                                    .. attribute:: bdpw_storm_control_type
                                    
                                    	Storm Control Type
                                    	**type**\: list of  		 :py:class:`BdpwStormControlType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes, self).__init__()

                                        self.yang_name = "bdpw-storm-control-types"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("bdpw-storm-control-type", ("bdpw_storm_control_type", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType))])
                                        self._leafs = OrderedDict()

                                        self.bdpw_storm_control_type = YList(self)
                                        self._segment_path = lambda: "bdpw-storm-control-types"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes, [], name, value)


                                    class BdpwStormControlType(Entity):
                                        """
                                        Storm Control Type
                                        
                                        .. attribute:: sctype  (key)
                                        
                                        	Storm Control Type
                                        	**type**\:  :py:class:`StormControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.StormControl>`
                                        
                                        .. attribute:: storm_control_unit
                                        
                                        	Specify units for Storm Control Configuration
                                        	**type**\:  :py:class:`StormControlUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType, self).__init__()

                                            self.yang_name = "bdpw-storm-control-type"
                                            self.yang_parent_name = "bdpw-storm-control-types"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['sctype']
                                            self._child_container_classes = OrderedDict([("storm-control-unit", ("storm_control_unit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('sctype', YLeaf(YType.enumeration, 'sctype')),
                                            ])
                                            self.sctype = None

                                            self.storm_control_unit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit()
                                            self.storm_control_unit.parent = self
                                            self._children_name_map["storm_control_unit"] = "storm-control-unit"
                                            self._children_yang_names.add("storm-control-unit")
                                            self._segment_path = lambda: "bdpw-storm-control-type" + "[sctype='" + str(self.sctype) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType, ['sctype'], name, value)


                                        class StormControlUnit(Entity):
                                            """
                                            Specify units for Storm Control Configuration
                                            
                                            .. attribute:: kbits_per_sec
                                            
                                            	Kilobits Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                            	**type**\: int
                                            
                                            	**range:** 64..1280000
                                            
                                            	**units**\: kbit/s
                                            
                                            .. attribute:: pkts_per_sec
                                            
                                            	Packets Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                            	**type**\: int
                                            
                                            	**range:** 1..160000
                                            
                                            	**units**\: packet/s
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit, self).__init__()

                                                self.yang_name = "storm-control-unit"
                                                self.yang_parent_name = "bdpw-storm-control-type"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('kbits_per_sec', YLeaf(YType.uint32, 'kbits-per-sec')),
                                                    ('pkts_per_sec', YLeaf(YType.uint32, 'pkts-per-sec')),
                                                ])
                                                self.kbits_per_sec = None
                                                self.pkts_per_sec = None
                                                self._segment_path = lambda: "storm-control-unit"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit, ['kbits_per_sec', 'pkts_per_sec'], name, value)


                                class PseudowireProfile(Entity):
                                    """
                                    Attach a DHCP profile
                                    
                                    .. attribute:: profile_id
                                    
                                    	Set the snooping profile
                                    	**type**\:  :py:class:`InterfaceProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile>`
                                    
                                    .. attribute:: dhcp_snooping_id
                                    
                                    	Disable DHCP snooping
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile, self).__init__()

                                        self.yang_name = "pseudowire-profile"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('profile_id', YLeaf(YType.enumeration, 'profile-id')),
                                            ('dhcp_snooping_id', YLeaf(YType.str, 'dhcp-snooping-id')),
                                        ])
                                        self.profile_id = None
                                        self.dhcp_snooping_id = None
                                        self._segment_path = lambda: "pseudowire-profile"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile, ['profile_id', 'dhcp_snooping_id'], name, value)


                                class BdPwStaticMacAddresses(Entity):
                                    """
                                    Static Mac Address Table
                                    
                                    .. attribute:: bd_pw_static_mac_address
                                    
                                    	Static Mac Address Configuration
                                    	**type**\: list of  		 :py:class:`BdPwStaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses, self).__init__()

                                        self.yang_name = "bd-pw-static-mac-addresses"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("bd-pw-static-mac-address", ("bd_pw_static_mac_address", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress))])
                                        self._leafs = OrderedDict()

                                        self.bd_pw_static_mac_address = YList(self)
                                        self._segment_path = lambda: "bd-pw-static-mac-addresses"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses, [], name, value)


                                    class BdPwStaticMacAddress(Entity):
                                        """
                                        Static Mac Address Configuration
                                        
                                        .. attribute:: address  (key)
                                        
                                        	Static MAC address
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress, self).__init__()

                                            self.yang_name = "bd-pw-static-mac-address"
                                            self.yang_parent_name = "bd-pw-static-mac-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['address']
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('address', YLeaf(YType.str, 'address')),
                                            ])
                                            self.address = None
                                            self._segment_path = lambda: "bd-pw-static-mac-address" + "[address='" + str(self.address) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress, ['address'], name, value)


                                class PseudowireIpSourceGuard(Entity):
                                    """
                                    IP Source Guard
                                    
                                    .. attribute:: logging
                                    
                                    	Logging Type
                                    	**type**\:  :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                    
                                    .. attribute:: disable
                                    
                                    	Disable Dynamic IP source guard
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable IP Source Guard
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard, self).__init__()

                                        self.yang_name = "pseudowire-ip-source-guard"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('logging', YLeaf(YType.enumeration, 'logging')),
                                            ('disable', YLeaf(YType.empty, 'disable')),
                                            ('enable', YLeaf(YType.empty, 'enable')),
                                        ])
                                        self.logging = None
                                        self.disable = None
                                        self.enable = None
                                        self._segment_path = lambda: "pseudowire-ip-source-guard"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard, ['logging', 'disable', 'enable'], name, value)


                                class PseudowireMac(Entity):
                                    """
                                    Bridge\-domain Pseudowire MAC
                                    configuration commands
                                    
                                    .. attribute:: pseudowire_mac_secure
                                    
                                    	MAC Secure
                                    	**type**\:  :py:class:`PseudowireMacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure>`
                                    
                                    .. attribute:: pseudowire_mac_aging
                                    
                                    	MAC\-Aging configuration commands
                                    	**type**\:  :py:class:`PseudowireMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging>`
                                    
                                    .. attribute:: pseudowire_mac_limit
                                    
                                    	MAC\-Limit configuration commands
                                    	**type**\:  :py:class:`PseudowireMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit>`
                                    
                                    .. attribute:: pseudowire_mac_port_down_flush
                                    
                                    	Enable/Disable MAC Flush When Port goes down
                                    	**type**\:  :py:class:`PortDownFlush <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.PortDownFlush>`
                                    
                                    .. attribute:: enable
                                    
                                    	Bridge\-domain Pseudowire MAC configuration mode
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: pseudowire_mac_learning
                                    
                                    	Enable MAC Learning
                                    	**type**\:  :py:class:`MacLearn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLearn>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac, self).__init__()

                                        self.yang_name = "pseudowire-mac"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("pseudowire-mac-secure", ("pseudowire_mac_secure", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure)), ("pseudowire-mac-aging", ("pseudowire_mac_aging", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging)), ("pseudowire-mac-limit", ("pseudowire_mac_limit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('pseudowire_mac_port_down_flush', YLeaf(YType.enumeration, 'pseudowire-mac-port-down-flush')),
                                            ('enable', YLeaf(YType.empty, 'enable')),
                                            ('pseudowire_mac_learning', YLeaf(YType.enumeration, 'pseudowire-mac-learning')),
                                        ])
                                        self.pseudowire_mac_port_down_flush = None
                                        self.enable = None
                                        self.pseudowire_mac_learning = None

                                        self.pseudowire_mac_secure = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure()
                                        self.pseudowire_mac_secure.parent = self
                                        self._children_name_map["pseudowire_mac_secure"] = "pseudowire-mac-secure"
                                        self._children_yang_names.add("pseudowire-mac-secure")

                                        self.pseudowire_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging()
                                        self.pseudowire_mac_aging.parent = self
                                        self._children_name_map["pseudowire_mac_aging"] = "pseudowire-mac-aging"
                                        self._children_yang_names.add("pseudowire-mac-aging")

                                        self.pseudowire_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit()
                                        self.pseudowire_mac_limit.parent = self
                                        self._children_name_map["pseudowire_mac_limit"] = "pseudowire-mac-limit"
                                        self._children_yang_names.add("pseudowire-mac-limit")
                                        self._segment_path = lambda: "pseudowire-mac"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac, ['pseudowire_mac_port_down_flush', 'enable', 'pseudowire_mac_learning'], name, value)


                                    class PseudowireMacSecure(Entity):
                                        """
                                        MAC Secure
                                        
                                        .. attribute:: logging
                                        
                                        	MAC Secure Logging
                                        	**type**\:  :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                        
                                        .. attribute:: disable
                                        
                                        	Disable L2 Pseudowire MAC Secure
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: action
                                        
                                        	MAC secure enforcement action
                                        	**type**\:  :py:class:`MacSecureAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacSecureAction>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable MAC Secure
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure, self).__init__()

                                            self.yang_name = "pseudowire-mac-secure"
                                            self.yang_parent_name = "pseudowire-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('logging', YLeaf(YType.enumeration, 'logging')),
                                                ('disable', YLeaf(YType.empty, 'disable')),
                                                ('action', YLeaf(YType.enumeration, 'action')),
                                                ('enable', YLeaf(YType.empty, 'enable')),
                                            ])
                                            self.logging = None
                                            self.disable = None
                                            self.action = None
                                            self.enable = None
                                            self._segment_path = lambda: "pseudowire-mac-secure"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure, ['logging', 'disable', 'action', 'enable'], name, value)


                                    class PseudowireMacAging(Entity):
                                        """
                                        MAC\-Aging configuration commands
                                        
                                        .. attribute:: pseudowire_mac_aging_type
                                        
                                        	MAC address aging type
                                        	**type**\:  :py:class:`MacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAging>`
                                        
                                        .. attribute:: pseudowire_mac_aging_time
                                        
                                        	MAC Aging Time
                                        	**type**\: int
                                        
                                        	**range:** 300..30000
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging, self).__init__()

                                            self.yang_name = "pseudowire-mac-aging"
                                            self.yang_parent_name = "pseudowire-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('pseudowire_mac_aging_type', YLeaf(YType.enumeration, 'pseudowire-mac-aging-type')),
                                                ('pseudowire_mac_aging_time', YLeaf(YType.uint32, 'pseudowire-mac-aging-time')),
                                            ])
                                            self.pseudowire_mac_aging_type = None
                                            self.pseudowire_mac_aging_time = None
                                            self._segment_path = lambda: "pseudowire-mac-aging"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging, ['pseudowire_mac_aging_type', 'pseudowire_mac_aging_time'], name, value)


                                    class PseudowireMacLimit(Entity):
                                        """
                                        MAC\-Limit configuration commands
                                        
                                        .. attribute:: pseudowire_mac_limit_action
                                        
                                        	Bridge Access Pseudowire MAC address limit enforcement action
                                        	**type**\:  :py:class:`MacLimitAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction>`
                                        
                                        .. attribute:: pseudowire_mac_limit_notif
                                        
                                        	MAC address limit notification action in a Bridge Access Pseudowire
                                        	**type**\:  :py:class:`MacNotification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotification>`
                                        
                                        .. attribute:: pseudowire_mac_limit_max
                                        
                                        	Number of MAC addresses on a Bridge Access Pseudowire after which MAC limit action is taken
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit, self).__init__()

                                            self.yang_name = "pseudowire-mac-limit"
                                            self.yang_parent_name = "pseudowire-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('pseudowire_mac_limit_action', YLeaf(YType.enumeration, 'pseudowire-mac-limit-action')),
                                                ('pseudowire_mac_limit_notif', YLeaf(YType.enumeration, 'pseudowire-mac-limit-notif')),
                                                ('pseudowire_mac_limit_max', YLeaf(YType.uint32, 'pseudowire-mac-limit-max')),
                                            ])
                                            self.pseudowire_mac_limit_action = None
                                            self.pseudowire_mac_limit_notif = None
                                            self.pseudowire_mac_limit_max = None
                                            self._segment_path = lambda: "pseudowire-mac-limit"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit, ['pseudowire_mac_limit_action', 'pseudowire_mac_limit_notif', 'pseudowire_mac_limit_max'], name, value)


                                class BdPwSplitHorizon(Entity):
                                    """
                                    Split Horizon
                                    
                                    .. attribute:: bd_pw_split_horizon_group
                                    
                                    	Split Horizon Group
                                    	**type**\:  :py:class:`BdPwSplitHorizonGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon, self).__init__()

                                        self.yang_name = "bd-pw-split-horizon"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("bd-pw-split-horizon-group", ("bd_pw_split_horizon_group", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict()

                                        self.bd_pw_split_horizon_group = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup()
                                        self.bd_pw_split_horizon_group.parent = self
                                        self._children_name_map["bd_pw_split_horizon_group"] = "bd-pw-split-horizon-group"
                                        self._children_yang_names.add("bd-pw-split-horizon-group")
                                        self._segment_path = lambda: "bd-pw-split-horizon"


                                    class BdPwSplitHorizonGroup(Entity):
                                        """
                                        Split Horizon Group
                                        
                                        .. attribute:: enable
                                        
                                        	Enable split horizon group
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup, self).__init__()

                                            self.yang_name = "bd-pw-split-horizon-group"
                                            self.yang_parent_name = "bd-pw-split-horizon"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', YLeaf(YType.empty, 'enable')),
                                            ])
                                            self.enable = None
                                            self._segment_path = lambda: "bd-pw-split-horizon-group"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup, ['enable'], name, value)


                                class BdPwMplsStaticLabels(Entity):
                                    """
                                    MPLS static labels
                                    
                                    .. attribute:: local_static_label
                                    
                                    	Pseudowire local static label
                                    	**type**\: int
                                    
                                    	**range:** 16..1048575
                                    
                                    .. attribute:: remote_static_label
                                    
                                    	Pseudowire remote static label
                                    	**type**\: int
                                    
                                    	**range:** 16..1048575
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels, self).__init__()

                                        self.yang_name = "bd-pw-mpls-static-labels"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('local_static_label', YLeaf(YType.uint32, 'local-static-label')),
                                            ('remote_static_label', YLeaf(YType.uint32, 'remote-static-label')),
                                        ])
                                        self.local_static_label = None
                                        self.remote_static_label = None
                                        self._segment_path = lambda: "bd-pw-mpls-static-labels"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels, ['local_static_label', 'remote_static_label'], name, value)


                                class BridgeDomainBackupPseudowires(Entity):
                                    """
                                    List of pseudowires
                                    
                                    .. attribute:: bridge_domain_backup_pseudowire
                                    
                                    	Backup pseudowire configuration
                                    	**type**\: list of  		 :py:class:`BridgeDomainBackupPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires, self).__init__()

                                        self.yang_name = "bridge-domain-backup-pseudowires"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("bridge-domain-backup-pseudowire", ("bridge_domain_backup_pseudowire", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire))])
                                        self._leafs = OrderedDict()

                                        self.bridge_domain_backup_pseudowire = YList(self)
                                        self._segment_path = lambda: "bridge-domain-backup-pseudowires"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires, [], name, value)


                                    class BridgeDomainBackupPseudowire(Entity):
                                        """
                                        Backup pseudowire configuration
                                        
                                        .. attribute:: neighbor  (key)
                                        
                                        	Neighbor IP address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: pseudowire_id  (key)
                                        
                                        	Pseudowire ID
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: bridge_domain_backup_pw_class
                                        
                                        	PW class template name to use for this pseudowire
                                        	**type**\: str
                                        
                                        	**length:** 1..32
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire, self).__init__()

                                            self.yang_name = "bridge-domain-backup-pseudowire"
                                            self.yang_parent_name = "bridge-domain-backup-pseudowires"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['neighbor','pseudowire_id']
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('neighbor', YLeaf(YType.str, 'neighbor')),
                                                ('pseudowire_id', YLeaf(YType.uint32, 'pseudowire-id')),
                                                ('bridge_domain_backup_pw_class', YLeaf(YType.str, 'bridge-domain-backup-pw-class')),
                                            ])
                                            self.neighbor = None
                                            self.pseudowire_id = None
                                            self.bridge_domain_backup_pw_class = None
                                            self._segment_path = lambda: "bridge-domain-backup-pseudowire" + "[neighbor='" + str(self.neighbor) + "']" + "[pseudowire-id='" + str(self.pseudowire_id) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire, ['neighbor', 'pseudowire_id', 'bridge_domain_backup_pw_class'], name, value)


                        class Vfis(Entity):
                            """
                            Specify the virtual forwarding interface
                            name
                            
                            .. attribute:: vfi
                            
                            	Name of the Virtual Forwarding Interface
                            	**type**\: list of  		 :py:class:`Vfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis, self).__init__()

                                self.yang_name = "vfis"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("vfi", ("vfi", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi))])
                                self._leafs = OrderedDict()

                                self.vfi = YList(self)
                                self._segment_path = lambda: "vfis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis, [], name, value)


                            class Vfi(Entity):
                                """
                                Name of the Virtual Forwarding Interface
                                
                                .. attribute:: name  (key)
                                
                                	Name of the Virtual Forwarding Interface
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                .. attribute:: multicast_p2mp
                                
                                	Enable Multicast P2MP in this VFI
                                	**type**\:  :py:class:`MulticastP2Mp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp>`
                                
                                .. attribute:: vfi_pseudowires
                                
                                	List of pseudowires
                                	**type**\:  :py:class:`VfiPseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires>`
                                
                                .. attribute:: bgp_auto_discovery
                                
                                	Enable Autodiscovery BGP in this VFI
                                	**type**\:  :py:class:`BgpAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery>`
                                
                                .. attribute:: vfi_shutdown
                                
                                	Enabling Shutdown
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: vpnid
                                
                                	VPN Identifier
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi, self).__init__()

                                    self.yang_name = "vfi"
                                    self.yang_parent_name = "vfis"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['name']
                                    self._child_container_classes = OrderedDict([("multicast-p2mp", ("multicast_p2mp", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp)), ("vfi-pseudowires", ("vfi_pseudowires", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires)), ("bgp-auto-discovery", ("bgp_auto_discovery", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('name', YLeaf(YType.str, 'name')),
                                        ('vfi_shutdown', YLeaf(YType.empty, 'vfi-shutdown')),
                                        ('vpnid', YLeaf(YType.uint32, 'vpnid')),
                                    ])
                                    self.name = None
                                    self.vfi_shutdown = None
                                    self.vpnid = None

                                    self.multicast_p2mp = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp()
                                    self.multicast_p2mp.parent = self
                                    self._children_name_map["multicast_p2mp"] = "multicast-p2mp"
                                    self._children_yang_names.add("multicast-p2mp")

                                    self.vfi_pseudowires = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires()
                                    self.vfi_pseudowires.parent = self
                                    self._children_name_map["vfi_pseudowires"] = "vfi-pseudowires"
                                    self._children_yang_names.add("vfi-pseudowires")

                                    self.bgp_auto_discovery = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery()
                                    self.bgp_auto_discovery.parent = self
                                    self._children_name_map["bgp_auto_discovery"] = "bgp-auto-discovery"
                                    self._children_yang_names.add("bgp-auto-discovery")
                                    self._segment_path = lambda: "vfi" + "[name='" + str(self.name) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi, ['name', 'vfi_shutdown', 'vpnid'], name, value)


                                class MulticastP2Mp(Entity):
                                    """
                                    Enable Multicast P2MP in this VFI
                                    
                                    .. attribute:: transports
                                    
                                    	Multicast P2MP Transport
                                    	**type**\:  :py:class:`Transports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports>`
                                    
                                    .. attribute:: signalings
                                    
                                    	Multicast P2MP Signaling Type
                                    	**type**\:  :py:class:`Signalings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable Autodiscovery P2MP
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp, self).__init__()

                                        self.yang_name = "multicast-p2mp"
                                        self.yang_parent_name = "vfi"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("transports", ("transports", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports)), ("signalings", ("signalings", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('enable', YLeaf(YType.empty, 'enable')),
                                        ])
                                        self.enable = None

                                        self.transports = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports()
                                        self.transports.parent = self
                                        self._children_name_map["transports"] = "transports"
                                        self._children_yang_names.add("transports")

                                        self.signalings = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings()
                                        self.signalings.parent = self
                                        self._children_name_map["signalings"] = "signalings"
                                        self._children_yang_names.add("signalings")
                                        self._segment_path = lambda: "multicast-p2mp"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp, ['enable'], name, value)


                                    class Transports(Entity):
                                        """
                                        Multicast P2MP Transport
                                        
                                        .. attribute:: transport
                                        
                                        	Multicast P2MP Transport Type
                                        	**type**\: list of  		 :py:class:`Transport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports, self).__init__()

                                            self.yang_name = "transports"
                                            self.yang_parent_name = "multicast-p2mp"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("transport", ("transport", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport))])
                                            self._leafs = OrderedDict()

                                            self.transport = YList(self)
                                            self._segment_path = lambda: "transports"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports, [], name, value)


                                        class Transport(Entity):
                                            """
                                            Multicast P2MP Transport Type
                                            
                                            .. attribute:: transport_name  (key)
                                            
                                            	Transport Type
                                            	**type**\: str
                                            
                                            	**pattern:** (RSVP\_TE)
                                            
                                            .. attribute:: attribute_set_name
                                            
                                            	Multicast P2MP TE Attribute Set Name
                                            	**type**\: str
                                            
                                            	**length:** 1..64
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport, self).__init__()

                                                self.yang_name = "transport"
                                                self.yang_parent_name = "transports"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['transport_name']
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('transport_name', YLeaf(YType.str, 'transport-name')),
                                                    ('attribute_set_name', YLeaf(YType.str, 'attribute-set-name')),
                                                ])
                                                self.transport_name = None
                                                self.attribute_set_name = None
                                                self._segment_path = lambda: "transport" + "[transport-name='" + str(self.transport_name) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport, ['transport_name', 'attribute_set_name'], name, value)


                                    class Signalings(Entity):
                                        """
                                        Multicast P2MP Signaling Type
                                        
                                        .. attribute:: signaling
                                        
                                        	Multicast P2MP Signaling Type
                                        	**type**\: list of  		 :py:class:`Signaling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings, self).__init__()

                                            self.yang_name = "signalings"
                                            self.yang_parent_name = "multicast-p2mp"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("signaling", ("signaling", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling))])
                                            self._leafs = OrderedDict()

                                            self.signaling = YList(self)
                                            self._segment_path = lambda: "signalings"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings, [], name, value)


                                        class Signaling(Entity):
                                            """
                                            Multicast P2MP Signaling Type
                                            
                                            .. attribute:: signaling_name  (key)
                                            
                                            	Signaling Type
                                            	**type**\: str
                                            
                                            	**pattern:** (BGP)
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling, self).__init__()

                                                self.yang_name = "signaling"
                                                self.yang_parent_name = "signalings"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['signaling_name']
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('signaling_name', YLeaf(YType.str, 'signaling-name')),
                                                ])
                                                self.signaling_name = None
                                                self._segment_path = lambda: "signaling" + "[signaling-name='" + str(self.signaling_name) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling, ['signaling_name'], name, value)


                                class VfiPseudowires(Entity):
                                    """
                                    List of pseudowires
                                    
                                    .. attribute:: vfi_pseudowire
                                    
                                    	Pseudowire configuration
                                    	**type**\: list of  		 :py:class:`VfiPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires, self).__init__()

                                        self.yang_name = "vfi-pseudowires"
                                        self.yang_parent_name = "vfi"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("vfi-pseudowire", ("vfi_pseudowire", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire))])
                                        self._leafs = OrderedDict()

                                        self.vfi_pseudowire = YList(self)
                                        self._segment_path = lambda: "vfi-pseudowires"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires, [], name, value)


                                    class VfiPseudowire(Entity):
                                        """
                                        Pseudowire configuration
                                        
                                        .. attribute:: neighbor  (key)
                                        
                                        	Neighbor IP address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: pseudowire_id  (key)
                                        
                                        	Pseudowire ID
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: vfi_pw_dhcp_snoop
                                        
                                        	Attach a DHCP Snooping profile
                                        	**type**\:  :py:class:`VfiPwDhcpSnoop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop>`
                                        
                                        .. attribute:: vfi_pw_mpls_static_labels
                                        
                                        	MPLS static labels
                                        	**type**\:  :py:class:`VfiPwMplsStaticLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels>`
                                        
                                        .. attribute:: pseudowire_static_mac_addresses
                                        
                                        	Static Mac Address Table
                                        	**type**\:  :py:class:`PseudowireStaticMacAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses>`
                                        
                                        .. attribute:: vfi_pw_class
                                        
                                        	PW class template name to use for this pseudowire
                                        	**type**\: str
                                        
                                        	**length:** 1..32
                                        
                                        .. attribute:: vfi_pw_igmp_snoop
                                        
                                        	Attach a IGMP Snooping profile
                                        	**type**\: str
                                        
                                        	**length:** 1..32
                                        
                                        .. attribute:: vfi_pw_mld_snoop
                                        
                                        	Attach a MLD Snooping profile
                                        	**type**\: str
                                        
                                        	**length:** 1..32
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire, self).__init__()

                                            self.yang_name = "vfi-pseudowire"
                                            self.yang_parent_name = "vfi-pseudowires"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['neighbor','pseudowire_id']
                                            self._child_container_classes = OrderedDict([("vfi-pw-dhcp-snoop", ("vfi_pw_dhcp_snoop", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop)), ("vfi-pw-mpls-static-labels", ("vfi_pw_mpls_static_labels", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels)), ("pseudowire-static-mac-addresses", ("pseudowire_static_mac_addresses", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('neighbor', YLeaf(YType.str, 'neighbor')),
                                                ('pseudowire_id', YLeaf(YType.uint32, 'pseudowire-id')),
                                                ('vfi_pw_class', YLeaf(YType.str, 'vfi-pw-class')),
                                                ('vfi_pw_igmp_snoop', YLeaf(YType.str, 'vfi-pw-igmp-snoop')),
                                                ('vfi_pw_mld_snoop', YLeaf(YType.str, 'vfi-pw-mld-snoop')),
                                            ])
                                            self.neighbor = None
                                            self.pseudowire_id = None
                                            self.vfi_pw_class = None
                                            self.vfi_pw_igmp_snoop = None
                                            self.vfi_pw_mld_snoop = None

                                            self.vfi_pw_dhcp_snoop = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop()
                                            self.vfi_pw_dhcp_snoop.parent = self
                                            self._children_name_map["vfi_pw_dhcp_snoop"] = "vfi-pw-dhcp-snoop"
                                            self._children_yang_names.add("vfi-pw-dhcp-snoop")

                                            self.vfi_pw_mpls_static_labels = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels()
                                            self.vfi_pw_mpls_static_labels.parent = self
                                            self._children_name_map["vfi_pw_mpls_static_labels"] = "vfi-pw-mpls-static-labels"
                                            self._children_yang_names.add("vfi-pw-mpls-static-labels")

                                            self.pseudowire_static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses()
                                            self.pseudowire_static_mac_addresses.parent = self
                                            self._children_name_map["pseudowire_static_mac_addresses"] = "pseudowire-static-mac-addresses"
                                            self._children_yang_names.add("pseudowire-static-mac-addresses")
                                            self._segment_path = lambda: "vfi-pseudowire" + "[neighbor='" + str(self.neighbor) + "']" + "[pseudowire-id='" + str(self.pseudowire_id) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire, ['neighbor', 'pseudowire_id', 'vfi_pw_class', 'vfi_pw_igmp_snoop', 'vfi_pw_mld_snoop'], name, value)


                                        class VfiPwDhcpSnoop(Entity):
                                            """
                                            Attach a DHCP Snooping profile
                                            
                                            .. attribute:: profile_id
                                            
                                            	Set the snooping profile
                                            	**type**\:  :py:class:`InterfaceProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile>`
                                            
                                            .. attribute:: dhcp_snooping_id
                                            
                                            	Disable DHCP snooping
                                            	**type**\: str
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop, self).__init__()

                                                self.yang_name = "vfi-pw-dhcp-snoop"
                                                self.yang_parent_name = "vfi-pseudowire"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('profile_id', YLeaf(YType.enumeration, 'profile-id')),
                                                    ('dhcp_snooping_id', YLeaf(YType.str, 'dhcp-snooping-id')),
                                                ])
                                                self.profile_id = None
                                                self.dhcp_snooping_id = None
                                                self._segment_path = lambda: "vfi-pw-dhcp-snoop"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop, ['profile_id', 'dhcp_snooping_id'], name, value)


                                        class VfiPwMplsStaticLabels(Entity):
                                            """
                                            MPLS static labels
                                            
                                            .. attribute:: local_static_label
                                            
                                            	Pseudowire local static label
                                            	**type**\: int
                                            
                                            	**range:** 16..1048575
                                            
                                            .. attribute:: remote_static_label
                                            
                                            	Pseudowire remote static label
                                            	**type**\: int
                                            
                                            	**range:** 16..1048575
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels, self).__init__()

                                                self.yang_name = "vfi-pw-mpls-static-labels"
                                                self.yang_parent_name = "vfi-pseudowire"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('local_static_label', YLeaf(YType.uint32, 'local-static-label')),
                                                    ('remote_static_label', YLeaf(YType.uint32, 'remote-static-label')),
                                                ])
                                                self.local_static_label = None
                                                self.remote_static_label = None
                                                self._segment_path = lambda: "vfi-pw-mpls-static-labels"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels, ['local_static_label', 'remote_static_label'], name, value)


                                        class PseudowireStaticMacAddresses(Entity):
                                            """
                                            Static Mac Address Table
                                            
                                            .. attribute:: pseudowire_static_mac_address
                                            
                                            	Static Mac Address Configuration
                                            	**type**\: list of  		 :py:class:`PseudowireStaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses, self).__init__()

                                                self.yang_name = "pseudowire-static-mac-addresses"
                                                self.yang_parent_name = "vfi-pseudowire"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([("pseudowire-static-mac-address", ("pseudowire_static_mac_address", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress))])
                                                self._leafs = OrderedDict()

                                                self.pseudowire_static_mac_address = YList(self)
                                                self._segment_path = lambda: "pseudowire-static-mac-addresses"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses, [], name, value)


                                            class PseudowireStaticMacAddress(Entity):
                                                """
                                                Static Mac Address Configuration
                                                
                                                .. attribute:: address  (key)
                                                
                                                	Static MAC address
                                                	**type**\: str
                                                
                                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2017-06-26'

                                                def __init__(self):
                                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress, self).__init__()

                                                    self.yang_name = "pseudowire-static-mac-address"
                                                    self.yang_parent_name = "pseudowire-static-mac-addresses"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['address']
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('address', YLeaf(YType.str, 'address')),
                                                    ])
                                                    self.address = None
                                                    self._segment_path = lambda: "pseudowire-static-mac-address" + "[address='" + str(self.address) + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress, ['address'], name, value)


                                class BgpAutoDiscovery(Entity):
                                    """
                                    Enable Autodiscovery BGP in this VFI
                                    
                                    .. attribute:: ldp_signaling_protocol
                                    
                                    	Signaling Protocol LDP in this VFI configuration
                                    	**type**\:  :py:class:`LdpSignalingProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol>`
                                    
                                    .. attribute:: bgp_route_policy
                                    
                                    	Route policy
                                    	**type**\:  :py:class:`BgpRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy>`
                                    
                                    .. attribute:: route_distinguisher
                                    
                                    	Route Distinguisher
                                    	**type**\:  :py:class:`RouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher>`
                                    
                                    .. attribute:: bgp_signaling_protocol
                                    
                                    	Enable Signaling Protocol BGP in this VFI
                                    	**type**\:  :py:class:`BgpSignalingProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol>`
                                    
                                    .. attribute:: route_targets
                                    
                                    	Route Target
                                    	**type**\:  :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets>`
                                    
                                    .. attribute:: table_policy
                                    
                                    	Table Policy for installation of forwarding data to L2FIB
                                    	**type**\: str
                                    
                                    .. attribute:: ad_control_word
                                    
                                    	Enable control\-word for this VFI
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable Autodiscovery BGP
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery, self).__init__()

                                        self.yang_name = "bgp-auto-discovery"
                                        self.yang_parent_name = "vfi"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("ldp-signaling-protocol", ("ldp_signaling_protocol", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol)), ("bgp-route-policy", ("bgp_route_policy", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy)), ("route-distinguisher", ("route_distinguisher", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher)), ("bgp-signaling-protocol", ("bgp_signaling_protocol", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol)), ("route-targets", ("route_targets", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('table_policy', YLeaf(YType.str, 'table-policy')),
                                            ('ad_control_word', YLeaf(YType.empty, 'ad-control-word')),
                                            ('enable', YLeaf(YType.empty, 'enable')),
                                        ])
                                        self.table_policy = None
                                        self.ad_control_word = None
                                        self.enable = None

                                        self.ldp_signaling_protocol = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol()
                                        self.ldp_signaling_protocol.parent = self
                                        self._children_name_map["ldp_signaling_protocol"] = "ldp-signaling-protocol"
                                        self._children_yang_names.add("ldp-signaling-protocol")

                                        self.bgp_route_policy = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy()
                                        self.bgp_route_policy.parent = self
                                        self._children_name_map["bgp_route_policy"] = "bgp-route-policy"
                                        self._children_yang_names.add("bgp-route-policy")

                                        self.route_distinguisher = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher()
                                        self.route_distinguisher.parent = self
                                        self._children_name_map["route_distinguisher"] = "route-distinguisher"
                                        self._children_yang_names.add("route-distinguisher")

                                        self.bgp_signaling_protocol = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol()
                                        self.bgp_signaling_protocol.parent = self
                                        self._children_name_map["bgp_signaling_protocol"] = "bgp-signaling-protocol"
                                        self._children_yang_names.add("bgp-signaling-protocol")

                                        self.route_targets = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets()
                                        self.route_targets.parent = self
                                        self._children_name_map["route_targets"] = "route-targets"
                                        self._children_yang_names.add("route-targets")
                                        self._segment_path = lambda: "bgp-auto-discovery"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery, ['table_policy', 'ad_control_word', 'enable'], name, value)


                                    class LdpSignalingProtocol(Entity):
                                        """
                                        Signaling Protocol LDP in this VFI
                                        configuration
                                        
                                        .. attribute:: vpls_id
                                        
                                        	VPLS ID
                                        	**type**\:  :py:class:`VplsId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.VplsId>`
                                        
                                        .. attribute:: flow_label_load_balance
                                        
                                        	Enable Flow Label based load balancing
                                        	**type**\:  :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable LDP as Signaling Protocol .Deletion of this object also causes deletion of all objects under LDPSignalingProtocol
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol, self).__init__()

                                            self.yang_name = "ldp-signaling-protocol"
                                            self.yang_parent_name = "bgp-auto-discovery"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("vpls-id", ("vpls_id", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.VplsId)), ("flow-label-load-balance", ("flow_label_load_balance", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', YLeaf(YType.empty, 'enable')),
                                            ])
                                            self.enable = None

                                            self.vpls_id = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.VplsId()
                                            self.vpls_id.parent = self
                                            self._children_name_map["vpls_id"] = "vpls-id"
                                            self._children_yang_names.add("vpls-id")

                                            self.flow_label_load_balance = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance()
                                            self.flow_label_load_balance.parent = self
                                            self._children_name_map["flow_label_load_balance"] = "flow-label-load-balance"
                                            self._children_yang_names.add("flow-label-load-balance")
                                            self._segment_path = lambda: "ldp-signaling-protocol"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol, ['enable'], name, value)


                                        class VplsId(Entity):
                                            """
                                            VPLS ID
                                            
                                            .. attribute:: type
                                            
                                            	VPLS\-ID Type
                                            	**type**\:  :py:class:`LdpVplsId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.LdpVplsId>`
                                            
                                            .. attribute:: as_
                                            
                                            	Two byte AS number
                                            	**type**\: int
                                            
                                            	**range:** 1..65535
                                            
                                            .. attribute:: as_index
                                            
                                            	AS index
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: address
                                            
                                            	IPV4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: address_index
                                            
                                            	Address index
                                            	**type**\: int
                                            
                                            	**range:** 0..32767
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.VplsId, self).__init__()

                                                self.yang_name = "vpls-id"
                                                self.yang_parent_name = "ldp-signaling-protocol"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('type', YLeaf(YType.enumeration, 'type')),
                                                    ('as_', YLeaf(YType.uint32, 'as')),
                                                    ('as_index', YLeaf(YType.uint32, 'as-index')),
                                                    ('address', YLeaf(YType.str, 'address')),
                                                    ('address_index', YLeaf(YType.uint32, 'address-index')),
                                                ])
                                                self.type = None
                                                self.as_ = None
                                                self.as_index = None
                                                self.address = None
                                                self.address_index = None
                                                self._segment_path = lambda: "vpls-id"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.VplsId, ['type', 'as_', 'as_index', 'address', 'address_index'], name, value)


                                        class FlowLabelLoadBalance(Entity):
                                            """
                                            Enable Flow Label based load balancing
                                            
                                            .. attribute:: flow_label
                                            
                                            	Flow Label load balance type
                                            	**type**\:  :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalance>`
                                            
                                            .. attribute:: static
                                            
                                            	Static Flow Label
                                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance, self).__init__()

                                                self.yang_name = "flow-label-load-balance"
                                                self.yang_parent_name = "ldp-signaling-protocol"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('flow_label', YLeaf(YType.enumeration, 'flow-label')),
                                                    ('static', YLeaf(YType.empty, 'static')),
                                                ])
                                                self.flow_label = None
                                                self.static = None
                                                self._segment_path = lambda: "flow-label-load-balance"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance, ['flow_label', 'static'], name, value)


                                    class BgpRoutePolicy(Entity):
                                        """
                                        Route policy
                                        
                                        .. attribute:: export
                                        
                                        	Export route policy
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy, self).__init__()

                                            self.yang_name = "bgp-route-policy"
                                            self.yang_parent_name = "bgp-auto-discovery"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('export', YLeaf(YType.str, 'export')),
                                            ])
                                            self.export = None
                                            self._segment_path = lambda: "bgp-route-policy"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy, ['export'], name, value)


                                    class RouteDistinguisher(Entity):
                                        """
                                        Route Distinguisher
                                        
                                        .. attribute:: type
                                        
                                        	Router Distinguisher Type
                                        	**type**\:  :py:class:`BgpRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher>`
                                        
                                        .. attribute:: as_
                                        
                                        	Two byte or 4 byte AS number
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: as_index
                                        
                                        	AS\:nn (hex or decimal format)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: address
                                        
                                        	IPV4 address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: addr_index
                                        
                                        	Addr index
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher, self).__init__()

                                            self.yang_name = "route-distinguisher"
                                            self.yang_parent_name = "bgp-auto-discovery"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('type', YLeaf(YType.enumeration, 'type')),
                                                ('as_', YLeaf(YType.uint32, 'as')),
                                                ('as_index', YLeaf(YType.uint32, 'as-index')),
                                                ('address', YLeaf(YType.str, 'address')),
                                                ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                                            ])
                                            self.type = None
                                            self.as_ = None
                                            self.as_index = None
                                            self.address = None
                                            self.addr_index = None
                                            self._segment_path = lambda: "route-distinguisher"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher, ['type', 'as_', 'as_index', 'address', 'addr_index'], name, value)


                                    class BgpSignalingProtocol(Entity):
                                        """
                                        Enable Signaling Protocol BGP in this
                                        VFI
                                        
                                        .. attribute:: flow_label_load_balance
                                        
                                        	Enable Flow Label based load balancing
                                        	**type**\:  :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance>`
                                        
                                        .. attribute:: ve_range
                                        
                                        	Local Virtual Edge Block Configurable Range
                                        	**type**\: int
                                        
                                        	**range:** 11..100
                                        
                                        .. attribute:: veid
                                        
                                        	Local Virtual Edge Identifier
                                        	**type**\: int
                                        
                                        	**range:** 1..16384
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP as Signaling Protocol
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol, self).__init__()

                                            self.yang_name = "bgp-signaling-protocol"
                                            self.yang_parent_name = "bgp-auto-discovery"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("flow-label-load-balance", ("flow_label_load_balance", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('ve_range', YLeaf(YType.uint32, 've-range')),
                                                ('veid', YLeaf(YType.uint32, 'veid')),
                                                ('enable', YLeaf(YType.empty, 'enable')),
                                            ])
                                            self.ve_range = None
                                            self.veid = None
                                            self.enable = None

                                            self.flow_label_load_balance = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance()
                                            self.flow_label_load_balance.parent = self
                                            self._children_name_map["flow_label_load_balance"] = "flow-label-load-balance"
                                            self._children_yang_names.add("flow-label-load-balance")
                                            self._segment_path = lambda: "bgp-signaling-protocol"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol, ['ve_range', 'veid', 'enable'], name, value)


                                        class FlowLabelLoadBalance(Entity):
                                            """
                                            Enable Flow Label based load balancing
                                            
                                            .. attribute:: flow_label
                                            
                                            	Flow Label load balance type
                                            	**type**\:  :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalance>`
                                            
                                            .. attribute:: static
                                            
                                            	Static Flow Label
                                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance, self).__init__()

                                                self.yang_name = "flow-label-load-balance"
                                                self.yang_parent_name = "bgp-signaling-protocol"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('flow_label', YLeaf(YType.enumeration, 'flow-label')),
                                                    ('static', YLeaf(YType.empty, 'static')),
                                                ])
                                                self.flow_label = None
                                                self.static = None
                                                self._segment_path = lambda: "flow-label-load-balance"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance, ['flow_label', 'static'], name, value)


                                    class RouteTargets(Entity):
                                        """
                                        Route Target
                                        
                                        .. attribute:: route_target
                                        
                                        	Name of the Route Target
                                        	**type**\: list of  		 :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets, self).__init__()

                                            self.yang_name = "route-targets"
                                            self.yang_parent_name = "bgp-auto-discovery"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("route-target", ("route_target", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget))])
                                            self._leafs = OrderedDict()

                                            self.route_target = YList(self)
                                            self._segment_path = lambda: "route-targets"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets, [], name, value)


                                        class RouteTarget(Entity):
                                            """
                                            Name of the Route Target
                                            
                                            .. attribute:: role  (key)
                                            
                                            	Role of the router target type
                                            	**type**\:  :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                                            
                                            .. attribute:: format  (key)
                                            
                                            	Format of the route target
                                            	**type**\:  :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                                            
                                            .. attribute:: two_byte_as_or_four_byte_as
                                            
                                            	two byte as or four byte as
                                            	**type**\: list of  		 :py:class:`TwoByteAsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	ipv4 address
                                            	**type**\: list of  		 :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget, self).__init__()

                                                self.yang_name = "route-target"
                                                self.yang_parent_name = "route-targets"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['role','format']
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([("two-byte-as-or-four-byte-as", ("two_byte_as_or_four_byte_as", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs)), ("ipv4-address", ("ipv4_address", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address))])
                                                self._leafs = OrderedDict([
                                                    ('role', YLeaf(YType.enumeration, 'role')),
                                                    ('format', YLeaf(YType.enumeration, 'format')),
                                                ])
                                                self.role = None
                                                self.format = None

                                                self.two_byte_as_or_four_byte_as = YList(self)
                                                self.ipv4_address = YList(self)
                                                self._segment_path = lambda: "route-target" + "[role='" + str(self.role) + "']" + "[format='" + str(self.format) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget, ['role', 'format'], name, value)


                                            class TwoByteAsOrFourByteAs(Entity):
                                                """
                                                two byte as or four byte as
                                                
                                                .. attribute:: as_  (key)
                                                
                                                	Two byte or 4 byte AS number
                                                	**type**\: int
                                                
                                                	**range:** 1..4294967295
                                                
                                                .. attribute:: as_index  (key)
                                                
                                                	AS\:nn (hex or decimal format)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2017-06-26'

                                                def __init__(self):
                                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs, self).__init__()

                                                    self.yang_name = "two-byte-as-or-four-byte-as"
                                                    self.yang_parent_name = "route-target"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['as_','as_index']
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('as_', YLeaf(YType.uint32, 'as')),
                                                        ('as_index', YLeaf(YType.uint32, 'as-index')),
                                                    ])
                                                    self.as_ = None
                                                    self.as_index = None
                                                    self._segment_path = lambda: "two-byte-as-or-four-byte-as" + "[as='" + str(self.as_) + "']" + "[as-index='" + str(self.as_index) + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs, ['as_', 'as_index'], name, value)


                                            class Ipv4Address(Entity):
                                                """
                                                ipv4 address
                                                
                                                .. attribute:: address  (key)
                                                
                                                	IPV4 address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: addr_index  (key)
                                                
                                                	Addr index
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2017-06-26'

                                                def __init__(self):
                                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address, self).__init__()

                                                    self.yang_name = "ipv4-address"
                                                    self.yang_parent_name = "route-target"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['address','addr_index']
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('address', YLeaf(YType.str, 'address')),
                                                        ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                                                    ])
                                                    self.address = None
                                                    self.addr_index = None
                                                    self._segment_path = lambda: "ipv4-address" + "[address='" + str(self.address) + "']" + "[addr-index='" + str(self.addr_index) + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address, ['address', 'addr_index'], name, value)


                        class BdAttachmentCircuits(Entity):
                            """
                            Attachment Circuit table
                            
                            .. attribute:: bd_attachment_circuit
                            
                            	Name of the Attachment Circuit
                            	**type**\: list of  		 :py:class:`BdAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits, self).__init__()

                                self.yang_name = "bd-attachment-circuits"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("bd-attachment-circuit", ("bd_attachment_circuit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit))])
                                self._leafs = OrderedDict()

                                self.bd_attachment_circuit = YList(self)
                                self._segment_path = lambda: "bd-attachment-circuits"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits, [], name, value)


                            class BdAttachmentCircuit(Entity):
                                """
                                Name of the Attachment Circuit
                                
                                .. attribute:: name  (key)
                                
                                	The name of the Attachment Circuit
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: interface_ip_source_guard
                                
                                	IP Source Guard
                                	**type**\:  :py:class:`InterfaceIpSourceGuard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard>`
                                
                                .. attribute:: interface_dai
                                
                                	L2 Interface Dynamic ARP Inspection
                                	**type**\:  :py:class:`InterfaceDai <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai>`
                                
                                .. attribute:: interface_profile
                                
                                	Attach a DHCP profile
                                	**type**\:  :py:class:`InterfaceProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile>`
                                
                                .. attribute:: bdac_storm_control_types
                                
                                	Storm Control
                                	**type**\:  :py:class:`BdacStormControlTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes>`
                                
                                .. attribute:: split_horizon
                                
                                	Split Horizon
                                	**type**\:  :py:class:`SplitHorizon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon>`
                                
                                .. attribute:: static_mac_addresses
                                
                                	Static Mac Address Table
                                	**type**\:  :py:class:`StaticMacAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses>`
                                
                                .. attribute:: interface_mac
                                
                                	MAC configuration commands
                                	**type**\:  :py:class:`InterfaceMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac>`
                                
                                .. attribute:: interface_flooding
                                
                                	Enable or Disable Flooding
                                	**type**\:  :py:class:`InterfaceTrafficFlood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFlood>`
                                
                                .. attribute:: interface_igmp_snoop
                                
                                	Attach a IGMP Snooping profile
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                .. attribute:: interface_flooding_unknown_unicast
                                
                                	Enable or Disable Unknown Unicast Flooding
                                	**type**\:  :py:class:`InterfaceTrafficFlood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFlood>`
                                
                                .. attribute:: interface_mld_snoop
                                
                                	Attach a MLD Snooping profile
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit, self).__init__()

                                    self.yang_name = "bd-attachment-circuit"
                                    self.yang_parent_name = "bd-attachment-circuits"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['name']
                                    self._child_container_classes = OrderedDict([("interface-ip-source-guard", ("interface_ip_source_guard", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard)), ("interface-dai", ("interface_dai", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai)), ("interface-profile", ("interface_profile", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile)), ("bdac-storm-control-types", ("bdac_storm_control_types", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes)), ("split-horizon", ("split_horizon", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon)), ("static-mac-addresses", ("static_mac_addresses", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses)), ("interface-mac", ("interface_mac", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('name', YLeaf(YType.str, 'name')),
                                        ('interface_flooding', YLeaf(YType.enumeration, 'interface-flooding')),
                                        ('interface_igmp_snoop', YLeaf(YType.str, 'interface-igmp-snoop')),
                                        ('interface_flooding_unknown_unicast', YLeaf(YType.enumeration, 'interface-flooding-unknown-unicast')),
                                        ('interface_mld_snoop', YLeaf(YType.str, 'interface-mld-snoop')),
                                    ])
                                    self.name = None
                                    self.interface_flooding = None
                                    self.interface_igmp_snoop = None
                                    self.interface_flooding_unknown_unicast = None
                                    self.interface_mld_snoop = None

                                    self.interface_ip_source_guard = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard()
                                    self.interface_ip_source_guard.parent = self
                                    self._children_name_map["interface_ip_source_guard"] = "interface-ip-source-guard"
                                    self._children_yang_names.add("interface-ip-source-guard")

                                    self.interface_dai = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai()
                                    self.interface_dai.parent = self
                                    self._children_name_map["interface_dai"] = "interface-dai"
                                    self._children_yang_names.add("interface-dai")

                                    self.interface_profile = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile()
                                    self.interface_profile.parent = self
                                    self._children_name_map["interface_profile"] = "interface-profile"
                                    self._children_yang_names.add("interface-profile")

                                    self.bdac_storm_control_types = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes()
                                    self.bdac_storm_control_types.parent = self
                                    self._children_name_map["bdac_storm_control_types"] = "bdac-storm-control-types"
                                    self._children_yang_names.add("bdac-storm-control-types")

                                    self.split_horizon = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon()
                                    self.split_horizon.parent = self
                                    self._children_name_map["split_horizon"] = "split-horizon"
                                    self._children_yang_names.add("split-horizon")

                                    self.static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses()
                                    self.static_mac_addresses.parent = self
                                    self._children_name_map["static_mac_addresses"] = "static-mac-addresses"
                                    self._children_yang_names.add("static-mac-addresses")

                                    self.interface_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac()
                                    self.interface_mac.parent = self
                                    self._children_name_map["interface_mac"] = "interface-mac"
                                    self._children_yang_names.add("interface-mac")
                                    self._segment_path = lambda: "bd-attachment-circuit" + "[name='" + str(self.name) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit, ['name', 'interface_flooding', 'interface_igmp_snoop', 'interface_flooding_unknown_unicast', 'interface_mld_snoop'], name, value)


                                class InterfaceIpSourceGuard(Entity):
                                    """
                                    IP Source Guard
                                    
                                    .. attribute:: logging
                                    
                                    	Logging Type
                                    	**type**\:  :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                    
                                    .. attribute:: disable
                                    
                                    	Disable L2 Interface Dynamic IP source guard
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable IP Source Guard
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard, self).__init__()

                                        self.yang_name = "interface-ip-source-guard"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('logging', YLeaf(YType.enumeration, 'logging')),
                                            ('disable', YLeaf(YType.empty, 'disable')),
                                            ('enable', YLeaf(YType.empty, 'enable')),
                                        ])
                                        self.logging = None
                                        self.disable = None
                                        self.enable = None
                                        self._segment_path = lambda: "interface-ip-source-guard"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard, ['logging', 'disable', 'enable'], name, value)


                                class InterfaceDai(Entity):
                                    """
                                    L2 Interface Dynamic ARP Inspection
                                    
                                    .. attribute:: interface_dai_address_validation
                                    
                                    	Address Validation
                                    	**type**\:  :py:class:`InterfaceDaiAddressValidation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation>`
                                    
                                    .. attribute:: logging
                                    
                                    	Logging Type
                                    	**type**\:  :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                    
                                    .. attribute:: disable
                                    
                                    	Disable L2 Interface Dynamic ARP Inspection
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable L2 Interface Dynamic ARP Inspection
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai, self).__init__()

                                        self.yang_name = "interface-dai"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("interface-dai-address-validation", ("interface_dai_address_validation", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('logging', YLeaf(YType.enumeration, 'logging')),
                                            ('disable', YLeaf(YType.empty, 'disable')),
                                            ('enable', YLeaf(YType.empty, 'enable')),
                                        ])
                                        self.logging = None
                                        self.disable = None
                                        self.enable = None

                                        self.interface_dai_address_validation = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation()
                                        self.interface_dai_address_validation.parent = self
                                        self._children_name_map["interface_dai_address_validation"] = "interface-dai-address-validation"
                                        self._children_yang_names.add("interface-dai-address-validation")
                                        self._segment_path = lambda: "interface-dai"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai, ['logging', 'disable', 'enable'], name, value)


                                    class InterfaceDaiAddressValidation(Entity):
                                        """
                                        Address Validation
                                        
                                        .. attribute:: ipv4_verification
                                        
                                        	IPv4 Verification
                                        	**type**\:  :py:class:`L2vpnVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification>`
                                        
                                        .. attribute:: destination_mac_verification
                                        
                                        	Destination MAC Verification
                                        	**type**\:  :py:class:`L2vpnVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification>`
                                        
                                        .. attribute:: source_mac_verification
                                        
                                        	Source MAC Verification
                                        	**type**\:  :py:class:`L2vpnVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable Address Validation
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation, self).__init__()

                                            self.yang_name = "interface-dai-address-validation"
                                            self.yang_parent_name = "interface-dai"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('ipv4_verification', YLeaf(YType.enumeration, 'ipv4-verification')),
                                                ('destination_mac_verification', YLeaf(YType.enumeration, 'destination-mac-verification')),
                                                ('source_mac_verification', YLeaf(YType.enumeration, 'source-mac-verification')),
                                                ('enable', YLeaf(YType.empty, 'enable')),
                                            ])
                                            self.ipv4_verification = None
                                            self.destination_mac_verification = None
                                            self.source_mac_verification = None
                                            self.enable = None
                                            self._segment_path = lambda: "interface-dai-address-validation"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation, ['ipv4_verification', 'destination_mac_verification', 'source_mac_verification', 'enable'], name, value)


                                class InterfaceProfile(Entity):
                                    """
                                    Attach a DHCP profile
                                    
                                    .. attribute:: profile_id
                                    
                                    	Set the snooping profile
                                    	**type**\:  :py:class:`InterfaceProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile>`
                                    
                                    .. attribute:: dhcp_snooping_id
                                    
                                    	Disable DHCP snooping
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile, self).__init__()

                                        self.yang_name = "interface-profile"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('profile_id', YLeaf(YType.enumeration, 'profile-id')),
                                            ('dhcp_snooping_id', YLeaf(YType.str, 'dhcp-snooping-id')),
                                        ])
                                        self.profile_id = None
                                        self.dhcp_snooping_id = None
                                        self._segment_path = lambda: "interface-profile"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile, ['profile_id', 'dhcp_snooping_id'], name, value)


                                class BdacStormControlTypes(Entity):
                                    """
                                    Storm Control
                                    
                                    .. attribute:: bdac_storm_control_type
                                    
                                    	Storm Control Type
                                    	**type**\: list of  		 :py:class:`BdacStormControlType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes, self).__init__()

                                        self.yang_name = "bdac-storm-control-types"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("bdac-storm-control-type", ("bdac_storm_control_type", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType))])
                                        self._leafs = OrderedDict()

                                        self.bdac_storm_control_type = YList(self)
                                        self._segment_path = lambda: "bdac-storm-control-types"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes, [], name, value)


                                    class BdacStormControlType(Entity):
                                        """
                                        Storm Control Type
                                        
                                        .. attribute:: sctype  (key)
                                        
                                        	Storm Control Type
                                        	**type**\:  :py:class:`StormControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.StormControl>`
                                        
                                        .. attribute:: storm_control_unit
                                        
                                        	Specify units for Storm Control Configuration
                                        	**type**\:  :py:class:`StormControlUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType, self).__init__()

                                            self.yang_name = "bdac-storm-control-type"
                                            self.yang_parent_name = "bdac-storm-control-types"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['sctype']
                                            self._child_container_classes = OrderedDict([("storm-control-unit", ("storm_control_unit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('sctype', YLeaf(YType.enumeration, 'sctype')),
                                            ])
                                            self.sctype = None

                                            self.storm_control_unit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit()
                                            self.storm_control_unit.parent = self
                                            self._children_name_map["storm_control_unit"] = "storm-control-unit"
                                            self._children_yang_names.add("storm-control-unit")
                                            self._segment_path = lambda: "bdac-storm-control-type" + "[sctype='" + str(self.sctype) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType, ['sctype'], name, value)


                                        class StormControlUnit(Entity):
                                            """
                                            Specify units for Storm Control Configuration
                                            
                                            .. attribute:: kbits_per_sec
                                            
                                            	Kilobits Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                            	**type**\: int
                                            
                                            	**range:** 64..1280000
                                            
                                            	**units**\: kbit/s
                                            
                                            .. attribute:: pkts_per_sec
                                            
                                            	Packets Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                            	**type**\: int
                                            
                                            	**range:** 1..160000
                                            
                                            	**units**\: packet/s
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit, self).__init__()

                                                self.yang_name = "storm-control-unit"
                                                self.yang_parent_name = "bdac-storm-control-type"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('kbits_per_sec', YLeaf(YType.uint32, 'kbits-per-sec')),
                                                    ('pkts_per_sec', YLeaf(YType.uint32, 'pkts-per-sec')),
                                                ])
                                                self.kbits_per_sec = None
                                                self.pkts_per_sec = None
                                                self._segment_path = lambda: "storm-control-unit"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit, ['kbits_per_sec', 'pkts_per_sec'], name, value)


                                class SplitHorizon(Entity):
                                    """
                                    Split Horizon
                                    
                                    .. attribute:: split_horizon_group_id
                                    
                                    	Split Horizon Group ID
                                    	**type**\:  :py:class:`SplitHorizonGroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon, self).__init__()

                                        self.yang_name = "split-horizon"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("split-horizon-group-id", ("split_horizon_group_id", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict()

                                        self.split_horizon_group_id = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId()
                                        self.split_horizon_group_id.parent = self
                                        self._children_name_map["split_horizon_group_id"] = "split-horizon-group-id"
                                        self._children_yang_names.add("split-horizon-group-id")
                                        self._segment_path = lambda: "split-horizon"


                                    class SplitHorizonGroupId(Entity):
                                        """
                                        Split Horizon Group ID
                                        
                                        .. attribute:: enable
                                        
                                        	Enable split horizon group
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId, self).__init__()

                                            self.yang_name = "split-horizon-group-id"
                                            self.yang_parent_name = "split-horizon"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', YLeaf(YType.empty, 'enable')),
                                            ])
                                            self.enable = None
                                            self._segment_path = lambda: "split-horizon-group-id"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId, ['enable'], name, value)


                                class StaticMacAddresses(Entity):
                                    """
                                    Static Mac Address Table
                                    
                                    .. attribute:: static_mac_address
                                    
                                    	Static Mac Address Configuration
                                    	**type**\: list of  		 :py:class:`StaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses, self).__init__()

                                        self.yang_name = "static-mac-addresses"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("static-mac-address", ("static_mac_address", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress))])
                                        self._leafs = OrderedDict()

                                        self.static_mac_address = YList(self)
                                        self._segment_path = lambda: "static-mac-addresses"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses, [], name, value)


                                    class StaticMacAddress(Entity):
                                        """
                                        Static Mac Address Configuration
                                        
                                        .. attribute:: address  (key)
                                        
                                        	Static MAC address
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress, self).__init__()

                                            self.yang_name = "static-mac-address"
                                            self.yang_parent_name = "static-mac-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['address']
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('address', YLeaf(YType.str, 'address')),
                                            ])
                                            self.address = None
                                            self._segment_path = lambda: "static-mac-address" + "[address='" + str(self.address) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress, ['address'], name, value)


                                class InterfaceMac(Entity):
                                    """
                                    MAC configuration commands
                                    
                                    .. attribute:: interface_mac_aging
                                    
                                    	MAC\-Aging configuration commands
                                    	**type**\:  :py:class:`InterfaceMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging>`
                                    
                                    .. attribute:: interface_mac_secure
                                    
                                    	MAC Secure
                                    	**type**\:  :py:class:`InterfaceMacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure>`
                                    
                                    .. attribute:: interface_mac_limit
                                    
                                    	MAC\-Limit configuration commands
                                    	**type**\:  :py:class:`InterfaceMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit>`
                                    
                                    .. attribute:: interface_mac_port_down_flush
                                    
                                    	Enable/Disable MAC Flush When Port goes down
                                    	**type**\:  :py:class:`PortDownFlush <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.PortDownFlush>`
                                    
                                    .. attribute:: interface_mac_learning
                                    
                                    	Enable Mac Learning
                                    	**type**\:  :py:class:`MacLearn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLearn>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac, self).__init__()

                                        self.yang_name = "interface-mac"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("interface-mac-aging", ("interface_mac_aging", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging)), ("interface-mac-secure", ("interface_mac_secure", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure)), ("interface-mac-limit", ("interface_mac_limit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('interface_mac_port_down_flush', YLeaf(YType.enumeration, 'interface-mac-port-down-flush')),
                                            ('interface_mac_learning', YLeaf(YType.enumeration, 'interface-mac-learning')),
                                        ])
                                        self.interface_mac_port_down_flush = None
                                        self.interface_mac_learning = None

                                        self.interface_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging()
                                        self.interface_mac_aging.parent = self
                                        self._children_name_map["interface_mac_aging"] = "interface-mac-aging"
                                        self._children_yang_names.add("interface-mac-aging")

                                        self.interface_mac_secure = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure()
                                        self.interface_mac_secure.parent = self
                                        self._children_name_map["interface_mac_secure"] = "interface-mac-secure"
                                        self._children_yang_names.add("interface-mac-secure")

                                        self.interface_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit()
                                        self.interface_mac_limit.parent = self
                                        self._children_name_map["interface_mac_limit"] = "interface-mac-limit"
                                        self._children_yang_names.add("interface-mac-limit")
                                        self._segment_path = lambda: "interface-mac"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac, ['interface_mac_port_down_flush', 'interface_mac_learning'], name, value)


                                    class InterfaceMacAging(Entity):
                                        """
                                        MAC\-Aging configuration commands
                                        
                                        .. attribute:: interface_mac_aging_time
                                        
                                        	Mac Aging Time
                                        	**type**\: int
                                        
                                        	**range:** 300..30000
                                        
                                        .. attribute:: interface_mac_aging_type
                                        
                                        	MAC address aging type
                                        	**type**\:  :py:class:`MacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAging>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging, self).__init__()

                                            self.yang_name = "interface-mac-aging"
                                            self.yang_parent_name = "interface-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('interface_mac_aging_time', YLeaf(YType.uint32, 'interface-mac-aging-time')),
                                                ('interface_mac_aging_type', YLeaf(YType.enumeration, 'interface-mac-aging-type')),
                                            ])
                                            self.interface_mac_aging_time = None
                                            self.interface_mac_aging_type = None
                                            self._segment_path = lambda: "interface-mac-aging"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging, ['interface_mac_aging_time', 'interface_mac_aging_type'], name, value)


                                    class InterfaceMacSecure(Entity):
                                        """
                                        MAC Secure
                                        
                                        .. attribute:: logging
                                        
                                        	MAC Secure Logging
                                        	**type**\:  :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                        
                                        .. attribute:: disable
                                        
                                        	Disable L2 Interface MAC Secure
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: action
                                        
                                        	MAC secure enforcement action
                                        	**type**\:  :py:class:`MacSecureAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacSecureAction>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable MAC Secure
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure, self).__init__()

                                            self.yang_name = "interface-mac-secure"
                                            self.yang_parent_name = "interface-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('logging', YLeaf(YType.enumeration, 'logging')),
                                                ('disable', YLeaf(YType.empty, 'disable')),
                                                ('action', YLeaf(YType.enumeration, 'action')),
                                                ('enable', YLeaf(YType.empty, 'enable')),
                                            ])
                                            self.logging = None
                                            self.disable = None
                                            self.action = None
                                            self.enable = None
                                            self._segment_path = lambda: "interface-mac-secure"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure, ['logging', 'disable', 'action', 'enable'], name, value)


                                    class InterfaceMacLimit(Entity):
                                        """
                                        MAC\-Limit configuration commands
                                        
                                        .. attribute:: interface_mac_limit_max
                                        
                                        	Number of MAC addresses on an Interface after which MAC limit action is taken
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: interface_mac_limit_notif
                                        
                                        	MAC address limit notification action in a Interface
                                        	**type**\:  :py:class:`MacNotification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotification>`
                                        
                                        .. attribute:: interface_mac_limit_action
                                        
                                        	Interface MAC address limit enforcement action
                                        	**type**\:  :py:class:`MacLimitAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit, self).__init__()

                                            self.yang_name = "interface-mac-limit"
                                            self.yang_parent_name = "interface-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('interface_mac_limit_max', YLeaf(YType.uint32, 'interface-mac-limit-max')),
                                                ('interface_mac_limit_notif', YLeaf(YType.enumeration, 'interface-mac-limit-notif')),
                                                ('interface_mac_limit_action', YLeaf(YType.enumeration, 'interface-mac-limit-action')),
                                            ])
                                            self.interface_mac_limit_max = None
                                            self.interface_mac_limit_notif = None
                                            self.interface_mac_limit_action = None
                                            self._segment_path = lambda: "interface-mac-limit"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit, ['interface_mac_limit_max', 'interface_mac_limit_notif', 'interface_mac_limit_action'], name, value)


                        class BdPseudowireEvpns(Entity):
                            """
                            List of EVPN pseudowires
                            
                            .. attribute:: bd_pseudowire_evpn
                            
                            	EVPN Pseudowire configuration
                            	**type**\: list of  		 :py:class:`BdPseudowireEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns, self).__init__()

                                self.yang_name = "bd-pseudowire-evpns"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("bd-pseudowire-evpn", ("bd_pseudowire_evpn", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn))])
                                self._leafs = OrderedDict()

                                self.bd_pseudowire_evpn = YList(self)
                                self._segment_path = lambda: "bd-pseudowire-evpns"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns, [], name, value)


                            class BdPseudowireEvpn(Entity):
                                """
                                EVPN Pseudowire configuration
                                
                                .. attribute:: eviid  (key)
                                
                                	Ethernet VPN ID
                                	**type**\: int
                                
                                	**range:** 1..65534
                                
                                .. attribute:: acid  (key)
                                
                                	AC ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn, self).__init__()

                                    self.yang_name = "bd-pseudowire-evpn"
                                    self.yang_parent_name = "bd-pseudowire-evpns"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['eviid','acid']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('eviid', YLeaf(YType.uint32, 'eviid')),
                                        ('acid', YLeaf(YType.uint32, 'acid')),
                                    ])
                                    self.eviid = None
                                    self.acid = None
                                    self._segment_path = lambda: "bd-pseudowire-evpn" + "[eviid='" + str(self.eviid) + "']" + "[acid='" + str(self.acid) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn, ['eviid', 'acid'], name, value)


                        class IpSourceGuard(Entity):
                            """
                            IP Source Guard
                            
                            .. attribute:: logging
                            
                            	Enable Logging
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: enable
                            
                            	Enable IP Source Guard
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard, self).__init__()

                                self.yang_name = "ip-source-guard"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', YLeaf(YType.empty, 'logging')),
                                    ('enable', YLeaf(YType.empty, 'enable')),
                                ])
                                self.logging = None
                                self.enable = None
                                self._segment_path = lambda: "ip-source-guard"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard, ['logging', 'enable'], name, value)


                        class Dai(Entity):
                            """
                            Dynamic ARP Inspection
                            
                            .. attribute:: dai_address_validation
                            
                            	Address Validation
                            	**type**\:  :py:class:`DaiAddressValidation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation>`
                            
                            .. attribute:: logging
                            
                            	Enable Logging
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: enable
                            
                            	Enable Dynamic ARP Inspection
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai, self).__init__()

                                self.yang_name = "dai"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("dai-address-validation", ("dai_address_validation", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', YLeaf(YType.empty, 'logging')),
                                    ('enable', YLeaf(YType.empty, 'enable')),
                                ])
                                self.logging = None
                                self.enable = None

                                self.dai_address_validation = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation()
                                self.dai_address_validation.parent = self
                                self._children_name_map["dai_address_validation"] = "dai-address-validation"
                                self._children_yang_names.add("dai-address-validation")
                                self._segment_path = lambda: "dai"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai, ['logging', 'enable'], name, value)


                            class DaiAddressValidation(Entity):
                                """
                                Address Validation
                                
                                .. attribute:: ipv4_verification
                                
                                	Enable IPv4 Verification
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: destination_mac_verification
                                
                                	Enable Destination MAC Verification
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: source_mac_verification
                                
                                	Enable Source MAC Verification
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: enable
                                
                                	Enable Address Validation
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation, self).__init__()

                                    self.yang_name = "dai-address-validation"
                                    self.yang_parent_name = "dai"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipv4_verification', YLeaf(YType.empty, 'ipv4-verification')),
                                        ('destination_mac_verification', YLeaf(YType.empty, 'destination-mac-verification')),
                                        ('source_mac_verification', YLeaf(YType.empty, 'source-mac-verification')),
                                        ('enable', YLeaf(YType.empty, 'enable')),
                                    ])
                                    self.ipv4_verification = None
                                    self.destination_mac_verification = None
                                    self.source_mac_verification = None
                                    self.enable = None
                                    self._segment_path = lambda: "dai-address-validation"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation, ['ipv4_verification', 'destination_mac_verification', 'source_mac_verification', 'enable'], name, value)


                        class RoutedInterfaces(Entity):
                            """
                            Bridge Domain Routed Interface Table
                            
                            .. attribute:: routed_interface
                            
                            	Bridge Domain Routed Interface
                            	**type**\: list of  		 :py:class:`RoutedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces, self).__init__()

                                self.yang_name = "routed-interfaces"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("routed-interface", ("routed_interface", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface))])
                                self._leafs = OrderedDict()

                                self.routed_interface = YList(self)
                                self._segment_path = lambda: "routed-interfaces"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces, [], name, value)


                            class RoutedInterface(Entity):
                                """
                                Bridge Domain Routed Interface
                                
                                .. attribute:: interface_name  (key)
                                
                                	The name of the Routed Interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: routed_interface_split_horizon_group
                                
                                	Routed interface split horizon group
                                	**type**\:  :py:class:`RoutedInterfaceSplitHorizonGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface, self).__init__()

                                    self.yang_name = "routed-interface"
                                    self.yang_parent_name = "routed-interfaces"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_container_classes = OrderedDict([("routed-interface-split-horizon-group", ("routed_interface_split_horizon_group", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ])
                                    self.interface_name = None

                                    self.routed_interface_split_horizon_group = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup()
                                    self.routed_interface_split_horizon_group.parent = self
                                    self._children_name_map["routed_interface_split_horizon_group"] = "routed-interface-split-horizon-group"
                                    self._children_yang_names.add("routed-interface-split-horizon-group")
                                    self._segment_path = lambda: "routed-interface" + "[interface-name='" + str(self.interface_name) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface, ['interface_name'], name, value)


                                class RoutedInterfaceSplitHorizonGroup(Entity):
                                    """
                                    Routed interface split horizon group
                                    
                                    .. attribute:: routed_interface_split_horizon_group_core
                                    
                                    	Configure BVI under SHG 1
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup, self).__init__()

                                        self.yang_name = "routed-interface-split-horizon-group"
                                        self.yang_parent_name = "routed-interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('routed_interface_split_horizon_group_core', YLeaf(YType.empty, 'routed-interface-split-horizon-group-core')),
                                        ])
                                        self.routed_interface_split_horizon_group_core = None
                                        self._segment_path = lambda: "routed-interface-split-horizon-group"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup, ['routed_interface_split_horizon_group_core'], name, value)


        class PseudowireClasses(Entity):
            """
            List of pseudowire classes
            
            .. attribute:: pseudowire_class
            
            	Pseudowire class
            	**type**\: list of  		 :py:class:`PseudowireClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Database.PseudowireClasses, self).__init__()

                self.yang_name = "pseudowire-classes"
                self.yang_parent_name = "database"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("pseudowire-class", ("pseudowire_class", L2Vpn.Database.PseudowireClasses.PseudowireClass))])
                self._leafs = OrderedDict()

                self.pseudowire_class = YList(self)
                self._segment_path = lambda: "pseudowire-classes"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.Database.PseudowireClasses, [], name, value)


            class PseudowireClass(Entity):
                """
                Pseudowire class
                
                .. attribute:: name  (key)
                
                	Name of the pseudowire class
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: l2tpv3_encapsulation
                
                	L2TPv3 encapsulation
                	**type**\:  :py:class:`L2Tpv3Encapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation>`
                
                .. attribute:: backup_disable_delay
                
                	Back Up Pseudowire class
                	**type**\:  :py:class:`BackupDisableDelay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay>`
                
                .. attribute:: mpls_encapsulation
                
                	MPLS encapsulation
                	**type**\:  :py:class:`MplsEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation>`
                
                .. attribute:: mac_withdraw
                
                	Enable backup MAC withdraw
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: enable
                
                	Enable pseudowire class
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.PseudowireClasses.PseudowireClass, self).__init__()

                    self.yang_name = "pseudowire-class"
                    self.yang_parent_name = "pseudowire-classes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([("l2tpv3-encapsulation", ("l2tpv3_encapsulation", L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation)), ("backup-disable-delay", ("backup_disable_delay", L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay)), ("mpls-encapsulation", ("mpls_encapsulation", L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('mac_withdraw', YLeaf(YType.empty, 'mac-withdraw')),
                        ('enable', YLeaf(YType.empty, 'enable')),
                    ])
                    self.name = None
                    self.mac_withdraw = None
                    self.enable = None

                    self.l2tpv3_encapsulation = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation()
                    self.l2tpv3_encapsulation.parent = self
                    self._children_name_map["l2tpv3_encapsulation"] = "l2tpv3-encapsulation"
                    self._children_yang_names.add("l2tpv3-encapsulation")

                    self.backup_disable_delay = L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay()
                    self.backup_disable_delay.parent = self
                    self._children_name_map["backup_disable_delay"] = "backup-disable-delay"
                    self._children_yang_names.add("backup-disable-delay")

                    self.mpls_encapsulation = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation()
                    self.mpls_encapsulation.parent = self
                    self._children_name_map["mpls_encapsulation"] = "mpls-encapsulation"
                    self._children_yang_names.add("mpls-encapsulation")
                    self._segment_path = lambda: "pseudowire-class" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/pseudowire-classes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass, ['name', 'mac_withdraw', 'enable'], name, value)


                class L2Tpv3Encapsulation(Entity):
                    """
                    L2TPv3 encapsulation
                    
                    .. attribute:: sequencing
                    
                    	Sequencing
                    	**type**\:  :py:class:`Sequencing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing>`
                    
                    .. attribute:: type_of_service
                    
                    	Type of service
                    	**type**\:  :py:class:`TypeOfService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService>`
                    
                    .. attribute:: signaling_protocol
                    
                    	L2TPv3 signaling protocol
                    	**type**\:  :py:class:`SignalingProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol>`
                    
                    .. attribute:: path_mtu
                    
                    	Path maximum transmission unit
                    	**type**\:  :py:class:`PathMtu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu>`
                    
                    .. attribute:: df_bit_set
                    
                    	Set the do not fragment bit to 1
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: cookie_size
                    
                    	Cookie size
                    	**type**\:  :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                    
                    	**default value**\: zero
                    
                    .. attribute:: source_address
                    
                    	Source IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: transport_mode
                    
                    	Transport mode
                    	**type**\:  :py:class:`TransportMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.TransportMode>`
                    
                    .. attribute:: enable
                    
                    	Enable L2TPv3 encapsulation
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: time_to_live
                    
                    	Time to live
                    	**type**\: int
                    
                    	**range:** 1..255
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation, self).__init__()

                        self.yang_name = "l2tpv3-encapsulation"
                        self.yang_parent_name = "pseudowire-class"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("sequencing", ("sequencing", L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing)), ("type-of-service", ("type_of_service", L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService)), ("signaling-protocol", ("signaling_protocol", L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol)), ("path-mtu", ("path_mtu", L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('df_bit_set', YLeaf(YType.empty, 'df-bit-set')),
                            ('cookie_size', YLeaf(YType.enumeration, 'cookie-size')),
                            ('source_address', YLeaf(YType.str, 'source-address')),
                            ('transport_mode', YLeaf(YType.enumeration, 'transport-mode')),
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('time_to_live', YLeaf(YType.uint32, 'time-to-live')),
                        ])
                        self.df_bit_set = None
                        self.cookie_size = None
                        self.source_address = None
                        self.transport_mode = None
                        self.enable = None
                        self.time_to_live = None

                        self.sequencing = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing()
                        self.sequencing.parent = self
                        self._children_name_map["sequencing"] = "sequencing"
                        self._children_yang_names.add("sequencing")

                        self.type_of_service = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService()
                        self.type_of_service.parent = self
                        self._children_name_map["type_of_service"] = "type-of-service"
                        self._children_yang_names.add("type-of-service")

                        self.signaling_protocol = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol()
                        self.signaling_protocol.parent = self
                        self._children_name_map["signaling_protocol"] = "signaling-protocol"
                        self._children_yang_names.add("signaling-protocol")

                        self.path_mtu = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu()
                        self.path_mtu.parent = self
                        self._children_name_map["path_mtu"] = "path-mtu"
                        self._children_yang_names.add("path-mtu")
                        self._segment_path = lambda: "l2tpv3-encapsulation"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation, ['df_bit_set', 'cookie_size', 'source_address', 'transport_mode', 'enable', 'time_to_live'], name, value)


                    class Sequencing(Entity):
                        """
                        Sequencing
                        
                        .. attribute:: sequencing
                        
                        	Sequencing
                        	**type**\:  :py:class:`L2tpv3Sequencing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpv3Sequencing>`
                        
                        	**default value**\: off
                        
                        .. attribute:: resync_threshold
                        
                        	Out of sequence threshold
                        	**type**\: int
                        
                        	**range:** 5..65535
                        
                        	**default value**\: 5
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing, self).__init__()

                            self.yang_name = "sequencing"
                            self.yang_parent_name = "l2tpv3-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sequencing', YLeaf(YType.enumeration, 'sequencing')),
                                ('resync_threshold', YLeaf(YType.uint32, 'resync-threshold')),
                            ])
                            self.sequencing = None
                            self.resync_threshold = None
                            self._segment_path = lambda: "sequencing"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing, ['sequencing', 'resync_threshold'], name, value)


                    class TypeOfService(Entity):
                        """
                        Type of service
                        
                        .. attribute:: type_of_service_value
                        
                        	Type of service value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: type_of_service_mode
                        
                        	Type of service mode
                        	**type**\:  :py:class:`TypeOfServiceMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.TypeOfServiceMode>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService, self).__init__()

                            self.yang_name = "type-of-service"
                            self.yang_parent_name = "l2tpv3-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type_of_service_value', YLeaf(YType.uint32, 'type-of-service-value')),
                                ('type_of_service_mode', YLeaf(YType.enumeration, 'type-of-service-mode')),
                            ])
                            self.type_of_service_value = None
                            self.type_of_service_mode = None
                            self._segment_path = lambda: "type-of-service"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService, ['type_of_service_value', 'type_of_service_mode'], name, value)


                    class SignalingProtocol(Entity):
                        """
                        L2TPv3 signaling protocol
                        
                        .. attribute:: protocol
                        
                        	L2TPv3 signaling protocol
                        	**type**\:  :py:class:`L2tpSignalingProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpSignalingProtocol>`
                        
                        	**default value**\: l2tpv3
                        
                        .. attribute:: l2tpv3_class_name
                        
                        	Name of the L2TPv3 class name
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol, self).__init__()

                            self.yang_name = "signaling-protocol"
                            self.yang_parent_name = "l2tpv3-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('protocol', YLeaf(YType.enumeration, 'protocol')),
                                ('l2tpv3_class_name', YLeaf(YType.str, 'l2tpv3-class-name')),
                            ])
                            self.protocol = None
                            self.l2tpv3_class_name = None
                            self._segment_path = lambda: "signaling-protocol"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol, ['protocol', 'l2tpv3_class_name'], name, value)


                    class PathMtu(Entity):
                        """
                        Path maximum transmission unit
                        
                        .. attribute:: enable
                        
                        	Enable path MTU
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: max_path_mtu
                        
                        	Maximum path maximum transmission unit
                        	**type**\: int
                        
                        	**range:** 68..65535
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu, self).__init__()

                            self.yang_name = "path-mtu"
                            self.yang_parent_name = "l2tpv3-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', YLeaf(YType.empty, 'enable')),
                                ('max_path_mtu', YLeaf(YType.uint32, 'max-path-mtu')),
                            ])
                            self.enable = None
                            self.max_path_mtu = None
                            self._segment_path = lambda: "path-mtu"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu, ['enable', 'max_path_mtu'], name, value)


                class BackupDisableDelay(Entity):
                    """
                    Back Up Pseudowire class
                    
                    .. attribute:: type
                    
                    	Delay or Never
                    	**type**\:  :py:class:`BackupDisable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BackupDisable>`
                    
                    .. attribute:: disable_backup
                    
                    	Disable backup delay
                    	**type**\: int
                    
                    	**range:** 0..180
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay, self).__init__()

                        self.yang_name = "backup-disable-delay"
                        self.yang_parent_name = "pseudowire-class"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('type', YLeaf(YType.enumeration, 'type')),
                            ('disable_backup', YLeaf(YType.uint32, 'disable-backup')),
                        ])
                        self.type = None
                        self.disable_backup = None
                        self._segment_path = lambda: "backup-disable-delay"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay, ['type', 'disable_backup'], name, value)


                class MplsEncapsulation(Entity):
                    """
                    MPLS encapsulation
                    
                    .. attribute:: sequencing
                    
                    	Sequencing
                    	**type**\:  :py:class:`Sequencing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing>`
                    
                    .. attribute:: mpls_redundancy
                    
                    	Redundancy options for MPLS encapsulation
                    	**type**\:  :py:class:`MplsRedundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy>`
                    
                    .. attribute:: preferred_path
                    
                    	Preferred path
                    	**type**\:  :py:class:`PreferredPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath>`
                    
                    .. attribute:: load_balance_group
                    
                    	Load Balancing
                    	**type**\:  :py:class:`LoadBalanceGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup>`
                    
                    .. attribute:: pw_switching_tlv
                    
                    	Pseudowire Switching Point Tlv
                    	**type**\:  :py:class:`PwSwitchingPointTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.PwSwitchingPointTlv>`
                    
                    .. attribute:: static_tag_rewrite
                    
                    	Static Tag rewrite
                    	**type**\: int
                    
                    	**range:** 1..4094
                    
                    .. attribute:: signaling_protocol
                    
                    	MPLS signaling protocol
                    	**type**\:  :py:class:`MplsSignalingProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MplsSignalingProtocol>`
                    
                    	**default value**\: ldp
                    
                    .. attribute:: vccv_type
                    
                    	VCCV verification type
                    	**type**\:  :py:class:`VccvVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.VccvVerification>`
                    
                    	**default value**\: lsp-ping
                    
                    .. attribute:: source_address
                    
                    	Source IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: transport_mode
                    
                    	Transport mode
                    	**type**\:  :py:class:`TransportMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.TransportMode>`
                    
                    .. attribute:: enable
                    
                    	Enable MPLS encapsulation
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: control_word
                    
                    	Enable control word
                    	**type**\:  :py:class:`ControlWord <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.ControlWord>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation, self).__init__()

                        self.yang_name = "mpls-encapsulation"
                        self.yang_parent_name = "pseudowire-class"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("sequencing", ("sequencing", L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing)), ("mpls-redundancy", ("mpls_redundancy", L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy)), ("preferred-path", ("preferred_path", L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath)), ("load-balance-group", ("load_balance_group", L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pw_switching_tlv', YLeaf(YType.enumeration, 'pw-switching-tlv')),
                            ('static_tag_rewrite', YLeaf(YType.uint32, 'static-tag-rewrite')),
                            ('signaling_protocol', YLeaf(YType.enumeration, 'signaling-protocol')),
                            ('vccv_type', YLeaf(YType.enumeration, 'vccv-type')),
                            ('source_address', YLeaf(YType.str, 'source-address')),
                            ('transport_mode', YLeaf(YType.enumeration, 'transport-mode')),
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('control_word', YLeaf(YType.enumeration, 'control-word')),
                        ])
                        self.pw_switching_tlv = None
                        self.static_tag_rewrite = None
                        self.signaling_protocol = None
                        self.vccv_type = None
                        self.source_address = None
                        self.transport_mode = None
                        self.enable = None
                        self.control_word = None

                        self.sequencing = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing()
                        self.sequencing.parent = self
                        self._children_name_map["sequencing"] = "sequencing"
                        self._children_yang_names.add("sequencing")

                        self.mpls_redundancy = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy()
                        self.mpls_redundancy.parent = self
                        self._children_name_map["mpls_redundancy"] = "mpls-redundancy"
                        self._children_yang_names.add("mpls-redundancy")

                        self.preferred_path = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath()
                        self.preferred_path.parent = self
                        self._children_name_map["preferred_path"] = "preferred-path"
                        self._children_yang_names.add("preferred-path")

                        self.load_balance_group = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup()
                        self.load_balance_group.parent = self
                        self._children_name_map["load_balance_group"] = "load-balance-group"
                        self._children_yang_names.add("load-balance-group")
                        self._segment_path = lambda: "mpls-encapsulation"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation, ['pw_switching_tlv', 'static_tag_rewrite', 'signaling_protocol', 'vccv_type', 'source_address', 'transport_mode', 'enable', 'control_word'], name, value)


                    class Sequencing(Entity):
                        """
                        Sequencing
                        
                        .. attribute:: sequencing
                        
                        	Sequencing
                        	**type**\:  :py:class:`MplsSequencing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MplsSequencing>`
                        
                        	**default value**\: off
                        
                        .. attribute:: resync_threshold
                        
                        	Out of sequence threshold
                        	**type**\: int
                        
                        	**range:** 5..65535
                        
                        	**default value**\: 5
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing, self).__init__()

                            self.yang_name = "sequencing"
                            self.yang_parent_name = "mpls-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sequencing', YLeaf(YType.enumeration, 'sequencing')),
                                ('resync_threshold', YLeaf(YType.uint32, 'resync-threshold')),
                            ])
                            self.sequencing = None
                            self.resync_threshold = None
                            self._segment_path = lambda: "sequencing"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing, ['sequencing', 'resync_threshold'], name, value)


                    class MplsRedundancy(Entity):
                        """
                        Redundancy options for MPLS encapsulation
                        
                        .. attribute:: redundancy_one_way
                        
                        	Force one\-way PW redundancy behavior in Redundancy Group
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: redundancy_initial_delay
                        
                        	Initial delay before activating the redundant PW, in seconds
                        	**type**\: int
                        
                        	**range:** 0..120
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy, self).__init__()

                            self.yang_name = "mpls-redundancy"
                            self.yang_parent_name = "mpls-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('redundancy_one_way', YLeaf(YType.empty, 'redundancy-one-way')),
                                ('redundancy_initial_delay', YLeaf(YType.uint32, 'redundancy-initial-delay')),
                            ])
                            self.redundancy_one_way = None
                            self.redundancy_initial_delay = None
                            self._segment_path = lambda: "mpls-redundancy"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy, ['redundancy_one_way', 'redundancy_initial_delay'], name, value)


                    class PreferredPath(Entity):
                        """
                        Preferred path
                        
                        .. attribute:: type
                        
                        	Preferred Path Type
                        	**type**\:  :py:class:`PreferredPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.PreferredPath>`
                        
                        .. attribute:: interface_tunnel_number
                        
                        	Interface Tunnel number for preferred path
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: fallback_disable
                        
                        	Fallback disable
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: srte_policy
                        
                        	Name of the SR TE Policy
                        	**type**\: str
                        
                        	**length:** 1..60
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath, self).__init__()

                            self.yang_name = "preferred-path"
                            self.yang_parent_name = "mpls-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', YLeaf(YType.enumeration, 'type')),
                                ('interface_tunnel_number', YLeaf(YType.uint32, 'interface-tunnel-number')),
                                ('fallback_disable', YLeaf(YType.empty, 'fallback-disable')),
                                ('srte_policy', YLeaf(YType.str, 'srte-policy')),
                            ])
                            self.type = None
                            self.interface_tunnel_number = None
                            self.fallback_disable = None
                            self.srte_policy = None
                            self._segment_path = lambda: "preferred-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath, ['type', 'interface_tunnel_number', 'fallback_disable', 'srte_policy'], name, value)


                    class LoadBalanceGroup(Entity):
                        """
                        Load Balancing
                        
                        .. attribute:: flow_label_load_balance
                        
                        	Enable Flow Label based load balancing
                        	**type**\:  :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance>`
                        
                        .. attribute:: flow_label_load_balance_code
                        
                        	Enable Legacy Flow Label TLV code
                        	**type**\:  :py:class:`FlowLabelTlvCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelTlvCode>`
                        
                        .. attribute:: pw_label_load_balance
                        
                        	Enable PW Label based Load Balancing
                        	**type**\:  :py:class:`LoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.LoadBalance>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup, self).__init__()

                            self.yang_name = "load-balance-group"
                            self.yang_parent_name = "mpls-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("flow-label-load-balance", ("flow_label_load_balance", L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('flow_label_load_balance_code', YLeaf(YType.enumeration, 'flow-label-load-balance-code')),
                                ('pw_label_load_balance', YLeaf(YType.enumeration, 'pw-label-load-balance')),
                            ])
                            self.flow_label_load_balance_code = None
                            self.pw_label_load_balance = None

                            self.flow_label_load_balance = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance()
                            self.flow_label_load_balance.parent = self
                            self._children_name_map["flow_label_load_balance"] = "flow-label-load-balance"
                            self._children_yang_names.add("flow-label-load-balance")
                            self._segment_path = lambda: "load-balance-group"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup, ['flow_label_load_balance_code', 'pw_label_load_balance'], name, value)


                        class FlowLabelLoadBalance(Entity):
                            """
                            Enable Flow Label based load balancing
                            
                            .. attribute:: flow_label
                            
                            	Flow Label load balance type
                            	**type**\:  :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalance>`
                            
                            .. attribute:: static
                            
                            	Static Flow Label
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance, self).__init__()

                                self.yang_name = "flow-label-load-balance"
                                self.yang_parent_name = "load-balance-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('flow_label', YLeaf(YType.enumeration, 'flow-label')),
                                    ('static', YLeaf(YType.empty, 'static')),
                                ])
                                self.flow_label = None
                                self.static = None
                                self._segment_path = lambda: "flow-label-load-balance"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance, ['flow_label', 'static'], name, value)


        class FlexibleXconnectServiceTable(Entity):
            """
            List of Flexible XConnect Services
            
            .. attribute:: vlan_unaware_flexible_xconnect_services
            
            	List of Vlan\-Unaware Flexible XConnect Services
            	**type**\:  :py:class:`VlanUnawareFlexibleXconnectServices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices>`
            
            .. attribute:: vlan_aware_flexible_xconnect_services
            
            	List of Vlan\-Aware Flexible XConnect Services
            	**type**\:  :py:class:`VlanAwareFlexibleXconnectServices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Database.FlexibleXconnectServiceTable, self).__init__()

                self.yang_name = "flexible-xconnect-service-table"
                self.yang_parent_name = "database"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("vlan-unaware-flexible-xconnect-services", ("vlan_unaware_flexible_xconnect_services", L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices)), ("vlan-aware-flexible-xconnect-services", ("vlan_aware_flexible_xconnect_services", L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.vlan_unaware_flexible_xconnect_services = L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices()
                self.vlan_unaware_flexible_xconnect_services.parent = self
                self._children_name_map["vlan_unaware_flexible_xconnect_services"] = "vlan-unaware-flexible-xconnect-services"
                self._children_yang_names.add("vlan-unaware-flexible-xconnect-services")

                self.vlan_aware_flexible_xconnect_services = L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices()
                self.vlan_aware_flexible_xconnect_services.parent = self
                self._children_name_map["vlan_aware_flexible_xconnect_services"] = "vlan-aware-flexible-xconnect-services"
                self._children_yang_names.add("vlan-aware-flexible-xconnect-services")
                self._segment_path = lambda: "flexible-xconnect-service-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/%s" % self._segment_path()


            class VlanUnawareFlexibleXconnectServices(Entity):
                """
                List of Vlan\-Unaware Flexible XConnect
                Services
                
                .. attribute:: vlan_unaware_flexible_xconnect_service
                
                	Flexible XConnect Service
                	**type**\: list of  		 :py:class:`VlanUnawareFlexibleXconnectService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices, self).__init__()

                    self.yang_name = "vlan-unaware-flexible-xconnect-services"
                    self.yang_parent_name = "flexible-xconnect-service-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("vlan-unaware-flexible-xconnect-service", ("vlan_unaware_flexible_xconnect_service", L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService))])
                    self._leafs = OrderedDict()

                    self.vlan_unaware_flexible_xconnect_service = YList(self)
                    self._segment_path = lambda: "vlan-unaware-flexible-xconnect-services"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/flexible-xconnect-service-table/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices, [], name, value)


                class VlanUnawareFlexibleXconnectService(Entity):
                    """
                    Flexible XConnect Service
                    
                    .. attribute:: name  (key)
                    
                    	Name of the Flexible XConnect Service
                    	**type**\: str
                    
                    	**length:** 1..23
                    
                    .. attribute:: vlan_unaware_fxc_attachment_circuits
                    
                    	List of attachment circuits
                    	**type**\:  :py:class:`VlanUnawareFxcAttachmentCircuits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits>`
                    
                    .. attribute:: vlan_unaware_fxc_pseudowire_evpns
                    
                    	List of EVPN Services
                    	**type**\:  :py:class:`VlanUnawareFxcPseudowireEvpns <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService, self).__init__()

                        self.yang_name = "vlan-unaware-flexible-xconnect-service"
                        self.yang_parent_name = "vlan-unaware-flexible-xconnect-services"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['name']
                        self._child_container_classes = OrderedDict([("vlan-unaware-fxc-attachment-circuits", ("vlan_unaware_fxc_attachment_circuits", L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits)), ("vlan-unaware-fxc-pseudowire-evpns", ("vlan_unaware_fxc_pseudowire_evpns", L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', YLeaf(YType.str, 'name')),
                        ])
                        self.name = None

                        self.vlan_unaware_fxc_attachment_circuits = L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits()
                        self.vlan_unaware_fxc_attachment_circuits.parent = self
                        self._children_name_map["vlan_unaware_fxc_attachment_circuits"] = "vlan-unaware-fxc-attachment-circuits"
                        self._children_yang_names.add("vlan-unaware-fxc-attachment-circuits")

                        self.vlan_unaware_fxc_pseudowire_evpns = L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns()
                        self.vlan_unaware_fxc_pseudowire_evpns.parent = self
                        self._children_name_map["vlan_unaware_fxc_pseudowire_evpns"] = "vlan-unaware-fxc-pseudowire-evpns"
                        self._children_yang_names.add("vlan-unaware-fxc-pseudowire-evpns")
                        self._segment_path = lambda: "vlan-unaware-flexible-xconnect-service" + "[name='" + str(self.name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/flexible-xconnect-service-table/vlan-unaware-flexible-xconnect-services/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService, ['name'], name, value)


                    class VlanUnawareFxcAttachmentCircuits(Entity):
                        """
                        List of attachment circuits
                        
                        .. attribute:: vlan_unaware_fxc_attachment_circuit
                        
                        	Attachment circuit interface
                        	**type**\: list of  		 :py:class:`VlanUnawareFxcAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits, self).__init__()

                            self.yang_name = "vlan-unaware-fxc-attachment-circuits"
                            self.yang_parent_name = "vlan-unaware-flexible-xconnect-service"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("vlan-unaware-fxc-attachment-circuit", ("vlan_unaware_fxc_attachment_circuit", L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit))])
                            self._leafs = OrderedDict()

                            self.vlan_unaware_fxc_attachment_circuit = YList(self)
                            self._segment_path = lambda: "vlan-unaware-fxc-attachment-circuits"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits, [], name, value)


                        class VlanUnawareFxcAttachmentCircuit(Entity):
                            """
                            Attachment circuit interface
                            
                            .. attribute:: name  (key)
                            
                            	Name of the attachment circuit interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit, self).__init__()

                                self.yang_name = "vlan-unaware-fxc-attachment-circuit"
                                self.yang_parent_name = "vlan-unaware-fxc-attachment-circuits"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['name']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', YLeaf(YType.str, 'name')),
                                ])
                                self.name = None
                                self._segment_path = lambda: "vlan-unaware-fxc-attachment-circuit" + "[name='" + str(self.name) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit, ['name'], name, value)


                    class VlanUnawareFxcPseudowireEvpns(Entity):
                        """
                        List of EVPN Services
                        
                        .. attribute:: vlan_unaware_fxc_pseudowire_evpn
                        
                        	EVPN FXC Service Configuration
                        	**type**\: list of  		 :py:class:`VlanUnawareFxcPseudowireEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns, self).__init__()

                            self.yang_name = "vlan-unaware-fxc-pseudowire-evpns"
                            self.yang_parent_name = "vlan-unaware-flexible-xconnect-service"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("vlan-unaware-fxc-pseudowire-evpn", ("vlan_unaware_fxc_pseudowire_evpn", L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn))])
                            self._leafs = OrderedDict()

                            self.vlan_unaware_fxc_pseudowire_evpn = YList(self)
                            self._segment_path = lambda: "vlan-unaware-fxc-pseudowire-evpns"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns, [], name, value)


                        class VlanUnawareFxcPseudowireEvpn(Entity):
                            """
                            EVPN FXC Service Configuration
                            
                            .. attribute:: eviid  (key)
                            
                            	Ethernet VPN ID
                            	**type**\: int
                            
                            	**range:** 1..65534
                            
                            .. attribute:: acid  (key)
                            
                            	AC ID
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn, self).__init__()

                                self.yang_name = "vlan-unaware-fxc-pseudowire-evpn"
                                self.yang_parent_name = "vlan-unaware-fxc-pseudowire-evpns"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['eviid','acid']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('eviid', YLeaf(YType.uint32, 'eviid')),
                                    ('acid', YLeaf(YType.uint32, 'acid')),
                                ])
                                self.eviid = None
                                self.acid = None
                                self._segment_path = lambda: "vlan-unaware-fxc-pseudowire-evpn" + "[eviid='" + str(self.eviid) + "']" + "[acid='" + str(self.acid) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn, ['eviid', 'acid'], name, value)


            class VlanAwareFlexibleXconnectServices(Entity):
                """
                List of Vlan\-Aware Flexible XConnect Services
                
                .. attribute:: vlan_aware_flexible_xconnect_service
                
                	Flexible XConnect Service
                	**type**\: list of  		 :py:class:`VlanAwareFlexibleXconnectService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices, self).__init__()

                    self.yang_name = "vlan-aware-flexible-xconnect-services"
                    self.yang_parent_name = "flexible-xconnect-service-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("vlan-aware-flexible-xconnect-service", ("vlan_aware_flexible_xconnect_service", L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService))])
                    self._leafs = OrderedDict()

                    self.vlan_aware_flexible_xconnect_service = YList(self)
                    self._segment_path = lambda: "vlan-aware-flexible-xconnect-services"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/flexible-xconnect-service-table/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices, [], name, value)


                class VlanAwareFlexibleXconnectService(Entity):
                    """
                    Flexible XConnect Service
                    
                    .. attribute:: eviid  (key)
                    
                    	Ethernet VPN ID
                    	**type**\: int
                    
                    	**range:** 1..65534
                    
                    .. attribute:: vlan_aware_fxc_attachment_circuits
                    
                    	List of attachment circuits
                    	**type**\:  :py:class:`VlanAwareFxcAttachmentCircuits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService, self).__init__()

                        self.yang_name = "vlan-aware-flexible-xconnect-service"
                        self.yang_parent_name = "vlan-aware-flexible-xconnect-services"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['eviid']
                        self._child_container_classes = OrderedDict([("vlan-aware-fxc-attachment-circuits", ("vlan_aware_fxc_attachment_circuits", L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('eviid', YLeaf(YType.uint32, 'eviid')),
                        ])
                        self.eviid = None

                        self.vlan_aware_fxc_attachment_circuits = L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits()
                        self.vlan_aware_fxc_attachment_circuits.parent = self
                        self._children_name_map["vlan_aware_fxc_attachment_circuits"] = "vlan-aware-fxc-attachment-circuits"
                        self._children_yang_names.add("vlan-aware-fxc-attachment-circuits")
                        self._segment_path = lambda: "vlan-aware-flexible-xconnect-service" + "[eviid='" + str(self.eviid) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/flexible-xconnect-service-table/vlan-aware-flexible-xconnect-services/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService, ['eviid'], name, value)


                    class VlanAwareFxcAttachmentCircuits(Entity):
                        """
                        List of attachment circuits
                        
                        .. attribute:: vlan_aware_fxc_attachment_circuit
                        
                        	Attachment circuit interface
                        	**type**\: list of  		 :py:class:`VlanAwareFxcAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits, self).__init__()

                            self.yang_name = "vlan-aware-fxc-attachment-circuits"
                            self.yang_parent_name = "vlan-aware-flexible-xconnect-service"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("vlan-aware-fxc-attachment-circuit", ("vlan_aware_fxc_attachment_circuit", L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit))])
                            self._leafs = OrderedDict()

                            self.vlan_aware_fxc_attachment_circuit = YList(self)
                            self._segment_path = lambda: "vlan-aware-fxc-attachment-circuits"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits, [], name, value)


                        class VlanAwareFxcAttachmentCircuit(Entity):
                            """
                            Attachment circuit interface
                            
                            .. attribute:: name  (key)
                            
                            	Name of the attachment circuit interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit, self).__init__()

                                self.yang_name = "vlan-aware-fxc-attachment-circuit"
                                self.yang_parent_name = "vlan-aware-fxc-attachment-circuits"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['name']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', YLeaf(YType.str, 'name')),
                                ])
                                self.name = None
                                self._segment_path = lambda: "vlan-aware-fxc-attachment-circuit" + "[name='" + str(self.name) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit, ['name'], name, value)


        class Redundancy(Entity):
            """
            Redundancy groups
            
            .. attribute:: iccp_redundancy_groups
            
            	List of Inter\-Chassis Communication Protocol redundancy groups
            	**type**\:  :py:class:`IccpRedundancyGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.Redundancy.IccpRedundancyGroups>`
            
            .. attribute:: enable
            
            	Enable redundancy groups
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Database.Redundancy, self).__init__()

                self.yang_name = "redundancy"
                self.yang_parent_name = "database"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("iccp-redundancy-groups", ("iccp_redundancy_groups", L2Vpn.Database.Redundancy.IccpRedundancyGroups))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', YLeaf(YType.empty, 'enable')),
                ])
                self.enable = None

                self.iccp_redundancy_groups = L2Vpn.Database.Redundancy.IccpRedundancyGroups()
                self.iccp_redundancy_groups.parent = self
                self._children_name_map["iccp_redundancy_groups"] = "iccp-redundancy-groups"
                self._children_yang_names.add("iccp-redundancy-groups")
                self._segment_path = lambda: "redundancy"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.Database.Redundancy, ['enable'], name, value)


            class IccpRedundancyGroups(Entity):
                """
                List of Inter\-Chassis Communication Protocol
                redundancy groups
                
                .. attribute:: iccp_redundancy_group
                
                	ICCP Redundancy group
                	**type**\: list of  		 :py:class:`IccpRedundancyGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.Redundancy.IccpRedundancyGroups, self).__init__()

                    self.yang_name = "iccp-redundancy-groups"
                    self.yang_parent_name = "redundancy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("iccp-redundancy-group", ("iccp_redundancy_group", L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup))])
                    self._leafs = OrderedDict()

                    self.iccp_redundancy_group = YList(self)
                    self._segment_path = lambda: "iccp-redundancy-groups"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/redundancy/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.Redundancy.IccpRedundancyGroups, [], name, value)


                class IccpRedundancyGroup(Entity):
                    """
                    ICCP Redundancy group
                    
                    .. attribute:: group_id  (key)
                    
                    	Group ID
                    	**type**\: int
                    
                    	**range:** 1..4294967295
                    
                    .. attribute:: iccp_interfaces
                    
                    	List of interfaces
                    	**type**\:  :py:class:`IccpInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces>`
                    
                    .. attribute:: multi_homing_node_id
                    
                    	ICCP\-based service multi\-homing node ID
                    	**type**\: int
                    
                    	**range:** 0..254
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup, self).__init__()

                        self.yang_name = "iccp-redundancy-group"
                        self.yang_parent_name = "iccp-redundancy-groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['group_id']
                        self._child_container_classes = OrderedDict([("iccp-interfaces", ("iccp_interfaces", L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('group_id', YLeaf(YType.uint32, 'group-id')),
                            ('multi_homing_node_id', YLeaf(YType.uint32, 'multi-homing-node-id')),
                        ])
                        self.group_id = None
                        self.multi_homing_node_id = None

                        self.iccp_interfaces = L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces()
                        self.iccp_interfaces.parent = self
                        self._children_name_map["iccp_interfaces"] = "iccp-interfaces"
                        self._children_yang_names.add("iccp-interfaces")
                        self._segment_path = lambda: "iccp-redundancy-group" + "[group-id='" + str(self.group_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/redundancy/iccp-redundancy-groups/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup, ['group_id', 'multi_homing_node_id'], name, value)


                    class IccpInterfaces(Entity):
                        """
                        List of interfaces
                        
                        .. attribute:: iccp_interface
                        
                        	Interface name
                        	**type**\: list of  		 :py:class:`IccpInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces, self).__init__()

                            self.yang_name = "iccp-interfaces"
                            self.yang_parent_name = "iccp-redundancy-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("iccp-interface", ("iccp_interface", L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface))])
                            self._leafs = OrderedDict()

                            self.iccp_interface = YList(self)
                            self._segment_path = lambda: "iccp-interfaces"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces, [], name, value)


                        class IccpInterface(Entity):
                            """
                            Interface name
                            
                            .. attribute:: interface_name  (key)
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: secondary_vlan_range
                            
                            	Secondary VLAN range, in the form of 1\-3,5 ,8\-11
                            	**type**\: str
                            
                            .. attribute:: recovery_delay
                            
                            	Failure clear recovery delay
                            	**type**\: int
                            
                            	**range:** 30..3600
                            
                            	**default value**\: 180
                            
                            .. attribute:: primary_vlan_range
                            
                            	Primary VLAN range, in the form of 1\-3,5 ,8\-11
                            	**type**\: str
                            
                            .. attribute:: mac_flush_tcn
                            
                            	Enable STP\-TCN MAC flushing
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface, self).__init__()

                                self.yang_name = "iccp-interface"
                                self.yang_parent_name = "iccp-interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('secondary_vlan_range', YLeaf(YType.str, 'secondary-vlan-range')),
                                    ('recovery_delay', YLeaf(YType.uint32, 'recovery-delay')),
                                    ('primary_vlan_range', YLeaf(YType.str, 'primary-vlan-range')),
                                    ('mac_flush_tcn', YLeaf(YType.empty, 'mac-flush-tcn')),
                                ])
                                self.interface_name = None
                                self.secondary_vlan_range = None
                                self.recovery_delay = None
                                self.primary_vlan_range = None
                                self.mac_flush_tcn = None
                                self._segment_path = lambda: "iccp-interface" + "[interface-name='" + str(self.interface_name) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface, ['interface_name', 'secondary_vlan_range', 'recovery_delay', 'primary_vlan_range', 'mac_flush_tcn'], name, value)


    class Pbb(Entity):
        """
        L2VPN PBB Global
        
        .. attribute:: backbone_source_mac
        
        	Backbone Source MAC
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(L2Vpn.Pbb, self).__init__()

            self.yang_name = "pbb"
            self.yang_parent_name = "l2vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('backbone_source_mac', YLeaf(YType.str, 'backbone-source-mac')),
            ])
            self.backbone_source_mac = None
            self._segment_path = lambda: "pbb"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Vpn.Pbb, ['backbone_source_mac'], name, value)


    class AutoDiscovery(Entity):
        """
        Global auto\-discovery attributes
        
        .. attribute:: bgp_signaling
        
        	Global bgp signaling attributes
        	**type**\:  :py:class:`BgpSignaling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.AutoDiscovery.BgpSignaling>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(L2Vpn.AutoDiscovery, self).__init__()

            self.yang_name = "auto-discovery"
            self.yang_parent_name = "l2vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("bgp-signaling", ("bgp_signaling", L2Vpn.AutoDiscovery.BgpSignaling))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.bgp_signaling = L2Vpn.AutoDiscovery.BgpSignaling()
            self.bgp_signaling.parent = self
            self._children_name_map["bgp_signaling"] = "bgp-signaling"
            self._children_yang_names.add("bgp-signaling")
            self._segment_path = lambda: "auto-discovery"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/%s" % self._segment_path()


        class BgpSignaling(Entity):
            """
            Global bgp signaling attributes
            
            .. attribute:: mtu_mismatch_ignore
            
            	Ignore MTU mismatch for auto\-discovered pseudowires
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.AutoDiscovery.BgpSignaling, self).__init__()

                self.yang_name = "bgp-signaling"
                self.yang_parent_name = "auto-discovery"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mtu_mismatch_ignore', YLeaf(YType.empty, 'mtu-mismatch-ignore')),
                ])
                self.mtu_mismatch_ignore = None
                self._segment_path = lambda: "bgp-signaling"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/auto-discovery/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.AutoDiscovery.BgpSignaling, ['mtu_mismatch_ignore'], name, value)


    class Utility(Entity):
        """
        L2VPN utilities
        
        .. attribute:: logging
        
        	L2VPN logging utility
        	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Utility.Logging>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(L2Vpn.Utility, self).__init__()

            self.yang_name = "utility"
            self.yang_parent_name = "l2vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("logging", ("logging", L2Vpn.Utility.Logging))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.logging = L2Vpn.Utility.Logging()
            self.logging.parent = self
            self._children_name_map["logging"] = "logging"
            self._children_yang_names.add("logging")
            self._segment_path = lambda: "utility"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/%s" % self._segment_path()


        class Logging(Entity):
            """
            L2VPN logging utility
            
            .. attribute:: bridge_domain_state_change
            
            	Enable Bridge Domain state change logging
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: pseudowire_state_change
            
            	Enable pseudowire state change logging
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: vfi
            
            	Enable VFI state change logging
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: nsr_state_change
            
            	Enable Non Stop Routing state change logging
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: pwhe_replication_state_change
            
            	Enable PW\-HE Replication state change logging
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Utility.Logging, self).__init__()

                self.yang_name = "logging"
                self.yang_parent_name = "utility"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bridge_domain_state_change', YLeaf(YType.empty, 'bridge-domain-state-change')),
                    ('pseudowire_state_change', YLeaf(YType.empty, 'pseudowire-state-change')),
                    ('vfi', YLeaf(YType.empty, 'vfi')),
                    ('nsr_state_change', YLeaf(YType.empty, 'nsr-state-change')),
                    ('pwhe_replication_state_change', YLeaf(YType.empty, 'pwhe-replication-state-change')),
                ])
                self.bridge_domain_state_change = None
                self.pseudowire_state_change = None
                self.vfi = None
                self.nsr_state_change = None
                self.pwhe_replication_state_change = None
                self._segment_path = lambda: "logging"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/utility/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.Utility.Logging, ['bridge_domain_state_change', 'pseudowire_state_change', 'vfi', 'nsr_state_change', 'pwhe_replication_state_change'], name, value)


    class Snmp(Entity):
        """
        SNMP related configuration
        
        .. attribute:: mib
        
        	MIB related configuration
        	**type**\:  :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Snmp.Mib>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(L2Vpn.Snmp, self).__init__()

            self.yang_name = "snmp"
            self.yang_parent_name = "l2vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("mib", ("mib", L2Vpn.Snmp.Mib))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.mib = L2Vpn.Snmp.Mib()
            self.mib.parent = self
            self._children_name_map["mib"] = "mib"
            self._children_yang_names.add("mib")
            self._segment_path = lambda: "snmp"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/%s" % self._segment_path()


        class Mib(Entity):
            """
            MIB related configuration
            
            .. attribute:: mib_interface
            
            	Interface related configuration for MIB
            	**type**\:  :py:class:`MibInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Snmp.Mib.MibInterface>`
            
            .. attribute:: mib_pseudowire
            
            	Pseudowire related configuration for MIB
            	**type**\:  :py:class:`MibPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Snmp.Mib.MibPseudowire>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Snmp.Mib, self).__init__()

                self.yang_name = "mib"
                self.yang_parent_name = "snmp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("mib-interface", ("mib_interface", L2Vpn.Snmp.Mib.MibInterface)), ("mib-pseudowire", ("mib_pseudowire", L2Vpn.Snmp.Mib.MibPseudowire))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.mib_interface = L2Vpn.Snmp.Mib.MibInterface()
                self.mib_interface.parent = self
                self._children_name_map["mib_interface"] = "mib-interface"
                self._children_yang_names.add("mib-interface")

                self.mib_pseudowire = L2Vpn.Snmp.Mib.MibPseudowire()
                self.mib_pseudowire.parent = self
                self._children_name_map["mib_pseudowire"] = "mib-pseudowire"
                self._children_yang_names.add("mib-pseudowire")
                self._segment_path = lambda: "mib"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/snmp/%s" % self._segment_path()


            class MibInterface(Entity):
                """
                Interface related configuration for MIB
                
                .. attribute:: format
                
                	MIB interface name output format
                	**type**\:  :py:class:`Format <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Snmp.Mib.MibInterface.Format>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Snmp.Mib.MibInterface, self).__init__()

                    self.yang_name = "mib-interface"
                    self.yang_parent_name = "mib"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("format", ("format", L2Vpn.Snmp.Mib.MibInterface.Format))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.format = L2Vpn.Snmp.Mib.MibInterface.Format()
                    self.format.parent = self
                    self._children_name_map["format"] = "format"
                    self._children_yang_names.add("format")
                    self._segment_path = lambda: "mib-interface"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/snmp/mib/%s" % self._segment_path()


                class Format(Entity):
                    """
                    MIB interface name output format
                    
                    .. attribute:: external_interface_format
                    
                    	Set MIB interface name output in slash format (/)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Snmp.Mib.MibInterface.Format, self).__init__()

                        self.yang_name = "format"
                        self.yang_parent_name = "mib-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('external_interface_format', YLeaf(YType.empty, 'external-interface-format')),
                        ])
                        self.external_interface_format = None
                        self._segment_path = lambda: "format"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/snmp/mib/mib-interface/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Snmp.Mib.MibInterface.Format, ['external_interface_format'], name, value)


            class MibPseudowire(Entity):
                """
                Pseudowire related configuration for MIB
                
                .. attribute:: statistics
                
                	Enable pseudowire statistics in MIB output
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Snmp.Mib.MibPseudowire, self).__init__()

                    self.yang_name = "mib-pseudowire"
                    self.yang_parent_name = "mib"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('statistics', YLeaf(YType.empty, 'statistics')),
                    ])
                    self.statistics = None
                    self._segment_path = lambda: "mib-pseudowire"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/snmp/mib/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Snmp.Mib.MibPseudowire, ['statistics'], name, value)

    def clone_ptr(self):
        self._top_entity = L2Vpn()
        return self._top_entity

class GenericInterfaceLists(Entity):
    """
    generic interface lists
    
    .. attribute:: generic_interface_list
    
    	Generic interface list
    	**type**\: list of  		 :py:class:`GenericInterfaceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.GenericInterfaceLists.GenericInterfaceList>`
    
    

    """

    _prefix = 'l2vpn-cfg'
    _revision = '2017-06-26'

    def __init__(self):
        super(GenericInterfaceLists, self).__init__()
        self._top_entity = None

        self.yang_name = "generic-interface-lists"
        self.yang_parent_name = "Cisco-IOS-XR-l2vpn-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("generic-interface-list", ("generic_interface_list", GenericInterfaceLists.GenericInterfaceList))])
        self._leafs = OrderedDict()

        self.generic_interface_list = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:generic-interface-lists"

    def __setattr__(self, name, value):
        self._perform_setattr(GenericInterfaceLists, [], name, value)


    class GenericInterfaceList(Entity):
        """
        Generic interface list
        
        .. attribute:: generic_interface_list_name  (key)
        
        	Name of the interface list
        	**type**\: str
        
        	**length:** 1..32
        
        .. attribute:: interfaces
        
        	Interface table
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.GenericInterfaceLists.GenericInterfaceList.Interfaces>`
        
        .. attribute:: enable
        
        	Enable interface list
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(GenericInterfaceLists.GenericInterfaceList, self).__init__()

            self.yang_name = "generic-interface-list"
            self.yang_parent_name = "generic-interface-lists"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['generic_interface_list_name']
            self._child_container_classes = OrderedDict([("interfaces", ("interfaces", GenericInterfaceLists.GenericInterfaceList.Interfaces))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('generic_interface_list_name', YLeaf(YType.str, 'generic-interface-list-name')),
                ('enable', YLeaf(YType.empty, 'enable')),
            ])
            self.generic_interface_list_name = None
            self.enable = None

            self.interfaces = GenericInterfaceLists.GenericInterfaceList.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")
            self._segment_path = lambda: "generic-interface-list" + "[generic-interface-list-name='" + str(self.generic_interface_list_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:generic-interface-lists/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(GenericInterfaceLists.GenericInterfaceList, ['generic_interface_list_name', 'enable'], name, value)


        class Interfaces(Entity):
            """
            Interface table
            
            .. attribute:: interface
            
            	Interface
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.GenericInterfaceLists.GenericInterfaceList.Interfaces.Interface>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(GenericInterfaceLists.GenericInterfaceList.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "generic-interface-list"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("interface", ("interface", GenericInterfaceLists.GenericInterfaceList.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"

            def __setattr__(self, name, value):
                self._perform_setattr(GenericInterfaceLists.GenericInterfaceList.Interfaces, [], name, value)


            class Interface(Entity):
                """
                Interface
                
                .. attribute:: interface_name  (key)
                
                	Name of the interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: enable
                
                	Enable interface
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(GenericInterfaceLists.GenericInterfaceList.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['interface_name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', YLeaf(YType.str, 'interface-name')),
                        ('enable', YLeaf(YType.empty, 'enable')),
                    ])
                    self.interface_name = None
                    self.enable = None
                    self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(GenericInterfaceLists.GenericInterfaceList.Interfaces.Interface, ['interface_name', 'enable'], name, value)

    def clone_ptr(self):
        self._top_entity = GenericInterfaceLists()
        return self._top_entity

class Evpn(Entity):
    """
    evpn
    
    .. attribute:: evpn_tables
    
    	EVPN submodes
    	**type**\:  :py:class:`EvpnTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables>`
    
    .. attribute:: enable
    
    	Enable EVPN feature
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'l2vpn-cfg'
    _revision = '2017-06-26'

    def __init__(self):
        super(Evpn, self).__init__()
        self._top_entity = None

        self.yang_name = "evpn"
        self.yang_parent_name = "Cisco-IOS-XR-l2vpn-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("evpn-tables", ("evpn_tables", Evpn.EvpnTables))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('enable', YLeaf(YType.empty, 'enable')),
        ])
        self.enable = None

        self.evpn_tables = Evpn.EvpnTables()
        self.evpn_tables.parent = self
        self._children_name_map["evpn_tables"] = "evpn-tables"
        self._children_yang_names.add("evpn-tables")
        self._segment_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn"

    def __setattr__(self, name, value):
        self._perform_setattr(Evpn, ['enable'], name, value)


    class EvpnTables(Entity):
        """
        EVPN submodes
        
        .. attribute:: evpn_timers
        
        	Enter EVPN timers configuration submode
        	**type**\:  :py:class:`EvpnTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnTimers>`
        
        .. attribute:: evpnmac
        
        	EVPN MAC Configuration
        	**type**\:  :py:class:`Evpnmac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnmac>`
        
        .. attribute:: evpnevis
        
        	Enter EVPN Instance configuration submode
        	**type**\:  :py:class:`Evpnevis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis>`
        
        .. attribute:: evpn_virtual_access_vfis
        
        	Virtual Access VFI interfaces
        	**type**\:  :py:class:`EvpnVirtualAccessVfis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis>`
        
        .. attribute:: evpn_load_balancing
        
        	Enter EVPN Loadbalancing configuration submode
        	**type**\:  :py:class:`EvpnLoadBalancing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnLoadBalancing>`
        
        .. attribute:: evpn_bgp_auto_discovery
        
        	Enable Autodiscovery BGP in EVPN
        	**type**\:  :py:class:`EvpnBgpAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnBgpAutoDiscovery>`
        
        .. attribute:: evpn_instances
        
        	Enter EVPN Instance configuration submode
        	**type**\:  :py:class:`EvpnInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances>`
        
        .. attribute:: evpn_logging
        
        	Enter EVPN Logging configuration submode
        	**type**\:  :py:class:`EvpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnLogging>`
        
        .. attribute:: evpn_interfaces
        
        	Attachment Circuit interfaces
        	**type**\:  :py:class:`EvpnInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces>`
        
        .. attribute:: evpn_virtual_access_pws
        
        	Virtual Access Pseudowire interfaces
        	**type**\:  :py:class:`EvpnVirtualAccessPws <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws>`
        
        .. attribute:: evpn_ethernet_segment
        
        	EVPN Global Ethernet Segment submode
        	**type**\:  :py:class:`EvpnEthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnEthernetSegment>`
        
        .. attribute:: evi_cost_out
        
        	Configure node to cost\-out
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: evpn_source_interface
        
        	Configure EVPN router\-id implicitly through Loopback Interface
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9./\-]+
        
        .. attribute:: evpn_cost_in_startup
        
        	Cost\-in node after given time (seconds) on startup timer
        	**type**\: int
        
        	**range:** 30..86400
        
        	**units**\: second
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(Evpn.EvpnTables, self).__init__()

            self.yang_name = "evpn-tables"
            self.yang_parent_name = "evpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("evpn-timers", ("evpn_timers", Evpn.EvpnTables.EvpnTimers)), ("evpnmac", ("evpnmac", Evpn.EvpnTables.Evpnmac)), ("evpnevis", ("evpnevis", Evpn.EvpnTables.Evpnevis)), ("evpn-virtual-access-vfis", ("evpn_virtual_access_vfis", Evpn.EvpnTables.EvpnVirtualAccessVfis)), ("evpn-load-balancing", ("evpn_load_balancing", Evpn.EvpnTables.EvpnLoadBalancing)), ("evpn-bgp-auto-discovery", ("evpn_bgp_auto_discovery", Evpn.EvpnTables.EvpnBgpAutoDiscovery)), ("evpn-instances", ("evpn_instances", Evpn.EvpnTables.EvpnInstances)), ("evpn-logging", ("evpn_logging", Evpn.EvpnTables.EvpnLogging)), ("evpn-interfaces", ("evpn_interfaces", Evpn.EvpnTables.EvpnInterfaces)), ("evpn-virtual-access-pws", ("evpn_virtual_access_pws", Evpn.EvpnTables.EvpnVirtualAccessPws)), ("evpn-ethernet-segment", ("evpn_ethernet_segment", Evpn.EvpnTables.EvpnEthernetSegment))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('evi_cost_out', YLeaf(YType.empty, 'evi-cost-out')),
                ('evpn_source_interface', YLeaf(YType.str, 'evpn-source-interface')),
                ('evpn_cost_in_startup', YLeaf(YType.uint32, 'evpn-cost-in-startup')),
            ])
            self.evi_cost_out = None
            self.evpn_source_interface = None
            self.evpn_cost_in_startup = None

            self.evpn_timers = Evpn.EvpnTables.EvpnTimers()
            self.evpn_timers.parent = self
            self._children_name_map["evpn_timers"] = "evpn-timers"
            self._children_yang_names.add("evpn-timers")

            self.evpnmac = Evpn.EvpnTables.Evpnmac()
            self.evpnmac.parent = self
            self._children_name_map["evpnmac"] = "evpnmac"
            self._children_yang_names.add("evpnmac")

            self.evpnevis = Evpn.EvpnTables.Evpnevis()
            self.evpnevis.parent = self
            self._children_name_map["evpnevis"] = "evpnevis"
            self._children_yang_names.add("evpnevis")

            self.evpn_virtual_access_vfis = Evpn.EvpnTables.EvpnVirtualAccessVfis()
            self.evpn_virtual_access_vfis.parent = self
            self._children_name_map["evpn_virtual_access_vfis"] = "evpn-virtual-access-vfis"
            self._children_yang_names.add("evpn-virtual-access-vfis")

            self.evpn_load_balancing = Evpn.EvpnTables.EvpnLoadBalancing()
            self.evpn_load_balancing.parent = self
            self._children_name_map["evpn_load_balancing"] = "evpn-load-balancing"
            self._children_yang_names.add("evpn-load-balancing")

            self.evpn_bgp_auto_discovery = Evpn.EvpnTables.EvpnBgpAutoDiscovery()
            self.evpn_bgp_auto_discovery.parent = self
            self._children_name_map["evpn_bgp_auto_discovery"] = "evpn-bgp-auto-discovery"
            self._children_yang_names.add("evpn-bgp-auto-discovery")

            self.evpn_instances = Evpn.EvpnTables.EvpnInstances()
            self.evpn_instances.parent = self
            self._children_name_map["evpn_instances"] = "evpn-instances"
            self._children_yang_names.add("evpn-instances")

            self.evpn_logging = Evpn.EvpnTables.EvpnLogging()
            self.evpn_logging.parent = self
            self._children_name_map["evpn_logging"] = "evpn-logging"
            self._children_yang_names.add("evpn-logging")

            self.evpn_interfaces = Evpn.EvpnTables.EvpnInterfaces()
            self.evpn_interfaces.parent = self
            self._children_name_map["evpn_interfaces"] = "evpn-interfaces"
            self._children_yang_names.add("evpn-interfaces")

            self.evpn_virtual_access_pws = Evpn.EvpnTables.EvpnVirtualAccessPws()
            self.evpn_virtual_access_pws.parent = self
            self._children_name_map["evpn_virtual_access_pws"] = "evpn-virtual-access-pws"
            self._children_yang_names.add("evpn-virtual-access-pws")

            self.evpn_ethernet_segment = Evpn.EvpnTables.EvpnEthernetSegment()
            self.evpn_ethernet_segment.parent = self
            self._children_name_map["evpn_ethernet_segment"] = "evpn-ethernet-segment"
            self._children_yang_names.add("evpn-ethernet-segment")
            self._segment_path = lambda: "evpn-tables"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Evpn.EvpnTables, ['evi_cost_out', 'evpn_source_interface', 'evpn_cost_in_startup'], name, value)


        class EvpnTimers(Entity):
            """
            Enter EVPN timers configuration submode
            
            .. attribute:: evpn_carving
            
            	Global Carving timer
            	**type**\: int
            
            	**range:** 0..10
            
            	**default value**\: 0
            
            .. attribute:: evpn_recovery
            
            	Global Recovery timer
            	**type**\: int
            
            	**range:** 20..3600
            
            	**default value**\: 30
            
            .. attribute:: enable
            
            	Enable EVPN timers
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: evpn_peering
            
            	Global Peering timer
            	**type**\: int
            
            	**range:** 0..300
            
            	**default value**\: 3
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnTimers, self).__init__()

                self.yang_name = "evpn-timers"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('evpn_carving', YLeaf(YType.uint32, 'evpn-carving')),
                    ('evpn_recovery', YLeaf(YType.uint32, 'evpn-recovery')),
                    ('enable', YLeaf(YType.empty, 'enable')),
                    ('evpn_peering', YLeaf(YType.uint32, 'evpn-peering')),
                ])
                self.evpn_carving = None
                self.evpn_recovery = None
                self.enable = None
                self.evpn_peering = None
                self._segment_path = lambda: "evpn-timers"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnTimers, ['evpn_carving', 'evpn_recovery', 'enable', 'evpn_peering'], name, value)


        class Evpnmac(Entity):
            """
            EVPN MAC Configuration
            
            .. attribute:: evpnmac_secure
            
            	EVPN MAC Secure Configuration
            	**type**\:  :py:class:`EvpnmacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnmac.EvpnmacSecure>`
            
            .. attribute:: enable
            
            	Enable EVPN MAC Configuration
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.Evpnmac, self).__init__()

                self.yang_name = "evpnmac"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("evpnmac-secure", ("evpnmac_secure", Evpn.EvpnTables.Evpnmac.EvpnmacSecure))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', YLeaf(YType.empty, 'enable')),
                ])
                self.enable = None

                self.evpnmac_secure = Evpn.EvpnTables.Evpnmac.EvpnmacSecure()
                self.evpnmac_secure.parent = self
                self._children_name_map["evpnmac_secure"] = "evpnmac-secure"
                self._children_yang_names.add("evpnmac-secure")
                self._segment_path = lambda: "evpnmac"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.Evpnmac, ['enable'], name, value)


            class EvpnmacSecure(Entity):
                """
                EVPN MAC Secure Configuration
                
                .. attribute:: evpnmac_secure_freeze_time
                
                	Length of time to lock the MAC after a MAC security violation
                	**type**\: int
                
                	**range:** 5..3600
                
                .. attribute:: enable
                
                	Enable EVPN MAC Secure Configuration
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evpnmac_secure_retry_count
                
                	Number of times to unfreeze a MAC before permanently freezing it
                	**type**\: int
                
                	**range:** 0..1000
                
                .. attribute:: evpnmac_secure_move_count
                
                	Number of moves to occur within the move interval before locking the MAC
                	**type**\: int
                
                	**range:** 1..1000
                
                .. attribute:: evpnmac_secure_move_interval
                
                	Interval to watch for subsequent MAC moves before locking the MAC
                	**type**\: int
                
                	**range:** 5..3600
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.Evpnmac.EvpnmacSecure, self).__init__()

                    self.yang_name = "evpnmac-secure"
                    self.yang_parent_name = "evpnmac"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('evpnmac_secure_freeze_time', YLeaf(YType.uint32, 'evpnmac-secure-freeze-time')),
                        ('enable', YLeaf(YType.empty, 'enable')),
                        ('evpnmac_secure_retry_count', YLeaf(YType.uint32, 'evpnmac-secure-retry-count')),
                        ('evpnmac_secure_move_count', YLeaf(YType.uint32, 'evpnmac-secure-move-count')),
                        ('evpnmac_secure_move_interval', YLeaf(YType.uint32, 'evpnmac-secure-move-interval')),
                    ])
                    self.evpnmac_secure_freeze_time = None
                    self.enable = None
                    self.evpnmac_secure_retry_count = None
                    self.evpnmac_secure_move_count = None
                    self.evpnmac_secure_move_interval = None
                    self._segment_path = lambda: "evpnmac-secure"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpnmac/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.Evpnmac.EvpnmacSecure, ['evpnmac_secure_freeze_time', 'enable', 'evpnmac_secure_retry_count', 'evpnmac_secure_move_count', 'evpnmac_secure_move_interval'], name, value)


        class Evpnevis(Entity):
            """
            Enter EVPN Instance configuration submode
            
            .. attribute:: evpnevi
            
            	Enter EVPN Instance configuration submode
            	**type**\: list of  		 :py:class:`Evpnevi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.Evpnevis, self).__init__()

                self.yang_name = "evpnevis"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("evpnevi", ("evpnevi", Evpn.EvpnTables.Evpnevis.Evpnevi))])
                self._leafs = OrderedDict()

                self.evpnevi = YList(self)
                self._segment_path = lambda: "evpnevis"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.Evpnevis, [], name, value)


            class Evpnevi(Entity):
                """
                Enter EVPN Instance configuration submode
                
                .. attribute:: eviid  (key)
                
                	EVI ID
                	**type**\: int
                
                	**range:** 1..65534
                
                .. attribute:: evi_load_balancing
                
                	Enter Loadbalancing configuration submode
                	**type**\:  :py:class:`EviLoadBalancing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing>`
                
                .. attribute:: evpnev_ibgp_auto_discovery
                
                	Enable Autodiscovery BGP in EVPN Instance
                	**type**\:  :py:class:`EvpnevIbgpAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery>`
                
                .. attribute:: evi_advertise_mac
                
                	Enter Advertise local MAC\-only routes configuration submode
                	**type**\:  :py:class:`EviAdvertiseMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EviAdvertiseMac>`
                
                .. attribute:: evi_reorig_disable
                
                	Disable route re\-origination
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evi_advertise_mac_deprecated
                
                	DEPRECATED\: Advertise local MAC\-only and BVI MAC routes
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evpnevi_description
                
                	EVPN Instance description
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: evi_ecmp_disable
                
                	Disable ECMP on the EVI
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evi_unknown_unicast_flooding_disable
                
                	Disable Unknown Unicast Flooding on this EVI
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evpn_evi_cw_disable
                
                	CW disable for EVPN EVI
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.Evpnevis.Evpnevi, self).__init__()

                    self.yang_name = "evpnevi"
                    self.yang_parent_name = "evpnevis"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['eviid']
                    self._child_container_classes = OrderedDict([("evi-load-balancing", ("evi_load_balancing", Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing)), ("evpnev-ibgp-auto-discovery", ("evpnev_ibgp_auto_discovery", Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery)), ("evi-advertise-mac", ("evi_advertise_mac", Evpn.EvpnTables.Evpnevis.Evpnevi.EviAdvertiseMac))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('eviid', YLeaf(YType.uint32, 'eviid')),
                        ('evi_reorig_disable', YLeaf(YType.empty, 'evi-reorig-disable')),
                        ('evi_advertise_mac_deprecated', YLeaf(YType.empty, 'evi-advertise-mac-deprecated')),
                        ('evpnevi_description', YLeaf(YType.str, 'evpnevi-description')),
                        ('evi_ecmp_disable', YLeaf(YType.empty, 'evi-ecmp-disable')),
                        ('evi_unknown_unicast_flooding_disable', YLeaf(YType.empty, 'evi-unknown-unicast-flooding-disable')),
                        ('evpn_evi_cw_disable', YLeaf(YType.empty, 'evpn-evi-cw-disable')),
                    ])
                    self.eviid = None
                    self.evi_reorig_disable = None
                    self.evi_advertise_mac_deprecated = None
                    self.evpnevi_description = None
                    self.evi_ecmp_disable = None
                    self.evi_unknown_unicast_flooding_disable = None
                    self.evpn_evi_cw_disable = None

                    self.evi_load_balancing = Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing()
                    self.evi_load_balancing.parent = self
                    self._children_name_map["evi_load_balancing"] = "evi-load-balancing"
                    self._children_yang_names.add("evi-load-balancing")

                    self.evpnev_ibgp_auto_discovery = Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery()
                    self.evpnev_ibgp_auto_discovery.parent = self
                    self._children_name_map["evpnev_ibgp_auto_discovery"] = "evpnev-ibgp-auto-discovery"
                    self._children_yang_names.add("evpnev-ibgp-auto-discovery")

                    self.evi_advertise_mac = Evpn.EvpnTables.Evpnevis.Evpnevi.EviAdvertiseMac()
                    self.evi_advertise_mac.parent = self
                    self._children_name_map["evi_advertise_mac"] = "evi-advertise-mac"
                    self._children_yang_names.add("evi-advertise-mac")
                    self._segment_path = lambda: "evpnevi" + "[eviid='" + str(self.eviid) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpnevis/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi, ['eviid', 'evi_reorig_disable', 'evi_advertise_mac_deprecated', 'evpnevi_description', 'evi_ecmp_disable', 'evi_unknown_unicast_flooding_disable', 'evpn_evi_cw_disable'], name, value)


                class EviLoadBalancing(Entity):
                    """
                    Enter Loadbalancing configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Loadbalancing
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evi_static_flow_label
                    
                    	Enable Static Flow Label based load balancing
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing, self).__init__()

                        self.yang_name = "evi-load-balancing"
                        self.yang_parent_name = "evpnevi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('evi_static_flow_label', YLeaf(YType.empty, 'evi-static-flow-label')),
                        ])
                        self.enable = None
                        self.evi_static_flow_label = None
                        self._segment_path = lambda: "evi-load-balancing"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing, ['enable', 'evi_static_flow_label'], name, value)


                class EvpnevIbgpAutoDiscovery(Entity):
                    """
                    Enable Autodiscovery BGP in EVPN Instance
                    
                    .. attribute:: enable
                    
                    	Enable Autodiscovery BGP
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: table_policy
                    
                    	Table Policy for installation of forwarding data to L2FIB
                    	**type**\: str
                    
                    .. attribute:: evpn_route_distinguisher
                    
                    	Route Distinguisher
                    	**type**\:  :py:class:`EvpnRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteDistinguisher>`
                    
                    .. attribute:: evpn_route_targets
                    
                    	Route Target
                    	**type**\:  :py:class:`EvpnRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery, self).__init__()

                        self.yang_name = "evpnev-ibgp-auto-discovery"
                        self.yang_parent_name = "evpnevi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("evpn-route-distinguisher", ("evpn_route_distinguisher", Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteDistinguisher)), ("evpn-route-targets", ("evpn_route_targets", Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('table_policy', YLeaf(YType.str, 'table-policy')),
                        ])
                        self.enable = None
                        self.table_policy = None

                        self.evpn_route_distinguisher = Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteDistinguisher()
                        self.evpn_route_distinguisher.parent = self
                        self._children_name_map["evpn_route_distinguisher"] = "evpn-route-distinguisher"
                        self._children_yang_names.add("evpn-route-distinguisher")

                        self.evpn_route_targets = Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets()
                        self.evpn_route_targets.parent = self
                        self._children_name_map["evpn_route_targets"] = "evpn-route-targets"
                        self._children_yang_names.add("evpn-route-targets")
                        self._segment_path = lambda: "evpnev-ibgp-auto-discovery"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery, ['enable', 'table_policy'], name, value)


                    class EvpnRouteDistinguisher(Entity):
                        """
                        Route Distinguisher
                        
                        .. attribute:: type
                        
                        	Router Distinguisher Type
                        	**type**\:  :py:class:`BgpRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher>`
                        
                        .. attribute:: as_
                        
                        	Two byte or 4 byte AS number
                        	**type**\: int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: as_index
                        
                        	AS\:nn (hex or decimal format)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: address
                        
                        	IPV4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: addr_index
                        
                        	Addr index
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteDistinguisher, self).__init__()

                            self.yang_name = "evpn-route-distinguisher"
                            self.yang_parent_name = "evpnev-ibgp-auto-discovery"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', YLeaf(YType.enumeration, 'type')),
                                ('as_', YLeaf(YType.uint32, 'as')),
                                ('as_index', YLeaf(YType.uint32, 'as-index')),
                                ('address', YLeaf(YType.str, 'address')),
                                ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                            ])
                            self.type = None
                            self.as_ = None
                            self.as_index = None
                            self.address = None
                            self.addr_index = None
                            self._segment_path = lambda: "evpn-route-distinguisher"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteDistinguisher, ['type', 'as_', 'as_index', 'address', 'addr_index'], name, value)


                    class EvpnRouteTargets(Entity):
                        """
                        Route Target
                        
                        .. attribute:: evpn_route_target_as
                        
                        	Name of the Route Target
                        	**type**\: list of  		 :py:class:`EvpnRouteTargetAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs>`
                        
                        .. attribute:: evpn_route_target_none
                        
                        	Name of the Route Target
                        	**type**\: list of  		 :py:class:`EvpnRouteTargetNone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone>`
                        
                        .. attribute:: evpn_route_target_ipv4_address
                        
                        	Name of the Route Target
                        	**type**\: list of  		 :py:class:`EvpnRouteTargetIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets, self).__init__()

                            self.yang_name = "evpn-route-targets"
                            self.yang_parent_name = "evpnev-ibgp-auto-discovery"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("evpn-route-target-as", ("evpn_route_target_as", Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs)), ("evpn-route-target-none", ("evpn_route_target_none", Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone)), ("evpn-route-target-ipv4-address", ("evpn_route_target_ipv4_address", Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address))])
                            self._leafs = OrderedDict()

                            self.evpn_route_target_as = YList(self)
                            self.evpn_route_target_none = YList(self)
                            self.evpn_route_target_ipv4_address = YList(self)
                            self._segment_path = lambda: "evpn-route-targets"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets, [], name, value)


                        class EvpnRouteTargetAs(Entity):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  (key)
                            
                            	Format of the route target
                            	**type**\:  :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                            
                            .. attribute:: role  (key)
                            
                            	Role of the router target type
                            	**type**\:  :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                            
                            .. attribute:: as_  (key)
                            
                            	Two byte or 4 byte AS number
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: as_index  (key)
                            
                            	AS\:nn (hex or decimal format)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stitching  (key)
                            
                            	whether RT is Stitching RT
                            	**type**\:  :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTarget>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs, self).__init__()

                                self.yang_name = "evpn-route-target-as"
                                self.yang_parent_name = "evpn-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['format','role','as_','as_index','stitching']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('format', YLeaf(YType.enumeration, 'format')),
                                    ('role', YLeaf(YType.enumeration, 'role')),
                                    ('as_', YLeaf(YType.uint32, 'as')),
                                    ('as_index', YLeaf(YType.uint32, 'as-index')),
                                    ('stitching', YLeaf(YType.enumeration, 'stitching')),
                                ])
                                self.format = None
                                self.role = None
                                self.as_ = None
                                self.as_index = None
                                self.stitching = None
                                self._segment_path = lambda: "evpn-route-target-as" + "[format='" + str(self.format) + "']" + "[role='" + str(self.role) + "']" + "[as='" + str(self.as_) + "']" + "[as-index='" + str(self.as_index) + "']" + "[stitching='" + str(self.stitching) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs, ['format', 'role', 'as_', 'as_index', 'stitching'], name, value)


                        class EvpnRouteTargetNone(Entity):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  (key)
                            
                            	Format of the route target
                            	**type**\:  :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                            
                            .. attribute:: role  (key)
                            
                            	Role of the router target type
                            	**type**\:  :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                            
                            .. attribute:: stitching  (key)
                            
                            	whether RT is Stitching RT
                            	**type**\:  :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTarget>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone, self).__init__()

                                self.yang_name = "evpn-route-target-none"
                                self.yang_parent_name = "evpn-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['format','role','stitching']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('format', YLeaf(YType.enumeration, 'format')),
                                    ('role', YLeaf(YType.enumeration, 'role')),
                                    ('stitching', YLeaf(YType.enumeration, 'stitching')),
                                ])
                                self.format = None
                                self.role = None
                                self.stitching = None
                                self._segment_path = lambda: "evpn-route-target-none" + "[format='" + str(self.format) + "']" + "[role='" + str(self.role) + "']" + "[stitching='" + str(self.stitching) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone, ['format', 'role', 'stitching'], name, value)


                        class EvpnRouteTargetIpv4Address(Entity):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  (key)
                            
                            	Format of the route target
                            	**type**\:  :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                            
                            .. attribute:: role  (key)
                            
                            	Role of the router target type
                            	**type**\:  :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                            
                            .. attribute:: address  (key)
                            
                            	IPV4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: addr_index  (key)
                            
                            	Addr index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: stitching  (key)
                            
                            	whether RT is Stitching RT
                            	**type**\:  :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTarget>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address, self).__init__()

                                self.yang_name = "evpn-route-target-ipv4-address"
                                self.yang_parent_name = "evpn-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['format','role','address','addr_index','stitching']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('format', YLeaf(YType.enumeration, 'format')),
                                    ('role', YLeaf(YType.enumeration, 'role')),
                                    ('address', YLeaf(YType.str, 'address')),
                                    ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                                    ('stitching', YLeaf(YType.enumeration, 'stitching')),
                                ])
                                self.format = None
                                self.role = None
                                self.address = None
                                self.addr_index = None
                                self.stitching = None
                                self._segment_path = lambda: "evpn-route-target-ipv4-address" + "[format='" + str(self.format) + "']" + "[role='" + str(self.role) + "']" + "[address='" + str(self.address) + "']" + "[addr-index='" + str(self.addr_index) + "']" + "[stitching='" + str(self.stitching) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address, ['format', 'role', 'address', 'addr_index', 'stitching'], name, value)


                class EviAdvertiseMac(Entity):
                    """
                    Enter Advertise local MAC\-only routes
                    configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Advertise local MAC\-only routes
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evi_advertise_mac_bvi
                    
                    	Advertise local MAC\-only and BVI MAC routes
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.Evpnevis.Evpnevi.EviAdvertiseMac, self).__init__()

                        self.yang_name = "evi-advertise-mac"
                        self.yang_parent_name = "evpnevi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('evi_advertise_mac_bvi', YLeaf(YType.empty, 'evi-advertise-mac-bvi')),
                        ])
                        self.enable = None
                        self.evi_advertise_mac_bvi = None
                        self._segment_path = lambda: "evi-advertise-mac"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EviAdvertiseMac, ['enable', 'evi_advertise_mac_bvi'], name, value)


        class EvpnVirtualAccessVfis(Entity):
            """
            Virtual Access VFI interfaces
            
            .. attribute:: evpn_virtual_access_vfi
            
            	Virtual Access VFI
            	**type**\: list of  		 :py:class:`EvpnVirtualAccessVfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnVirtualAccessVfis, self).__init__()

                self.yang_name = "evpn-virtual-access-vfis"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("evpn-virtual-access-vfi", ("evpn_virtual_access_vfi", Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi))])
                self._leafs = OrderedDict()

                self.evpn_virtual_access_vfi = YList(self)
                self._segment_path = lambda: "evpn-virtual-access-vfis"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessVfis, [], name, value)


            class EvpnVirtualAccessVfi(Entity):
                """
                Virtual Access VFI
                
                .. attribute:: name  (key)
                
                	Name of the Virtual Access VFI
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: evpn_virtual_access_vfi_timers
                
                	Enter Virtual Forwarding Interface timers configuration submode
                	**type**\:  :py:class:`EvpnVirtualAccessVfiTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers>`
                
                .. attribute:: evpn_virtual_ethernet_segment
                
                	Enter Ethernet Segment configuration submode
                	**type**\:  :py:class:`EvpnVirtualEthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi, self).__init__()

                    self.yang_name = "evpn-virtual-access-vfi"
                    self.yang_parent_name = "evpn-virtual-access-vfis"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([("evpn-virtual-access-vfi-timers", ("evpn_virtual_access_vfi_timers", Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers)), ("evpn-virtual-ethernet-segment", ("evpn_virtual_ethernet_segment", Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                    ])
                    self.name = None

                    self.evpn_virtual_access_vfi_timers = Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers()
                    self.evpn_virtual_access_vfi_timers.parent = self
                    self._children_name_map["evpn_virtual_access_vfi_timers"] = "evpn-virtual-access-vfi-timers"
                    self._children_yang_names.add("evpn-virtual-access-vfi-timers")

                    self.evpn_virtual_ethernet_segment = Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment()
                    self.evpn_virtual_ethernet_segment.parent = self
                    self._children_name_map["evpn_virtual_ethernet_segment"] = "evpn-virtual-ethernet-segment"
                    self._children_yang_names.add("evpn-virtual-ethernet-segment")
                    self._segment_path = lambda: "evpn-virtual-access-vfi" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-virtual-access-vfis/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi, ['name'], name, value)


                class EvpnVirtualAccessVfiTimers(Entity):
                    """
                    Enter Virtual Forwarding Interface timers
                    configuration submode
                    
                    .. attribute:: evpn_virtual_access_vfi_recovery
                    
                    	Virtual Forwarding Interface\-specific Recovery timer
                    	**type**\: int
                    
                    	**range:** 20..3600
                    
                    	**default value**\: 30
                    
                    .. attribute:: evpn_virtual_access_vfi_peering
                    
                    	Virtual Forwarding Interface\-specific Peering timer
                    	**type**\: int
                    
                    	**range:** 0..300
                    
                    	**default value**\: 3
                    
                    .. attribute:: evpn_virtual_access_vfi_carving
                    
                    	Virtual Forwarding Interface\-specific Carving timer
                    	**type**\: int
                    
                    	**range:** 0..10
                    
                    	**default value**\: 0
                    
                    .. attribute:: enable
                    
                    	Enable Virtual Forwarding Interface timers
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers, self).__init__()

                        self.yang_name = "evpn-virtual-access-vfi-timers"
                        self.yang_parent_name = "evpn-virtual-access-vfi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('evpn_virtual_access_vfi_recovery', YLeaf(YType.uint32, 'evpn-virtual-access-vfi-recovery')),
                            ('evpn_virtual_access_vfi_peering', YLeaf(YType.uint32, 'evpn-virtual-access-vfi-peering')),
                            ('evpn_virtual_access_vfi_carving', YLeaf(YType.uint32, 'evpn-virtual-access-vfi-carving')),
                            ('enable', YLeaf(YType.empty, 'enable')),
                        ])
                        self.evpn_virtual_access_vfi_recovery = None
                        self.evpn_virtual_access_vfi_peering = None
                        self.evpn_virtual_access_vfi_carving = None
                        self.enable = None
                        self._segment_path = lambda: "evpn-virtual-access-vfi-timers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers, ['evpn_virtual_access_vfi_recovery', 'evpn_virtual_access_vfi_peering', 'evpn_virtual_access_vfi_carving', 'enable'], name, value)


                class EvpnVirtualEthernetSegment(Entity):
                    """
                    Enter Ethernet Segment configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Ethernet Segment
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: es_import_route_target
                    
                    	ES\-Import Route Target
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: identifier
                    
                    	Ethernet segment identifier
                    	**type**\:  :py:class:`Identifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.Identifier>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: manual_service_carving
                    
                    	Enter Manual service carving configuration submode
                    	**type**\:  :py:class:`ManualServiceCarving <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment, self).__init__()

                        self.yang_name = "evpn-virtual-ethernet-segment"
                        self.yang_parent_name = "evpn-virtual-access-vfi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("identifier", ("identifier", Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.Identifier)), ("manual-service-carving", ("manual_service_carving", Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('es_import_route_target', YLeaf(YType.str, 'es-import-route-target')),
                        ])
                        self.enable = None
                        self.es_import_route_target = None

                        self.identifier = None
                        self._children_name_map["identifier"] = "identifier"
                        self._children_yang_names.add("identifier")

                        self.manual_service_carving = Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving()
                        self.manual_service_carving.parent = self
                        self._children_name_map["manual_service_carving"] = "manual-service-carving"
                        self._children_yang_names.add("manual-service-carving")
                        self._segment_path = lambda: "evpn-virtual-ethernet-segment"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment, ['enable', 'es_import_route_target'], name, value)


                    class Identifier(Entity):
                        """
                        Ethernet segment identifier
                        
                        .. attribute:: bytes01
                        
                        	Type 0's 1st Byte or Type Byte and 1st Byte
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        .. attribute:: bytes23
                        
                        	2nd and 3rd Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes45
                        
                        	4th and 5th Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes67
                        
                        	6th and 7th Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes89
                        
                        	8th and 9th Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: type
                        
                        	Ethernet segment identifier type
                        	**type**\:  :py:class:`EthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EthernetSegmentIdentifier>`
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.Identifier, self).__init__()

                            self.yang_name = "identifier"
                            self.yang_parent_name = "evpn-virtual-ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('bytes01', YLeaf(YType.str, 'bytes01')),
                                ('bytes23', YLeaf(YType.str, 'bytes23')),
                                ('bytes45', YLeaf(YType.str, 'bytes45')),
                                ('bytes67', YLeaf(YType.str, 'bytes67')),
                                ('bytes89', YLeaf(YType.str, 'bytes89')),
                                ('type', YLeaf(YType.enumeration, 'type')),
                            ])
                            self.bytes01 = None
                            self.bytes23 = None
                            self.bytes45 = None
                            self.bytes67 = None
                            self.bytes89 = None
                            self.type = None
                            self._segment_path = lambda: "identifier"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.Identifier, ['bytes01', 'bytes23', 'bytes45', 'bytes67', 'bytes89', 'type'], name, value)


                    class ManualServiceCarving(Entity):
                        """
                        Enter Manual service carving configuration
                        submode
                        
                        .. attribute:: service_list
                        
                        	Manual service carving primary,secondary lists
                        	**type**\:  :py:class:`ServiceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList>`
                        
                        .. attribute:: enable
                        
                        	Enable Manual service carving
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving, self).__init__()

                            self.yang_name = "manual-service-carving"
                            self.yang_parent_name = "evpn-virtual-ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("service-list", ("service_list", Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', YLeaf(YType.empty, 'enable')),
                            ])
                            self.enable = None

                            self.service_list = Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList()
                            self.service_list.parent = self
                            self._children_name_map["service_list"] = "service-list"
                            self._children_yang_names.add("service-list")
                            self._segment_path = lambda: "manual-service-carving"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving, ['enable'], name, value)


                        class ServiceList(Entity):
                            """
                            Manual service carving primary,secondary lists
                            
                            .. attribute:: primary
                            
                            	Primary services list
                            	**type**\: str
                            
                            	**length:** 1..150
                            
                            .. attribute:: secondary
                            
                            	Secondary services list
                            	**type**\: str
                            
                            	**length:** 1..150
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList, self).__init__()

                                self.yang_name = "service-list"
                                self.yang_parent_name = "manual-service-carving"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('primary', YLeaf(YType.str, 'primary')),
                                    ('secondary', YLeaf(YType.str, 'secondary')),
                                ])
                                self.primary = None
                                self.secondary = None
                                self._segment_path = lambda: "service-list"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList, ['primary', 'secondary'], name, value)


        class EvpnLoadBalancing(Entity):
            """
            Enter EVPN Loadbalancing configuration submode
            
            .. attribute:: evpn_static_flow_label
            
            	Enable Static Flow Label based load balancing
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable EVPN Loadbalancing
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnLoadBalancing, self).__init__()

                self.yang_name = "evpn-load-balancing"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('evpn_static_flow_label', YLeaf(YType.empty, 'evpn-static-flow-label')),
                    ('enable', YLeaf(YType.empty, 'enable')),
                ])
                self.evpn_static_flow_label = None
                self.enable = None
                self._segment_path = lambda: "evpn-load-balancing"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnLoadBalancing, ['evpn_static_flow_label', 'enable'], name, value)


        class EvpnBgpAutoDiscovery(Entity):
            """
            Enable Autodiscovery BGP in EVPN
            
            .. attribute:: enable
            
            	Enable Autodiscovery BGP
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: evpn_route_distinguisher
            
            	Route Distinguisher
            	**type**\:  :py:class:`EvpnRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnBgpAutoDiscovery.EvpnRouteDistinguisher>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnBgpAutoDiscovery, self).__init__()

                self.yang_name = "evpn-bgp-auto-discovery"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("evpn-route-distinguisher", ("evpn_route_distinguisher", Evpn.EvpnTables.EvpnBgpAutoDiscovery.EvpnRouteDistinguisher))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', YLeaf(YType.empty, 'enable')),
                ])
                self.enable = None

                self.evpn_route_distinguisher = Evpn.EvpnTables.EvpnBgpAutoDiscovery.EvpnRouteDistinguisher()
                self.evpn_route_distinguisher.parent = self
                self._children_name_map["evpn_route_distinguisher"] = "evpn-route-distinguisher"
                self._children_yang_names.add("evpn-route-distinguisher")
                self._segment_path = lambda: "evpn-bgp-auto-discovery"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnBgpAutoDiscovery, ['enable'], name, value)


            class EvpnRouteDistinguisher(Entity):
                """
                Route Distinguisher
                
                .. attribute:: type
                
                	Router Distinguisher Type
                	**type**\:  :py:class:`BgpRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher>`
                
                .. attribute:: as_
                
                	Two byte or 4 byte AS number
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: as_index
                
                	AS\:nn (hex or decimal format)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: address
                
                	IPV4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: addr_index
                
                	Addr index
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.EvpnBgpAutoDiscovery.EvpnRouteDistinguisher, self).__init__()

                    self.yang_name = "evpn-route-distinguisher"
                    self.yang_parent_name = "evpn-bgp-auto-discovery"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', YLeaf(YType.enumeration, 'type')),
                        ('as_', YLeaf(YType.uint32, 'as')),
                        ('as_index', YLeaf(YType.uint32, 'as-index')),
                        ('address', YLeaf(YType.str, 'address')),
                        ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                    ])
                    self.type = None
                    self.as_ = None
                    self.as_index = None
                    self.address = None
                    self.addr_index = None
                    self._segment_path = lambda: "evpn-route-distinguisher"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-bgp-auto-discovery/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.EvpnBgpAutoDiscovery.EvpnRouteDistinguisher, ['type', 'as_', 'as_index', 'address', 'addr_index'], name, value)


        class EvpnInstances(Entity):
            """
            Enter EVPN Instance configuration submode
            
            .. attribute:: evpn_instance
            
            	Enter EVPN Instance configuration submode
            	**type**\: list of  		 :py:class:`EvpnInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnInstances, self).__init__()

                self.yang_name = "evpn-instances"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("evpn-instance", ("evpn_instance", Evpn.EvpnTables.EvpnInstances.EvpnInstance))])
                self._leafs = OrderedDict()

                self.evpn_instance = YList(self)
                self._segment_path = lambda: "evpn-instances"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnInstances, [], name, value)


            class EvpnInstance(Entity):
                """
                Enter EVPN Instance configuration submode
                
                .. attribute:: eviid  (key)
                
                	EVPN Instance ID
                	**type**\: int
                
                	**range:** 1..65534
                
                .. attribute:: encapsulation  (key)
                
                	EVPN Instance Encapsulation
                	**type**\:  :py:class:`EvpnEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EvpnEncapsulation>`
                
                .. attribute:: side  (key)
                
                	EVPN Instance Side
                	**type**\:  :py:class:`EvpnSide <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EvpnSide>`
                
                .. attribute:: evpn_instance_bgp_auto_discovery
                
                	Enable Autodiscovery BGP in EVPN Instance
                	**type**\:  :py:class:`EvpnInstanceBgpAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery>`
                
                .. attribute:: evpn_instance_advertise_mac
                
                	Enter Advertise local MAC\-only routes configuration submode
                	**type**\:  :py:class:`EvpnInstanceAdvertiseMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceAdvertiseMac>`
                
                .. attribute:: evpn_instance_load_balancing
                
                	Enter Loadbalancing configuration submode
                	**type**\:  :py:class:`EvpnInstanceLoadBalancing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceLoadBalancing>`
                
                .. attribute:: evi_reorig_disable
                
                	Disable route re\-origination
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evi_advertise_mac_deprecated
                
                	DEPRECATED\: Advertise local MAC\-only and BVI MAC routes
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evpnevi_description
                
                	EVPN Instance description
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: evi_ecmp_disable
                
                	Disable ECMP on the EVI
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evi_unknown_unicast_flooding_disable
                
                	Disable Unknown Unicast Flooding on this EVI
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evpn_evi_cw_disable
                
                	CW disable for EVPN EVI
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.EvpnInstances.EvpnInstance, self).__init__()

                    self.yang_name = "evpn-instance"
                    self.yang_parent_name = "evpn-instances"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['eviid','encapsulation','side']
                    self._child_container_classes = OrderedDict([("evpn-instance-bgp-auto-discovery", ("evpn_instance_bgp_auto_discovery", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery)), ("evpn-instance-advertise-mac", ("evpn_instance_advertise_mac", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceAdvertiseMac)), ("evpn-instance-load-balancing", ("evpn_instance_load_balancing", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceLoadBalancing))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('eviid', YLeaf(YType.uint32, 'eviid')),
                        ('encapsulation', YLeaf(YType.enumeration, 'encapsulation')),
                        ('side', YLeaf(YType.enumeration, 'side')),
                        ('evi_reorig_disable', YLeaf(YType.empty, 'evi-reorig-disable')),
                        ('evi_advertise_mac_deprecated', YLeaf(YType.empty, 'evi-advertise-mac-deprecated')),
                        ('evpnevi_description', YLeaf(YType.str, 'evpnevi-description')),
                        ('evi_ecmp_disable', YLeaf(YType.empty, 'evi-ecmp-disable')),
                        ('evi_unknown_unicast_flooding_disable', YLeaf(YType.empty, 'evi-unknown-unicast-flooding-disable')),
                        ('evpn_evi_cw_disable', YLeaf(YType.empty, 'evpn-evi-cw-disable')),
                    ])
                    self.eviid = None
                    self.encapsulation = None
                    self.side = None
                    self.evi_reorig_disable = None
                    self.evi_advertise_mac_deprecated = None
                    self.evpnevi_description = None
                    self.evi_ecmp_disable = None
                    self.evi_unknown_unicast_flooding_disable = None
                    self.evpn_evi_cw_disable = None

                    self.evpn_instance_bgp_auto_discovery = Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery()
                    self.evpn_instance_bgp_auto_discovery.parent = self
                    self._children_name_map["evpn_instance_bgp_auto_discovery"] = "evpn-instance-bgp-auto-discovery"
                    self._children_yang_names.add("evpn-instance-bgp-auto-discovery")

                    self.evpn_instance_advertise_mac = Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceAdvertiseMac()
                    self.evpn_instance_advertise_mac.parent = self
                    self._children_name_map["evpn_instance_advertise_mac"] = "evpn-instance-advertise-mac"
                    self._children_yang_names.add("evpn-instance-advertise-mac")

                    self.evpn_instance_load_balancing = Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceLoadBalancing()
                    self.evpn_instance_load_balancing.parent = self
                    self._children_name_map["evpn_instance_load_balancing"] = "evpn-instance-load-balancing"
                    self._children_yang_names.add("evpn-instance-load-balancing")
                    self._segment_path = lambda: "evpn-instance" + "[eviid='" + str(self.eviid) + "']" + "[encapsulation='" + str(self.encapsulation) + "']" + "[side='" + str(self.side) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-instances/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance, ['eviid', 'encapsulation', 'side', 'evi_reorig_disable', 'evi_advertise_mac_deprecated', 'evpnevi_description', 'evi_ecmp_disable', 'evi_unknown_unicast_flooding_disable', 'evpn_evi_cw_disable'], name, value)


                class EvpnInstanceBgpAutoDiscovery(Entity):
                    """
                    Enable Autodiscovery BGP in EVPN Instance
                    
                    .. attribute:: enable
                    
                    	Enable Autodiscovery BGP
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: table_policy
                    
                    	Table Policy for installation of forwarding data to L2FIB
                    	**type**\: str
                    
                    .. attribute:: evpn_route_distinguisher
                    
                    	Route Distinguisher
                    	**type**\:  :py:class:`EvpnRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteDistinguisher>`
                    
                    .. attribute:: evpn_route_targets
                    
                    	Route Target
                    	**type**\:  :py:class:`EvpnRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery, self).__init__()

                        self.yang_name = "evpn-instance-bgp-auto-discovery"
                        self.yang_parent_name = "evpn-instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("evpn-route-distinguisher", ("evpn_route_distinguisher", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteDistinguisher)), ("evpn-route-targets", ("evpn_route_targets", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('table_policy', YLeaf(YType.str, 'table-policy')),
                        ])
                        self.enable = None
                        self.table_policy = None

                        self.evpn_route_distinguisher = Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteDistinguisher()
                        self.evpn_route_distinguisher.parent = self
                        self._children_name_map["evpn_route_distinguisher"] = "evpn-route-distinguisher"
                        self._children_yang_names.add("evpn-route-distinguisher")

                        self.evpn_route_targets = Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets()
                        self.evpn_route_targets.parent = self
                        self._children_name_map["evpn_route_targets"] = "evpn-route-targets"
                        self._children_yang_names.add("evpn-route-targets")
                        self._segment_path = lambda: "evpn-instance-bgp-auto-discovery"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery, ['enable', 'table_policy'], name, value)


                    class EvpnRouteDistinguisher(Entity):
                        """
                        Route Distinguisher
                        
                        .. attribute:: type
                        
                        	Router Distinguisher Type
                        	**type**\:  :py:class:`BgpRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher>`
                        
                        .. attribute:: as_
                        
                        	Two byte or 4 byte AS number
                        	**type**\: int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: as_index
                        
                        	AS\:nn (hex or decimal format)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: address
                        
                        	IPV4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: addr_index
                        
                        	Addr index
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteDistinguisher, self).__init__()

                            self.yang_name = "evpn-route-distinguisher"
                            self.yang_parent_name = "evpn-instance-bgp-auto-discovery"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', YLeaf(YType.enumeration, 'type')),
                                ('as_', YLeaf(YType.uint32, 'as')),
                                ('as_index', YLeaf(YType.uint32, 'as-index')),
                                ('address', YLeaf(YType.str, 'address')),
                                ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                            ])
                            self.type = None
                            self.as_ = None
                            self.as_index = None
                            self.address = None
                            self.addr_index = None
                            self._segment_path = lambda: "evpn-route-distinguisher"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteDistinguisher, ['type', 'as_', 'as_index', 'address', 'addr_index'], name, value)


                    class EvpnRouteTargets(Entity):
                        """
                        Route Target
                        
                        .. attribute:: evpn_route_target_as
                        
                        	Name of the Route Target
                        	**type**\: list of  		 :py:class:`EvpnRouteTargetAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs>`
                        
                        .. attribute:: evpn_route_target_none
                        
                        	Name of the Route Target
                        	**type**\: list of  		 :py:class:`EvpnRouteTargetNone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone>`
                        
                        .. attribute:: evpn_route_target_ipv4_address
                        
                        	Name of the Route Target
                        	**type**\: list of  		 :py:class:`EvpnRouteTargetIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets, self).__init__()

                            self.yang_name = "evpn-route-targets"
                            self.yang_parent_name = "evpn-instance-bgp-auto-discovery"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("evpn-route-target-as", ("evpn_route_target_as", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs)), ("evpn-route-target-none", ("evpn_route_target_none", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone)), ("evpn-route-target-ipv4-address", ("evpn_route_target_ipv4_address", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address))])
                            self._leafs = OrderedDict()

                            self.evpn_route_target_as = YList(self)
                            self.evpn_route_target_none = YList(self)
                            self.evpn_route_target_ipv4_address = YList(self)
                            self._segment_path = lambda: "evpn-route-targets"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets, [], name, value)


                        class EvpnRouteTargetAs(Entity):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  (key)
                            
                            	Format of the route target
                            	**type**\:  :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                            
                            .. attribute:: role  (key)
                            
                            	Role of the router target type
                            	**type**\:  :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                            
                            .. attribute:: as_  (key)
                            
                            	Two byte or 4 byte AS number
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: as_index  (key)
                            
                            	AS\:nn (hex or decimal format)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stitching  (key)
                            
                            	whether RT is Stitching RT
                            	**type**\:  :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTarget>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs, self).__init__()

                                self.yang_name = "evpn-route-target-as"
                                self.yang_parent_name = "evpn-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['format','role','as_','as_index','stitching']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('format', YLeaf(YType.enumeration, 'format')),
                                    ('role', YLeaf(YType.enumeration, 'role')),
                                    ('as_', YLeaf(YType.uint32, 'as')),
                                    ('as_index', YLeaf(YType.uint32, 'as-index')),
                                    ('stitching', YLeaf(YType.enumeration, 'stitching')),
                                ])
                                self.format = None
                                self.role = None
                                self.as_ = None
                                self.as_index = None
                                self.stitching = None
                                self._segment_path = lambda: "evpn-route-target-as" + "[format='" + str(self.format) + "']" + "[role='" + str(self.role) + "']" + "[as='" + str(self.as_) + "']" + "[as-index='" + str(self.as_index) + "']" + "[stitching='" + str(self.stitching) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs, ['format', 'role', 'as_', 'as_index', 'stitching'], name, value)


                        class EvpnRouteTargetNone(Entity):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  (key)
                            
                            	Format of the route target
                            	**type**\:  :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                            
                            .. attribute:: role  (key)
                            
                            	Role of the router target type
                            	**type**\:  :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                            
                            .. attribute:: stitching  (key)
                            
                            	whether RT is Stitching RT
                            	**type**\:  :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTarget>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone, self).__init__()

                                self.yang_name = "evpn-route-target-none"
                                self.yang_parent_name = "evpn-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['format','role','stitching']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('format', YLeaf(YType.enumeration, 'format')),
                                    ('role', YLeaf(YType.enumeration, 'role')),
                                    ('stitching', YLeaf(YType.enumeration, 'stitching')),
                                ])
                                self.format = None
                                self.role = None
                                self.stitching = None
                                self._segment_path = lambda: "evpn-route-target-none" + "[format='" + str(self.format) + "']" + "[role='" + str(self.role) + "']" + "[stitching='" + str(self.stitching) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone, ['format', 'role', 'stitching'], name, value)


                        class EvpnRouteTargetIpv4Address(Entity):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  (key)
                            
                            	Format of the route target
                            	**type**\:  :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                            
                            .. attribute:: role  (key)
                            
                            	Role of the router target type
                            	**type**\:  :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                            
                            .. attribute:: address  (key)
                            
                            	IPV4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: addr_index  (key)
                            
                            	Addr index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: stitching  (key)
                            
                            	whether RT is Stitching RT
                            	**type**\:  :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTarget>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address, self).__init__()

                                self.yang_name = "evpn-route-target-ipv4-address"
                                self.yang_parent_name = "evpn-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['format','role','address','addr_index','stitching']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('format', YLeaf(YType.enumeration, 'format')),
                                    ('role', YLeaf(YType.enumeration, 'role')),
                                    ('address', YLeaf(YType.str, 'address')),
                                    ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                                    ('stitching', YLeaf(YType.enumeration, 'stitching')),
                                ])
                                self.format = None
                                self.role = None
                                self.address = None
                                self.addr_index = None
                                self.stitching = None
                                self._segment_path = lambda: "evpn-route-target-ipv4-address" + "[format='" + str(self.format) + "']" + "[role='" + str(self.role) + "']" + "[address='" + str(self.address) + "']" + "[addr-index='" + str(self.addr_index) + "']" + "[stitching='" + str(self.stitching) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address, ['format', 'role', 'address', 'addr_index', 'stitching'], name, value)


                class EvpnInstanceAdvertiseMac(Entity):
                    """
                    Enter Advertise local MAC\-only routes
                    configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Advertise local MAC\-only routes
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evi_advertise_mac_bvi
                    
                    	Advertise local MAC\-only and BVI MAC routes
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceAdvertiseMac, self).__init__()

                        self.yang_name = "evpn-instance-advertise-mac"
                        self.yang_parent_name = "evpn-instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('evi_advertise_mac_bvi', YLeaf(YType.empty, 'evi-advertise-mac-bvi')),
                        ])
                        self.enable = None
                        self.evi_advertise_mac_bvi = None
                        self._segment_path = lambda: "evpn-instance-advertise-mac"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceAdvertiseMac, ['enable', 'evi_advertise_mac_bvi'], name, value)


                class EvpnInstanceLoadBalancing(Entity):
                    """
                    Enter Loadbalancing configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Loadbalancing
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evi_static_flow_label
                    
                    	Enable Static Flow Label based load balancing
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceLoadBalancing, self).__init__()

                        self.yang_name = "evpn-instance-load-balancing"
                        self.yang_parent_name = "evpn-instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('evi_static_flow_label', YLeaf(YType.empty, 'evi-static-flow-label')),
                        ])
                        self.enable = None
                        self.evi_static_flow_label = None
                        self._segment_path = lambda: "evpn-instance-load-balancing"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceLoadBalancing, ['enable', 'evi_static_flow_label'], name, value)


        class EvpnLogging(Entity):
            """
            Enter EVPN Logging configuration submode
            
            .. attribute:: evpn_df_election
            
            	Enable Designated Forwarder election logging
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable EVPN Logging
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnLogging, self).__init__()

                self.yang_name = "evpn-logging"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('evpn_df_election', YLeaf(YType.empty, 'evpn-df-election')),
                    ('enable', YLeaf(YType.empty, 'enable')),
                ])
                self.evpn_df_election = None
                self.enable = None
                self._segment_path = lambda: "evpn-logging"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnLogging, ['evpn_df_election', 'enable'], name, value)


        class EvpnInterfaces(Entity):
            """
            Attachment Circuit interfaces
            
            .. attribute:: evpn_interface
            
            	Attachment circuit interface
            	**type**\: list of  		 :py:class:`EvpnInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnInterfaces, self).__init__()

                self.yang_name = "evpn-interfaces"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("evpn-interface", ("evpn_interface", Evpn.EvpnTables.EvpnInterfaces.EvpnInterface))])
                self._leafs = OrderedDict()

                self.evpn_interface = YList(self)
                self._segment_path = lambda: "evpn-interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces, [], name, value)


            class EvpnInterface(Entity):
                """
                Attachment circuit interface
                
                .. attribute:: interface_name  (key)
                
                	Name of the attachment circuit interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: evpnac_timers
                
                	Enter Interface\-specific timers configuration submode
                	**type**\:  :py:class:`EvpnacTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers>`
                
                .. attribute:: ethernet_segment
                
                	Enter Ethernet Segment configuration submode
                	**type**\:  :py:class:`EthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment>`
                
                .. attribute:: mac_flush
                
                	Enable MAC Flushing
                	**type**\:  :py:class:`MacFlushMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacFlushMode>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface, self).__init__()

                    self.yang_name = "evpn-interface"
                    self.yang_parent_name = "evpn-interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_container_classes = OrderedDict([("evpnac-timers", ("evpnac_timers", Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers)), ("ethernet-segment", ("ethernet_segment", Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', YLeaf(YType.str, 'interface-name')),
                        ('mac_flush', YLeaf(YType.enumeration, 'mac-flush')),
                    ])
                    self.interface_name = None
                    self.mac_flush = None

                    self.evpnac_timers = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers()
                    self.evpnac_timers.parent = self
                    self._children_name_map["evpnac_timers"] = "evpnac-timers"
                    self._children_yang_names.add("evpnac-timers")

                    self.ethernet_segment = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment()
                    self.ethernet_segment.parent = self
                    self._children_name_map["ethernet_segment"] = "ethernet-segment"
                    self._children_yang_names.add("ethernet-segment")
                    self._segment_path = lambda: "evpn-interface" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface, ['interface_name', 'mac_flush'], name, value)


                class EvpnacTimers(Entity):
                    """
                    Enter Interface\-specific timers configuration
                    submode
                    
                    .. attribute:: evpnac_peering
                    
                    	Interface\-specific Peering timer
                    	**type**\: int
                    
                    	**range:** 0..300
                    
                    	**default value**\: 3
                    
                    .. attribute:: evpnac_carving
                    
                    	Interface\-specific Carving timer
                    	**type**\: int
                    
                    	**range:** 0..10
                    
                    	**default value**\: 0
                    
                    .. attribute:: enable
                    
                    	Enable Interface\-specific timers
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evpnac_recovery
                    
                    	Interface\-specific Recovery timer
                    	**type**\: int
                    
                    	**range:** 20..3600
                    
                    	**default value**\: 30
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers, self).__init__()

                        self.yang_name = "evpnac-timers"
                        self.yang_parent_name = "evpn-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('evpnac_peering', YLeaf(YType.uint32, 'evpnac-peering')),
                            ('evpnac_carving', YLeaf(YType.uint32, 'evpnac-carving')),
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('evpnac_recovery', YLeaf(YType.uint32, 'evpnac-recovery')),
                        ])
                        self.evpnac_peering = None
                        self.evpnac_carving = None
                        self.enable = None
                        self.evpnac_recovery = None
                        self._segment_path = lambda: "evpnac-timers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers, ['evpnac_peering', 'evpnac_carving', 'enable', 'evpnac_recovery'], name, value)


                class EthernetSegment(Entity):
                    """
                    Enter Ethernet Segment configuration submode
                    
                    .. attribute:: force_single_homed
                    
                    	Force ethernet segment to remain single\-homed
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: load_balancing_single_active
                    
                    	Enable single\-active load balancing mode
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: enable
                    
                    	Enable Ethernet Segment
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: backbone_source_mac
                    
                    	Backbone Source MAC
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: es_import_route_target
                    
                    	ES\-Import Route Target
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: identifier
                    
                    	Ethernet segment identifier
                    	**type**\:  :py:class:`Identifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.Identifier>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: manual_service_carving
                    
                    	Enter Manual service carving configuration submode
                    	**type**\:  :py:class:`ManualServiceCarving <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment, self).__init__()

                        self.yang_name = "ethernet-segment"
                        self.yang_parent_name = "evpn-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("identifier", ("identifier", Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.Identifier)), ("manual-service-carving", ("manual_service_carving", Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('force_single_homed', YLeaf(YType.empty, 'force-single-homed')),
                            ('load_balancing_single_active', YLeaf(YType.empty, 'load-balancing-single-active')),
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('backbone_source_mac', YLeaf(YType.str, 'backbone-source-mac')),
                            ('es_import_route_target', YLeaf(YType.str, 'es-import-route-target')),
                        ])
                        self.force_single_homed = None
                        self.load_balancing_single_active = None
                        self.enable = None
                        self.backbone_source_mac = None
                        self.es_import_route_target = None

                        self.identifier = None
                        self._children_name_map["identifier"] = "identifier"
                        self._children_yang_names.add("identifier")

                        self.manual_service_carving = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving()
                        self.manual_service_carving.parent = self
                        self._children_name_map["manual_service_carving"] = "manual-service-carving"
                        self._children_yang_names.add("manual-service-carving")
                        self._segment_path = lambda: "ethernet-segment"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment, ['force_single_homed', 'load_balancing_single_active', 'enable', 'backbone_source_mac', 'es_import_route_target'], name, value)


                    class Identifier(Entity):
                        """
                        Ethernet segment identifier
                        
                        .. attribute:: bytes01
                        
                        	Type 0's 1st Byte or Type Byte and 1st Byte
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        .. attribute:: bytes23
                        
                        	2nd and 3rd Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes45
                        
                        	4th and 5th Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes67
                        
                        	6th and 7th Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes89
                        
                        	8th and 9th Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: type
                        
                        	Ethernet segment identifier type
                        	**type**\:  :py:class:`EthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EthernetSegmentIdentifier>`
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.Identifier, self).__init__()

                            self.yang_name = "identifier"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('bytes01', YLeaf(YType.str, 'bytes01')),
                                ('bytes23', YLeaf(YType.str, 'bytes23')),
                                ('bytes45', YLeaf(YType.str, 'bytes45')),
                                ('bytes67', YLeaf(YType.str, 'bytes67')),
                                ('bytes89', YLeaf(YType.str, 'bytes89')),
                                ('type', YLeaf(YType.enumeration, 'type')),
                            ])
                            self.bytes01 = None
                            self.bytes23 = None
                            self.bytes45 = None
                            self.bytes67 = None
                            self.bytes89 = None
                            self.type = None
                            self._segment_path = lambda: "identifier"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.Identifier, ['bytes01', 'bytes23', 'bytes45', 'bytes67', 'bytes89', 'type'], name, value)


                    class ManualServiceCarving(Entity):
                        """
                        Enter Manual service carving configuration
                        submode
                        
                        .. attribute:: service_list
                        
                        	Manual service carving primary,secondary lists
                        	**type**\:  :py:class:`ServiceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving.ServiceList>`
                        
                        .. attribute:: enable
                        
                        	Enable Manual service carving
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving, self).__init__()

                            self.yang_name = "manual-service-carving"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("service-list", ("service_list", Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving.ServiceList))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', YLeaf(YType.empty, 'enable')),
                            ])
                            self.enable = None

                            self.service_list = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving.ServiceList()
                            self.service_list.parent = self
                            self._children_name_map["service_list"] = "service-list"
                            self._children_yang_names.add("service-list")
                            self._segment_path = lambda: "manual-service-carving"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving, ['enable'], name, value)


                        class ServiceList(Entity):
                            """
                            Manual service carving primary,secondary lists
                            
                            .. attribute:: primary
                            
                            	Primary services list
                            	**type**\: str
                            
                            	**length:** 1..150
                            
                            .. attribute:: secondary
                            
                            	Secondary services list
                            	**type**\: str
                            
                            	**length:** 1..150
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving.ServiceList, self).__init__()

                                self.yang_name = "service-list"
                                self.yang_parent_name = "manual-service-carving"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('primary', YLeaf(YType.str, 'primary')),
                                    ('secondary', YLeaf(YType.str, 'secondary')),
                                ])
                                self.primary = None
                                self.secondary = None
                                self._segment_path = lambda: "service-list"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving.ServiceList, ['primary', 'secondary'], name, value)


        class EvpnVirtualAccessPws(Entity):
            """
            Virtual Access Pseudowire interfaces
            
            .. attribute:: evpn_virtual_access_pw
            
            	Virtual Access Pseudowire
            	**type**\: list of  		 :py:class:`EvpnVirtualAccessPw <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnVirtualAccessPws, self).__init__()

                self.yang_name = "evpn-virtual-access-pws"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("evpn-virtual-access-pw", ("evpn_virtual_access_pw", Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw))])
                self._leafs = OrderedDict()

                self.evpn_virtual_access_pw = YList(self)
                self._segment_path = lambda: "evpn-virtual-access-pws"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessPws, [], name, value)


            class EvpnVirtualAccessPw(Entity):
                """
                Virtual Access Pseudowire
                
                .. attribute:: neighbor  (key)
                
                	Neighbor IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: pseudowire_id  (key)
                
                	Pseudowire ID
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: evpn_virtual_access_pw_timers
                
                	Enter Virtual Access Pseudowire\-specific timers configuration submode
                	**type**\:  :py:class:`EvpnVirtualAccessPwTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers>`
                
                .. attribute:: evpn_virtual_ethernet_segment
                
                	Enter Ethernet Segment configuration submode
                	**type**\:  :py:class:`EvpnVirtualEthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw, self).__init__()

                    self.yang_name = "evpn-virtual-access-pw"
                    self.yang_parent_name = "evpn-virtual-access-pws"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['neighbor','pseudowire_id']
                    self._child_container_classes = OrderedDict([("evpn-virtual-access-pw-timers", ("evpn_virtual_access_pw_timers", Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers)), ("evpn-virtual-ethernet-segment", ("evpn_virtual_ethernet_segment", Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('neighbor', YLeaf(YType.str, 'neighbor')),
                        ('pseudowire_id', YLeaf(YType.uint32, 'pseudowire-id')),
                    ])
                    self.neighbor = None
                    self.pseudowire_id = None

                    self.evpn_virtual_access_pw_timers = Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers()
                    self.evpn_virtual_access_pw_timers.parent = self
                    self._children_name_map["evpn_virtual_access_pw_timers"] = "evpn-virtual-access-pw-timers"
                    self._children_yang_names.add("evpn-virtual-access-pw-timers")

                    self.evpn_virtual_ethernet_segment = Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment()
                    self.evpn_virtual_ethernet_segment.parent = self
                    self._children_name_map["evpn_virtual_ethernet_segment"] = "evpn-virtual-ethernet-segment"
                    self._children_yang_names.add("evpn-virtual-ethernet-segment")
                    self._segment_path = lambda: "evpn-virtual-access-pw" + "[neighbor='" + str(self.neighbor) + "']" + "[pseudowire-id='" + str(self.pseudowire_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-virtual-access-pws/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw, ['neighbor', 'pseudowire_id'], name, value)


                class EvpnVirtualAccessPwTimers(Entity):
                    """
                    Enter Virtual Access Pseudowire\-specific
                    timers configuration submode
                    
                    .. attribute:: evpn_virtual_access_pw_recovery
                    
                    	Virtual Access Pseudowire\-specific Recovery timer
                    	**type**\: int
                    
                    	**range:** 20..3600
                    
                    	**default value**\: 30
                    
                    .. attribute:: evpn_virtual_access_pw_peering
                    
                    	Virtual Access Pseudowire\-specific Peering timer
                    	**type**\: int
                    
                    	**range:** 0..300
                    
                    	**default value**\: 3
                    
                    .. attribute:: enable
                    
                    	Enable Virtual Access Pseudowire\-specific timers
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evpn_virtual_access_pw_carving
                    
                    	Virtual Access Pseudowire\-specific Carving timer
                    	**type**\: int
                    
                    	**range:** 0..10
                    
                    	**default value**\: 0
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers, self).__init__()

                        self.yang_name = "evpn-virtual-access-pw-timers"
                        self.yang_parent_name = "evpn-virtual-access-pw"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('evpn_virtual_access_pw_recovery', YLeaf(YType.uint32, 'evpn-virtual-access-pw-recovery')),
                            ('evpn_virtual_access_pw_peering', YLeaf(YType.uint32, 'evpn-virtual-access-pw-peering')),
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('evpn_virtual_access_pw_carving', YLeaf(YType.uint32, 'evpn-virtual-access-pw-carving')),
                        ])
                        self.evpn_virtual_access_pw_recovery = None
                        self.evpn_virtual_access_pw_peering = None
                        self.enable = None
                        self.evpn_virtual_access_pw_carving = None
                        self._segment_path = lambda: "evpn-virtual-access-pw-timers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers, ['evpn_virtual_access_pw_recovery', 'evpn_virtual_access_pw_peering', 'enable', 'evpn_virtual_access_pw_carving'], name, value)


                class EvpnVirtualEthernetSegment(Entity):
                    """
                    Enter Ethernet Segment configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Ethernet Segment
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: es_import_route_target
                    
                    	ES\-Import Route Target
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: identifier
                    
                    	Ethernet segment identifier
                    	**type**\:  :py:class:`Identifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.Identifier>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: manual_service_carving
                    
                    	Enter Manual service carving configuration submode
                    	**type**\:  :py:class:`ManualServiceCarving <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment, self).__init__()

                        self.yang_name = "evpn-virtual-ethernet-segment"
                        self.yang_parent_name = "evpn-virtual-access-pw"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("identifier", ("identifier", Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.Identifier)), ("manual-service-carving", ("manual_service_carving", Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('es_import_route_target', YLeaf(YType.str, 'es-import-route-target')),
                        ])
                        self.enable = None
                        self.es_import_route_target = None

                        self.identifier = None
                        self._children_name_map["identifier"] = "identifier"
                        self._children_yang_names.add("identifier")

                        self.manual_service_carving = Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving()
                        self.manual_service_carving.parent = self
                        self._children_name_map["manual_service_carving"] = "manual-service-carving"
                        self._children_yang_names.add("manual-service-carving")
                        self._segment_path = lambda: "evpn-virtual-ethernet-segment"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment, ['enable', 'es_import_route_target'], name, value)


                    class Identifier(Entity):
                        """
                        Ethernet segment identifier
                        
                        .. attribute:: bytes01
                        
                        	Type 0's 1st Byte or Type Byte and 1st Byte
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        .. attribute:: bytes23
                        
                        	2nd and 3rd Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes45
                        
                        	4th and 5th Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes67
                        
                        	6th and 7th Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes89
                        
                        	8th and 9th Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: type
                        
                        	Ethernet segment identifier type
                        	**type**\:  :py:class:`EthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EthernetSegmentIdentifier>`
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.Identifier, self).__init__()

                            self.yang_name = "identifier"
                            self.yang_parent_name = "evpn-virtual-ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('bytes01', YLeaf(YType.str, 'bytes01')),
                                ('bytes23', YLeaf(YType.str, 'bytes23')),
                                ('bytes45', YLeaf(YType.str, 'bytes45')),
                                ('bytes67', YLeaf(YType.str, 'bytes67')),
                                ('bytes89', YLeaf(YType.str, 'bytes89')),
                                ('type', YLeaf(YType.enumeration, 'type')),
                            ])
                            self.bytes01 = None
                            self.bytes23 = None
                            self.bytes45 = None
                            self.bytes67 = None
                            self.bytes89 = None
                            self.type = None
                            self._segment_path = lambda: "identifier"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.Identifier, ['bytes01', 'bytes23', 'bytes45', 'bytes67', 'bytes89', 'type'], name, value)


                    class ManualServiceCarving(Entity):
                        """
                        Enter Manual service carving configuration
                        submode
                        
                        .. attribute:: service_list
                        
                        	Manual service carving primary,secondary lists
                        	**type**\:  :py:class:`ServiceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList>`
                        
                        .. attribute:: enable
                        
                        	Enable Manual service carving
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving, self).__init__()

                            self.yang_name = "manual-service-carving"
                            self.yang_parent_name = "evpn-virtual-ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("service-list", ("service_list", Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', YLeaf(YType.empty, 'enable')),
                            ])
                            self.enable = None

                            self.service_list = Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList()
                            self.service_list.parent = self
                            self._children_name_map["service_list"] = "service-list"
                            self._children_yang_names.add("service-list")
                            self._segment_path = lambda: "manual-service-carving"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving, ['enable'], name, value)


                        class ServiceList(Entity):
                            """
                            Manual service carving primary,secondary lists
                            
                            .. attribute:: primary
                            
                            	Primary services list
                            	**type**\: str
                            
                            	**length:** 1..150
                            
                            .. attribute:: secondary
                            
                            	Secondary services list
                            	**type**\: str
                            
                            	**length:** 1..150
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList, self).__init__()

                                self.yang_name = "service-list"
                                self.yang_parent_name = "manual-service-carving"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('primary', YLeaf(YType.str, 'primary')),
                                    ('secondary', YLeaf(YType.str, 'secondary')),
                                ])
                                self.primary = None
                                self.secondary = None
                                self._segment_path = lambda: "service-list"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList, ['primary', 'secondary'], name, value)


        class EvpnEthernetSegment(Entity):
            """
            EVPN Global Ethernet Segment submode
            
            .. attribute:: evpn_esi_types
            
            	EVPN ESI type table
            	**type**\:  :py:class:`EvpnEsiTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes>`
            
            .. attribute:: enable
            
            	Enable EVPN Global Ethernet Segment submode
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnEthernetSegment, self).__init__()

                self.yang_name = "evpn-ethernet-segment"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("evpn-esi-types", ("evpn_esi_types", Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', YLeaf(YType.empty, 'enable')),
                ])
                self.enable = None

                self.evpn_esi_types = Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes()
                self.evpn_esi_types.parent = self
                self._children_name_map["evpn_esi_types"] = "evpn-esi-types"
                self._children_yang_names.add("evpn-esi-types")
                self._segment_path = lambda: "evpn-ethernet-segment"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnEthernetSegment, ['enable'], name, value)


            class EvpnEsiTypes(Entity):
                """
                EVPN ESI type table
                
                .. attribute:: evpn_esi_type
                
                	ESI type
                	**type**\: list of  		 :py:class:`EvpnEsiType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes.EvpnEsiType>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes, self).__init__()

                    self.yang_name = "evpn-esi-types"
                    self.yang_parent_name = "evpn-ethernet-segment"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("evpn-esi-type", ("evpn_esi_type", Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes.EvpnEsiType))])
                    self._leafs = OrderedDict()

                    self.evpn_esi_type = YList(self)
                    self._segment_path = lambda: "evpn-esi-types"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-ethernet-segment/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes, [], name, value)


                class EvpnEsiType(Entity):
                    """
                    ESI type
                    
                    .. attribute:: esi_type  (key)
                    
                    	ESI type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: disable_auto_generation
                    
                    	Disable ESI Autogeneration
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes.EvpnEsiType, self).__init__()

                        self.yang_name = "evpn-esi-type"
                        self.yang_parent_name = "evpn-esi-types"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['esi_type']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('esi_type', YLeaf(YType.uint32, 'esi-type')),
                            ('disable_auto_generation', YLeaf(YType.empty, 'disable-auto-generation')),
                        ])
                        self.esi_type = None
                        self.disable_auto_generation = None
                        self._segment_path = lambda: "evpn-esi-type" + "[esi-type='" + str(self.esi_type) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-ethernet-segment/evpn-esi-types/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes.EvpnEsiType, ['esi_type', 'disable_auto_generation'], name, value)

    def clone_ptr(self):
        self._top_entity = Evpn()
        return self._top_entity

