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
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BackupDisable(Enum):
    """
    BackupDisable

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
    BdmacLearn

    Bdmac learn

    .. data:: disable_learning = 2

    	Disable Learning

    """

    disable_learning = Enum.YLeaf(2, "disable-learning")


class BgpRouteDistinguisher(Enum):
    """
    BgpRouteDistinguisher

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
    BgpRouteTarget

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
    BgpRouteTargetFormat

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
    BgpRouteTargetRole

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
    BridgeDomainTransportMode

    Bridge domain transport mode

    .. data:: vlan_passthrough = 3

    	Vlan tagged passthrough mode

    """

    vlan_passthrough = Enum.YLeaf(3, "vlan-passthrough")


class ControlWord(Enum):
    """
    ControlWord

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
    ErpPort

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
    ErpPort1

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
    Erpaps

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
    EthernetSegmentIdentifier

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
    EvpnEncapsulation

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
    EvpnSide

    Evpn side

    .. data:: evpn_side_stitching = 2

    	EVPN Instance side defined as stitching

    """

    evpn_side_stitching = Enum.YLeaf(2, "evpn-side-stitching")


class FlowLabelLoadBalance(Enum):
    """
    FlowLabelLoadBalance

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
    FlowLabelTlvCode

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
    InterfaceProfile

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
    InterfaceTrafficFlood

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
    Interworking

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
    L2Encapsulation

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
    L2tpCookieSize

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
    L2tpSignalingProtocol

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
    L2tpv3Sequencing

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
    L2vpnCapabilityMode

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
    L2vpnLogging

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
    L2vpnVerification

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
    LdpVplsId

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
    LoadBalance

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
    MacAging

    Mac aging

    .. data:: absolute = 1

    	Absolute aging type

    .. data:: inactivity = 2

    	Inactivity aging type

    """

    absolute = Enum.YLeaf(1, "absolute")

    inactivity = Enum.YLeaf(2, "inactivity")


class MacLearn(Enum):
    """
    MacLearn

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
    MacLimitAction

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
    MacNotification

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
    MacSecureAction

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
    MacWithdrawBehavior

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
    MplsSequencing

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
    MplsSignalingProtocol

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
    PortDownFlush

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
    PreferredPath

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
    PwSwitchingPointTlv

    Pw switching point tlv

    .. data:: hide = 2

    	Hide TLV

    """

    hide = Enum.YLeaf(2, "hide")


class RplRole(Enum):
    """
    RplRole

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
    StormControl

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
    TransportMode

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
    TypeOfServiceMode

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
    VccvVerification

    Vccv verification

    .. data:: none = 0

    	No connectivity verification over VCCV

    .. data:: lsp_ping = 2

    	LSP Ping over VCCV

    """

    none = Enum.YLeaf(0, "none")

    lsp_ping = Enum.YLeaf(2, "lsp-ping")



class Evpn(Entity):
    """
    evpn
    
    .. attribute:: enable
    
    	Enable EVPN feature
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: evpn_tables
    
    	EVPN submodes
    	**type**\:   :py:class:`EvpnTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables>`
    
    

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
        self._child_container_classes = {"evpn-tables" : ("evpn_tables", Evpn.EvpnTables)}
        self._child_list_classes = {}

        self.enable = YLeaf(YType.empty, "enable")

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
        
        .. attribute:: evi_cost_out
        
        	Configure node to cost\-out
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: evpn_bgp_auto_discovery
        
        	Enable Autodiscovery BGP in EVPN
        	**type**\:   :py:class:`EvpnBgpAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnBgpAutoDiscovery>`
        
        .. attribute:: evpn_cost_in_startup
        
        	Cost\-in node after given time (seconds) on startup timer
        	**type**\:  int
        
        	**range:** 30..86400
        
        	**units**\: second
        
        .. attribute:: evpn_ethernet_segment
        
        	EVPN Global Ethernet Segment submode
        	**type**\:   :py:class:`EvpnEthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnEthernetSegment>`
        
        .. attribute:: evpn_instances
        
        	Enter EVPN Instance configuration submode
        	**type**\:   :py:class:`EvpnInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances>`
        
        .. attribute:: evpn_interfaces
        
        	Attachment Circuit interfaces
        	**type**\:   :py:class:`EvpnInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces>`
        
        .. attribute:: evpn_load_balancing
        
        	Enter EVPN Loadbalancing configuration submode
        	**type**\:   :py:class:`EvpnLoadBalancing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnLoadBalancing>`
        
        .. attribute:: evpn_logging
        
        	Enter EVPN Logging configuration submode
        	**type**\:   :py:class:`EvpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnLogging>`
        
        .. attribute:: evpn_source_interface
        
        	Configure EVPN router\-id implicitly through Loopback Interface
        	**type**\:  str
        
        	**pattern:** [a\-zA\-Z0\-9./\-]+
        
        .. attribute:: evpn_timers
        
        	Enter EVPN timers configuration submode
        	**type**\:   :py:class:`EvpnTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnTimers>`
        
        .. attribute:: evpn_virtual_access_pws
        
        	Virtual Access Pseudowire interfaces
        	**type**\:   :py:class:`EvpnVirtualAccessPws <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws>`
        
        .. attribute:: evpn_virtual_access_vfis
        
        	Virtual Access VFI interfaces
        	**type**\:   :py:class:`EvpnVirtualAccessVfis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis>`
        
        .. attribute:: evpnevis
        
        	Enter EVPN Instance configuration submode
        	**type**\:   :py:class:`Evpnevis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis>`
        
        .. attribute:: evpnmac
        
        	EVPN MAC Configuration
        	**type**\:   :py:class:`Evpnmac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnmac>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(Evpn.EvpnTables, self).__init__()

            self.yang_name = "evpn-tables"
            self.yang_parent_name = "evpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"evpn-bgp-auto-discovery" : ("evpn_bgp_auto_discovery", Evpn.EvpnTables.EvpnBgpAutoDiscovery), "evpn-ethernet-segment" : ("evpn_ethernet_segment", Evpn.EvpnTables.EvpnEthernetSegment), "evpn-instances" : ("evpn_instances", Evpn.EvpnTables.EvpnInstances), "evpn-interfaces" : ("evpn_interfaces", Evpn.EvpnTables.EvpnInterfaces), "evpn-load-balancing" : ("evpn_load_balancing", Evpn.EvpnTables.EvpnLoadBalancing), "evpn-logging" : ("evpn_logging", Evpn.EvpnTables.EvpnLogging), "evpn-timers" : ("evpn_timers", Evpn.EvpnTables.EvpnTimers), "evpn-virtual-access-pws" : ("evpn_virtual_access_pws", Evpn.EvpnTables.EvpnVirtualAccessPws), "evpn-virtual-access-vfis" : ("evpn_virtual_access_vfis", Evpn.EvpnTables.EvpnVirtualAccessVfis), "evpnevis" : ("evpnevis", Evpn.EvpnTables.Evpnevis), "evpnmac" : ("evpnmac", Evpn.EvpnTables.Evpnmac)}
            self._child_list_classes = {}

            self.evi_cost_out = YLeaf(YType.empty, "evi-cost-out")

            self.evpn_cost_in_startup = YLeaf(YType.uint32, "evpn-cost-in-startup")

            self.evpn_source_interface = YLeaf(YType.str, "evpn-source-interface")

            self.evpn_bgp_auto_discovery = Evpn.EvpnTables.EvpnBgpAutoDiscovery()
            self.evpn_bgp_auto_discovery.parent = self
            self._children_name_map["evpn_bgp_auto_discovery"] = "evpn-bgp-auto-discovery"
            self._children_yang_names.add("evpn-bgp-auto-discovery")

            self.evpn_ethernet_segment = Evpn.EvpnTables.EvpnEthernetSegment()
            self.evpn_ethernet_segment.parent = self
            self._children_name_map["evpn_ethernet_segment"] = "evpn-ethernet-segment"
            self._children_yang_names.add("evpn-ethernet-segment")

            self.evpn_instances = Evpn.EvpnTables.EvpnInstances()
            self.evpn_instances.parent = self
            self._children_name_map["evpn_instances"] = "evpn-instances"
            self._children_yang_names.add("evpn-instances")

            self.evpn_interfaces = Evpn.EvpnTables.EvpnInterfaces()
            self.evpn_interfaces.parent = self
            self._children_name_map["evpn_interfaces"] = "evpn-interfaces"
            self._children_yang_names.add("evpn-interfaces")

            self.evpn_load_balancing = Evpn.EvpnTables.EvpnLoadBalancing()
            self.evpn_load_balancing.parent = self
            self._children_name_map["evpn_load_balancing"] = "evpn-load-balancing"
            self._children_yang_names.add("evpn-load-balancing")

            self.evpn_logging = Evpn.EvpnTables.EvpnLogging()
            self.evpn_logging.parent = self
            self._children_name_map["evpn_logging"] = "evpn-logging"
            self._children_yang_names.add("evpn-logging")

            self.evpn_timers = Evpn.EvpnTables.EvpnTimers()
            self.evpn_timers.parent = self
            self._children_name_map["evpn_timers"] = "evpn-timers"
            self._children_yang_names.add("evpn-timers")

            self.evpn_virtual_access_pws = Evpn.EvpnTables.EvpnVirtualAccessPws()
            self.evpn_virtual_access_pws.parent = self
            self._children_name_map["evpn_virtual_access_pws"] = "evpn-virtual-access-pws"
            self._children_yang_names.add("evpn-virtual-access-pws")

            self.evpn_virtual_access_vfis = Evpn.EvpnTables.EvpnVirtualAccessVfis()
            self.evpn_virtual_access_vfis.parent = self
            self._children_name_map["evpn_virtual_access_vfis"] = "evpn-virtual-access-vfis"
            self._children_yang_names.add("evpn-virtual-access-vfis")

            self.evpnevis = Evpn.EvpnTables.Evpnevis()
            self.evpnevis.parent = self
            self._children_name_map["evpnevis"] = "evpnevis"
            self._children_yang_names.add("evpnevis")

            self.evpnmac = Evpn.EvpnTables.Evpnmac()
            self.evpnmac.parent = self
            self._children_name_map["evpnmac"] = "evpnmac"
            self._children_yang_names.add("evpnmac")
            self._segment_path = lambda: "evpn-tables"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Evpn.EvpnTables, ['evi_cost_out', 'evpn_cost_in_startup', 'evpn_source_interface'], name, value)


        class EvpnBgpAutoDiscovery(Entity):
            """
            Enable Autodiscovery BGP in EVPN
            
            .. attribute:: enable
            
            	Enable Autodiscovery BGP
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: evpn_route_distinguisher
            
            	Route Distinguisher
            	**type**\:   :py:class:`EvpnRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnBgpAutoDiscovery.EvpnRouteDistinguisher>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnBgpAutoDiscovery, self).__init__()

                self.yang_name = "evpn-bgp-auto-discovery"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"evpn-route-distinguisher" : ("evpn_route_distinguisher", Evpn.EvpnTables.EvpnBgpAutoDiscovery.EvpnRouteDistinguisher)}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

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
                
                .. attribute:: addr_index
                
                	Addr index
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: address
                
                	IPV4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: as_
                
                	Two byte or 4 byte AS number
                	**type**\:  int
                
                	**range:** 1..4294967295
                
                .. attribute:: as_index
                
                	AS\:nn (hex or decimal format)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Router Distinguisher Type
                	**type**\:   :py:class:`BgpRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.EvpnBgpAutoDiscovery.EvpnRouteDistinguisher, self).__init__()

                    self.yang_name = "evpn-route-distinguisher"
                    self.yang_parent_name = "evpn-bgp-auto-discovery"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.addr_index = YLeaf(YType.uint32, "addr-index")

                    self.address = YLeaf(YType.str, "address")

                    self.as_ = YLeaf(YType.uint32, "as")

                    self.as_index = YLeaf(YType.uint32, "as-index")

                    self.type = YLeaf(YType.enumeration, "type")
                    self._segment_path = lambda: "evpn-route-distinguisher"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-bgp-auto-discovery/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.EvpnBgpAutoDiscovery.EvpnRouteDistinguisher, ['addr_index', 'address', 'as_', 'as_index', 'type'], name, value)


        class EvpnEthernetSegment(Entity):
            """
            EVPN Global Ethernet Segment submode
            
            .. attribute:: enable
            
            	Enable EVPN Global Ethernet Segment submode
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: evpn_esi_types
            
            	EVPN ESI type table
            	**type**\:   :py:class:`EvpnEsiTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnEthernetSegment, self).__init__()

                self.yang_name = "evpn-ethernet-segment"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"evpn-esi-types" : ("evpn_esi_types", Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes)}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

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
                	**type**\: list of    :py:class:`EvpnEsiType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes.EvpnEsiType>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes, self).__init__()

                    self.yang_name = "evpn-esi-types"
                    self.yang_parent_name = "evpn-ethernet-segment"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"evpn-esi-type" : ("evpn_esi_type", Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes.EvpnEsiType)}

                    self.evpn_esi_type = YList(self)
                    self._segment_path = lambda: "evpn-esi-types"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-ethernet-segment/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes, [], name, value)


                class EvpnEsiType(Entity):
                    """
                    ESI type
                    
                    .. attribute:: esi_type  <key>
                    
                    	ESI type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: disable_auto_generation
                    
                    	Disable ESI Autogeneration
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes.EvpnEsiType, self).__init__()

                        self.yang_name = "evpn-esi-type"
                        self.yang_parent_name = "evpn-esi-types"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.esi_type = YLeaf(YType.uint32, "esi-type")

                        self.disable_auto_generation = YLeaf(YType.empty, "disable-auto-generation")
                        self._segment_path = lambda: "evpn-esi-type" + "[esi-type='" + self.esi_type.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-ethernet-segment/evpn-esi-types/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnEthernetSegment.EvpnEsiTypes.EvpnEsiType, ['esi_type', 'disable_auto_generation'], name, value)


        class EvpnInstances(Entity):
            """
            Enter EVPN Instance configuration submode
            
            .. attribute:: evpn_instance
            
            	Enter EVPN Instance configuration submode
            	**type**\: list of    :py:class:`EvpnInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnInstances, self).__init__()

                self.yang_name = "evpn-instances"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"evpn-instance" : ("evpn_instance", Evpn.EvpnTables.EvpnInstances.EvpnInstance)}

                self.evpn_instance = YList(self)
                self._segment_path = lambda: "evpn-instances"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnInstances, [], name, value)


            class EvpnInstance(Entity):
                """
                Enter EVPN Instance configuration submode
                
                .. attribute:: eviid  <key>
                
                	EVPN Instance ID
                	**type**\:  int
                
                	**range:** 1..65534
                
                .. attribute:: encapsulation  <key>
                
                	EVPN Instance Encapsulation
                	**type**\:   :py:class:`EvpnEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EvpnEncapsulation>`
                
                .. attribute:: side  <key>
                
                	EVPN Instance Side
                	**type**\:   :py:class:`EvpnSide <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EvpnSide>`
                
                .. attribute:: evi_advertise_mac_deprecated
                
                	DEPRECATED\: Advertise local MAC\-only and BVI MAC routes
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evi_reorig_disable
                
                	Disable route re\-origination
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evi_unknown_unicast_flooding_disable
                
                	Disable Unknown Unicast Flooding on this EVI
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evpn_evi_cw_disable
                
                	CW disable for EVPN EVI
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evpn_instance_advertise_mac
                
                	Enter Advertise local MAC\-only routes configuration submode
                	**type**\:   :py:class:`EvpnInstanceAdvertiseMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceAdvertiseMac>`
                
                .. attribute:: evpn_instance_bgp_auto_discovery
                
                	Enable Autodiscovery BGP in EVPN Instance
                	**type**\:   :py:class:`EvpnInstanceBgpAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery>`
                
                .. attribute:: evpn_instance_load_balancing
                
                	Enter Loadbalancing configuration submode
                	**type**\:   :py:class:`EvpnInstanceLoadBalancing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceLoadBalancing>`
                
                .. attribute:: evpnevi_description
                
                	EVPN Instance description
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.EvpnInstances.EvpnInstance, self).__init__()

                    self.yang_name = "evpn-instance"
                    self.yang_parent_name = "evpn-instances"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"evpn-instance-advertise-mac" : ("evpn_instance_advertise_mac", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceAdvertiseMac), "evpn-instance-bgp-auto-discovery" : ("evpn_instance_bgp_auto_discovery", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery), "evpn-instance-load-balancing" : ("evpn_instance_load_balancing", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceLoadBalancing)}
                    self._child_list_classes = {}

                    self.eviid = YLeaf(YType.uint32, "eviid")

                    self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                    self.side = YLeaf(YType.enumeration, "side")

                    self.evi_advertise_mac_deprecated = YLeaf(YType.empty, "evi-advertise-mac-deprecated")

                    self.evi_reorig_disable = YLeaf(YType.empty, "evi-reorig-disable")

                    self.evi_unknown_unicast_flooding_disable = YLeaf(YType.empty, "evi-unknown-unicast-flooding-disable")

                    self.evpn_evi_cw_disable = YLeaf(YType.empty, "evpn-evi-cw-disable")

                    self.evpnevi_description = YLeaf(YType.str, "evpnevi-description")

                    self.evpn_instance_advertise_mac = Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceAdvertiseMac()
                    self.evpn_instance_advertise_mac.parent = self
                    self._children_name_map["evpn_instance_advertise_mac"] = "evpn-instance-advertise-mac"
                    self._children_yang_names.add("evpn-instance-advertise-mac")

                    self.evpn_instance_bgp_auto_discovery = Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery()
                    self.evpn_instance_bgp_auto_discovery.parent = self
                    self._children_name_map["evpn_instance_bgp_auto_discovery"] = "evpn-instance-bgp-auto-discovery"
                    self._children_yang_names.add("evpn-instance-bgp-auto-discovery")

                    self.evpn_instance_load_balancing = Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceLoadBalancing()
                    self.evpn_instance_load_balancing.parent = self
                    self._children_name_map["evpn_instance_load_balancing"] = "evpn-instance-load-balancing"
                    self._children_yang_names.add("evpn-instance-load-balancing")
                    self._segment_path = lambda: "evpn-instance" + "[eviid='" + self.eviid.get() + "']" + "[encapsulation='" + self.encapsulation.get() + "']" + "[side='" + self.side.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-instances/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance, ['eviid', 'encapsulation', 'side', 'evi_advertise_mac_deprecated', 'evi_reorig_disable', 'evi_unknown_unicast_flooding_disable', 'evpn_evi_cw_disable', 'evpnevi_description'], name, value)


                class EvpnInstanceAdvertiseMac(Entity):
                    """
                    Enter Advertise local MAC\-only routes
                    configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Advertise local MAC\-only routes
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evi_advertise_mac_bvi
                    
                    	Advertise local MAC\-only and BVI MAC routes
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceAdvertiseMac, self).__init__()

                        self.yang_name = "evpn-instance-advertise-mac"
                        self.yang_parent_name = "evpn-instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.empty, "enable")

                        self.evi_advertise_mac_bvi = YLeaf(YType.empty, "evi-advertise-mac-bvi")
                        self._segment_path = lambda: "evpn-instance-advertise-mac"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceAdvertiseMac, ['enable', 'evi_advertise_mac_bvi'], name, value)


                class EvpnInstanceBgpAutoDiscovery(Entity):
                    """
                    Enable Autodiscovery BGP in EVPN Instance
                    
                    .. attribute:: enable
                    
                    	Enable Autodiscovery BGP
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evpn_route_distinguisher
                    
                    	Route Distinguisher
                    	**type**\:   :py:class:`EvpnRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteDistinguisher>`
                    
                    .. attribute:: evpn_route_targets
                    
                    	Route Target
                    	**type**\:   :py:class:`EvpnRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets>`
                    
                    .. attribute:: table_policy
                    
                    	Table Policy for installation of forwarding data to L2FIB
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery, self).__init__()

                        self.yang_name = "evpn-instance-bgp-auto-discovery"
                        self.yang_parent_name = "evpn-instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"evpn-route-distinguisher" : ("evpn_route_distinguisher", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteDistinguisher), "evpn-route-targets" : ("evpn_route_targets", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets)}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.empty, "enable")

                        self.table_policy = YLeaf(YType.str, "table-policy")

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
                        
                        .. attribute:: addr_index
                        
                        	Addr index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: address
                        
                        	IPV4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: as_
                        
                        	Two byte or 4 byte AS number
                        	**type**\:  int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: as_index
                        
                        	AS\:nn (hex or decimal format)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Router Distinguisher Type
                        	**type**\:   :py:class:`BgpRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteDistinguisher, self).__init__()

                            self.yang_name = "evpn-route-distinguisher"
                            self.yang_parent_name = "evpn-instance-bgp-auto-discovery"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.addr_index = YLeaf(YType.uint32, "addr-index")

                            self.address = YLeaf(YType.str, "address")

                            self.as_ = YLeaf(YType.uint32, "as")

                            self.as_index = YLeaf(YType.uint32, "as-index")

                            self.type = YLeaf(YType.enumeration, "type")
                            self._segment_path = lambda: "evpn-route-distinguisher"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteDistinguisher, ['addr_index', 'address', 'as_', 'as_index', 'type'], name, value)


                    class EvpnRouteTargets(Entity):
                        """
                        Route Target
                        
                        .. attribute:: evpn_route_target_as
                        
                        	Name of the Route Target
                        	**type**\: list of    :py:class:`EvpnRouteTargetAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs>`
                        
                        .. attribute:: evpn_route_target_ipv4_address
                        
                        	Name of the Route Target
                        	**type**\: list of    :py:class:`EvpnRouteTargetIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address>`
                        
                        .. attribute:: evpn_route_target_none
                        
                        	Name of the Route Target
                        	**type**\: list of    :py:class:`EvpnRouteTargetNone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets, self).__init__()

                            self.yang_name = "evpn-route-targets"
                            self.yang_parent_name = "evpn-instance-bgp-auto-discovery"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"evpn-route-target-as" : ("evpn_route_target_as", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs), "evpn-route-target-ipv4-address" : ("evpn_route_target_ipv4_address", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address), "evpn-route-target-none" : ("evpn_route_target_none", Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone)}

                            self.evpn_route_target_as = YList(self)
                            self.evpn_route_target_ipv4_address = YList(self)
                            self.evpn_route_target_none = YList(self)
                            self._segment_path = lambda: "evpn-route-targets"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets, [], name, value)


                        class EvpnRouteTargetAs(Entity):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  <key>
                            
                            	Format of the route target
                            	**type**\:   :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                            
                            .. attribute:: role  <key>
                            
                            	Role of the router target type
                            	**type**\:   :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                            
                            .. attribute:: as_  <key>
                            
                            	Two byte or 4 byte AS number
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: as_index  <key>
                            
                            	AS\:nn (hex or decimal format)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stitching  <key>
                            
                            	whether RT is Stitching RT
                            	**type**\:   :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTarget>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs, self).__init__()

                                self.yang_name = "evpn-route-target-as"
                                self.yang_parent_name = "evpn-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.format = YLeaf(YType.enumeration, "format")

                                self.role = YLeaf(YType.enumeration, "role")

                                self.as_ = YLeaf(YType.uint32, "as")

                                self.as_index = YLeaf(YType.uint32, "as-index")

                                self.stitching = YLeaf(YType.enumeration, "stitching")
                                self._segment_path = lambda: "evpn-route-target-as" + "[format='" + self.format.get() + "']" + "[role='" + self.role.get() + "']" + "[as='" + self.as_.get() + "']" + "[as-index='" + self.as_index.get() + "']" + "[stitching='" + self.stitching.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs, ['format', 'role', 'as_', 'as_index', 'stitching'], name, value)


                        class EvpnRouteTargetIpv4Address(Entity):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  <key>
                            
                            	Format of the route target
                            	**type**\:   :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                            
                            .. attribute:: role  <key>
                            
                            	Role of the router target type
                            	**type**\:   :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                            
                            .. attribute:: address  <key>
                            
                            	IPV4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: addr_index  <key>
                            
                            	Addr index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: stitching  <key>
                            
                            	whether RT is Stitching RT
                            	**type**\:   :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTarget>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address, self).__init__()

                                self.yang_name = "evpn-route-target-ipv4-address"
                                self.yang_parent_name = "evpn-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.format = YLeaf(YType.enumeration, "format")

                                self.role = YLeaf(YType.enumeration, "role")

                                self.address = YLeaf(YType.str, "address")

                                self.addr_index = YLeaf(YType.uint32, "addr-index")

                                self.stitching = YLeaf(YType.enumeration, "stitching")
                                self._segment_path = lambda: "evpn-route-target-ipv4-address" + "[format='" + self.format.get() + "']" + "[role='" + self.role.get() + "']" + "[address='" + self.address.get() + "']" + "[addr-index='" + self.addr_index.get() + "']" + "[stitching='" + self.stitching.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address, ['format', 'role', 'address', 'addr_index', 'stitching'], name, value)


                        class EvpnRouteTargetNone(Entity):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  <key>
                            
                            	Format of the route target
                            	**type**\:   :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                            
                            .. attribute:: role  <key>
                            
                            	Role of the router target type
                            	**type**\:   :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                            
                            .. attribute:: stitching  <key>
                            
                            	whether RT is Stitching RT
                            	**type**\:   :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTarget>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone, self).__init__()

                                self.yang_name = "evpn-route-target-none"
                                self.yang_parent_name = "evpn-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.format = YLeaf(YType.enumeration, "format")

                                self.role = YLeaf(YType.enumeration, "role")

                                self.stitching = YLeaf(YType.enumeration, "stitching")
                                self._segment_path = lambda: "evpn-route-target-none" + "[format='" + self.format.get() + "']" + "[role='" + self.role.get() + "']" + "[stitching='" + self.stitching.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceBgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone, ['format', 'role', 'stitching'], name, value)


                class EvpnInstanceLoadBalancing(Entity):
                    """
                    Enter Loadbalancing configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Loadbalancing
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evi_flow_label
                    
                    	Enable Flow Label based load balancing
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceLoadBalancing, self).__init__()

                        self.yang_name = "evpn-instance-load-balancing"
                        self.yang_parent_name = "evpn-instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.empty, "enable")

                        self.evi_flow_label = YLeaf(YType.empty, "evi-flow-label")
                        self._segment_path = lambda: "evpn-instance-load-balancing"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnInstances.EvpnInstance.EvpnInstanceLoadBalancing, ['enable', 'evi_flow_label'], name, value)


        class EvpnInterfaces(Entity):
            """
            Attachment Circuit interfaces
            
            .. attribute:: evpn_interface
            
            	Attachment circuit interface
            	**type**\: list of    :py:class:`EvpnInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnInterfaces, self).__init__()

                self.yang_name = "evpn-interfaces"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"evpn-interface" : ("evpn_interface", Evpn.EvpnTables.EvpnInterfaces.EvpnInterface)}

                self.evpn_interface = YList(self)
                self._segment_path = lambda: "evpn-interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces, [], name, value)


            class EvpnInterface(Entity):
                """
                Attachment circuit interface
                
                .. attribute:: interface_name  <key>
                
                	Name of the attachment circuit interface
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: ethernet_segment
                
                	Enter Ethernet Segment configuration submode
                	**type**\:   :py:class:`EthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment>`
                
                .. attribute:: evpnac_timers
                
                	Enter Interface\-specific timers configuration submode
                	**type**\:   :py:class:`EvpnacTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers>`
                
                .. attribute:: mac_flush
                
                	Enable MVRP MAC Flush mode
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface, self).__init__()

                    self.yang_name = "evpn-interface"
                    self.yang_parent_name = "evpn-interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"ethernet-segment" : ("ethernet_segment", Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment), "evpnac-timers" : ("evpnac_timers", Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers)}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.mac_flush = YLeaf(YType.empty, "mac-flush")

                    self.ethernet_segment = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment()
                    self.ethernet_segment.parent = self
                    self._children_name_map["ethernet_segment"] = "ethernet-segment"
                    self._children_yang_names.add("ethernet-segment")

                    self.evpnac_timers = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers()
                    self.evpnac_timers.parent = self
                    self._children_name_map["evpnac_timers"] = "evpnac-timers"
                    self._children_yang_names.add("evpnac-timers")
                    self._segment_path = lambda: "evpn-interface" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface, ['interface_name', 'mac_flush'], name, value)


                class EthernetSegment(Entity):
                    """
                    Enter Ethernet Segment configuration submode
                    
                    .. attribute:: backbone_source_mac
                    
                    	Backbone Source MAC
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: enable
                    
                    	Enable Ethernet Segment
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: es_import_route_target
                    
                    	ES\-Import Route Target
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: force_single_homed
                    
                    	Force ethernet segment to remain single\-homed
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: identifier
                    
                    	Ethernet segment identifier
                    	**type**\:   :py:class:`Identifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.Identifier>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: load_balancing_single_active
                    
                    	Enable single\-active load balancing mode
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: manual_service_carving
                    
                    	Enter Manual service carving configuration submode
                    	**type**\:   :py:class:`ManualServiceCarving <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment, self).__init__()

                        self.yang_name = "ethernet-segment"
                        self.yang_parent_name = "evpn-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"identifier" : ("identifier", Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.Identifier), "manual-service-carving" : ("manual_service_carving", Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving)}
                        self._child_list_classes = {}

                        self.backbone_source_mac = YLeaf(YType.str, "backbone-source-mac")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.es_import_route_target = YLeaf(YType.str, "es-import-route-target")

                        self.force_single_homed = YLeaf(YType.empty, "force-single-homed")

                        self.load_balancing_single_active = YLeaf(YType.empty, "load-balancing-single-active")

                        self.identifier = None
                        self._children_name_map["identifier"] = "identifier"
                        self._children_yang_names.add("identifier")

                        self.manual_service_carving = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving()
                        self.manual_service_carving.parent = self
                        self._children_name_map["manual_service_carving"] = "manual-service-carving"
                        self._children_yang_names.add("manual-service-carving")
                        self._segment_path = lambda: "ethernet-segment"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment, ['backbone_source_mac', 'enable', 'es_import_route_target', 'force_single_homed', 'load_balancing_single_active'], name, value)


                    class Identifier(Entity):
                        """
                        Ethernet segment identifier
                        
                        .. attribute:: bytes01
                        
                        	Type 0's 1st Byte or Type Byte and 1st Byte
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        .. attribute:: bytes23
                        
                        	2nd and 3rd Bytes
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes45
                        
                        	4th and 5th Bytes
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes67
                        
                        	6th and 7th Bytes
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes89
                        
                        	8th and 9th Bytes
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: type
                        
                        	Ethernet segment identifier type
                        	**type**\:   :py:class:`EthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EthernetSegmentIdentifier>`
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.bytes01 = YLeaf(YType.str, "bytes01")

                            self.bytes23 = YLeaf(YType.str, "bytes23")

                            self.bytes45 = YLeaf(YType.str, "bytes45")

                            self.bytes67 = YLeaf(YType.str, "bytes67")

                            self.bytes89 = YLeaf(YType.str, "bytes89")

                            self.type = YLeaf(YType.enumeration, "type")
                            self._segment_path = lambda: "identifier"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.Identifier, ['bytes01', 'bytes23', 'bytes45', 'bytes67', 'bytes89', 'type'], name, value)


                    class ManualServiceCarving(Entity):
                        """
                        Enter Manual service carving configuration
                        submode
                        
                        .. attribute:: enable
                        
                        	Enable Manual service carving
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: service_list
                        
                        	Manual service carving primary,secondary lists
                        	**type**\:   :py:class:`ServiceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving.ServiceList>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving, self).__init__()

                            self.yang_name = "manual-service-carving"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"service-list" : ("service_list", Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving.ServiceList)}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")

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
                            	**type**\:  str
                            
                            	**length:** 1..150
                            
                            .. attribute:: secondary
                            
                            	Secondary services list
                            	**type**\:  str
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.primary = YLeaf(YType.str, "primary")

                                self.secondary = YLeaf(YType.str, "secondary")
                                self._segment_path = lambda: "service-list"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving.ServiceList, ['primary', 'secondary'], name, value)


                class EvpnacTimers(Entity):
                    """
                    Enter Interface\-specific timers configuration
                    submode
                    
                    .. attribute:: enable
                    
                    	Enable Interface\-specific timers
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evpnac_peering
                    
                    	Interface\-specific Peering timer
                    	**type**\:  int
                    
                    	**range:** 0..300
                    
                    	**default value**\: 3
                    
                    .. attribute:: evpnac_recovery
                    
                    	Interface\-specific Recovery timer
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.empty, "enable")

                        self.evpnac_peering = YLeaf(YType.uint32, "evpnac-peering")

                        self.evpnac_recovery = YLeaf(YType.uint32, "evpnac-recovery")
                        self._segment_path = lambda: "evpnac-timers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers, ['enable', 'evpnac_peering', 'evpnac_recovery'], name, value)


        class EvpnLoadBalancing(Entity):
            """
            Enter EVPN Loadbalancing configuration submode
            
            .. attribute:: enable
            
            	Enable EVPN Loadbalancing
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: evpn_flow_label
            
            	Enable Flow Label based load balancing
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnLoadBalancing, self).__init__()

                self.yang_name = "evpn-load-balancing"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

                self.evpn_flow_label = YLeaf(YType.empty, "evpn-flow-label")
                self._segment_path = lambda: "evpn-load-balancing"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnLoadBalancing, ['enable', 'evpn_flow_label'], name, value)


        class EvpnLogging(Entity):
            """
            Enter EVPN Logging configuration submode
            
            .. attribute:: enable
            
            	Enable EVPN Logging
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: evpn_df_election
            
            	Enable Designated Forwarder election logging
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnLogging, self).__init__()

                self.yang_name = "evpn-logging"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

                self.evpn_df_election = YLeaf(YType.empty, "evpn-df-election")
                self._segment_path = lambda: "evpn-logging"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnLogging, ['enable', 'evpn_df_election'], name, value)


        class EvpnTimers(Entity):
            """
            Enter EVPN timers configuration submode
            
            .. attribute:: enable
            
            	Enable EVPN timers
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: evpn_peering
            
            	Global Peering timer
            	**type**\:  int
            
            	**range:** 0..300
            
            	**default value**\: 3
            
            .. attribute:: evpn_recovery
            
            	Global Recovery timer
            	**type**\:  int
            
            	**range:** 20..3600
            
            	**default value**\: 30
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnTimers, self).__init__()

                self.yang_name = "evpn-timers"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

                self.evpn_peering = YLeaf(YType.uint32, "evpn-peering")

                self.evpn_recovery = YLeaf(YType.uint32, "evpn-recovery")
                self._segment_path = lambda: "evpn-timers"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnTimers, ['enable', 'evpn_peering', 'evpn_recovery'], name, value)


        class EvpnVirtualAccessPws(Entity):
            """
            Virtual Access Pseudowire interfaces
            
            .. attribute:: evpn_virtual_access_pw
            
            	Virtual Access Pseudowire
            	**type**\: list of    :py:class:`EvpnVirtualAccessPw <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnVirtualAccessPws, self).__init__()

                self.yang_name = "evpn-virtual-access-pws"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"evpn-virtual-access-pw" : ("evpn_virtual_access_pw", Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw)}

                self.evpn_virtual_access_pw = YList(self)
                self._segment_path = lambda: "evpn-virtual-access-pws"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessPws, [], name, value)


            class EvpnVirtualAccessPw(Entity):
                """
                Virtual Access Pseudowire
                
                .. attribute:: neighbor  <key>
                
                	Neighbor IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: pseudowire_id  <key>
                
                	Pseudowire ID
                	**type**\:  int
                
                	**range:** 1..4294967295
                
                .. attribute:: evpn_virtual_access_pw_timers
                
                	Enter Virtual Access Pseudowire\-specific timers configuration submode
                	**type**\:   :py:class:`EvpnVirtualAccessPwTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers>`
                
                .. attribute:: evpn_virtual_ethernet_segment
                
                	Enter Ethernet Segment configuration submode
                	**type**\:   :py:class:`EvpnVirtualEthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw, self).__init__()

                    self.yang_name = "evpn-virtual-access-pw"
                    self.yang_parent_name = "evpn-virtual-access-pws"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"evpn-virtual-access-pw-timers" : ("evpn_virtual_access_pw_timers", Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers), "evpn-virtual-ethernet-segment" : ("evpn_virtual_ethernet_segment", Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment)}
                    self._child_list_classes = {}

                    self.neighbor = YLeaf(YType.str, "neighbor")

                    self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                    self.evpn_virtual_access_pw_timers = Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers()
                    self.evpn_virtual_access_pw_timers.parent = self
                    self._children_name_map["evpn_virtual_access_pw_timers"] = "evpn-virtual-access-pw-timers"
                    self._children_yang_names.add("evpn-virtual-access-pw-timers")

                    self.evpn_virtual_ethernet_segment = Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment()
                    self.evpn_virtual_ethernet_segment.parent = self
                    self._children_name_map["evpn_virtual_ethernet_segment"] = "evpn-virtual-ethernet-segment"
                    self._children_yang_names.add("evpn-virtual-ethernet-segment")
                    self._segment_path = lambda: "evpn-virtual-access-pw" + "[neighbor='" + self.neighbor.get() + "']" + "[pseudowire-id='" + self.pseudowire_id.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-virtual-access-pws/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw, ['neighbor', 'pseudowire_id'], name, value)


                class EvpnVirtualAccessPwTimers(Entity):
                    """
                    Enter Virtual Access Pseudowire\-specific
                    timers configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Virtual Access Pseudowire\-specific timers
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evpn_virtual_access_pw_peering
                    
                    	Virtual Access Pseudowire\-specific Peering timer
                    	**type**\:  int
                    
                    	**range:** 0..300
                    
                    	**default value**\: 3
                    
                    .. attribute:: evpn_virtual_access_pw_recovery
                    
                    	Virtual Access Pseudowire\-specific Recovery timer
                    	**type**\:  int
                    
                    	**range:** 20..3600
                    
                    	**default value**\: 30
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers, self).__init__()

                        self.yang_name = "evpn-virtual-access-pw-timers"
                        self.yang_parent_name = "evpn-virtual-access-pw"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.empty, "enable")

                        self.evpn_virtual_access_pw_peering = YLeaf(YType.uint32, "evpn-virtual-access-pw-peering")

                        self.evpn_virtual_access_pw_recovery = YLeaf(YType.uint32, "evpn-virtual-access-pw-recovery")
                        self._segment_path = lambda: "evpn-virtual-access-pw-timers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers, ['enable', 'evpn_virtual_access_pw_peering', 'evpn_virtual_access_pw_recovery'], name, value)


                class EvpnVirtualEthernetSegment(Entity):
                    """
                    Enter Ethernet Segment configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Ethernet Segment
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: es_import_route_target
                    
                    	ES\-Import Route Target
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: identifier
                    
                    	Ethernet segment identifier
                    	**type**\:   :py:class:`Identifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.Identifier>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: manual_service_carving
                    
                    	Enter Manual service carving configuration submode
                    	**type**\:   :py:class:`ManualServiceCarving <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment, self).__init__()

                        self.yang_name = "evpn-virtual-ethernet-segment"
                        self.yang_parent_name = "evpn-virtual-access-pw"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"identifier" : ("identifier", Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.Identifier), "manual-service-carving" : ("manual_service_carving", Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving)}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.empty, "enable")

                        self.es_import_route_target = YLeaf(YType.str, "es-import-route-target")

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
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        .. attribute:: bytes23
                        
                        	2nd and 3rd Bytes
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes45
                        
                        	4th and 5th Bytes
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes67
                        
                        	6th and 7th Bytes
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes89
                        
                        	8th and 9th Bytes
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: type
                        
                        	Ethernet segment identifier type
                        	**type**\:   :py:class:`EthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EthernetSegmentIdentifier>`
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.bytes01 = YLeaf(YType.str, "bytes01")

                            self.bytes23 = YLeaf(YType.str, "bytes23")

                            self.bytes45 = YLeaf(YType.str, "bytes45")

                            self.bytes67 = YLeaf(YType.str, "bytes67")

                            self.bytes89 = YLeaf(YType.str, "bytes89")

                            self.type = YLeaf(YType.enumeration, "type")
                            self._segment_path = lambda: "identifier"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.Identifier, ['bytes01', 'bytes23', 'bytes45', 'bytes67', 'bytes89', 'type'], name, value)


                    class ManualServiceCarving(Entity):
                        """
                        Enter Manual service carving configuration
                        submode
                        
                        .. attribute:: enable
                        
                        	Enable Manual service carving
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: service_list
                        
                        	Manual service carving primary,secondary lists
                        	**type**\:   :py:class:`ServiceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving, self).__init__()

                            self.yang_name = "manual-service-carving"
                            self.yang_parent_name = "evpn-virtual-ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"service-list" : ("service_list", Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList)}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")

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
                            	**type**\:  str
                            
                            	**length:** 1..150
                            
                            .. attribute:: secondary
                            
                            	Secondary services list
                            	**type**\:  str
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.primary = YLeaf(YType.str, "primary")

                                self.secondary = YLeaf(YType.str, "secondary")
                                self._segment_path = lambda: "service-list"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList, ['primary', 'secondary'], name, value)


        class EvpnVirtualAccessVfis(Entity):
            """
            Virtual Access VFI interfaces
            
            .. attribute:: evpn_virtual_access_vfi
            
            	Virtual Access VFI
            	**type**\: list of    :py:class:`EvpnVirtualAccessVfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.EvpnVirtualAccessVfis, self).__init__()

                self.yang_name = "evpn-virtual-access-vfis"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"evpn-virtual-access-vfi" : ("evpn_virtual_access_vfi", Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi)}

                self.evpn_virtual_access_vfi = YList(self)
                self._segment_path = lambda: "evpn-virtual-access-vfis"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessVfis, [], name, value)


            class EvpnVirtualAccessVfi(Entity):
                """
                Virtual Access VFI
                
                .. attribute:: name  <key>
                
                	Name of the Virtual Access VFI
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: evpn_virtual_access_vfi_timers
                
                	Enter Virtual Forwarding Interface timers configuration submode
                	**type**\:   :py:class:`EvpnVirtualAccessVfiTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers>`
                
                .. attribute:: evpn_virtual_ethernet_segment
                
                	Enter Ethernet Segment configuration submode
                	**type**\:   :py:class:`EvpnVirtualEthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi, self).__init__()

                    self.yang_name = "evpn-virtual-access-vfi"
                    self.yang_parent_name = "evpn-virtual-access-vfis"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"evpn-virtual-access-vfi-timers" : ("evpn_virtual_access_vfi_timers", Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers), "evpn-virtual-ethernet-segment" : ("evpn_virtual_ethernet_segment", Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.evpn_virtual_access_vfi_timers = Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers()
                    self.evpn_virtual_access_vfi_timers.parent = self
                    self._children_name_map["evpn_virtual_access_vfi_timers"] = "evpn-virtual-access-vfi-timers"
                    self._children_yang_names.add("evpn-virtual-access-vfi-timers")

                    self.evpn_virtual_ethernet_segment = Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment()
                    self.evpn_virtual_ethernet_segment.parent = self
                    self._children_name_map["evpn_virtual_ethernet_segment"] = "evpn-virtual-ethernet-segment"
                    self._children_yang_names.add("evpn-virtual-ethernet-segment")
                    self._segment_path = lambda: "evpn-virtual-access-vfi" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpn-virtual-access-vfis/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi, ['name'], name, value)


                class EvpnVirtualAccessVfiTimers(Entity):
                    """
                    Enter Virtual Forwarding Interface timers
                    configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Virtual Forwarding Interface timers
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evpn_virtual_access_vfi_peering
                    
                    	Virtual Forwarding Interface\-specific Peering timer
                    	**type**\:  int
                    
                    	**range:** 0..300
                    
                    	**default value**\: 3
                    
                    .. attribute:: evpn_virtual_access_vfi_recovery
                    
                    	Virtual Forwarding Interface\-specific Recovery timer
                    	**type**\:  int
                    
                    	**range:** 20..3600
                    
                    	**default value**\: 30
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers, self).__init__()

                        self.yang_name = "evpn-virtual-access-vfi-timers"
                        self.yang_parent_name = "evpn-virtual-access-vfi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.empty, "enable")

                        self.evpn_virtual_access_vfi_peering = YLeaf(YType.uint32, "evpn-virtual-access-vfi-peering")

                        self.evpn_virtual_access_vfi_recovery = YLeaf(YType.uint32, "evpn-virtual-access-vfi-recovery")
                        self._segment_path = lambda: "evpn-virtual-access-vfi-timers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers, ['enable', 'evpn_virtual_access_vfi_peering', 'evpn_virtual_access_vfi_recovery'], name, value)


                class EvpnVirtualEthernetSegment(Entity):
                    """
                    Enter Ethernet Segment configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Ethernet Segment
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: es_import_route_target
                    
                    	ES\-Import Route Target
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: identifier
                    
                    	Ethernet segment identifier
                    	**type**\:   :py:class:`Identifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.Identifier>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: manual_service_carving
                    
                    	Enter Manual service carving configuration submode
                    	**type**\:   :py:class:`ManualServiceCarving <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment, self).__init__()

                        self.yang_name = "evpn-virtual-ethernet-segment"
                        self.yang_parent_name = "evpn-virtual-access-vfi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"identifier" : ("identifier", Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.Identifier), "manual-service-carving" : ("manual_service_carving", Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving)}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.empty, "enable")

                        self.es_import_route_target = YLeaf(YType.str, "es-import-route-target")

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
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        .. attribute:: bytes23
                        
                        	2nd and 3rd Bytes
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes45
                        
                        	4th and 5th Bytes
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes67
                        
                        	6th and 7th Bytes
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes89
                        
                        	8th and 9th Bytes
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**mandatory**\: True
                        
                        	**units**\: byte
                        
                        .. attribute:: type
                        
                        	Ethernet segment identifier type
                        	**type**\:   :py:class:`EthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EthernetSegmentIdentifier>`
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.bytes01 = YLeaf(YType.str, "bytes01")

                            self.bytes23 = YLeaf(YType.str, "bytes23")

                            self.bytes45 = YLeaf(YType.str, "bytes45")

                            self.bytes67 = YLeaf(YType.str, "bytes67")

                            self.bytes89 = YLeaf(YType.str, "bytes89")

                            self.type = YLeaf(YType.enumeration, "type")
                            self._segment_path = lambda: "identifier"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.Identifier, ['bytes01', 'bytes23', 'bytes45', 'bytes67', 'bytes89', 'type'], name, value)


                    class ManualServiceCarving(Entity):
                        """
                        Enter Manual service carving configuration
                        submode
                        
                        .. attribute:: enable
                        
                        	Enable Manual service carving
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: service_list
                        
                        	Manual service carving primary,secondary lists
                        	**type**\:   :py:class:`ServiceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving, self).__init__()

                            self.yang_name = "manual-service-carving"
                            self.yang_parent_name = "evpn-virtual-ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"service-list" : ("service_list", Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList)}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")

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
                            	**type**\:  str
                            
                            	**length:** 1..150
                            
                            .. attribute:: secondary
                            
                            	Secondary services list
                            	**type**\:  str
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.primary = YLeaf(YType.str, "primary")

                                self.secondary = YLeaf(YType.str, "secondary")
                                self._segment_path = lambda: "service-list"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.ManualServiceCarving.ServiceList, ['primary', 'secondary'], name, value)


        class Evpnevis(Entity):
            """
            Enter EVPN Instance configuration submode
            
            .. attribute:: evpnevi
            
            	Enter EVPN Instance configuration submode
            	**type**\: list of    :py:class:`Evpnevi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.Evpnevis, self).__init__()

                self.yang_name = "evpnevis"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"evpnevi" : ("evpnevi", Evpn.EvpnTables.Evpnevis.Evpnevi)}

                self.evpnevi = YList(self)
                self._segment_path = lambda: "evpnevis"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.EvpnTables.Evpnevis, [], name, value)


            class Evpnevi(Entity):
                """
                Enter EVPN Instance configuration submode
                
                .. attribute:: eviid  <key>
                
                	EVI ID
                	**type**\:  int
                
                	**range:** 1..65534
                
                .. attribute:: evi_advertise_mac
                
                	Enter Advertise local MAC\-only routes configuration submode
                	**type**\:   :py:class:`EviAdvertiseMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EviAdvertiseMac>`
                
                .. attribute:: evi_advertise_mac_deprecated
                
                	DEPRECATED\: Advertise local MAC\-only and BVI MAC routes
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evi_load_balancing
                
                	Enter Loadbalancing configuration submode
                	**type**\:   :py:class:`EviLoadBalancing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing>`
                
                .. attribute:: evi_reorig_disable
                
                	Disable route re\-origination
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evi_unknown_unicast_flooding_disable
                
                	Disable Unknown Unicast Flooding on this EVI
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evpn_evi_cw_disable
                
                	CW disable for EVPN EVI
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evpnev_ibgp_auto_discovery
                
                	Enable Autodiscovery BGP in EVPN Instance
                	**type**\:   :py:class:`EvpnevIbgpAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery>`
                
                .. attribute:: evpnevi_description
                
                	EVPN Instance description
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.Evpnevis.Evpnevi, self).__init__()

                    self.yang_name = "evpnevi"
                    self.yang_parent_name = "evpnevis"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"evi-advertise-mac" : ("evi_advertise_mac", Evpn.EvpnTables.Evpnevis.Evpnevi.EviAdvertiseMac), "evi-load-balancing" : ("evi_load_balancing", Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing), "evpnev-ibgp-auto-discovery" : ("evpnev_ibgp_auto_discovery", Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery)}
                    self._child_list_classes = {}

                    self.eviid = YLeaf(YType.uint32, "eviid")

                    self.evi_advertise_mac_deprecated = YLeaf(YType.empty, "evi-advertise-mac-deprecated")

                    self.evi_reorig_disable = YLeaf(YType.empty, "evi-reorig-disable")

                    self.evi_unknown_unicast_flooding_disable = YLeaf(YType.empty, "evi-unknown-unicast-flooding-disable")

                    self.evpn_evi_cw_disable = YLeaf(YType.empty, "evpn-evi-cw-disable")

                    self.evpnevi_description = YLeaf(YType.str, "evpnevi-description")

                    self.evi_advertise_mac = Evpn.EvpnTables.Evpnevis.Evpnevi.EviAdvertiseMac()
                    self.evi_advertise_mac.parent = self
                    self._children_name_map["evi_advertise_mac"] = "evi-advertise-mac"
                    self._children_yang_names.add("evi-advertise-mac")

                    self.evi_load_balancing = Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing()
                    self.evi_load_balancing.parent = self
                    self._children_name_map["evi_load_balancing"] = "evi-load-balancing"
                    self._children_yang_names.add("evi-load-balancing")

                    self.evpnev_ibgp_auto_discovery = Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery()
                    self.evpnev_ibgp_auto_discovery.parent = self
                    self._children_name_map["evpnev_ibgp_auto_discovery"] = "evpnev-ibgp-auto-discovery"
                    self._children_yang_names.add("evpnev-ibgp-auto-discovery")
                    self._segment_path = lambda: "evpnevi" + "[eviid='" + self.eviid.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpnevis/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi, ['eviid', 'evi_advertise_mac_deprecated', 'evi_reorig_disable', 'evi_unknown_unicast_flooding_disable', 'evpn_evi_cw_disable', 'evpnevi_description'], name, value)


                class EviAdvertiseMac(Entity):
                    """
                    Enter Advertise local MAC\-only routes
                    configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Advertise local MAC\-only routes
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evi_advertise_mac_bvi
                    
                    	Advertise local MAC\-only and BVI MAC routes
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.Evpnevis.Evpnevi.EviAdvertiseMac, self).__init__()

                        self.yang_name = "evi-advertise-mac"
                        self.yang_parent_name = "evpnevi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.empty, "enable")

                        self.evi_advertise_mac_bvi = YLeaf(YType.empty, "evi-advertise-mac-bvi")
                        self._segment_path = lambda: "evi-advertise-mac"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EviAdvertiseMac, ['enable', 'evi_advertise_mac_bvi'], name, value)


                class EviLoadBalancing(Entity):
                    """
                    Enter Loadbalancing configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable Loadbalancing
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evi_flow_label
                    
                    	Enable Flow Label based load balancing
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing, self).__init__()

                        self.yang_name = "evi-load-balancing"
                        self.yang_parent_name = "evpnevi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.empty, "enable")

                        self.evi_flow_label = YLeaf(YType.empty, "evi-flow-label")
                        self._segment_path = lambda: "evi-load-balancing"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing, ['enable', 'evi_flow_label'], name, value)


                class EvpnevIbgpAutoDiscovery(Entity):
                    """
                    Enable Autodiscovery BGP in EVPN Instance
                    
                    .. attribute:: enable
                    
                    	Enable Autodiscovery BGP
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evpn_route_distinguisher
                    
                    	Route Distinguisher
                    	**type**\:   :py:class:`EvpnRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteDistinguisher>`
                    
                    .. attribute:: evpn_route_targets
                    
                    	Route Target
                    	**type**\:   :py:class:`EvpnRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets>`
                    
                    .. attribute:: table_policy
                    
                    	Table Policy for installation of forwarding data to L2FIB
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery, self).__init__()

                        self.yang_name = "evpnev-ibgp-auto-discovery"
                        self.yang_parent_name = "evpnevi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"evpn-route-distinguisher" : ("evpn_route_distinguisher", Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteDistinguisher), "evpn-route-targets" : ("evpn_route_targets", Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets)}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.empty, "enable")

                        self.table_policy = YLeaf(YType.str, "table-policy")

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
                        
                        .. attribute:: addr_index
                        
                        	Addr index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: address
                        
                        	IPV4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: as_
                        
                        	Two byte or 4 byte AS number
                        	**type**\:  int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: as_index
                        
                        	AS\:nn (hex or decimal format)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Router Distinguisher Type
                        	**type**\:   :py:class:`BgpRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteDistinguisher, self).__init__()

                            self.yang_name = "evpn-route-distinguisher"
                            self.yang_parent_name = "evpnev-ibgp-auto-discovery"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.addr_index = YLeaf(YType.uint32, "addr-index")

                            self.address = YLeaf(YType.str, "address")

                            self.as_ = YLeaf(YType.uint32, "as")

                            self.as_index = YLeaf(YType.uint32, "as-index")

                            self.type = YLeaf(YType.enumeration, "type")
                            self._segment_path = lambda: "evpn-route-distinguisher"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteDistinguisher, ['addr_index', 'address', 'as_', 'as_index', 'type'], name, value)


                    class EvpnRouteTargets(Entity):
                        """
                        Route Target
                        
                        .. attribute:: evpn_route_target_as
                        
                        	Name of the Route Target
                        	**type**\: list of    :py:class:`EvpnRouteTargetAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs>`
                        
                        .. attribute:: evpn_route_target_ipv4_address
                        
                        	Name of the Route Target
                        	**type**\: list of    :py:class:`EvpnRouteTargetIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address>`
                        
                        .. attribute:: evpn_route_target_none
                        
                        	Name of the Route Target
                        	**type**\: list of    :py:class:`EvpnRouteTargetNone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets, self).__init__()

                            self.yang_name = "evpn-route-targets"
                            self.yang_parent_name = "evpnev-ibgp-auto-discovery"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"evpn-route-target-as" : ("evpn_route_target_as", Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs), "evpn-route-target-ipv4-address" : ("evpn_route_target_ipv4_address", Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address), "evpn-route-target-none" : ("evpn_route_target_none", Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone)}

                            self.evpn_route_target_as = YList(self)
                            self.evpn_route_target_ipv4_address = YList(self)
                            self.evpn_route_target_none = YList(self)
                            self._segment_path = lambda: "evpn-route-targets"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets, [], name, value)


                        class EvpnRouteTargetAs(Entity):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  <key>
                            
                            	Format of the route target
                            	**type**\:   :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                            
                            .. attribute:: role  <key>
                            
                            	Role of the router target type
                            	**type**\:   :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                            
                            .. attribute:: as_  <key>
                            
                            	Two byte or 4 byte AS number
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: as_index  <key>
                            
                            	AS\:nn (hex or decimal format)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stitching  <key>
                            
                            	whether RT is Stitching RT
                            	**type**\:   :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTarget>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs, self).__init__()

                                self.yang_name = "evpn-route-target-as"
                                self.yang_parent_name = "evpn-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.format = YLeaf(YType.enumeration, "format")

                                self.role = YLeaf(YType.enumeration, "role")

                                self.as_ = YLeaf(YType.uint32, "as")

                                self.as_index = YLeaf(YType.uint32, "as-index")

                                self.stitching = YLeaf(YType.enumeration, "stitching")
                                self._segment_path = lambda: "evpn-route-target-as" + "[format='" + self.format.get() + "']" + "[role='" + self.role.get() + "']" + "[as='" + self.as_.get() + "']" + "[as-index='" + self.as_index.get() + "']" + "[stitching='" + self.stitching.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs, ['format', 'role', 'as_', 'as_index', 'stitching'], name, value)


                        class EvpnRouteTargetIpv4Address(Entity):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  <key>
                            
                            	Format of the route target
                            	**type**\:   :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                            
                            .. attribute:: role  <key>
                            
                            	Role of the router target type
                            	**type**\:   :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                            
                            .. attribute:: address  <key>
                            
                            	IPV4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: addr_index  <key>
                            
                            	Addr index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: stitching  <key>
                            
                            	whether RT is Stitching RT
                            	**type**\:   :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTarget>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address, self).__init__()

                                self.yang_name = "evpn-route-target-ipv4-address"
                                self.yang_parent_name = "evpn-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.format = YLeaf(YType.enumeration, "format")

                                self.role = YLeaf(YType.enumeration, "role")

                                self.address = YLeaf(YType.str, "address")

                                self.addr_index = YLeaf(YType.uint32, "addr-index")

                                self.stitching = YLeaf(YType.enumeration, "stitching")
                                self._segment_path = lambda: "evpn-route-target-ipv4-address" + "[format='" + self.format.get() + "']" + "[role='" + self.role.get() + "']" + "[address='" + self.address.get() + "']" + "[addr-index='" + self.addr_index.get() + "']" + "[stitching='" + self.stitching.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address, ['format', 'role', 'address', 'addr_index', 'stitching'], name, value)


                        class EvpnRouteTargetNone(Entity):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  <key>
                            
                            	Format of the route target
                            	**type**\:   :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                            
                            .. attribute:: role  <key>
                            
                            	Role of the router target type
                            	**type**\:   :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                            
                            .. attribute:: stitching  <key>
                            
                            	whether RT is Stitching RT
                            	**type**\:   :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTarget>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone, self).__init__()

                                self.yang_name = "evpn-route-target-none"
                                self.yang_parent_name = "evpn-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.format = YLeaf(YType.enumeration, "format")

                                self.role = YLeaf(YType.enumeration, "role")

                                self.stitching = YLeaf(YType.enumeration, "stitching")
                                self._segment_path = lambda: "evpn-route-target-none" + "[format='" + self.format.get() + "']" + "[role='" + self.role.get() + "']" + "[stitching='" + self.stitching.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevIbgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone, ['format', 'role', 'stitching'], name, value)


        class Evpnmac(Entity):
            """
            EVPN MAC Configuration
            
            .. attribute:: enable
            
            	Enable EVPN MAC Configuration
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: evpnmac_secure
            
            	EVPN MAC Secure Configuration
            	**type**\:   :py:class:`EvpnmacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnmac.EvpnmacSecure>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(Evpn.EvpnTables.Evpnmac, self).__init__()

                self.yang_name = "evpnmac"
                self.yang_parent_name = "evpn-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"evpnmac-secure" : ("evpnmac_secure", Evpn.EvpnTables.Evpnmac.EvpnmacSecure)}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

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
                
                .. attribute:: enable
                
                	Enable EVPN MAC Secure Configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evpnmac_secure_freeze_time
                
                	Length of time to lock the MAC after a MAC security violation
                	**type**\:  int
                
                	**range:** 5..3600
                
                .. attribute:: evpnmac_secure_move_count
                
                	Number of moves to occur within the move interval before locking the MAC
                	**type**\:  int
                
                	**range:** 1..1000
                
                .. attribute:: evpnmac_secure_move_interval
                
                	Interval to watch for subsequent MAC moves before locking the MAC
                	**type**\:  int
                
                	**range:** 5..3600
                
                .. attribute:: evpnmac_secure_retry_count
                
                	Number of times to unfreeze a MAC before permanently freezing it
                	**type**\:  int
                
                	**range:** 0..1000
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Evpn.EvpnTables.Evpnmac.EvpnmacSecure, self).__init__()

                    self.yang_name = "evpnmac-secure"
                    self.yang_parent_name = "evpnmac"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.enable = YLeaf(YType.empty, "enable")

                    self.evpnmac_secure_freeze_time = YLeaf(YType.uint32, "evpnmac-secure-freeze-time")

                    self.evpnmac_secure_move_count = YLeaf(YType.uint32, "evpnmac-secure-move-count")

                    self.evpnmac_secure_move_interval = YLeaf(YType.uint32, "evpnmac-secure-move-interval")

                    self.evpnmac_secure_retry_count = YLeaf(YType.uint32, "evpnmac-secure-retry-count")
                    self._segment_path = lambda: "evpnmac-secure"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:evpn/evpn-tables/evpnmac/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.EvpnTables.Evpnmac.EvpnmacSecure, ['enable', 'evpnmac_secure_freeze_time', 'evpnmac_secure_move_count', 'evpnmac_secure_move_interval', 'evpnmac_secure_retry_count'], name, value)

    def clone_ptr(self):
        self._top_entity = Evpn()
        return self._top_entity

class GenericInterfaceLists(Entity):
    """
    generic interface lists
    
    .. attribute:: generic_interface
    
    	Bridge group
    	**type**\: list of    :py:class:`GenericInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.GenericInterfaceLists.GenericInterface>`
    
    

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
        self._child_container_classes = {}
        self._child_list_classes = {"generic-interface" : ("generic_interface", GenericInterfaceLists.GenericInterface)}

        self.generic_interface = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:generic-interface-lists"

    def __setattr__(self, name, value):
        self._perform_setattr(GenericInterfaceLists, [], name, value)


    class GenericInterface(Entity):
        """
        Bridge group
        
        .. attribute:: generic_interface_list_name  <key>
        
        	Name of the interface list
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: enable
        
        	Enable interface list
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: interfaces
        
        	Interface table
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.GenericInterfaceLists.GenericInterface.Interfaces>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(GenericInterfaceLists.GenericInterface, self).__init__()

            self.yang_name = "generic-interface"
            self.yang_parent_name = "generic-interface-lists"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"interfaces" : ("interfaces", GenericInterfaceLists.GenericInterface.Interfaces)}
            self._child_list_classes = {}

            self.generic_interface_list_name = YLeaf(YType.str, "generic-interface-list-name")

            self.enable = YLeaf(YType.empty, "enable")

            self.interfaces = GenericInterfaceLists.GenericInterface.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")
            self._segment_path = lambda: "generic-interface" + "[generic-interface-list-name='" + self.generic_interface_list_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:generic-interface-lists/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(GenericInterfaceLists.GenericInterface, ['generic_interface_list_name', 'enable'], name, value)


        class Interfaces(Entity):
            """
            Interface table
            
            .. attribute:: interface
            
            	Interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.GenericInterfaceLists.GenericInterface.Interfaces.Interface>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(GenericInterfaceLists.GenericInterface.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "generic-interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", GenericInterfaceLists.GenericInterface.Interfaces.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"

            def __setattr__(self, name, value):
                self._perform_setattr(GenericInterfaceLists.GenericInterface.Interfaces, [], name, value)


            class Interface(Entity):
                """
                Interface
                
                .. attribute:: interface_name  <key>
                
                	Name of the interface
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: enable
                
                	Enable interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(GenericInterfaceLists.GenericInterface.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.enable = YLeaf(YType.empty, "enable")
                    self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(GenericInterfaceLists.GenericInterface.Interfaces.Interface, ['interface_name', 'enable'], name, value)

    def clone_ptr(self):
        self._top_entity = GenericInterfaceLists()
        return self._top_entity

class L2Vpn(Entity):
    """
    L2VPN configuration
    
    .. attribute:: auto_discovery
    
    	Global auto\-discovery attributes
    	**type**\:   :py:class:`AutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.AutoDiscovery>`
    
    .. attribute:: capability
    
    	L2VPN Capability Mode
    	**type**\:   :py:class:`L2vpnCapabilityMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnCapabilityMode>`
    
    .. attribute:: database
    
    	L2VPN databases
    	**type**\:   :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database>`
    
    .. attribute:: enable
    
    	Enable L2VPN feature
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: l2vpn_router_id
    
    	Global L2VPN Router ID
    	**type**\:  str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    .. attribute:: load_balance
    
    	Enable flow load balancing on l2vpn bridges
    	**type**\:   :py:class:`LoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.LoadBalance>`
    
    .. attribute:: mac_limit_threshold
    
    	Configure MAC limit threshold percent
    	**type**\:  int
    
    	**range:** 1..100
    
    	**units**\: percentage
    
    .. attribute:: mspw_description
    
    	MS\-PW global description
    	**type**\:  str
    
    	**length:** 1..64
    
    .. attribute:: mtu_mismatch_ignore
    
    	Ignore MTU Mismatch for XCs
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: neighbor
    
    	L2VPN neighbor submode
    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Neighbor>`
    
    .. attribute:: nsr
    
    	Enable Non\-Stop Routing
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: pbb
    
    	L2VPN PBB Global
    	**type**\:   :py:class:`Pbb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Pbb>`
    
    .. attribute:: pw_grouping
    
    	Enable PW grouping
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: pw_routing
    
    	Pseudowire\-routing attributes
    	**type**\:   :py:class:`PwRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.PwRouting>`
    
    .. attribute:: pw_status_disable
    
    	Disable PW status
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: pwoam_refresh
    
    	Configure PW OAM refresh interval
    	**type**\:  int
    
    	**range:** 1..4095
    
    	**units**\: second
    
    .. attribute:: snmp
    
    	SNMP related configuration
    	**type**\:   :py:class:`Snmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Snmp>`
    
    .. attribute:: tcn_propagation
    
    	Topology change notification propagation
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: utility
    
    	L2VPN utilities
    	**type**\:   :py:class:`Utility <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Utility>`
    
    

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
        self._child_container_classes = {"auto-discovery" : ("auto_discovery", L2Vpn.AutoDiscovery), "database" : ("database", L2Vpn.Database), "neighbor" : ("neighbor", L2Vpn.Neighbor), "pbb" : ("pbb", L2Vpn.Pbb), "pw-routing" : ("pw_routing", L2Vpn.PwRouting), "snmp" : ("snmp", L2Vpn.Snmp), "utility" : ("utility", L2Vpn.Utility)}
        self._child_list_classes = {}

        self.capability = YLeaf(YType.enumeration, "capability")

        self.enable = YLeaf(YType.empty, "enable")

        self.l2vpn_router_id = YLeaf(YType.str, "l2vpn-router-id")

        self.load_balance = YLeaf(YType.enumeration, "load-balance")

        self.mac_limit_threshold = YLeaf(YType.uint32, "mac-limit-threshold")

        self.mspw_description = YLeaf(YType.str, "mspw-description")

        self.mtu_mismatch_ignore = YLeaf(YType.empty, "mtu-mismatch-ignore")

        self.nsr = YLeaf(YType.empty, "nsr")

        self.pw_grouping = YLeaf(YType.empty, "pw-grouping")

        self.pw_status_disable = YLeaf(YType.empty, "pw-status-disable")

        self.pwoam_refresh = YLeaf(YType.uint32, "pwoam-refresh")

        self.tcn_propagation = YLeaf(YType.empty, "tcn-propagation")

        self.auto_discovery = L2Vpn.AutoDiscovery()
        self.auto_discovery.parent = self
        self._children_name_map["auto_discovery"] = "auto-discovery"
        self._children_yang_names.add("auto-discovery")

        self.database = L2Vpn.Database()
        self.database.parent = self
        self._children_name_map["database"] = "database"
        self._children_yang_names.add("database")

        self.neighbor = L2Vpn.Neighbor()
        self.neighbor.parent = self
        self._children_name_map["neighbor"] = "neighbor"
        self._children_yang_names.add("neighbor")

        self.pbb = L2Vpn.Pbb()
        self.pbb.parent = self
        self._children_name_map["pbb"] = "pbb"
        self._children_yang_names.add("pbb")

        self.pw_routing = L2Vpn.PwRouting()
        self.pw_routing.parent = self
        self._children_name_map["pw_routing"] = "pw-routing"
        self._children_yang_names.add("pw-routing")

        self.snmp = L2Vpn.Snmp()
        self.snmp.parent = self
        self._children_name_map["snmp"] = "snmp"
        self._children_yang_names.add("snmp")

        self.utility = L2Vpn.Utility()
        self.utility.parent = self
        self._children_name_map["utility"] = "utility"
        self._children_yang_names.add("utility")
        self._segment_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn"

    def __setattr__(self, name, value):
        self._perform_setattr(L2Vpn, ['capability', 'enable', 'l2vpn_router_id', 'load_balance', 'mac_limit_threshold', 'mspw_description', 'mtu_mismatch_ignore', 'nsr', 'pw_grouping', 'pw_status_disable', 'pwoam_refresh', 'tcn_propagation'], name, value)


    class AutoDiscovery(Entity):
        """
        Global auto\-discovery attributes
        
        .. attribute:: bgp_signaling
        
        	Global bgp signaling attributes
        	**type**\:   :py:class:`BgpSignaling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.AutoDiscovery.BgpSignaling>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(L2Vpn.AutoDiscovery, self).__init__()

            self.yang_name = "auto-discovery"
            self.yang_parent_name = "l2vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"bgp-signaling" : ("bgp_signaling", L2Vpn.AutoDiscovery.BgpSignaling)}
            self._child_list_classes = {}

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
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.AutoDiscovery.BgpSignaling, self).__init__()

                self.yang_name = "bgp-signaling"
                self.yang_parent_name = "auto-discovery"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.mtu_mismatch_ignore = YLeaf(YType.empty, "mtu-mismatch-ignore")
                self._segment_path = lambda: "bgp-signaling"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/auto-discovery/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.AutoDiscovery.BgpSignaling, ['mtu_mismatch_ignore'], name, value)


    class Database(Entity):
        """
        L2VPN databases
        
        .. attribute:: bridge_domain_groups
        
        	List of bridge  groups
        	**type**\:   :py:class:`BridgeDomainGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups>`
        
        .. attribute:: flexible_xconnect_service_table
        
        	List of Flexible XConnect Services
        	**type**\:   :py:class:`FlexibleXconnectServiceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable>`
        
        .. attribute:: g8032_rings
        
        	List of G8032 Ring
        	**type**\:   :py:class:`G8032Rings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings>`
        
        .. attribute:: pseudowire_classes
        
        	List of pseudowire classes
        	**type**\:   :py:class:`PseudowireClasses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses>`
        
        .. attribute:: redundancy
        
        	Redundancy groups
        	**type**\:   :py:class:`Redundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.Redundancy>`
        
        .. attribute:: xconnect_groups
        
        	List of xconnect groups
        	**type**\:   :py:class:`XconnectGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(L2Vpn.Database, self).__init__()

            self.yang_name = "database"
            self.yang_parent_name = "l2vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"bridge-domain-groups" : ("bridge_domain_groups", L2Vpn.Database.BridgeDomainGroups), "flexible-xconnect-service-table" : ("flexible_xconnect_service_table", L2Vpn.Database.FlexibleXconnectServiceTable), "g8032-rings" : ("g8032_rings", L2Vpn.Database.G8032Rings), "pseudowire-classes" : ("pseudowire_classes", L2Vpn.Database.PseudowireClasses), "redundancy" : ("redundancy", L2Vpn.Database.Redundancy), "xconnect-groups" : ("xconnect_groups", L2Vpn.Database.XconnectGroups)}
            self._child_list_classes = {}

            self.bridge_domain_groups = L2Vpn.Database.BridgeDomainGroups()
            self.bridge_domain_groups.parent = self
            self._children_name_map["bridge_domain_groups"] = "bridge-domain-groups"
            self._children_yang_names.add("bridge-domain-groups")

            self.flexible_xconnect_service_table = L2Vpn.Database.FlexibleXconnectServiceTable()
            self.flexible_xconnect_service_table.parent = self
            self._children_name_map["flexible_xconnect_service_table"] = "flexible-xconnect-service-table"
            self._children_yang_names.add("flexible-xconnect-service-table")

            self.g8032_rings = L2Vpn.Database.G8032Rings()
            self.g8032_rings.parent = self
            self._children_name_map["g8032_rings"] = "g8032-rings"
            self._children_yang_names.add("g8032-rings")

            self.pseudowire_classes = L2Vpn.Database.PseudowireClasses()
            self.pseudowire_classes.parent = self
            self._children_name_map["pseudowire_classes"] = "pseudowire-classes"
            self._children_yang_names.add("pseudowire-classes")

            self.redundancy = L2Vpn.Database.Redundancy()
            self.redundancy.parent = self
            self._children_name_map["redundancy"] = "redundancy"
            self._children_yang_names.add("redundancy")

            self.xconnect_groups = L2Vpn.Database.XconnectGroups()
            self.xconnect_groups.parent = self
            self._children_name_map["xconnect_groups"] = "xconnect-groups"
            self._children_yang_names.add("xconnect-groups")
            self._segment_path = lambda: "database"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/%s" % self._segment_path()


        class BridgeDomainGroups(Entity):
            """
            List of bridge  groups
            
            .. attribute:: bridge_domain_group
            
            	Bridge group
            	**type**\: list of    :py:class:`BridgeDomainGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Database.BridgeDomainGroups, self).__init__()

                self.yang_name = "bridge-domain-groups"
                self.yang_parent_name = "database"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"bridge-domain-group" : ("bridge_domain_group", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup)}

                self.bridge_domain_group = YList(self)
                self._segment_path = lambda: "bridge-domain-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups, [], name, value)


            class BridgeDomainGroup(Entity):
                """
                Bridge group
                
                .. attribute:: name  <key>
                
                	Name of the Bridge group
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: bridge_domains
                
                	List of Bridge Domain
                	**type**\:   :py:class:`BridgeDomains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup, self).__init__()

                    self.yang_name = "bridge-domain-group"
                    self.yang_parent_name = "bridge-domain-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"bridge-domains" : ("bridge_domains", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.bridge_domains = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains()
                    self.bridge_domains.parent = self
                    self._children_name_map["bridge_domains"] = "bridge-domains"
                    self._children_yang_names.add("bridge-domains")
                    self._segment_path = lambda: "bridge-domain-group" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/bridge-domain-groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup, ['name'], name, value)


                class BridgeDomains(Entity):
                    """
                    List of Bridge Domain
                    
                    .. attribute:: bridge_domain
                    
                    	bridge domain
                    	**type**\: list of    :py:class:`BridgeDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains, self).__init__()

                        self.yang_name = "bridge-domains"
                        self.yang_parent_name = "bridge-domain-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"bridge-domain" : ("bridge_domain", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain)}

                        self.bridge_domain = YList(self)
                        self._segment_path = lambda: "bridge-domains"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains, [], name, value)


                    class BridgeDomain(Entity):
                        """
                        bridge domain
                        
                        .. attribute:: name  <key>
                        
                        	Name of the bridge domain
                        	**type**\:  str
                        
                        	**length:** 1..27
                        
                        .. attribute:: access_vfis
                        
                        	Specify the access virtual forwarding interface name
                        	**type**\:   :py:class:`AccessVfis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis>`
                        
                        .. attribute:: bd_attachment_circuits
                        
                        	Attachment Circuit table
                        	**type**\:   :py:class:`BdAttachmentCircuits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits>`
                        
                        .. attribute:: bd_pseudowire_evpns
                        
                        	List of EVPN pseudowires
                        	**type**\:   :py:class:`BdPseudowireEvpns <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns>`
                        
                        .. attribute:: bd_pseudowires
                        
                        	List of pseudowires
                        	**type**\:   :py:class:`BdPseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires>`
                        
                        .. attribute:: bd_storm_controls
                        
                        	Storm Control
                        	**type**\:   :py:class:`BdStormControls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls>`
                        
                        .. attribute:: bridge_description
                        
                        	Bridge\-domain description Name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: bridge_domain_evis
                        
                        	Bridge Domain EVI Table
                        	**type**\:   :py:class:`BridgeDomainEvis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis>`
                        
                        .. attribute:: bridge_domain_mac
                        
                        	MAC configuration commands
                        	**type**\:   :py:class:`BridgeDomainMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac>`
                        
                        .. attribute:: bridge_domain_mtu
                        
                        	Maximum transmission unit for this Bridge Domain
                        	**type**\:  int
                        
                        	**range:** 46..65535
                        
                        	**units**\: byte
                        
                        .. attribute:: bridge_domain_pbb
                        
                        	Bridge Domain PBB
                        	**type**\:   :py:class:`BridgeDomainPbb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb>`
                        
                        .. attribute:: coupled_mode
                        
                        	Coupled\-mode configuration
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: dai
                        
                        	Dynamic ARP Inspection
                        	**type**\:   :py:class:`Dai <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai>`
                        
                        .. attribute:: dhcp
                        
                        	DHCPv4 Snooping profile name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: flooding
                        
                        	Disable flooding
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: flooding_unknown_unicast
                        
                        	Disable Unknown Unicast flooding
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: igmp_snooping
                        
                        	Attach IGMP Snooping Profile Name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: igmp_snooping_disable
                        
                        	Disable IGMP Snooping
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: ip_source_guard
                        
                        	IP Source Guard
                        	**type**\:   :py:class:`IpSourceGuard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard>`
                        
                        .. attribute:: member_vnis
                        
                        	Bridge Domain VxLAN Network Identifier Table
                        	**type**\:   :py:class:`MemberVnis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis>`
                        
                        .. attribute:: mld_snooping
                        
                        	Attach MLD Snooping Profile Name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: nv_satellite
                        
                        	nV Satellite
                        	**type**\:   :py:class:`NvSatellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite>`
                        
                        .. attribute:: routed_interfaces
                        
                        	Bridge Domain Routed Interface Table
                        	**type**\:   :py:class:`RoutedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces>`
                        
                        .. attribute:: shutdown
                        
                        	shutdown the Bridge Domain
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: transport_mode
                        
                        	Bridge Domain Transport mode
                        	**type**\:   :py:class:`BridgeDomainTransportMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BridgeDomainTransportMode>`
                        
                        .. attribute:: vfis
                        
                        	Specify the virtual forwarding interface name
                        	**type**\:   :py:class:`Vfis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain, self).__init__()

                            self.yang_name = "bridge-domain"
                            self.yang_parent_name = "bridge-domains"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"access-vfis" : ("access_vfis", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis), "bd-attachment-circuits" : ("bd_attachment_circuits", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits), "bd-pseudowire-evpns" : ("bd_pseudowire_evpns", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns), "bd-pseudowires" : ("bd_pseudowires", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires), "bd-storm-controls" : ("bd_storm_controls", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls), "bridge-domain-evis" : ("bridge_domain_evis", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis), "bridge-domain-mac" : ("bridge_domain_mac", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac), "bridge-domain-pbb" : ("bridge_domain_pbb", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb), "dai" : ("dai", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai), "ip-source-guard" : ("ip_source_guard", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard), "member-vnis" : ("member_vnis", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis), "nv-satellite" : ("nv_satellite", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite), "routed-interfaces" : ("routed_interfaces", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces), "vfis" : ("vfis", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis)}
                            self._child_list_classes = {}

                            self.name = YLeaf(YType.str, "name")

                            self.bridge_description = YLeaf(YType.str, "bridge-description")

                            self.bridge_domain_mtu = YLeaf(YType.uint32, "bridge-domain-mtu")

                            self.coupled_mode = YLeaf(YType.empty, "coupled-mode")

                            self.dhcp = YLeaf(YType.str, "dhcp")

                            self.flooding = YLeaf(YType.empty, "flooding")

                            self.flooding_unknown_unicast = YLeaf(YType.empty, "flooding-unknown-unicast")

                            self.igmp_snooping = YLeaf(YType.str, "igmp-snooping")

                            self.igmp_snooping_disable = YLeaf(YType.empty, "igmp-snooping-disable")

                            self.mld_snooping = YLeaf(YType.str, "mld-snooping")

                            self.shutdown = YLeaf(YType.empty, "shutdown")

                            self.transport_mode = YLeaf(YType.enumeration, "transport-mode")

                            self.access_vfis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis()
                            self.access_vfis.parent = self
                            self._children_name_map["access_vfis"] = "access-vfis"
                            self._children_yang_names.add("access-vfis")

                            self.bd_attachment_circuits = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits()
                            self.bd_attachment_circuits.parent = self
                            self._children_name_map["bd_attachment_circuits"] = "bd-attachment-circuits"
                            self._children_yang_names.add("bd-attachment-circuits")

                            self.bd_pseudowire_evpns = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns()
                            self.bd_pseudowire_evpns.parent = self
                            self._children_name_map["bd_pseudowire_evpns"] = "bd-pseudowire-evpns"
                            self._children_yang_names.add("bd-pseudowire-evpns")

                            self.bd_pseudowires = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires()
                            self.bd_pseudowires.parent = self
                            self._children_name_map["bd_pseudowires"] = "bd-pseudowires"
                            self._children_yang_names.add("bd-pseudowires")

                            self.bd_storm_controls = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls()
                            self.bd_storm_controls.parent = self
                            self._children_name_map["bd_storm_controls"] = "bd-storm-controls"
                            self._children_yang_names.add("bd-storm-controls")

                            self.bridge_domain_evis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis()
                            self.bridge_domain_evis.parent = self
                            self._children_name_map["bridge_domain_evis"] = "bridge-domain-evis"
                            self._children_yang_names.add("bridge-domain-evis")

                            self.bridge_domain_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac()
                            self.bridge_domain_mac.parent = self
                            self._children_name_map["bridge_domain_mac"] = "bridge-domain-mac"
                            self._children_yang_names.add("bridge-domain-mac")

                            self.bridge_domain_pbb = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb()
                            self.bridge_domain_pbb.parent = self
                            self._children_name_map["bridge_domain_pbb"] = "bridge-domain-pbb"
                            self._children_yang_names.add("bridge-domain-pbb")

                            self.dai = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai()
                            self.dai.parent = self
                            self._children_name_map["dai"] = "dai"
                            self._children_yang_names.add("dai")

                            self.ip_source_guard = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard()
                            self.ip_source_guard.parent = self
                            self._children_name_map["ip_source_guard"] = "ip-source-guard"
                            self._children_yang_names.add("ip-source-guard")

                            self.member_vnis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis()
                            self.member_vnis.parent = self
                            self._children_name_map["member_vnis"] = "member-vnis"
                            self._children_yang_names.add("member-vnis")

                            self.nv_satellite = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite()
                            self.nv_satellite.parent = self
                            self._children_name_map["nv_satellite"] = "nv-satellite"
                            self._children_yang_names.add("nv-satellite")

                            self.routed_interfaces = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces()
                            self.routed_interfaces.parent = self
                            self._children_name_map["routed_interfaces"] = "routed-interfaces"
                            self._children_yang_names.add("routed-interfaces")

                            self.vfis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis()
                            self.vfis.parent = self
                            self._children_name_map["vfis"] = "vfis"
                            self._children_yang_names.add("vfis")
                            self._segment_path = lambda: "bridge-domain" + "[name='" + self.name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain, ['name', 'bridge_description', 'bridge_domain_mtu', 'coupled_mode', 'dhcp', 'flooding', 'flooding_unknown_unicast', 'igmp_snooping', 'igmp_snooping_disable', 'mld_snooping', 'shutdown', 'transport_mode'], name, value)


                        class AccessVfis(Entity):
                            """
                            Specify the access virtual forwarding
                            interface name
                            
                            .. attribute:: access_vfi
                            
                            	Name of the Acess Virtual Forwarding Interface
                            	**type**\: list of    :py:class:`AccessVfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis, self).__init__()

                                self.yang_name = "access-vfis"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"access-vfi" : ("access_vfi", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi)}

                                self.access_vfi = YList(self)
                                self._segment_path = lambda: "access-vfis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis, [], name, value)


                            class AccessVfi(Entity):
                                """
                                Name of the Acess Virtual Forwarding
                                Interface
                                
                                .. attribute:: name  <key>
                                
                                	Name of the AccessVirtual Forwarding Interface
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: access_vfi_pseudowires
                                
                                	List of pseudowires
                                	**type**\:   :py:class:`AccessVfiPseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires>`
                                
                                .. attribute:: access_vfi_shutdown
                                
                                	shutdown the AccessVfi
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi, self).__init__()

                                    self.yang_name = "access-vfi"
                                    self.yang_parent_name = "access-vfis"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"access-vfi-pseudowires" : ("access_vfi_pseudowires", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires)}
                                    self._child_list_classes = {}

                                    self.name = YLeaf(YType.str, "name")

                                    self.access_vfi_shutdown = YLeaf(YType.empty, "access-vfi-shutdown")

                                    self.access_vfi_pseudowires = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires()
                                    self.access_vfi_pseudowires.parent = self
                                    self._children_name_map["access_vfi_pseudowires"] = "access-vfi-pseudowires"
                                    self._children_yang_names.add("access-vfi-pseudowires")
                                    self._segment_path = lambda: "access-vfi" + "[name='" + self.name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi, ['name', 'access_vfi_shutdown'], name, value)


                                class AccessVfiPseudowires(Entity):
                                    """
                                    List of pseudowires
                                    
                                    .. attribute:: access_vfi_pseudowire
                                    
                                    	Pseudowire configuration
                                    	**type**\: list of    :py:class:`AccessVfiPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires, self).__init__()

                                        self.yang_name = "access-vfi-pseudowires"
                                        self.yang_parent_name = "access-vfi"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"access-vfi-pseudowire" : ("access_vfi_pseudowire", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire)}

                                        self.access_vfi_pseudowire = YList(self)
                                        self._segment_path = lambda: "access-vfi-pseudowires"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires, [], name, value)


                                    class AccessVfiPseudowire(Entity):
                                        """
                                        Pseudowire configuration
                                        
                                        .. attribute:: neighbor  <key>
                                        
                                        	Neighbor IP address
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: pseudowire_id  <key>
                                        
                                        	Pseudowire ID
                                        	**type**\:  int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: access_vfi_pseudowire_static_mac_addresses
                                        
                                        	Static Mac Address Table
                                        	**type**\:   :py:class:`AccessVfiPseudowireStaticMacAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses>`
                                        
                                        .. attribute:: access_vfi_pw_class
                                        
                                        	Pseudowire class template name to use for this pseudowire
                                        	**type**\:  str
                                        
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
                                            self._child_container_classes = {"access-vfi-pseudowire-static-mac-addresses" : ("access_vfi_pseudowire_static_mac_addresses", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses)}
                                            self._child_list_classes = {}

                                            self.neighbor = YLeaf(YType.str, "neighbor")

                                            self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                                            self.access_vfi_pw_class = YLeaf(YType.str, "access-vfi-pw-class")

                                            self.access_vfi_pseudowire_static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses()
                                            self.access_vfi_pseudowire_static_mac_addresses.parent = self
                                            self._children_name_map["access_vfi_pseudowire_static_mac_addresses"] = "access-vfi-pseudowire-static-mac-addresses"
                                            self._children_yang_names.add("access-vfi-pseudowire-static-mac-addresses")
                                            self._segment_path = lambda: "access-vfi-pseudowire" + "[neighbor='" + self.neighbor.get() + "']" + "[pseudowire-id='" + self.pseudowire_id.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire, ['neighbor', 'pseudowire_id', 'access_vfi_pw_class'], name, value)


                                        class AccessVfiPseudowireStaticMacAddresses(Entity):
                                            """
                                            Static Mac Address Table
                                            
                                            .. attribute:: access_vfi_pseudowire_static_mac_address
                                            
                                            	Static Mac Address Configuration
                                            	**type**\: list of    :py:class:`AccessVfiPseudowireStaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses, self).__init__()

                                                self.yang_name = "access-vfi-pseudowire-static-mac-addresses"
                                                self.yang_parent_name = "access-vfi-pseudowire"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"access-vfi-pseudowire-static-mac-address" : ("access_vfi_pseudowire_static_mac_address", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress)}

                                                self.access_vfi_pseudowire_static_mac_address = YList(self)
                                                self._segment_path = lambda: "access-vfi-pseudowire-static-mac-addresses"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses, [], name, value)


                                            class AccessVfiPseudowireStaticMacAddress(Entity):
                                                """
                                                Static Mac Address Configuration
                                                
                                                .. attribute:: address  <key>
                                                
                                                	Static MAC address
                                                	**type**\:  str
                                                
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
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.address = YLeaf(YType.str, "address")
                                                    self._segment_path = lambda: "access-vfi-pseudowire-static-mac-address" + "[address='" + self.address.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress, ['address'], name, value)


                        class BdAttachmentCircuits(Entity):
                            """
                            Attachment Circuit table
                            
                            .. attribute:: bd_attachment_circuit
                            
                            	Name of the Attachment Circuit
                            	**type**\: list of    :py:class:`BdAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits, self).__init__()

                                self.yang_name = "bd-attachment-circuits"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"bd-attachment-circuit" : ("bd_attachment_circuit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit)}

                                self.bd_attachment_circuit = YList(self)
                                self._segment_path = lambda: "bd-attachment-circuits"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits, [], name, value)


                            class BdAttachmentCircuit(Entity):
                                """
                                Name of the Attachment Circuit
                                
                                .. attribute:: name  <key>
                                
                                	The name of the Attachment Circuit
                                	**type**\:  str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: bdac_storm_control_types
                                
                                	Storm Control
                                	**type**\:   :py:class:`BdacStormControlTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes>`
                                
                                .. attribute:: interface_dai
                                
                                	L2 Interface Dynamic ARP Inspection
                                	**type**\:   :py:class:`InterfaceDai <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai>`
                                
                                .. attribute:: interface_flooding
                                
                                	Enable or Disable Flooding
                                	**type**\:   :py:class:`InterfaceTrafficFlood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFlood>`
                                
                                .. attribute:: interface_flooding_unknown_unicast
                                
                                	Enable or Disable Unknown Unicast Flooding
                                	**type**\:   :py:class:`InterfaceTrafficFlood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFlood>`
                                
                                .. attribute:: interface_igmp_snoop
                                
                                	Attach a IGMP Snooping profile
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: interface_ip_source_guard
                                
                                	IP Source Guard
                                	**type**\:   :py:class:`InterfaceIpSourceGuard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard>`
                                
                                .. attribute:: interface_mac
                                
                                	MAC configuration commands
                                	**type**\:   :py:class:`InterfaceMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac>`
                                
                                .. attribute:: interface_mld_snoop
                                
                                	Attach a MLD Snooping profile
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: interface_profile
                                
                                	Attach a DHCP profile
                                	**type**\:   :py:class:`InterfaceProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile>`
                                
                                .. attribute:: split_horizon
                                
                                	Split Horizon
                                	**type**\:   :py:class:`SplitHorizon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon>`
                                
                                .. attribute:: static_mac_addresses
                                
                                	Static Mac Address Table
                                	**type**\:   :py:class:`StaticMacAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit, self).__init__()

                                    self.yang_name = "bd-attachment-circuit"
                                    self.yang_parent_name = "bd-attachment-circuits"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"bdac-storm-control-types" : ("bdac_storm_control_types", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes), "interface-dai" : ("interface_dai", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai), "interface-ip-source-guard" : ("interface_ip_source_guard", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard), "interface-mac" : ("interface_mac", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac), "interface-profile" : ("interface_profile", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile), "split-horizon" : ("split_horizon", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon), "static-mac-addresses" : ("static_mac_addresses", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses)}
                                    self._child_list_classes = {}

                                    self.name = YLeaf(YType.str, "name")

                                    self.interface_flooding = YLeaf(YType.enumeration, "interface-flooding")

                                    self.interface_flooding_unknown_unicast = YLeaf(YType.enumeration, "interface-flooding-unknown-unicast")

                                    self.interface_igmp_snoop = YLeaf(YType.str, "interface-igmp-snoop")

                                    self.interface_mld_snoop = YLeaf(YType.str, "interface-mld-snoop")

                                    self.bdac_storm_control_types = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes()
                                    self.bdac_storm_control_types.parent = self
                                    self._children_name_map["bdac_storm_control_types"] = "bdac-storm-control-types"
                                    self._children_yang_names.add("bdac-storm-control-types")

                                    self.interface_dai = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai()
                                    self.interface_dai.parent = self
                                    self._children_name_map["interface_dai"] = "interface-dai"
                                    self._children_yang_names.add("interface-dai")

                                    self.interface_ip_source_guard = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard()
                                    self.interface_ip_source_guard.parent = self
                                    self._children_name_map["interface_ip_source_guard"] = "interface-ip-source-guard"
                                    self._children_yang_names.add("interface-ip-source-guard")

                                    self.interface_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac()
                                    self.interface_mac.parent = self
                                    self._children_name_map["interface_mac"] = "interface-mac"
                                    self._children_yang_names.add("interface-mac")

                                    self.interface_profile = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile()
                                    self.interface_profile.parent = self
                                    self._children_name_map["interface_profile"] = "interface-profile"
                                    self._children_yang_names.add("interface-profile")

                                    self.split_horizon = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon()
                                    self.split_horizon.parent = self
                                    self._children_name_map["split_horizon"] = "split-horizon"
                                    self._children_yang_names.add("split-horizon")

                                    self.static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses()
                                    self.static_mac_addresses.parent = self
                                    self._children_name_map["static_mac_addresses"] = "static-mac-addresses"
                                    self._children_yang_names.add("static-mac-addresses")
                                    self._segment_path = lambda: "bd-attachment-circuit" + "[name='" + self.name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit, ['name', 'interface_flooding', 'interface_flooding_unknown_unicast', 'interface_igmp_snoop', 'interface_mld_snoop'], name, value)


                                class BdacStormControlTypes(Entity):
                                    """
                                    Storm Control
                                    
                                    .. attribute:: bdac_storm_control_type
                                    
                                    	Storm Control Type
                                    	**type**\: list of    :py:class:`BdacStormControlType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes, self).__init__()

                                        self.yang_name = "bdac-storm-control-types"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"bdac-storm-control-type" : ("bdac_storm_control_type", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType)}

                                        self.bdac_storm_control_type = YList(self)
                                        self._segment_path = lambda: "bdac-storm-control-types"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes, [], name, value)


                                    class BdacStormControlType(Entity):
                                        """
                                        Storm Control Type
                                        
                                        .. attribute:: sctype  <key>
                                        
                                        	Storm Control Type
                                        	**type**\:   :py:class:`StormControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.StormControl>`
                                        
                                        .. attribute:: storm_control_unit
                                        
                                        	Specify units for Storm Control Configuration
                                        	**type**\:   :py:class:`StormControlUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType, self).__init__()

                                            self.yang_name = "bdac-storm-control-type"
                                            self.yang_parent_name = "bdac-storm-control-types"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"storm-control-unit" : ("storm_control_unit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit)}
                                            self._child_list_classes = {}

                                            self.sctype = YLeaf(YType.enumeration, "sctype")

                                            self.storm_control_unit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit()
                                            self.storm_control_unit.parent = self
                                            self._children_name_map["storm_control_unit"] = "storm-control-unit"
                                            self._children_yang_names.add("storm-control-unit")
                                            self._segment_path = lambda: "bdac-storm-control-type" + "[sctype='" + self.sctype.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType, ['sctype'], name, value)


                                        class StormControlUnit(Entity):
                                            """
                                            Specify units for Storm Control Configuration
                                            
                                            .. attribute:: kbits_per_sec
                                            
                                            	Kilobits Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                            	**type**\:  int
                                            
                                            	**range:** 64..1280000
                                            
                                            	**units**\: kbit/s
                                            
                                            .. attribute:: pkts_per_sec
                                            
                                            	Packets Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                            	**type**\:  int
                                            
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
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.kbits_per_sec = YLeaf(YType.uint32, "kbits-per-sec")

                                                self.pkts_per_sec = YLeaf(YType.uint32, "pkts-per-sec")
                                                self._segment_path = lambda: "storm-control-unit"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit, ['kbits_per_sec', 'pkts_per_sec'], name, value)


                                class InterfaceDai(Entity):
                                    """
                                    L2 Interface Dynamic ARP Inspection
                                    
                                    .. attribute:: disable
                                    
                                    	Disable L2 Interface Dynamic ARP Inspection
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable L2 Interface Dynamic ARP Inspection
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: interface_dai_address_validation
                                    
                                    	Address Validation
                                    	**type**\:   :py:class:`InterfaceDaiAddressValidation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation>`
                                    
                                    .. attribute:: logging
                                    
                                    	Logging Type
                                    	**type**\:   :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai, self).__init__()

                                        self.yang_name = "interface-dai"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"interface-dai-address-validation" : ("interface_dai_address_validation", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation)}
                                        self._child_list_classes = {}

                                        self.disable = YLeaf(YType.empty, "disable")

                                        self.enable = YLeaf(YType.empty, "enable")

                                        self.logging = YLeaf(YType.enumeration, "logging")

                                        self.interface_dai_address_validation = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation()
                                        self.interface_dai_address_validation.parent = self
                                        self._children_name_map["interface_dai_address_validation"] = "interface-dai-address-validation"
                                        self._children_yang_names.add("interface-dai-address-validation")
                                        self._segment_path = lambda: "interface-dai"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai, ['disable', 'enable', 'logging'], name, value)


                                    class InterfaceDaiAddressValidation(Entity):
                                        """
                                        Address Validation
                                        
                                        .. attribute:: destination_mac_verification
                                        
                                        	Destination MAC Verification
                                        	**type**\:   :py:class:`L2vpnVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable Address Validation
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: ipv4_verification
                                        
                                        	IPv4 Verification
                                        	**type**\:   :py:class:`L2vpnVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification>`
                                        
                                        .. attribute:: source_mac_verification
                                        
                                        	Source MAC Verification
                                        	**type**\:   :py:class:`L2vpnVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation, self).__init__()

                                            self.yang_name = "interface-dai-address-validation"
                                            self.yang_parent_name = "interface-dai"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.destination_mac_verification = YLeaf(YType.enumeration, "destination-mac-verification")

                                            self.enable = YLeaf(YType.empty, "enable")

                                            self.ipv4_verification = YLeaf(YType.enumeration, "ipv4-verification")

                                            self.source_mac_verification = YLeaf(YType.enumeration, "source-mac-verification")
                                            self._segment_path = lambda: "interface-dai-address-validation"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation, ['destination_mac_verification', 'enable', 'ipv4_verification', 'source_mac_verification'], name, value)


                                class InterfaceIpSourceGuard(Entity):
                                    """
                                    IP Source Guard
                                    
                                    .. attribute:: disable
                                    
                                    	Disable L2 Interface Dynamic IP source guard
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable IP Source Guard
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: logging
                                    
                                    	Logging Type
                                    	**type**\:   :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard, self).__init__()

                                        self.yang_name = "interface-ip-source-guard"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.disable = YLeaf(YType.empty, "disable")

                                        self.enable = YLeaf(YType.empty, "enable")

                                        self.logging = YLeaf(YType.enumeration, "logging")
                                        self._segment_path = lambda: "interface-ip-source-guard"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard, ['disable', 'enable', 'logging'], name, value)


                                class InterfaceMac(Entity):
                                    """
                                    MAC configuration commands
                                    
                                    .. attribute:: interface_mac_aging
                                    
                                    	MAC\-Aging configuration commands
                                    	**type**\:   :py:class:`InterfaceMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging>`
                                    
                                    .. attribute:: interface_mac_learning
                                    
                                    	Enable Mac Learning
                                    	**type**\:   :py:class:`MacLearn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLearn>`
                                    
                                    .. attribute:: interface_mac_limit
                                    
                                    	MAC\-Limit configuration commands
                                    	**type**\:   :py:class:`InterfaceMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit>`
                                    
                                    .. attribute:: interface_mac_port_down_flush
                                    
                                    	Enable/Disable MAC Flush When Port goes down
                                    	**type**\:   :py:class:`PortDownFlush <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.PortDownFlush>`
                                    
                                    .. attribute:: interface_mac_secure
                                    
                                    	MAC Secure
                                    	**type**\:   :py:class:`InterfaceMacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac, self).__init__()

                                        self.yang_name = "interface-mac"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"interface-mac-aging" : ("interface_mac_aging", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging), "interface-mac-limit" : ("interface_mac_limit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit), "interface-mac-secure" : ("interface_mac_secure", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure)}
                                        self._child_list_classes = {}

                                        self.interface_mac_learning = YLeaf(YType.enumeration, "interface-mac-learning")

                                        self.interface_mac_port_down_flush = YLeaf(YType.enumeration, "interface-mac-port-down-flush")

                                        self.interface_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging()
                                        self.interface_mac_aging.parent = self
                                        self._children_name_map["interface_mac_aging"] = "interface-mac-aging"
                                        self._children_yang_names.add("interface-mac-aging")

                                        self.interface_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit()
                                        self.interface_mac_limit.parent = self
                                        self._children_name_map["interface_mac_limit"] = "interface-mac-limit"
                                        self._children_yang_names.add("interface-mac-limit")

                                        self.interface_mac_secure = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure()
                                        self.interface_mac_secure.parent = self
                                        self._children_name_map["interface_mac_secure"] = "interface-mac-secure"
                                        self._children_yang_names.add("interface-mac-secure")
                                        self._segment_path = lambda: "interface-mac"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac, ['interface_mac_learning', 'interface_mac_port_down_flush'], name, value)


                                    class InterfaceMacAging(Entity):
                                        """
                                        MAC\-Aging configuration commands
                                        
                                        .. attribute:: interface_mac_aging_time
                                        
                                        	Mac Aging Time
                                        	**type**\:  int
                                        
                                        	**range:** 300..30000
                                        
                                        .. attribute:: interface_mac_aging_type
                                        
                                        	MAC address aging type
                                        	**type**\:   :py:class:`MacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAging>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging, self).__init__()

                                            self.yang_name = "interface-mac-aging"
                                            self.yang_parent_name = "interface-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.interface_mac_aging_time = YLeaf(YType.uint32, "interface-mac-aging-time")

                                            self.interface_mac_aging_type = YLeaf(YType.enumeration, "interface-mac-aging-type")
                                            self._segment_path = lambda: "interface-mac-aging"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging, ['interface_mac_aging_time', 'interface_mac_aging_type'], name, value)


                                    class InterfaceMacLimit(Entity):
                                        """
                                        MAC\-Limit configuration commands
                                        
                                        .. attribute:: interface_mac_limit_action
                                        
                                        	Interface MAC address limit enforcement action
                                        	**type**\:   :py:class:`MacLimitAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction>`
                                        
                                        .. attribute:: interface_mac_limit_max
                                        
                                        	Number of MAC addresses on an Interface after which MAC limit action is taken
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: interface_mac_limit_notif
                                        
                                        	MAC address limit notification action in a Interface
                                        	**type**\:   :py:class:`MacNotification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotification>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit, self).__init__()

                                            self.yang_name = "interface-mac-limit"
                                            self.yang_parent_name = "interface-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.interface_mac_limit_action = YLeaf(YType.enumeration, "interface-mac-limit-action")

                                            self.interface_mac_limit_max = YLeaf(YType.uint32, "interface-mac-limit-max")

                                            self.interface_mac_limit_notif = YLeaf(YType.enumeration, "interface-mac-limit-notif")
                                            self._segment_path = lambda: "interface-mac-limit"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit, ['interface_mac_limit_action', 'interface_mac_limit_max', 'interface_mac_limit_notif'], name, value)


                                    class InterfaceMacSecure(Entity):
                                        """
                                        MAC Secure
                                        
                                        .. attribute:: action
                                        
                                        	MAC secure enforcement action
                                        	**type**\:   :py:class:`MacSecureAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacSecureAction>`
                                        
                                        .. attribute:: disable
                                        
                                        	Disable L2 Interface MAC Secure
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable MAC Secure
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: logging
                                        
                                        	MAC Secure Logging
                                        	**type**\:   :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure, self).__init__()

                                            self.yang_name = "interface-mac-secure"
                                            self.yang_parent_name = "interface-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.action = YLeaf(YType.enumeration, "action")

                                            self.disable = YLeaf(YType.empty, "disable")

                                            self.enable = YLeaf(YType.empty, "enable")

                                            self.logging = YLeaf(YType.enumeration, "logging")
                                            self._segment_path = lambda: "interface-mac-secure"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure, ['action', 'disable', 'enable', 'logging'], name, value)


                                class InterfaceProfile(Entity):
                                    """
                                    Attach a DHCP profile
                                    
                                    .. attribute:: dhcp_snooping_id
                                    
                                    	Disable DHCP snooping
                                    	**type**\:  str
                                    
                                    .. attribute:: profile_id
                                    
                                    	Set the snooping profile
                                    	**type**\:   :py:class:`InterfaceProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile, self).__init__()

                                        self.yang_name = "interface-profile"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.dhcp_snooping_id = YLeaf(YType.str, "dhcp-snooping-id")

                                        self.profile_id = YLeaf(YType.enumeration, "profile-id")
                                        self._segment_path = lambda: "interface-profile"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile, ['dhcp_snooping_id', 'profile_id'], name, value)


                                class SplitHorizon(Entity):
                                    """
                                    Split Horizon
                                    
                                    .. attribute:: split_horizon_group_id
                                    
                                    	Split Horizon Group ID
                                    	**type**\:   :py:class:`SplitHorizonGroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon, self).__init__()

                                        self.yang_name = "split-horizon"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"split-horizon-group-id" : ("split_horizon_group_id", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId)}
                                        self._child_list_classes = {}

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
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId, self).__init__()

                                            self.yang_name = "split-horizon-group-id"
                                            self.yang_parent_name = "split-horizon"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.enable = YLeaf(YType.empty, "enable")
                                            self._segment_path = lambda: "split-horizon-group-id"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId, ['enable'], name, value)


                                class StaticMacAddresses(Entity):
                                    """
                                    Static Mac Address Table
                                    
                                    .. attribute:: static_mac_address
                                    
                                    	Static Mac Address Configuration
                                    	**type**\: list of    :py:class:`StaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses, self).__init__()

                                        self.yang_name = "static-mac-addresses"
                                        self.yang_parent_name = "bd-attachment-circuit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"static-mac-address" : ("static_mac_address", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress)}

                                        self.static_mac_address = YList(self)
                                        self._segment_path = lambda: "static-mac-addresses"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses, [], name, value)


                                    class StaticMacAddress(Entity):
                                        """
                                        Static Mac Address Configuration
                                        
                                        .. attribute:: address  <key>
                                        
                                        	Static MAC address
                                        	**type**\:  str
                                        
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
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.address = YLeaf(YType.str, "address")
                                            self._segment_path = lambda: "static-mac-address" + "[address='" + self.address.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress, ['address'], name, value)


                        class BdPseudowireEvpns(Entity):
                            """
                            List of EVPN pseudowires
                            
                            .. attribute:: bd_pseudowire_evpn
                            
                            	EVPN Pseudowire configuration
                            	**type**\: list of    :py:class:`BdPseudowireEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns, self).__init__()

                                self.yang_name = "bd-pseudowire-evpns"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"bd-pseudowire-evpn" : ("bd_pseudowire_evpn", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn)}

                                self.bd_pseudowire_evpn = YList(self)
                                self._segment_path = lambda: "bd-pseudowire-evpns"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns, [], name, value)


                            class BdPseudowireEvpn(Entity):
                                """
                                EVPN Pseudowire configuration
                                
                                .. attribute:: eviid  <key>
                                
                                	Ethernet VPN ID
                                	**type**\:  int
                                
                                	**range:** 1..65534
                                
                                .. attribute:: acid  <key>
                                
                                	AC ID
                                	**type**\:  int
                                
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
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.eviid = YLeaf(YType.uint32, "eviid")

                                    self.acid = YLeaf(YType.uint32, "acid")
                                    self._segment_path = lambda: "bd-pseudowire-evpn" + "[eviid='" + self.eviid.get() + "']" + "[acid='" + self.acid.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn, ['eviid', 'acid'], name, value)


                        class BdPseudowires(Entity):
                            """
                            List of pseudowires
                            
                            .. attribute:: bd_pseudowire
                            
                            	Pseudowire configuration
                            	**type**\: list of    :py:class:`BdPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires, self).__init__()

                                self.yang_name = "bd-pseudowires"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"bd-pseudowire" : ("bd_pseudowire", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire)}

                                self.bd_pseudowire = YList(self)
                                self._segment_path = lambda: "bd-pseudowires"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires, [], name, value)


                            class BdPseudowire(Entity):
                                """
                                Pseudowire configuration
                                
                                .. attribute:: neighbor  <key>
                                
                                	Neighbor IP address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: pseudowire_id  <key>
                                
                                	Pseudowire ID
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: bd_pw_class
                                
                                	PW class template name to use for this pseudowire
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: bd_pw_mpls_static_labels
                                
                                	MPLS static labels
                                	**type**\:   :py:class:`BdPwMplsStaticLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels>`
                                
                                .. attribute:: bd_pw_split_horizon
                                
                                	Split Horizon
                                	**type**\:   :py:class:`BdPwSplitHorizon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon>`
                                
                                .. attribute:: bd_pw_static_mac_addresses
                                
                                	Static Mac Address Table
                                	**type**\:   :py:class:`BdPwStaticMacAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses>`
                                
                                .. attribute:: bdpw_storm_control_types
                                
                                	Storm Control
                                	**type**\:   :py:class:`BdpwStormControlTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes>`
                                
                                .. attribute:: bridge_domain_backup_pseudowires
                                
                                	List of pseudowires
                                	**type**\:   :py:class:`BridgeDomainBackupPseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires>`
                                
                                .. attribute:: pseudowire_dai
                                
                                	Access Pseudowire Dynamic ARP Inspection
                                	**type**\:   :py:class:`PseudowireDai <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai>`
                                
                                .. attribute:: pseudowire_flooding
                                
                                	Bridge\-domain Pseudowire flooding
                                	**type**\:   :py:class:`InterfaceTrafficFlood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFlood>`
                                
                                .. attribute:: pseudowire_flooding_unknown_unicast
                                
                                	Bridge\-domain Pseudowire flooding Unknown Unicast
                                	**type**\:   :py:class:`InterfaceTrafficFlood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFlood>`
                                
                                .. attribute:: pseudowire_igmp_snoop
                                
                                	Attach a IGMP Snooping profile
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: pseudowire_ip_source_guard
                                
                                	IP Source Guard
                                	**type**\:   :py:class:`PseudowireIpSourceGuard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard>`
                                
                                .. attribute:: pseudowire_mac
                                
                                	Bridge\-domain Pseudowire MAC configuration commands
                                	**type**\:   :py:class:`PseudowireMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac>`
                                
                                .. attribute:: pseudowire_mld_snoop
                                
                                	Attach a MLD Snooping profile
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: pseudowire_profile
                                
                                	Attach a DHCP profile
                                	**type**\:   :py:class:`PseudowireProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire, self).__init__()

                                    self.yang_name = "bd-pseudowire"
                                    self.yang_parent_name = "bd-pseudowires"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"bd-pw-mpls-static-labels" : ("bd_pw_mpls_static_labels", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels), "bd-pw-split-horizon" : ("bd_pw_split_horizon", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon), "bd-pw-static-mac-addresses" : ("bd_pw_static_mac_addresses", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses), "bdpw-storm-control-types" : ("bdpw_storm_control_types", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes), "bridge-domain-backup-pseudowires" : ("bridge_domain_backup_pseudowires", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires), "pseudowire-dai" : ("pseudowire_dai", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai), "pseudowire-ip-source-guard" : ("pseudowire_ip_source_guard", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard), "pseudowire-mac" : ("pseudowire_mac", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac), "pseudowire-profile" : ("pseudowire_profile", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile)}
                                    self._child_list_classes = {}

                                    self.neighbor = YLeaf(YType.str, "neighbor")

                                    self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                                    self.bd_pw_class = YLeaf(YType.str, "bd-pw-class")

                                    self.pseudowire_flooding = YLeaf(YType.enumeration, "pseudowire-flooding")

                                    self.pseudowire_flooding_unknown_unicast = YLeaf(YType.enumeration, "pseudowire-flooding-unknown-unicast")

                                    self.pseudowire_igmp_snoop = YLeaf(YType.str, "pseudowire-igmp-snoop")

                                    self.pseudowire_mld_snoop = YLeaf(YType.str, "pseudowire-mld-snoop")

                                    self.bd_pw_mpls_static_labels = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels()
                                    self.bd_pw_mpls_static_labels.parent = self
                                    self._children_name_map["bd_pw_mpls_static_labels"] = "bd-pw-mpls-static-labels"
                                    self._children_yang_names.add("bd-pw-mpls-static-labels")

                                    self.bd_pw_split_horizon = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon()
                                    self.bd_pw_split_horizon.parent = self
                                    self._children_name_map["bd_pw_split_horizon"] = "bd-pw-split-horizon"
                                    self._children_yang_names.add("bd-pw-split-horizon")

                                    self.bd_pw_static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses()
                                    self.bd_pw_static_mac_addresses.parent = self
                                    self._children_name_map["bd_pw_static_mac_addresses"] = "bd-pw-static-mac-addresses"
                                    self._children_yang_names.add("bd-pw-static-mac-addresses")

                                    self.bdpw_storm_control_types = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes()
                                    self.bdpw_storm_control_types.parent = self
                                    self._children_name_map["bdpw_storm_control_types"] = "bdpw-storm-control-types"
                                    self._children_yang_names.add("bdpw-storm-control-types")

                                    self.bridge_domain_backup_pseudowires = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires()
                                    self.bridge_domain_backup_pseudowires.parent = self
                                    self._children_name_map["bridge_domain_backup_pseudowires"] = "bridge-domain-backup-pseudowires"
                                    self._children_yang_names.add("bridge-domain-backup-pseudowires")

                                    self.pseudowire_dai = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai()
                                    self.pseudowire_dai.parent = self
                                    self._children_name_map["pseudowire_dai"] = "pseudowire-dai"
                                    self._children_yang_names.add("pseudowire-dai")

                                    self.pseudowire_ip_source_guard = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard()
                                    self.pseudowire_ip_source_guard.parent = self
                                    self._children_name_map["pseudowire_ip_source_guard"] = "pseudowire-ip-source-guard"
                                    self._children_yang_names.add("pseudowire-ip-source-guard")

                                    self.pseudowire_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac()
                                    self.pseudowire_mac.parent = self
                                    self._children_name_map["pseudowire_mac"] = "pseudowire-mac"
                                    self._children_yang_names.add("pseudowire-mac")

                                    self.pseudowire_profile = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile()
                                    self.pseudowire_profile.parent = self
                                    self._children_name_map["pseudowire_profile"] = "pseudowire-profile"
                                    self._children_yang_names.add("pseudowire-profile")
                                    self._segment_path = lambda: "bd-pseudowire" + "[neighbor='" + self.neighbor.get() + "']" + "[pseudowire-id='" + self.pseudowire_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire, ['neighbor', 'pseudowire_id', 'bd_pw_class', 'pseudowire_flooding', 'pseudowire_flooding_unknown_unicast', 'pseudowire_igmp_snoop', 'pseudowire_mld_snoop'], name, value)


                                class BdPwMplsStaticLabels(Entity):
                                    """
                                    MPLS static labels
                                    
                                    .. attribute:: local_static_label
                                    
                                    	Pseudowire local static label
                                    	**type**\:  int
                                    
                                    	**range:** 16..1048575
                                    
                                    .. attribute:: remote_static_label
                                    
                                    	Pseudowire remote static label
                                    	**type**\:  int
                                    
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
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.local_static_label = YLeaf(YType.uint32, "local-static-label")

                                        self.remote_static_label = YLeaf(YType.uint32, "remote-static-label")
                                        self._segment_path = lambda: "bd-pw-mpls-static-labels"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels, ['local_static_label', 'remote_static_label'], name, value)


                                class BdPwSplitHorizon(Entity):
                                    """
                                    Split Horizon
                                    
                                    .. attribute:: bd_pw_split_horizon_group
                                    
                                    	Split Horizon Group
                                    	**type**\:   :py:class:`BdPwSplitHorizonGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon, self).__init__()

                                        self.yang_name = "bd-pw-split-horizon"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"bd-pw-split-horizon-group" : ("bd_pw_split_horizon_group", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup)}
                                        self._child_list_classes = {}

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
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup, self).__init__()

                                            self.yang_name = "bd-pw-split-horizon-group"
                                            self.yang_parent_name = "bd-pw-split-horizon"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.enable = YLeaf(YType.empty, "enable")
                                            self._segment_path = lambda: "bd-pw-split-horizon-group"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup, ['enable'], name, value)


                                class BdPwStaticMacAddresses(Entity):
                                    """
                                    Static Mac Address Table
                                    
                                    .. attribute:: bd_pw_static_mac_address
                                    
                                    	Static Mac Address Configuration
                                    	**type**\: list of    :py:class:`BdPwStaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses, self).__init__()

                                        self.yang_name = "bd-pw-static-mac-addresses"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"bd-pw-static-mac-address" : ("bd_pw_static_mac_address", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress)}

                                        self.bd_pw_static_mac_address = YList(self)
                                        self._segment_path = lambda: "bd-pw-static-mac-addresses"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses, [], name, value)


                                    class BdPwStaticMacAddress(Entity):
                                        """
                                        Static Mac Address Configuration
                                        
                                        .. attribute:: address  <key>
                                        
                                        	Static MAC address
                                        	**type**\:  str
                                        
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
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.address = YLeaf(YType.str, "address")
                                            self._segment_path = lambda: "bd-pw-static-mac-address" + "[address='" + self.address.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress, ['address'], name, value)


                                class BdpwStormControlTypes(Entity):
                                    """
                                    Storm Control
                                    
                                    .. attribute:: bdpw_storm_control_type
                                    
                                    	Storm Control Type
                                    	**type**\: list of    :py:class:`BdpwStormControlType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes, self).__init__()

                                        self.yang_name = "bdpw-storm-control-types"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"bdpw-storm-control-type" : ("bdpw_storm_control_type", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType)}

                                        self.bdpw_storm_control_type = YList(self)
                                        self._segment_path = lambda: "bdpw-storm-control-types"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes, [], name, value)


                                    class BdpwStormControlType(Entity):
                                        """
                                        Storm Control Type
                                        
                                        .. attribute:: sctype  <key>
                                        
                                        	Storm Control Type
                                        	**type**\:   :py:class:`StormControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.StormControl>`
                                        
                                        .. attribute:: storm_control_unit
                                        
                                        	Specify units for Storm Control Configuration
                                        	**type**\:   :py:class:`StormControlUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType, self).__init__()

                                            self.yang_name = "bdpw-storm-control-type"
                                            self.yang_parent_name = "bdpw-storm-control-types"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"storm-control-unit" : ("storm_control_unit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit)}
                                            self._child_list_classes = {}

                                            self.sctype = YLeaf(YType.enumeration, "sctype")

                                            self.storm_control_unit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit()
                                            self.storm_control_unit.parent = self
                                            self._children_name_map["storm_control_unit"] = "storm-control-unit"
                                            self._children_yang_names.add("storm-control-unit")
                                            self._segment_path = lambda: "bdpw-storm-control-type" + "[sctype='" + self.sctype.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType, ['sctype'], name, value)


                                        class StormControlUnit(Entity):
                                            """
                                            Specify units for Storm Control Configuration
                                            
                                            .. attribute:: kbits_per_sec
                                            
                                            	Kilobits Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                            	**type**\:  int
                                            
                                            	**range:** 64..1280000
                                            
                                            	**units**\: kbit/s
                                            
                                            .. attribute:: pkts_per_sec
                                            
                                            	Packets Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                            	**type**\:  int
                                            
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
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.kbits_per_sec = YLeaf(YType.uint32, "kbits-per-sec")

                                                self.pkts_per_sec = YLeaf(YType.uint32, "pkts-per-sec")
                                                self._segment_path = lambda: "storm-control-unit"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit, ['kbits_per_sec', 'pkts_per_sec'], name, value)


                                class BridgeDomainBackupPseudowires(Entity):
                                    """
                                    List of pseudowires
                                    
                                    .. attribute:: bridge_domain_backup_pseudowire
                                    
                                    	Backup pseudowire configuration
                                    	**type**\: list of    :py:class:`BridgeDomainBackupPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires, self).__init__()

                                        self.yang_name = "bridge-domain-backup-pseudowires"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"bridge-domain-backup-pseudowire" : ("bridge_domain_backup_pseudowire", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire)}

                                        self.bridge_domain_backup_pseudowire = YList(self)
                                        self._segment_path = lambda: "bridge-domain-backup-pseudowires"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires, [], name, value)


                                    class BridgeDomainBackupPseudowire(Entity):
                                        """
                                        Backup pseudowire configuration
                                        
                                        .. attribute:: neighbor  <key>
                                        
                                        	Neighbor IP address
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: pseudowire_id  <key>
                                        
                                        	Pseudowire ID
                                        	**type**\:  int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: bridge_domain_backup_pw_class
                                        
                                        	PW class template name to use for this pseudowire
                                        	**type**\:  str
                                        
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
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.neighbor = YLeaf(YType.str, "neighbor")

                                            self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                                            self.bridge_domain_backup_pw_class = YLeaf(YType.str, "bridge-domain-backup-pw-class")
                                            self._segment_path = lambda: "bridge-domain-backup-pseudowire" + "[neighbor='" + self.neighbor.get() + "']" + "[pseudowire-id='" + self.pseudowire_id.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire, ['neighbor', 'pseudowire_id', 'bridge_domain_backup_pw_class'], name, value)


                                class PseudowireDai(Entity):
                                    """
                                    Access Pseudowire Dynamic ARP Inspection
                                    
                                    .. attribute:: disable
                                    
                                    	Disable Dynamic ARP Inspection
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable Access Pseudowire Dynamic ARP Inspection
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: logging
                                    
                                    	Logging Type
                                    	**type**\:   :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                    
                                    .. attribute:: pseudowire_dai_address_validation
                                    
                                    	Address Validation
                                    	**type**\:   :py:class:`PseudowireDaiAddressValidation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai, self).__init__()

                                        self.yang_name = "pseudowire-dai"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"pseudowire-dai-address-validation" : ("pseudowire_dai_address_validation", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation)}
                                        self._child_list_classes = {}

                                        self.disable = YLeaf(YType.empty, "disable")

                                        self.enable = YLeaf(YType.empty, "enable")

                                        self.logging = YLeaf(YType.enumeration, "logging")

                                        self.pseudowire_dai_address_validation = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation()
                                        self.pseudowire_dai_address_validation.parent = self
                                        self._children_name_map["pseudowire_dai_address_validation"] = "pseudowire-dai-address-validation"
                                        self._children_yang_names.add("pseudowire-dai-address-validation")
                                        self._segment_path = lambda: "pseudowire-dai"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai, ['disable', 'enable', 'logging'], name, value)


                                    class PseudowireDaiAddressValidation(Entity):
                                        """
                                        Address Validation
                                        
                                        .. attribute:: destination_mac_verification
                                        
                                        	Destination MAC Verification
                                        	**type**\:   :py:class:`L2vpnVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification>`
                                        
                                        .. attribute:: ipv4_verification
                                        
                                        	IPv4 Verification
                                        	**type**\:   :py:class:`L2vpnVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification>`
                                        
                                        .. attribute:: source_mac_verification
                                        
                                        	Source MAC Verification
                                        	**type**\:   :py:class:`L2vpnVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation, self).__init__()

                                            self.yang_name = "pseudowire-dai-address-validation"
                                            self.yang_parent_name = "pseudowire-dai"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.destination_mac_verification = YLeaf(YType.enumeration, "destination-mac-verification")

                                            self.ipv4_verification = YLeaf(YType.enumeration, "ipv4-verification")

                                            self.source_mac_verification = YLeaf(YType.enumeration, "source-mac-verification")
                                            self._segment_path = lambda: "pseudowire-dai-address-validation"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation, ['destination_mac_verification', 'ipv4_verification', 'source_mac_verification'], name, value)


                                class PseudowireIpSourceGuard(Entity):
                                    """
                                    IP Source Guard
                                    
                                    .. attribute:: disable
                                    
                                    	Disable Dynamic IP source guard
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable IP Source Guard
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: logging
                                    
                                    	Logging Type
                                    	**type**\:   :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard, self).__init__()

                                        self.yang_name = "pseudowire-ip-source-guard"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.disable = YLeaf(YType.empty, "disable")

                                        self.enable = YLeaf(YType.empty, "enable")

                                        self.logging = YLeaf(YType.enumeration, "logging")
                                        self._segment_path = lambda: "pseudowire-ip-source-guard"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard, ['disable', 'enable', 'logging'], name, value)


                                class PseudowireMac(Entity):
                                    """
                                    Bridge\-domain Pseudowire MAC
                                    configuration commands
                                    
                                    .. attribute:: enable
                                    
                                    	Bridge\-domain Pseudowire MAC configuration mode
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: pseudowire_mac_aging
                                    
                                    	MAC\-Aging configuration commands
                                    	**type**\:   :py:class:`PseudowireMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging>`
                                    
                                    .. attribute:: pseudowire_mac_learning
                                    
                                    	Enable MAC Learning
                                    	**type**\:   :py:class:`MacLearn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLearn>`
                                    
                                    .. attribute:: pseudowire_mac_limit
                                    
                                    	MAC\-Limit configuration commands
                                    	**type**\:   :py:class:`PseudowireMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit>`
                                    
                                    .. attribute:: pseudowire_mac_port_down_flush
                                    
                                    	Enable/Disable MAC Flush When Port goes down
                                    	**type**\:   :py:class:`PortDownFlush <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.PortDownFlush>`
                                    
                                    .. attribute:: pseudowire_mac_secure
                                    
                                    	MAC Secure
                                    	**type**\:   :py:class:`PseudowireMacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac, self).__init__()

                                        self.yang_name = "pseudowire-mac"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"pseudowire-mac-aging" : ("pseudowire_mac_aging", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging), "pseudowire-mac-limit" : ("pseudowire_mac_limit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit), "pseudowire-mac-secure" : ("pseudowire_mac_secure", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure)}
                                        self._child_list_classes = {}

                                        self.enable = YLeaf(YType.empty, "enable")

                                        self.pseudowire_mac_learning = YLeaf(YType.enumeration, "pseudowire-mac-learning")

                                        self.pseudowire_mac_port_down_flush = YLeaf(YType.enumeration, "pseudowire-mac-port-down-flush")

                                        self.pseudowire_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging()
                                        self.pseudowire_mac_aging.parent = self
                                        self._children_name_map["pseudowire_mac_aging"] = "pseudowire-mac-aging"
                                        self._children_yang_names.add("pseudowire-mac-aging")

                                        self.pseudowire_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit()
                                        self.pseudowire_mac_limit.parent = self
                                        self._children_name_map["pseudowire_mac_limit"] = "pseudowire-mac-limit"
                                        self._children_yang_names.add("pseudowire-mac-limit")

                                        self.pseudowire_mac_secure = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure()
                                        self.pseudowire_mac_secure.parent = self
                                        self._children_name_map["pseudowire_mac_secure"] = "pseudowire-mac-secure"
                                        self._children_yang_names.add("pseudowire-mac-secure")
                                        self._segment_path = lambda: "pseudowire-mac"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac, ['enable', 'pseudowire_mac_learning', 'pseudowire_mac_port_down_flush'], name, value)


                                    class PseudowireMacAging(Entity):
                                        """
                                        MAC\-Aging configuration commands
                                        
                                        .. attribute:: pseudowire_mac_aging_time
                                        
                                        	MAC Aging Time
                                        	**type**\:  int
                                        
                                        	**range:** 300..30000
                                        
                                        .. attribute:: pseudowire_mac_aging_type
                                        
                                        	MAC address aging type
                                        	**type**\:   :py:class:`MacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAging>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging, self).__init__()

                                            self.yang_name = "pseudowire-mac-aging"
                                            self.yang_parent_name = "pseudowire-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.pseudowire_mac_aging_time = YLeaf(YType.uint32, "pseudowire-mac-aging-time")

                                            self.pseudowire_mac_aging_type = YLeaf(YType.enumeration, "pseudowire-mac-aging-type")
                                            self._segment_path = lambda: "pseudowire-mac-aging"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging, ['pseudowire_mac_aging_time', 'pseudowire_mac_aging_type'], name, value)


                                    class PseudowireMacLimit(Entity):
                                        """
                                        MAC\-Limit configuration commands
                                        
                                        .. attribute:: pseudowire_mac_limit_action
                                        
                                        	Bridge Access Pseudowire MAC address limit enforcement action
                                        	**type**\:   :py:class:`MacLimitAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction>`
                                        
                                        .. attribute:: pseudowire_mac_limit_max
                                        
                                        	Number of MAC addresses on a Bridge Access Pseudowire after which MAC limit action is taken
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pseudowire_mac_limit_notif
                                        
                                        	MAC address limit notification action in a Bridge Access Pseudowire
                                        	**type**\:   :py:class:`MacNotification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotification>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit, self).__init__()

                                            self.yang_name = "pseudowire-mac-limit"
                                            self.yang_parent_name = "pseudowire-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.pseudowire_mac_limit_action = YLeaf(YType.enumeration, "pseudowire-mac-limit-action")

                                            self.pseudowire_mac_limit_max = YLeaf(YType.uint32, "pseudowire-mac-limit-max")

                                            self.pseudowire_mac_limit_notif = YLeaf(YType.enumeration, "pseudowire-mac-limit-notif")
                                            self._segment_path = lambda: "pseudowire-mac-limit"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit, ['pseudowire_mac_limit_action', 'pseudowire_mac_limit_max', 'pseudowire_mac_limit_notif'], name, value)


                                    class PseudowireMacSecure(Entity):
                                        """
                                        MAC Secure
                                        
                                        .. attribute:: action
                                        
                                        	MAC secure enforcement action
                                        	**type**\:   :py:class:`MacSecureAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacSecureAction>`
                                        
                                        .. attribute:: disable
                                        
                                        	Disable L2 Pseudowire MAC Secure
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable MAC Secure
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: logging
                                        
                                        	MAC Secure Logging
                                        	**type**\:   :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure, self).__init__()

                                            self.yang_name = "pseudowire-mac-secure"
                                            self.yang_parent_name = "pseudowire-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.action = YLeaf(YType.enumeration, "action")

                                            self.disable = YLeaf(YType.empty, "disable")

                                            self.enable = YLeaf(YType.empty, "enable")

                                            self.logging = YLeaf(YType.enumeration, "logging")
                                            self._segment_path = lambda: "pseudowire-mac-secure"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure, ['action', 'disable', 'enable', 'logging'], name, value)


                                class PseudowireProfile(Entity):
                                    """
                                    Attach a DHCP profile
                                    
                                    .. attribute:: dhcp_snooping_id
                                    
                                    	Disable DHCP snooping
                                    	**type**\:  str
                                    
                                    .. attribute:: profile_id
                                    
                                    	Set the snooping profile
                                    	**type**\:   :py:class:`InterfaceProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile, self).__init__()

                                        self.yang_name = "pseudowire-profile"
                                        self.yang_parent_name = "bd-pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.dhcp_snooping_id = YLeaf(YType.str, "dhcp-snooping-id")

                                        self.profile_id = YLeaf(YType.enumeration, "profile-id")
                                        self._segment_path = lambda: "pseudowire-profile"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile, ['dhcp_snooping_id', 'profile_id'], name, value)


                        class BdStormControls(Entity):
                            """
                            Storm Control
                            
                            .. attribute:: bd_storm_control
                            
                            	Storm Control Type
                            	**type**\: list of    :py:class:`BdStormControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls, self).__init__()

                                self.yang_name = "bd-storm-controls"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"bd-storm-control" : ("bd_storm_control", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl)}

                                self.bd_storm_control = YList(self)
                                self._segment_path = lambda: "bd-storm-controls"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls, [], name, value)


                            class BdStormControl(Entity):
                                """
                                Storm Control Type
                                
                                .. attribute:: sctype  <key>
                                
                                	Storm Control Type
                                	**type**\:   :py:class:`StormControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.StormControl>`
                                
                                .. attribute:: storm_control_unit
                                
                                	Specify units for Storm Control Configuration
                                	**type**\:   :py:class:`StormControlUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl, self).__init__()

                                    self.yang_name = "bd-storm-control"
                                    self.yang_parent_name = "bd-storm-controls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"storm-control-unit" : ("storm_control_unit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit)}
                                    self._child_list_classes = {}

                                    self.sctype = YLeaf(YType.enumeration, "sctype")

                                    self.storm_control_unit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit()
                                    self.storm_control_unit.parent = self
                                    self._children_name_map["storm_control_unit"] = "storm-control-unit"
                                    self._children_yang_names.add("storm-control-unit")
                                    self._segment_path = lambda: "bd-storm-control" + "[sctype='" + self.sctype.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl, ['sctype'], name, value)


                                class StormControlUnit(Entity):
                                    """
                                    Specify units for Storm Control Configuration
                                    
                                    .. attribute:: kbits_per_sec
                                    
                                    	Kilobits Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                    	**type**\:  int
                                    
                                    	**range:** 64..1280000
                                    
                                    	**units**\: kbit/s
                                    
                                    .. attribute:: pkts_per_sec
                                    
                                    	Packets Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                    	**type**\:  int
                                    
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
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.kbits_per_sec = YLeaf(YType.uint32, "kbits-per-sec")

                                        self.pkts_per_sec = YLeaf(YType.uint32, "pkts-per-sec")
                                        self._segment_path = lambda: "storm-control-unit"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit, ['kbits_per_sec', 'pkts_per_sec'], name, value)


                        class BridgeDomainEvis(Entity):
                            """
                            Bridge Domain EVI Table
                            
                            .. attribute:: bridge_domain_evi
                            
                            	Bridge Domain EVI
                            	**type**\: list of    :py:class:`BridgeDomainEvi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis, self).__init__()

                                self.yang_name = "bridge-domain-evis"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"bridge-domain-evi" : ("bridge_domain_evi", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi)}

                                self.bridge_domain_evi = YList(self)
                                self._segment_path = lambda: "bridge-domain-evis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis, [], name, value)


                            class BridgeDomainEvi(Entity):
                                """
                                Bridge Domain EVI
                                
                                .. attribute:: eviid  <key>
                                
                                	Ethernet VPN ID
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi, self).__init__()

                                    self.yang_name = "bridge-domain-evi"
                                    self.yang_parent_name = "bridge-domain-evis"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.eviid = YLeaf(YType.uint32, "eviid")
                                    self._segment_path = lambda: "bridge-domain-evi" + "[eviid='" + self.eviid.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi, ['eviid'], name, value)


                        class BridgeDomainMac(Entity):
                            """
                            MAC configuration commands
                            
                            .. attribute:: bd_mac_aging
                            
                            	MAC\-Aging configuration commands
                            	**type**\:   :py:class:`BdMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging>`
                            
                            .. attribute:: bd_mac_filters
                            
                            	Filter Mac Address
                            	**type**\:   :py:class:`BdMacFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters>`
                            
                            .. attribute:: bd_mac_learn
                            
                            	Mac Learning Type
                            	**type**\:   :py:class:`BdmacLearn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BdmacLearn>`
                            
                            .. attribute:: bd_mac_limit
                            
                            	MAC\-Limit configuration commands
                            	**type**\:   :py:class:`BdMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit>`
                            
                            .. attribute:: bd_mac_port_down_flush
                            
                            	Disable MAC Flush when Port goes Down
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bd_mac_withdraw
                            
                            	Disable Mac Withdraw
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bd_mac_withdraw_access_pw_disable
                            
                            	MAC withdraw on Access PW
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bd_mac_withdraw_behavior
                            
                            	MAC withdraw sent on bridge port down
                            	**type**\:   :py:class:`MacWithdrawBehavior <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacWithdrawBehavior>`
                            
                            .. attribute:: bd_mac_withdraw_relay
                            
                            	Mac withdraw sent from access PW to access PW
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: mac_secure
                            
                            	MAC Secure
                            	**type**\:   :py:class:`MacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac, self).__init__()

                                self.yang_name = "bridge-domain-mac"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bd-mac-aging" : ("bd_mac_aging", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging), "bd-mac-filters" : ("bd_mac_filters", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters), "bd-mac-limit" : ("bd_mac_limit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit), "mac-secure" : ("mac_secure", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure)}
                                self._child_list_classes = {}

                                self.bd_mac_learn = YLeaf(YType.enumeration, "bd-mac-learn")

                                self.bd_mac_port_down_flush = YLeaf(YType.empty, "bd-mac-port-down-flush")

                                self.bd_mac_withdraw = YLeaf(YType.empty, "bd-mac-withdraw")

                                self.bd_mac_withdraw_access_pw_disable = YLeaf(YType.empty, "bd-mac-withdraw-access-pw-disable")

                                self.bd_mac_withdraw_behavior = YLeaf(YType.enumeration, "bd-mac-withdraw-behavior")

                                self.bd_mac_withdraw_relay = YLeaf(YType.empty, "bd-mac-withdraw-relay")

                                self.bd_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging()
                                self.bd_mac_aging.parent = self
                                self._children_name_map["bd_mac_aging"] = "bd-mac-aging"
                                self._children_yang_names.add("bd-mac-aging")

                                self.bd_mac_filters = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters()
                                self.bd_mac_filters.parent = self
                                self._children_name_map["bd_mac_filters"] = "bd-mac-filters"
                                self._children_yang_names.add("bd-mac-filters")

                                self.bd_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit()
                                self.bd_mac_limit.parent = self
                                self._children_name_map["bd_mac_limit"] = "bd-mac-limit"
                                self._children_yang_names.add("bd-mac-limit")

                                self.mac_secure = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure()
                                self.mac_secure.parent = self
                                self._children_name_map["mac_secure"] = "mac-secure"
                                self._children_yang_names.add("mac-secure")
                                self._segment_path = lambda: "bridge-domain-mac"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac, ['bd_mac_learn', 'bd_mac_port_down_flush', 'bd_mac_withdraw', 'bd_mac_withdraw_access_pw_disable', 'bd_mac_withdraw_behavior', 'bd_mac_withdraw_relay'], name, value)


                            class BdMacAging(Entity):
                                """
                                MAC\-Aging configuration commands
                                
                                .. attribute:: bd_mac_aging_time
                                
                                	Mac Aging Time
                                	**type**\:  int
                                
                                	**range:** 300..30000
                                
                                .. attribute:: bd_mac_aging_type
                                
                                	MAC address aging type
                                	**type**\:   :py:class:`MacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAging>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging, self).__init__()

                                    self.yang_name = "bd-mac-aging"
                                    self.yang_parent_name = "bridge-domain-mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.bd_mac_aging_time = YLeaf(YType.uint32, "bd-mac-aging-time")

                                    self.bd_mac_aging_type = YLeaf(YType.enumeration, "bd-mac-aging-type")
                                    self._segment_path = lambda: "bd-mac-aging"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging, ['bd_mac_aging_time', 'bd_mac_aging_type'], name, value)


                            class BdMacFilters(Entity):
                                """
                                Filter Mac Address
                                
                                .. attribute:: bd_mac_filter
                                
                                	Static MAC address
                                	**type**\: list of    :py:class:`BdMacFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters, self).__init__()

                                    self.yang_name = "bd-mac-filters"
                                    self.yang_parent_name = "bridge-domain-mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"bd-mac-filter" : ("bd_mac_filter", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter)}

                                    self.bd_mac_filter = YList(self)
                                    self._segment_path = lambda: "bd-mac-filters"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters, [], name, value)


                                class BdMacFilter(Entity):
                                    """
                                    Static MAC address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	Static MAC address
                                    	**type**\:  str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    .. attribute:: drop
                                    
                                    	MAC address for filtering
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter, self).__init__()

                                        self.yang_name = "bd-mac-filter"
                                        self.yang_parent_name = "bd-mac-filters"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.address = YLeaf(YType.str, "address")

                                        self.drop = YLeaf(YType.empty, "drop")
                                        self._segment_path = lambda: "bd-mac-filter" + "[address='" + self.address.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter, ['address', 'drop'], name, value)


                            class BdMacLimit(Entity):
                                """
                                MAC\-Limit configuration commands
                                
                                .. attribute:: bd_mac_limit_action
                                
                                	MAC address limit enforcement action
                                	**type**\:   :py:class:`MacLimitAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction>`
                                
                                .. attribute:: bd_mac_limit_max
                                
                                	Number of MAC addresses after which MAC limit action is taken
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: bd_mac_limit_notif
                                
                                	Mac Address Limit Notification
                                	**type**\:   :py:class:`MacNotification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotification>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit, self).__init__()

                                    self.yang_name = "bd-mac-limit"
                                    self.yang_parent_name = "bridge-domain-mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.bd_mac_limit_action = YLeaf(YType.enumeration, "bd-mac-limit-action")

                                    self.bd_mac_limit_max = YLeaf(YType.uint32, "bd-mac-limit-max")

                                    self.bd_mac_limit_notif = YLeaf(YType.enumeration, "bd-mac-limit-notif")
                                    self._segment_path = lambda: "bd-mac-limit"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit, ['bd_mac_limit_action', 'bd_mac_limit_max', 'bd_mac_limit_notif'], name, value)


                            class MacSecure(Entity):
                                """
                                MAC Secure
                                
                                .. attribute:: action
                                
                                	MAC secure enforcement action
                                	**type**\:   :py:class:`MacSecureAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacSecureAction>`
                                
                                .. attribute:: enable
                                
                                	Enable MAC Secure
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: logging
                                
                                	MAC Secure Logging
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: threshold
                                
                                	MAC Secure Threshold
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure, self).__init__()

                                    self.yang_name = "mac-secure"
                                    self.yang_parent_name = "bridge-domain-mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.action = YLeaf(YType.enumeration, "action")

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.logging = YLeaf(YType.empty, "logging")

                                    self.threshold = YLeaf(YType.empty, "threshold")
                                    self._segment_path = lambda: "mac-secure"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure, ['action', 'enable', 'logging', 'threshold'], name, value)


                        class BridgeDomainPbb(Entity):
                            """
                            Bridge Domain PBB
                            
                            .. attribute:: pbb_core
                            
                            	PBB Core
                            	**type**\:   :py:class:`PbbCore <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore>`
                            
                            .. attribute:: pbb_edges
                            
                            	PBB Edge
                            	**type**\:   :py:class:`PbbEdges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb, self).__init__()

                                self.yang_name = "bridge-domain-pbb"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pbb-core" : ("pbb_core", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore), "pbb-edges" : ("pbb_edges", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges)}
                                self._child_list_classes = {}

                                self.pbb_core = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore()
                                self.pbb_core.parent = self
                                self._children_name_map["pbb_core"] = "pbb-core"
                                self._children_yang_names.add("pbb-core")

                                self.pbb_edges = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges()
                                self.pbb_edges.parent = self
                                self._children_name_map["pbb_edges"] = "pbb-edges"
                                self._children_yang_names.add("pbb-edges")
                                self._segment_path = lambda: "bridge-domain-pbb"


                            class PbbCore(Entity):
                                """
                                PBB Core
                                
                                .. attribute:: enable
                                
                                	Enable Bridge Domain PBB Core Configuration
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: pbb_core_dhcp_profile
                                
                                	Attach a DHCP profile
                                	**type**\:   :py:class:`PbbCoreDhcpProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile>`
                                
                                .. attribute:: pbb_core_evis
                                
                                	PBB Core EVI Table
                                	**type**\:   :py:class:`PbbCoreEvis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis>`
                                
                                .. attribute:: pbb_core_igmp_profile
                                
                                	Attach a IGMP Snooping profile
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: pbb_core_mac
                                
                                	MAC configuration commands
                                	**type**\:   :py:class:`PbbCoreMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac>`
                                
                                .. attribute:: pbb_core_mmrp_flood_optimization
                                
                                	Enabling MMRP PBB\-VPLS Flood Optimization
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN ID to push
                                	**type**\:  int
                                
                                	**range:** 1..4094
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore, self).__init__()

                                    self.yang_name = "pbb-core"
                                    self.yang_parent_name = "bridge-domain-pbb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"pbb-core-dhcp-profile" : ("pbb_core_dhcp_profile", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile), "pbb-core-evis" : ("pbb_core_evis", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis), "pbb-core-mac" : ("pbb_core_mac", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac)}
                                    self._child_list_classes = {}

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.pbb_core_igmp_profile = YLeaf(YType.str, "pbb-core-igmp-profile")

                                    self.pbb_core_mmrp_flood_optimization = YLeaf(YType.empty, "pbb-core-mmrp-flood-optimization")

                                    self.vlan_id = YLeaf(YType.uint32, "vlan-id")

                                    self.pbb_core_dhcp_profile = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile()
                                    self.pbb_core_dhcp_profile.parent = self
                                    self._children_name_map["pbb_core_dhcp_profile"] = "pbb-core-dhcp-profile"
                                    self._children_yang_names.add("pbb-core-dhcp-profile")

                                    self.pbb_core_evis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis()
                                    self.pbb_core_evis.parent = self
                                    self._children_name_map["pbb_core_evis"] = "pbb-core-evis"
                                    self._children_yang_names.add("pbb-core-evis")

                                    self.pbb_core_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac()
                                    self.pbb_core_mac.parent = self
                                    self._children_name_map["pbb_core_mac"] = "pbb-core-mac"
                                    self._children_yang_names.add("pbb-core-mac")
                                    self._segment_path = lambda: "pbb-core"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore, ['enable', 'pbb_core_igmp_profile', 'pbb_core_mmrp_flood_optimization', 'vlan_id'], name, value)


                                class PbbCoreDhcpProfile(Entity):
                                    """
                                    Attach a DHCP profile
                                    
                                    .. attribute:: dhcp_snooping_id
                                    
                                    	Disable DHCP snooping
                                    	**type**\:  str
                                    
                                    .. attribute:: profile_id
                                    
                                    	Set the snooping profile
                                    	**type**\:   :py:class:`InterfaceProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile, self).__init__()

                                        self.yang_name = "pbb-core-dhcp-profile"
                                        self.yang_parent_name = "pbb-core"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.dhcp_snooping_id = YLeaf(YType.str, "dhcp-snooping-id")

                                        self.profile_id = YLeaf(YType.enumeration, "profile-id")
                                        self._segment_path = lambda: "pbb-core-dhcp-profile"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile, ['dhcp_snooping_id', 'profile_id'], name, value)


                                class PbbCoreEvis(Entity):
                                    """
                                    PBB Core EVI Table
                                    
                                    .. attribute:: pbb_core_evi
                                    
                                    	PBB Core EVI
                                    	**type**\: list of    :py:class:`PbbCoreEvi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis, self).__init__()

                                        self.yang_name = "pbb-core-evis"
                                        self.yang_parent_name = "pbb-core"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"pbb-core-evi" : ("pbb_core_evi", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi)}

                                        self.pbb_core_evi = YList(self)
                                        self._segment_path = lambda: "pbb-core-evis"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis, [], name, value)


                                    class PbbCoreEvi(Entity):
                                        """
                                        PBB Core EVI
                                        
                                        .. attribute:: eviid  <key>
                                        
                                        	Ethernet VPN ID
                                        	**type**\:  int
                                        
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
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.eviid = YLeaf(YType.uint32, "eviid")
                                            self._segment_path = lambda: "pbb-core-evi" + "[eviid='" + self.eviid.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi, ['eviid'], name, value)


                                class PbbCoreMac(Entity):
                                    """
                                    MAC configuration commands
                                    
                                    .. attribute:: pbb_core_mac_aging
                                    
                                    	MAC\-Aging configuration commands
                                    	**type**\:   :py:class:`PbbCoreMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging>`
                                    
                                    .. attribute:: pbb_core_mac_learning
                                    
                                    	Enable Mac Learning
                                    	**type**\:   :py:class:`MacLearn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLearn>`
                                    
                                    .. attribute:: pbb_core_mac_limit
                                    
                                    	MAC\-Limit configuration commands
                                    	**type**\:   :py:class:`PbbCoreMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac, self).__init__()

                                        self.yang_name = "pbb-core-mac"
                                        self.yang_parent_name = "pbb-core"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"pbb-core-mac-aging" : ("pbb_core_mac_aging", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging), "pbb-core-mac-limit" : ("pbb_core_mac_limit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit)}
                                        self._child_list_classes = {}

                                        self.pbb_core_mac_learning = YLeaf(YType.enumeration, "pbb-core-mac-learning")

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
                                        
                                        .. attribute:: pbb_core_mac_aging_time
                                        
                                        	Mac Aging Time
                                        	**type**\:  int
                                        
                                        	**range:** 300..30000
                                        
                                        .. attribute:: pbb_core_mac_aging_type
                                        
                                        	MAC address aging type
                                        	**type**\:   :py:class:`MacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAging>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging, self).__init__()

                                            self.yang_name = "pbb-core-mac-aging"
                                            self.yang_parent_name = "pbb-core-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.pbb_core_mac_aging_time = YLeaf(YType.uint32, "pbb-core-mac-aging-time")

                                            self.pbb_core_mac_aging_type = YLeaf(YType.enumeration, "pbb-core-mac-aging-type")
                                            self._segment_path = lambda: "pbb-core-mac-aging"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging, ['pbb_core_mac_aging_time', 'pbb_core_mac_aging_type'], name, value)


                                    class PbbCoreMacLimit(Entity):
                                        """
                                        MAC\-Limit configuration commands
                                        
                                        .. attribute:: pbb_core_mac_limit_action
                                        
                                        	MAC address limit enforcement action
                                        	**type**\:   :py:class:`MacLimitAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction>`
                                        
                                        .. attribute:: pbb_core_mac_limit_max
                                        
                                        	Number of MAC addresses after which MAC limit action is taken
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pbb_core_mac_limit_notif
                                        
                                        	MAC address limit notification action
                                        	**type**\:   :py:class:`MacNotification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotification>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit, self).__init__()

                                            self.yang_name = "pbb-core-mac-limit"
                                            self.yang_parent_name = "pbb-core-mac"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.pbb_core_mac_limit_action = YLeaf(YType.enumeration, "pbb-core-mac-limit-action")

                                            self.pbb_core_mac_limit_max = YLeaf(YType.uint32, "pbb-core-mac-limit-max")

                                            self.pbb_core_mac_limit_notif = YLeaf(YType.enumeration, "pbb-core-mac-limit-notif")
                                            self._segment_path = lambda: "pbb-core-mac-limit"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit, ['pbb_core_mac_limit_action', 'pbb_core_mac_limit_max', 'pbb_core_mac_limit_notif'], name, value)


                            class PbbEdges(Entity):
                                """
                                PBB Edge
                                
                                .. attribute:: pbb_edge
                                
                                	Configure BD as PBB Edge with ISID and associated PBB Core BD
                                	**type**\: list of    :py:class:`PbbEdge <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges, self).__init__()

                                    self.yang_name = "pbb-edges"
                                    self.yang_parent_name = "bridge-domain-pbb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"pbb-edge" : ("pbb_edge", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge)}

                                    self.pbb_edge = YList(self)
                                    self._segment_path = lambda: "pbb-edges"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges, [], name, value)


                                class PbbEdge(Entity):
                                    """
                                    Configure BD as PBB Edge with ISID and
                                    associated PBB Core BD
                                    
                                    .. attribute:: isid  <key>
                                    
                                    	ISID
                                    	**type**\:  int
                                    
                                    	**range:** 256..16777214
                                    
                                    .. attribute:: core_bd_name  <key>
                                    
                                    	Core BD Name
                                    	**type**\:  str
                                    
                                    	**length:** 1..27
                                    
                                    .. attribute:: pbb_edge_dhcp_profile
                                    
                                    	Attach a DHCP profile
                                    	**type**\:   :py:class:`PbbEdgeDhcpProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile>`
                                    
                                    .. attribute:: pbb_edge_igmp_profile
                                    
                                    	Attach a IGMP Snooping profile
                                    	**type**\:  str
                                    
                                    	**length:** 1..32
                                    
                                    .. attribute:: pbb_edge_mac
                                    
                                    	MAC configuration commands
                                    	**type**\:   :py:class:`PbbEdgeMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac>`
                                    
                                    .. attribute:: pbb_edge_split_horizon_group
                                    
                                    	Split Horizon Group
                                    	**type**\:   :py:class:`PbbEdgeSplitHorizonGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup>`
                                    
                                    .. attribute:: pbb_static_mac_mappings
                                    
                                    	PBB Static Mac Address Mapping Table
                                    	**type**\:   :py:class:`PbbStaticMacMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings>`
                                    
                                    .. attribute:: unknown_unicast_bmac
                                    
                                    	Configure Unknown Unicast BMAC address for PBB Edge Port
                                    	**type**\:  str
                                    
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
                                        self._child_container_classes = {"pbb-edge-dhcp-profile" : ("pbb_edge_dhcp_profile", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile), "pbb-edge-mac" : ("pbb_edge_mac", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac), "pbb-edge-split-horizon-group" : ("pbb_edge_split_horizon_group", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup), "pbb-static-mac-mappings" : ("pbb_static_mac_mappings", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings)}
                                        self._child_list_classes = {}

                                        self.isid = YLeaf(YType.uint32, "isid")

                                        self.core_bd_name = YLeaf(YType.str, "core-bd-name")

                                        self.pbb_edge_igmp_profile = YLeaf(YType.str, "pbb-edge-igmp-profile")

                                        self.unknown_unicast_bmac = YLeaf(YType.str, "unknown-unicast-bmac")

                                        self.pbb_edge_dhcp_profile = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile()
                                        self.pbb_edge_dhcp_profile.parent = self
                                        self._children_name_map["pbb_edge_dhcp_profile"] = "pbb-edge-dhcp-profile"
                                        self._children_yang_names.add("pbb-edge-dhcp-profile")

                                        self.pbb_edge_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac()
                                        self.pbb_edge_mac.parent = self
                                        self._children_name_map["pbb_edge_mac"] = "pbb-edge-mac"
                                        self._children_yang_names.add("pbb-edge-mac")

                                        self.pbb_edge_split_horizon_group = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup()
                                        self.pbb_edge_split_horizon_group.parent = self
                                        self._children_name_map["pbb_edge_split_horizon_group"] = "pbb-edge-split-horizon-group"
                                        self._children_yang_names.add("pbb-edge-split-horizon-group")

                                        self.pbb_static_mac_mappings = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings()
                                        self.pbb_static_mac_mappings.parent = self
                                        self._children_name_map["pbb_static_mac_mappings"] = "pbb-static-mac-mappings"
                                        self._children_yang_names.add("pbb-static-mac-mappings")
                                        self._segment_path = lambda: "pbb-edge" + "[isid='" + self.isid.get() + "']" + "[core-bd-name='" + self.core_bd_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge, ['isid', 'core_bd_name', 'pbb_edge_igmp_profile', 'unknown_unicast_bmac'], name, value)


                                    class PbbEdgeDhcpProfile(Entity):
                                        """
                                        Attach a DHCP profile
                                        
                                        .. attribute:: dhcp_snooping_id
                                        
                                        	Disable DHCP snooping
                                        	**type**\:  str
                                        
                                        .. attribute:: profile_id
                                        
                                        	Set the snooping profile
                                        	**type**\:   :py:class:`InterfaceProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile, self).__init__()

                                            self.yang_name = "pbb-edge-dhcp-profile"
                                            self.yang_parent_name = "pbb-edge"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.dhcp_snooping_id = YLeaf(YType.str, "dhcp-snooping-id")

                                            self.profile_id = YLeaf(YType.enumeration, "profile-id")
                                            self._segment_path = lambda: "pbb-edge-dhcp-profile"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile, ['dhcp_snooping_id', 'profile_id'], name, value)


                                    class PbbEdgeMac(Entity):
                                        """
                                        MAC configuration commands
                                        
                                        .. attribute:: pbb_edge_mac_aging
                                        
                                        	MAC\-Aging configuration commands
                                        	**type**\:   :py:class:`PbbEdgeMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging>`
                                        
                                        .. attribute:: pbb_edge_mac_learning
                                        
                                        	Enable Mac Learning
                                        	**type**\:   :py:class:`MacLearn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLearn>`
                                        
                                        .. attribute:: pbb_edge_mac_limit
                                        
                                        	MAC\-Limit configuration commands
                                        	**type**\:   :py:class:`PbbEdgeMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit>`
                                        
                                        .. attribute:: pbb_edge_mac_secure
                                        
                                        	MAC Secure
                                        	**type**\:   :py:class:`PbbEdgeMacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac, self).__init__()

                                            self.yang_name = "pbb-edge-mac"
                                            self.yang_parent_name = "pbb-edge"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"pbb-edge-mac-aging" : ("pbb_edge_mac_aging", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging), "pbb-edge-mac-limit" : ("pbb_edge_mac_limit", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit), "pbb-edge-mac-secure" : ("pbb_edge_mac_secure", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure)}
                                            self._child_list_classes = {}

                                            self.pbb_edge_mac_learning = YLeaf(YType.enumeration, "pbb-edge-mac-learning")

                                            self.pbb_edge_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging()
                                            self.pbb_edge_mac_aging.parent = self
                                            self._children_name_map["pbb_edge_mac_aging"] = "pbb-edge-mac-aging"
                                            self._children_yang_names.add("pbb-edge-mac-aging")

                                            self.pbb_edge_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit()
                                            self.pbb_edge_mac_limit.parent = self
                                            self._children_name_map["pbb_edge_mac_limit"] = "pbb-edge-mac-limit"
                                            self._children_yang_names.add("pbb-edge-mac-limit")

                                            self.pbb_edge_mac_secure = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure()
                                            self.pbb_edge_mac_secure.parent = self
                                            self._children_name_map["pbb_edge_mac_secure"] = "pbb-edge-mac-secure"
                                            self._children_yang_names.add("pbb-edge-mac-secure")
                                            self._segment_path = lambda: "pbb-edge-mac"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac, ['pbb_edge_mac_learning'], name, value)


                                        class PbbEdgeMacAging(Entity):
                                            """
                                            MAC\-Aging configuration commands
                                            
                                            .. attribute:: pbb_edge_mac_aging_time
                                            
                                            	Mac Aging Time
                                            	**type**\:  int
                                            
                                            	**range:** 300..30000
                                            
                                            .. attribute:: pbb_edge_mac_aging_type
                                            
                                            	MAC address aging type
                                            	**type**\:   :py:class:`MacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAging>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging, self).__init__()

                                                self.yang_name = "pbb-edge-mac-aging"
                                                self.yang_parent_name = "pbb-edge-mac"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.pbb_edge_mac_aging_time = YLeaf(YType.uint32, "pbb-edge-mac-aging-time")

                                                self.pbb_edge_mac_aging_type = YLeaf(YType.enumeration, "pbb-edge-mac-aging-type")
                                                self._segment_path = lambda: "pbb-edge-mac-aging"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging, ['pbb_edge_mac_aging_time', 'pbb_edge_mac_aging_type'], name, value)


                                        class PbbEdgeMacLimit(Entity):
                                            """
                                            MAC\-Limit configuration commands
                                            
                                            .. attribute:: pbb_edge_mac_limit_action
                                            
                                            	MAC address limit enforcement action
                                            	**type**\:   :py:class:`MacLimitAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction>`
                                            
                                            .. attribute:: pbb_edge_mac_limit_max
                                            
                                            	Number of MAC addresses after which MAC limit action is taken
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: pbb_edge_mac_limit_notif
                                            
                                            	MAC address limit notification action
                                            	**type**\:   :py:class:`MacNotification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotification>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit, self).__init__()

                                                self.yang_name = "pbb-edge-mac-limit"
                                                self.yang_parent_name = "pbb-edge-mac"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.pbb_edge_mac_limit_action = YLeaf(YType.enumeration, "pbb-edge-mac-limit-action")

                                                self.pbb_edge_mac_limit_max = YLeaf(YType.uint32, "pbb-edge-mac-limit-max")

                                                self.pbb_edge_mac_limit_notif = YLeaf(YType.enumeration, "pbb-edge-mac-limit-notif")
                                                self._segment_path = lambda: "pbb-edge-mac-limit"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit, ['pbb_edge_mac_limit_action', 'pbb_edge_mac_limit_max', 'pbb_edge_mac_limit_notif'], name, value)


                                        class PbbEdgeMacSecure(Entity):
                                            """
                                            MAC Secure
                                            
                                            .. attribute:: accept_shutdown
                                            
                                            	Accept Virtual instance port to be shutdown on mac violation
                                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                            
                                            .. attribute:: action
                                            
                                            	MAC secure enforcement action
                                            	**type**\:   :py:class:`MacSecureAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacSecureAction>`
                                            
                                            .. attribute:: disable
                                            
                                            	Disable Virtual instance port MAC Secure
                                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                            
                                            .. attribute:: enable
                                            
                                            	Enable MAC Secure
                                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                            
                                            .. attribute:: logging
                                            
                                            	MAC Secure Logging
                                            	**type**\:   :py:class:`L2vpnLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure, self).__init__()

                                                self.yang_name = "pbb-edge-mac-secure"
                                                self.yang_parent_name = "pbb-edge-mac"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.accept_shutdown = YLeaf(YType.empty, "accept-shutdown")

                                                self.action = YLeaf(YType.enumeration, "action")

                                                self.disable = YLeaf(YType.empty, "disable")

                                                self.enable = YLeaf(YType.empty, "enable")

                                                self.logging = YLeaf(YType.enumeration, "logging")
                                                self._segment_path = lambda: "pbb-edge-mac-secure"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure, ['accept_shutdown', 'action', 'disable', 'enable', 'logging'], name, value)


                                    class PbbEdgeSplitHorizonGroup(Entity):
                                        """
                                        Split Horizon Group
                                        
                                        .. attribute:: disable
                                        
                                        	Disable split horizon group
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup, self).__init__()

                                            self.yang_name = "pbb-edge-split-horizon-group"
                                            self.yang_parent_name = "pbb-edge"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.disable = YLeaf(YType.empty, "disable")
                                            self._segment_path = lambda: "pbb-edge-split-horizon-group"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup, ['disable'], name, value)


                                    class PbbStaticMacMappings(Entity):
                                        """
                                        PBB Static Mac Address Mapping Table
                                        
                                        .. attribute:: pbb_static_mac_mapping
                                        
                                        	PBB Static Mac Address Mapping Configuration
                                        	**type**\: list of    :py:class:`PbbStaticMacMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings, self).__init__()

                                            self.yang_name = "pbb-static-mac-mappings"
                                            self.yang_parent_name = "pbb-edge"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"pbb-static-mac-mapping" : ("pbb_static_mac_mapping", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping)}

                                            self.pbb_static_mac_mapping = YList(self)
                                            self._segment_path = lambda: "pbb-static-mac-mappings"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings, [], name, value)


                                        class PbbStaticMacMapping(Entity):
                                            """
                                            PBB Static Mac Address Mapping
                                            Configuration
                                            
                                            .. attribute:: address  <key>
                                            
                                            	Static MAC address
                                            	**type**\:  str
                                            
                                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                            
                                            .. attribute:: pbb_static_mac_mapping_bmac
                                            
                                            	Static backbone MAC address to map with
                                            	**type**\:  str
                                            
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
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.address = YLeaf(YType.str, "address")

                                                self.pbb_static_mac_mapping_bmac = YLeaf(YType.str, "pbb-static-mac-mapping-bmac")
                                                self._segment_path = lambda: "pbb-static-mac-mapping" + "[address='" + self.address.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping, ['address', 'pbb_static_mac_mapping_bmac'], name, value)


                        class Dai(Entity):
                            """
                            Dynamic ARP Inspection
                            
                            .. attribute:: dai_address_validation
                            
                            	Address Validation
                            	**type**\:   :py:class:`DaiAddressValidation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation>`
                            
                            .. attribute:: enable
                            
                            	Enable Dynamic ARP Inspection
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: logging
                            
                            	Enable Logging
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai, self).__init__()

                                self.yang_name = "dai"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"dai-address-validation" : ("dai_address_validation", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation)}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")

                                self.logging = YLeaf(YType.empty, "logging")

                                self.dai_address_validation = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation()
                                self.dai_address_validation.parent = self
                                self._children_name_map["dai_address_validation"] = "dai-address-validation"
                                self._children_yang_names.add("dai-address-validation")
                                self._segment_path = lambda: "dai"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai, ['enable', 'logging'], name, value)


                            class DaiAddressValidation(Entity):
                                """
                                Address Validation
                                
                                .. attribute:: destination_mac_verification
                                
                                	Enable Destination MAC Verification
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: enable
                                
                                	Enable Address Validation
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: ipv4_verification
                                
                                	Enable IPv4 Verification
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: source_mac_verification
                                
                                	Enable Source MAC Verification
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation, self).__init__()

                                    self.yang_name = "dai-address-validation"
                                    self.yang_parent_name = "dai"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.destination_mac_verification = YLeaf(YType.empty, "destination-mac-verification")

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.ipv4_verification = YLeaf(YType.empty, "ipv4-verification")

                                    self.source_mac_verification = YLeaf(YType.empty, "source-mac-verification")
                                    self._segment_path = lambda: "dai-address-validation"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation, ['destination_mac_verification', 'enable', 'ipv4_verification', 'source_mac_verification'], name, value)


                        class IpSourceGuard(Entity):
                            """
                            IP Source Guard
                            
                            .. attribute:: enable
                            
                            	Enable IP Source Guard
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: logging
                            
                            	Enable Logging
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard, self).__init__()

                                self.yang_name = "ip-source-guard"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")

                                self.logging = YLeaf(YType.empty, "logging")
                                self._segment_path = lambda: "ip-source-guard"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard, ['enable', 'logging'], name, value)


                        class MemberVnis(Entity):
                            """
                            Bridge Domain VxLAN Network Identifier
                            Table
                            
                            .. attribute:: member_vni
                            
                            	Bridge Domain Member VxLAN Network Identifier 
                            	**type**\: list of    :py:class:`MemberVni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis, self).__init__()

                                self.yang_name = "member-vnis"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"member-vni" : ("member_vni", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni)}

                                self.member_vni = YList(self)
                                self._segment_path = lambda: "member-vnis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis, [], name, value)


                            class MemberVni(Entity):
                                """
                                Bridge Domain Member VxLAN Network
                                Identifier 
                                
                                .. attribute:: vni  <key>
                                
                                	VxLAN Network Identifier number
                                	**type**\:  int
                                
                                	**range:** 1..16777215
                                
                                .. attribute:: member_vni_static_mac_addresses
                                
                                	Static Mac Address Table
                                	**type**\:   :py:class:`MemberVniStaticMacAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni, self).__init__()

                                    self.yang_name = "member-vni"
                                    self.yang_parent_name = "member-vnis"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"member-vni-static-mac-addresses" : ("member_vni_static_mac_addresses", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses)}
                                    self._child_list_classes = {}

                                    self.vni = YLeaf(YType.uint32, "vni")

                                    self.member_vni_static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses()
                                    self.member_vni_static_mac_addresses.parent = self
                                    self._children_name_map["member_vni_static_mac_addresses"] = "member-vni-static-mac-addresses"
                                    self._children_yang_names.add("member-vni-static-mac-addresses")
                                    self._segment_path = lambda: "member-vni" + "[vni='" + self.vni.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni, ['vni'], name, value)


                                class MemberVniStaticMacAddresses(Entity):
                                    """
                                    Static Mac Address Table
                                    
                                    .. attribute:: member_vni_static_mac_address
                                    
                                    	Static Mac Address Configuration
                                    	**type**\: list of    :py:class:`MemberVniStaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses, self).__init__()

                                        self.yang_name = "member-vni-static-mac-addresses"
                                        self.yang_parent_name = "member-vni"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"member-vni-static-mac-address" : ("member_vni_static_mac_address", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress)}

                                        self.member_vni_static_mac_address = YList(self)
                                        self._segment_path = lambda: "member-vni-static-mac-addresses"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses, [], name, value)


                                    class MemberVniStaticMacAddress(Entity):
                                        """
                                        Static Mac Address Configuration
                                        
                                        .. attribute:: mac_address  <key>
                                        
                                        	Static MAC address
                                        	**type**\:  str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        .. attribute:: next_hop_ip
                                        
                                        	Enable Static Mac Address Configuration
                                        	**type**\:  str
                                        
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
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.mac_address = YLeaf(YType.str, "mac-address")

                                            self.next_hop_ip = YLeaf(YType.str, "next-hop-ip")
                                            self._segment_path = lambda: "member-vni-static-mac-address" + "[mac-address='" + self.mac_address.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress, ['mac_address', 'next_hop_ip'], name, value)


                        class NvSatellite(Entity):
                            """
                            nV Satellite
                            
                            .. attribute:: enable
                            
                            	Enable nV Satellite Settings
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: offload_ipv4_multicast_enable
                            
                            	Enable IPv4 Multicast Offload to Satellite Nodes
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite, self).__init__()

                                self.yang_name = "nv-satellite"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")

                                self.offload_ipv4_multicast_enable = YLeaf(YType.empty, "offload-ipv4-multicast-enable")
                                self._segment_path = lambda: "nv-satellite"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite, ['enable', 'offload_ipv4_multicast_enable'], name, value)


                        class RoutedInterfaces(Entity):
                            """
                            Bridge Domain Routed Interface Table
                            
                            .. attribute:: routed_interface
                            
                            	Bridge Domain Routed Interface
                            	**type**\: list of    :py:class:`RoutedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces, self).__init__()

                                self.yang_name = "routed-interfaces"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"routed-interface" : ("routed_interface", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface)}

                                self.routed_interface = YList(self)
                                self._segment_path = lambda: "routed-interfaces"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces, [], name, value)


                            class RoutedInterface(Entity):
                                """
                                Bridge Domain Routed Interface
                                
                                .. attribute:: interface_name  <key>
                                
                                	The name of the Routed Interface
                                	**type**\:  str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: routed_interface_split_horizon_group
                                
                                	Routed interface split horizon group
                                	**type**\:   :py:class:`RoutedInterfaceSplitHorizonGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface, self).__init__()

                                    self.yang_name = "routed-interface"
                                    self.yang_parent_name = "routed-interfaces"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"routed-interface-split-horizon-group" : ("routed_interface_split_horizon_group", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup)}
                                    self._child_list_classes = {}

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.routed_interface_split_horizon_group = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup()
                                    self.routed_interface_split_horizon_group.parent = self
                                    self._children_name_map["routed_interface_split_horizon_group"] = "routed-interface-split-horizon-group"
                                    self._children_yang_names.add("routed-interface-split-horizon-group")
                                    self._segment_path = lambda: "routed-interface" + "[interface-name='" + self.interface_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface, ['interface_name'], name, value)


                                class RoutedInterfaceSplitHorizonGroup(Entity):
                                    """
                                    Routed interface split horizon group
                                    
                                    .. attribute:: routed_interface_split_horizon_group_core
                                    
                                    	Configure BVI under SHG 1
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup, self).__init__()

                                        self.yang_name = "routed-interface-split-horizon-group"
                                        self.yang_parent_name = "routed-interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.routed_interface_split_horizon_group_core = YLeaf(YType.empty, "routed-interface-split-horizon-group-core")
                                        self._segment_path = lambda: "routed-interface-split-horizon-group"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup, ['routed_interface_split_horizon_group_core'], name, value)


                        class Vfis(Entity):
                            """
                            Specify the virtual forwarding interface
                            name
                            
                            .. attribute:: vfi
                            
                            	Name of the Virtual Forwarding Interface
                            	**type**\: list of    :py:class:`Vfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis, self).__init__()

                                self.yang_name = "vfis"
                                self.yang_parent_name = "bridge-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"vfi" : ("vfi", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi)}

                                self.vfi = YList(self)
                                self._segment_path = lambda: "vfis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis, [], name, value)


                            class Vfi(Entity):
                                """
                                Name of the Virtual Forwarding Interface
                                
                                .. attribute:: name  <key>
                                
                                	Name of the Virtual Forwarding Interface
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: bgp_auto_discovery
                                
                                	Enable Autodiscovery BGP in this VFI
                                	**type**\:   :py:class:`BgpAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery>`
                                
                                .. attribute:: multicast_p2mp
                                
                                	Enable Multicast P2MP in this VFI
                                	**type**\:   :py:class:`MulticastP2Mp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp>`
                                
                                .. attribute:: vfi_pseudowires
                                
                                	List of pseudowires
                                	**type**\:   :py:class:`VfiPseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires>`
                                
                                .. attribute:: vfi_shutdown
                                
                                	Enabling Shutdown
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: vpnid
                                
                                	VPN Identifier
                                	**type**\:  int
                                
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
                                    self._child_container_classes = {"bgp-auto-discovery" : ("bgp_auto_discovery", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery), "multicast-p2mp" : ("multicast_p2mp", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp), "vfi-pseudowires" : ("vfi_pseudowires", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires)}
                                    self._child_list_classes = {}

                                    self.name = YLeaf(YType.str, "name")

                                    self.vfi_shutdown = YLeaf(YType.empty, "vfi-shutdown")

                                    self.vpnid = YLeaf(YType.uint32, "vpnid")

                                    self.bgp_auto_discovery = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery()
                                    self.bgp_auto_discovery.parent = self
                                    self._children_name_map["bgp_auto_discovery"] = "bgp-auto-discovery"
                                    self._children_yang_names.add("bgp-auto-discovery")

                                    self.multicast_p2mp = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp()
                                    self.multicast_p2mp.parent = self
                                    self._children_name_map["multicast_p2mp"] = "multicast-p2mp"
                                    self._children_yang_names.add("multicast-p2mp")

                                    self.vfi_pseudowires = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires()
                                    self.vfi_pseudowires.parent = self
                                    self._children_name_map["vfi_pseudowires"] = "vfi-pseudowires"
                                    self._children_yang_names.add("vfi-pseudowires")
                                    self._segment_path = lambda: "vfi" + "[name='" + self.name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi, ['name', 'vfi_shutdown', 'vpnid'], name, value)


                                class BgpAutoDiscovery(Entity):
                                    """
                                    Enable Autodiscovery BGP in this VFI
                                    
                                    .. attribute:: ad_control_word
                                    
                                    	Enable control\-word for this VFI
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: bgp_route_policy
                                    
                                    	Route policy
                                    	**type**\:   :py:class:`BgpRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy>`
                                    
                                    .. attribute:: bgp_signaling_protocol
                                    
                                    	Enable Signaling Protocol BGP in this VFI
                                    	**type**\:   :py:class:`BgpSignalingProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable Autodiscovery BGP
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: ldp_signaling_protocol
                                    
                                    	Signaling Protocol LDP in this VFI configuration
                                    	**type**\:   :py:class:`LdpSignalingProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol>`
                                    
                                    .. attribute:: route_distinguisher
                                    
                                    	Route Distinguisher
                                    	**type**\:   :py:class:`RouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher>`
                                    
                                    .. attribute:: route_targets
                                    
                                    	Route Target
                                    	**type**\:   :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets>`
                                    
                                    .. attribute:: table_policy
                                    
                                    	Table Policy for installation of forwarding data to L2FIB
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery, self).__init__()

                                        self.yang_name = "bgp-auto-discovery"
                                        self.yang_parent_name = "vfi"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"bgp-route-policy" : ("bgp_route_policy", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy), "bgp-signaling-protocol" : ("bgp_signaling_protocol", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol), "ldp-signaling-protocol" : ("ldp_signaling_protocol", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol), "route-distinguisher" : ("route_distinguisher", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher), "route-targets" : ("route_targets", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets)}
                                        self._child_list_classes = {}

                                        self.ad_control_word = YLeaf(YType.empty, "ad-control-word")

                                        self.enable = YLeaf(YType.empty, "enable")

                                        self.table_policy = YLeaf(YType.str, "table-policy")

                                        self.bgp_route_policy = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy()
                                        self.bgp_route_policy.parent = self
                                        self._children_name_map["bgp_route_policy"] = "bgp-route-policy"
                                        self._children_yang_names.add("bgp-route-policy")

                                        self.bgp_signaling_protocol = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol()
                                        self.bgp_signaling_protocol.parent = self
                                        self._children_name_map["bgp_signaling_protocol"] = "bgp-signaling-protocol"
                                        self._children_yang_names.add("bgp-signaling-protocol")

                                        self.ldp_signaling_protocol = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol()
                                        self.ldp_signaling_protocol.parent = self
                                        self._children_name_map["ldp_signaling_protocol"] = "ldp-signaling-protocol"
                                        self._children_yang_names.add("ldp-signaling-protocol")

                                        self.route_distinguisher = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher()
                                        self.route_distinguisher.parent = self
                                        self._children_name_map["route_distinguisher"] = "route-distinguisher"
                                        self._children_yang_names.add("route-distinguisher")

                                        self.route_targets = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets()
                                        self.route_targets.parent = self
                                        self._children_name_map["route_targets"] = "route-targets"
                                        self._children_yang_names.add("route-targets")
                                        self._segment_path = lambda: "bgp-auto-discovery"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery, ['ad_control_word', 'enable', 'table_policy'], name, value)


                                    class BgpRoutePolicy(Entity):
                                        """
                                        Route policy
                                        
                                        .. attribute:: export
                                        
                                        	Export route policy
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy, self).__init__()

                                            self.yang_name = "bgp-route-policy"
                                            self.yang_parent_name = "bgp-auto-discovery"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.export = YLeaf(YType.str, "export")
                                            self._segment_path = lambda: "bgp-route-policy"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy, ['export'], name, value)


                                    class BgpSignalingProtocol(Entity):
                                        """
                                        Enable Signaling Protocol BGP in this
                                        VFI
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP as Signaling Protocol
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: flow_label_load_balance
                                        
                                        	Enable Flow Label based load balancing
                                        	**type**\:   :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance>`
                                        
                                        .. attribute:: ve_range
                                        
                                        	Local Virtual Edge Block Configurable Range
                                        	**type**\:  int
                                        
                                        	**range:** 11..100
                                        
                                        .. attribute:: veid
                                        
                                        	Local Virtual Edge Identifier
                                        	**type**\:  int
                                        
                                        	**range:** 1..16384
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol, self).__init__()

                                            self.yang_name = "bgp-signaling-protocol"
                                            self.yang_parent_name = "bgp-auto-discovery"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"flow-label-load-balance" : ("flow_label_load_balance", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance)}
                                            self._child_list_classes = {}

                                            self.enable = YLeaf(YType.empty, "enable")

                                            self.ve_range = YLeaf(YType.uint32, "ve-range")

                                            self.veid = YLeaf(YType.uint32, "veid")

                                            self.flow_label_load_balance = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance()
                                            self.flow_label_load_balance.parent = self
                                            self._children_name_map["flow_label_load_balance"] = "flow-label-load-balance"
                                            self._children_yang_names.add("flow-label-load-balance")
                                            self._segment_path = lambda: "bgp-signaling-protocol"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol, ['enable', 've_range', 'veid'], name, value)


                                        class FlowLabelLoadBalance(Entity):
                                            """
                                            Enable Flow Label based load balancing
                                            
                                            .. attribute:: flow_label
                                            
                                            	Flow Label load balance type
                                            	**type**\:   :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalance>`
                                            
                                            .. attribute:: static
                                            
                                            	Static Flow Label
                                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance, self).__init__()

                                                self.yang_name = "flow-label-load-balance"
                                                self.yang_parent_name = "bgp-signaling-protocol"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.flow_label = YLeaf(YType.enumeration, "flow-label")

                                                self.static = YLeaf(YType.empty, "static")
                                                self._segment_path = lambda: "flow-label-load-balance"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance, ['flow_label', 'static'], name, value)


                                    class LdpSignalingProtocol(Entity):
                                        """
                                        Signaling Protocol LDP in this VFI
                                        configuration
                                        
                                        .. attribute:: enable
                                        
                                        	Enable LDP as Signaling Protocol .Deletion of this object also causes deletion of all objects under LDPSignalingProtocol
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: flow_label_load_balance
                                        
                                        	Enable Flow Label based load balancing
                                        	**type**\:   :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance>`
                                        
                                        .. attribute:: vpls_id
                                        
                                        	VPLS ID
                                        	**type**\:   :py:class:`VplsId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.VplsId>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol, self).__init__()

                                            self.yang_name = "ldp-signaling-protocol"
                                            self.yang_parent_name = "bgp-auto-discovery"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"flow-label-load-balance" : ("flow_label_load_balance", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance), "vpls-id" : ("vpls_id", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.VplsId)}
                                            self._child_list_classes = {}

                                            self.enable = YLeaf(YType.empty, "enable")

                                            self.flow_label_load_balance = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance()
                                            self.flow_label_load_balance.parent = self
                                            self._children_name_map["flow_label_load_balance"] = "flow-label-load-balance"
                                            self._children_yang_names.add("flow-label-load-balance")

                                            self.vpls_id = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.VplsId()
                                            self.vpls_id.parent = self
                                            self._children_name_map["vpls_id"] = "vpls-id"
                                            self._children_yang_names.add("vpls-id")
                                            self._segment_path = lambda: "ldp-signaling-protocol"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol, ['enable'], name, value)


                                        class FlowLabelLoadBalance(Entity):
                                            """
                                            Enable Flow Label based load balancing
                                            
                                            .. attribute:: flow_label
                                            
                                            	Flow Label load balance type
                                            	**type**\:   :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalance>`
                                            
                                            .. attribute:: static
                                            
                                            	Static Flow Label
                                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance, self).__init__()

                                                self.yang_name = "flow-label-load-balance"
                                                self.yang_parent_name = "ldp-signaling-protocol"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.flow_label = YLeaf(YType.enumeration, "flow-label")

                                                self.static = YLeaf(YType.empty, "static")
                                                self._segment_path = lambda: "flow-label-load-balance"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance, ['flow_label', 'static'], name, value)


                                        class VplsId(Entity):
                                            """
                                            VPLS ID
                                            
                                            .. attribute:: address
                                            
                                            	IPV4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: address_index
                                            
                                            	Address index
                                            	**type**\:  int
                                            
                                            	**range:** 0..32767
                                            
                                            .. attribute:: as_
                                            
                                            	Two byte AS number
                                            	**type**\:  int
                                            
                                            	**range:** 1..65535
                                            
                                            .. attribute:: as_index
                                            
                                            	AS index
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: type
                                            
                                            	VPLS\-ID Type
                                            	**type**\:   :py:class:`LdpVplsId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.LdpVplsId>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.VplsId, self).__init__()

                                                self.yang_name = "vpls-id"
                                                self.yang_parent_name = "ldp-signaling-protocol"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.address = YLeaf(YType.str, "address")

                                                self.address_index = YLeaf(YType.uint32, "address-index")

                                                self.as_ = YLeaf(YType.uint32, "as")

                                                self.as_index = YLeaf(YType.uint32, "as-index")

                                                self.type = YLeaf(YType.enumeration, "type")
                                                self._segment_path = lambda: "vpls-id"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.VplsId, ['address', 'address_index', 'as_', 'as_index', 'type'], name, value)


                                    class RouteDistinguisher(Entity):
                                        """
                                        Route Distinguisher
                                        
                                        .. attribute:: addr_index
                                        
                                        	Addr index
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: address
                                        
                                        	IPV4 address
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: as_
                                        
                                        	Two byte or 4 byte AS number
                                        	**type**\:  int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: as_index
                                        
                                        	AS\:nn (hex or decimal format)
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: type
                                        
                                        	Router Distinguisher Type
                                        	**type**\:   :py:class:`BgpRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher, self).__init__()

                                            self.yang_name = "route-distinguisher"
                                            self.yang_parent_name = "bgp-auto-discovery"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.addr_index = YLeaf(YType.uint32, "addr-index")

                                            self.address = YLeaf(YType.str, "address")

                                            self.as_ = YLeaf(YType.uint32, "as")

                                            self.as_index = YLeaf(YType.uint32, "as-index")

                                            self.type = YLeaf(YType.enumeration, "type")
                                            self._segment_path = lambda: "route-distinguisher"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher, ['addr_index', 'address', 'as_', 'as_index', 'type'], name, value)


                                    class RouteTargets(Entity):
                                        """
                                        Route Target
                                        
                                        .. attribute:: route_target
                                        
                                        	Name of the Route Target
                                        	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets, self).__init__()

                                            self.yang_name = "route-targets"
                                            self.yang_parent_name = "bgp-auto-discovery"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"route-target" : ("route_target", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget)}

                                            self.route_target = YList(self)
                                            self._segment_path = lambda: "route-targets"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets, [], name, value)


                                        class RouteTarget(Entity):
                                            """
                                            Name of the Route Target
                                            
                                            .. attribute:: role  <key>
                                            
                                            	Role of the router target type
                                            	**type**\:   :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                                            
                                            .. attribute:: format  <key>
                                            
                                            	Format of the route target
                                            	**type**\:   :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	ipv4 address
                                            	**type**\: list of    :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address>`
                                            
                                            .. attribute:: two_byte_as_or_four_byte_as
                                            
                                            	two byte as or four byte as
                                            	**type**\: list of    :py:class:`TwoByteAsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget, self).__init__()

                                                self.yang_name = "route-target"
                                                self.yang_parent_name = "route-targets"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"ipv4-address" : ("ipv4_address", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address), "two-byte-as-or-four-byte-as" : ("two_byte_as_or_four_byte_as", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs)}

                                                self.role = YLeaf(YType.enumeration, "role")

                                                self.format = YLeaf(YType.enumeration, "format")

                                                self.ipv4_address = YList(self)
                                                self.two_byte_as_or_four_byte_as = YList(self)
                                                self._segment_path = lambda: "route-target" + "[role='" + self.role.get() + "']" + "[format='" + self.format.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget, ['role', 'format'], name, value)


                                            class Ipv4Address(Entity):
                                                """
                                                ipv4 address
                                                
                                                .. attribute:: address  <key>
                                                
                                                	IPV4 address
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: addr_index  <key>
                                                
                                                	Addr index
                                                	**type**\:  int
                                                
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
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.address = YLeaf(YType.str, "address")

                                                    self.addr_index = YLeaf(YType.uint32, "addr-index")
                                                    self._segment_path = lambda: "ipv4-address" + "[address='" + self.address.get() + "']" + "[addr-index='" + self.addr_index.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address, ['address', 'addr_index'], name, value)


                                            class TwoByteAsOrFourByteAs(Entity):
                                                """
                                                two byte as or four byte as
                                                
                                                .. attribute:: as_  <key>
                                                
                                                	Two byte or 4 byte AS number
                                                	**type**\:  int
                                                
                                                	**range:** 1..4294967295
                                                
                                                .. attribute:: as_index  <key>
                                                
                                                	AS\:nn (hex or decimal format)
                                                	**type**\:  int
                                                
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
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.as_ = YLeaf(YType.uint32, "as")

                                                    self.as_index = YLeaf(YType.uint32, "as-index")
                                                    self._segment_path = lambda: "two-byte-as-or-four-byte-as" + "[as='" + self.as_.get() + "']" + "[as-index='" + self.as_index.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs, ['as_', 'as_index'], name, value)


                                class MulticastP2Mp(Entity):
                                    """
                                    Enable Multicast P2MP in this VFI
                                    
                                    .. attribute:: enable
                                    
                                    	Enable Autodiscovery P2MP
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: signalings
                                    
                                    	Multicast P2MP Signaling Type
                                    	**type**\:   :py:class:`Signalings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings>`
                                    
                                    .. attribute:: transports
                                    
                                    	Multicast P2MP Transport
                                    	**type**\:   :py:class:`Transports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp, self).__init__()

                                        self.yang_name = "multicast-p2mp"
                                        self.yang_parent_name = "vfi"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"signalings" : ("signalings", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings), "transports" : ("transports", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports)}
                                        self._child_list_classes = {}

                                        self.enable = YLeaf(YType.empty, "enable")

                                        self.signalings = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings()
                                        self.signalings.parent = self
                                        self._children_name_map["signalings"] = "signalings"
                                        self._children_yang_names.add("signalings")

                                        self.transports = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports()
                                        self.transports.parent = self
                                        self._children_name_map["transports"] = "transports"
                                        self._children_yang_names.add("transports")
                                        self._segment_path = lambda: "multicast-p2mp"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp, ['enable'], name, value)


                                    class Signalings(Entity):
                                        """
                                        Multicast P2MP Signaling Type
                                        
                                        .. attribute:: signaling
                                        
                                        	Multicast P2MP Signaling Type
                                        	**type**\: list of    :py:class:`Signaling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings, self).__init__()

                                            self.yang_name = "signalings"
                                            self.yang_parent_name = "multicast-p2mp"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"signaling" : ("signaling", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling)}

                                            self.signaling = YList(self)
                                            self._segment_path = lambda: "signalings"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings, [], name, value)


                                        class Signaling(Entity):
                                            """
                                            Multicast P2MP Signaling Type
                                            
                                            .. attribute:: signaling_name  <key>
                                            
                                            	Signaling Type
                                            	**type**\:  str
                                            
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
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.signaling_name = YLeaf(YType.str, "signaling-name")
                                                self._segment_path = lambda: "signaling" + "[signaling-name='" + self.signaling_name.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling, ['signaling_name'], name, value)


                                    class Transports(Entity):
                                        """
                                        Multicast P2MP Transport
                                        
                                        .. attribute:: transport
                                        
                                        	Multicast P2MP Transport Type
                                        	**type**\: list of    :py:class:`Transport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports, self).__init__()

                                            self.yang_name = "transports"
                                            self.yang_parent_name = "multicast-p2mp"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"transport" : ("transport", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport)}

                                            self.transport = YList(self)
                                            self._segment_path = lambda: "transports"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports, [], name, value)


                                        class Transport(Entity):
                                            """
                                            Multicast P2MP Transport Type
                                            
                                            .. attribute:: transport_name  <key>
                                            
                                            	Transport Type
                                            	**type**\:  str
                                            
                                            	**pattern:** (RSVP\_TE)
                                            
                                            .. attribute:: attribute_set_name
                                            
                                            	Multicast P2MP TE Attribute Set Name
                                            	**type**\:  str
                                            
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
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.transport_name = YLeaf(YType.str, "transport-name")

                                                self.attribute_set_name = YLeaf(YType.str, "attribute-set-name")
                                                self._segment_path = lambda: "transport" + "[transport-name='" + self.transport_name.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport, ['transport_name', 'attribute_set_name'], name, value)


                                class VfiPseudowires(Entity):
                                    """
                                    List of pseudowires
                                    
                                    .. attribute:: vfi_pseudowire
                                    
                                    	Pseudowire configuration
                                    	**type**\: list of    :py:class:`VfiPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires, self).__init__()

                                        self.yang_name = "vfi-pseudowires"
                                        self.yang_parent_name = "vfi"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"vfi-pseudowire" : ("vfi_pseudowire", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire)}

                                        self.vfi_pseudowire = YList(self)
                                        self._segment_path = lambda: "vfi-pseudowires"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires, [], name, value)


                                    class VfiPseudowire(Entity):
                                        """
                                        Pseudowire configuration
                                        
                                        .. attribute:: neighbor  <key>
                                        
                                        	Neighbor IP address
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: pseudowire_id  <key>
                                        
                                        	Pseudowire ID
                                        	**type**\:  int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: pseudowire_static_mac_addresses
                                        
                                        	Static Mac Address Table
                                        	**type**\:   :py:class:`PseudowireStaticMacAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses>`
                                        
                                        .. attribute:: vfi_pw_class
                                        
                                        	PW class template name to use for this pseudowire
                                        	**type**\:  str
                                        
                                        	**length:** 1..32
                                        
                                        .. attribute:: vfi_pw_dhcp_snoop
                                        
                                        	Attach a DHCP Snooping profile
                                        	**type**\:   :py:class:`VfiPwDhcpSnoop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop>`
                                        
                                        .. attribute:: vfi_pw_igmp_snoop
                                        
                                        	Attach a IGMP Snooping profile
                                        	**type**\:  str
                                        
                                        	**length:** 1..32
                                        
                                        .. attribute:: vfi_pw_mld_snoop
                                        
                                        	Attach a MLD Snooping profile
                                        	**type**\:  str
                                        
                                        	**length:** 1..32
                                        
                                        .. attribute:: vfi_pw_mpls_static_labels
                                        
                                        	MPLS static labels
                                        	**type**\:   :py:class:`VfiPwMplsStaticLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire, self).__init__()

                                            self.yang_name = "vfi-pseudowire"
                                            self.yang_parent_name = "vfi-pseudowires"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"pseudowire-static-mac-addresses" : ("pseudowire_static_mac_addresses", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses), "vfi-pw-dhcp-snoop" : ("vfi_pw_dhcp_snoop", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop), "vfi-pw-mpls-static-labels" : ("vfi_pw_mpls_static_labels", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels)}
                                            self._child_list_classes = {}

                                            self.neighbor = YLeaf(YType.str, "neighbor")

                                            self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                                            self.vfi_pw_class = YLeaf(YType.str, "vfi-pw-class")

                                            self.vfi_pw_igmp_snoop = YLeaf(YType.str, "vfi-pw-igmp-snoop")

                                            self.vfi_pw_mld_snoop = YLeaf(YType.str, "vfi-pw-mld-snoop")

                                            self.pseudowire_static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses()
                                            self.pseudowire_static_mac_addresses.parent = self
                                            self._children_name_map["pseudowire_static_mac_addresses"] = "pseudowire-static-mac-addresses"
                                            self._children_yang_names.add("pseudowire-static-mac-addresses")

                                            self.vfi_pw_dhcp_snoop = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop()
                                            self.vfi_pw_dhcp_snoop.parent = self
                                            self._children_name_map["vfi_pw_dhcp_snoop"] = "vfi-pw-dhcp-snoop"
                                            self._children_yang_names.add("vfi-pw-dhcp-snoop")

                                            self.vfi_pw_mpls_static_labels = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels()
                                            self.vfi_pw_mpls_static_labels.parent = self
                                            self._children_name_map["vfi_pw_mpls_static_labels"] = "vfi-pw-mpls-static-labels"
                                            self._children_yang_names.add("vfi-pw-mpls-static-labels")
                                            self._segment_path = lambda: "vfi-pseudowire" + "[neighbor='" + self.neighbor.get() + "']" + "[pseudowire-id='" + self.pseudowire_id.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire, ['neighbor', 'pseudowire_id', 'vfi_pw_class', 'vfi_pw_igmp_snoop', 'vfi_pw_mld_snoop'], name, value)


                                        class PseudowireStaticMacAddresses(Entity):
                                            """
                                            Static Mac Address Table
                                            
                                            .. attribute:: pseudowire_static_mac_address
                                            
                                            	Static Mac Address Configuration
                                            	**type**\: list of    :py:class:`PseudowireStaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses, self).__init__()

                                                self.yang_name = "pseudowire-static-mac-addresses"
                                                self.yang_parent_name = "vfi-pseudowire"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"pseudowire-static-mac-address" : ("pseudowire_static_mac_address", L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress)}

                                                self.pseudowire_static_mac_address = YList(self)
                                                self._segment_path = lambda: "pseudowire-static-mac-addresses"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses, [], name, value)


                                            class PseudowireStaticMacAddress(Entity):
                                                """
                                                Static Mac Address Configuration
                                                
                                                .. attribute:: address  <key>
                                                
                                                	Static MAC address
                                                	**type**\:  str
                                                
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
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.address = YLeaf(YType.str, "address")
                                                    self._segment_path = lambda: "pseudowire-static-mac-address" + "[address='" + self.address.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress, ['address'], name, value)


                                        class VfiPwDhcpSnoop(Entity):
                                            """
                                            Attach a DHCP Snooping profile
                                            
                                            .. attribute:: dhcp_snooping_id
                                            
                                            	Disable DHCP snooping
                                            	**type**\:  str
                                            
                                            .. attribute:: profile_id
                                            
                                            	Set the snooping profile
                                            	**type**\:   :py:class:`InterfaceProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop, self).__init__()

                                                self.yang_name = "vfi-pw-dhcp-snoop"
                                                self.yang_parent_name = "vfi-pseudowire"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.dhcp_snooping_id = YLeaf(YType.str, "dhcp-snooping-id")

                                                self.profile_id = YLeaf(YType.enumeration, "profile-id")
                                                self._segment_path = lambda: "vfi-pw-dhcp-snoop"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop, ['dhcp_snooping_id', 'profile_id'], name, value)


                                        class VfiPwMplsStaticLabels(Entity):
                                            """
                                            MPLS static labels
                                            
                                            .. attribute:: local_static_label
                                            
                                            	Pseudowire local static label
                                            	**type**\:  int
                                            
                                            	**range:** 16..1048575
                                            
                                            .. attribute:: remote_static_label
                                            
                                            	Pseudowire remote static label
                                            	**type**\:  int
                                            
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
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.local_static_label = YLeaf(YType.uint32, "local-static-label")

                                                self.remote_static_label = YLeaf(YType.uint32, "remote-static-label")
                                                self._segment_path = lambda: "vfi-pw-mpls-static-labels"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels, ['local_static_label', 'remote_static_label'], name, value)


        class FlexibleXconnectServiceTable(Entity):
            """
            List of Flexible XConnect Services
            
            .. attribute:: vlan_aware_flexible_xconnect_services
            
            	List of Vlan\-Aware Flexible XConnect Services
            	**type**\:   :py:class:`VlanAwareFlexibleXconnectServices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices>`
            
            .. attribute:: vlan_unaware_flexible_xconnect_services
            
            	List of Vlan\-Unaware Flexible XConnect Services
            	**type**\:   :py:class:`VlanUnawareFlexibleXconnectServices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Database.FlexibleXconnectServiceTable, self).__init__()

                self.yang_name = "flexible-xconnect-service-table"
                self.yang_parent_name = "database"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"vlan-aware-flexible-xconnect-services" : ("vlan_aware_flexible_xconnect_services", L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices), "vlan-unaware-flexible-xconnect-services" : ("vlan_unaware_flexible_xconnect_services", L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices)}
                self._child_list_classes = {}

                self.vlan_aware_flexible_xconnect_services = L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices()
                self.vlan_aware_flexible_xconnect_services.parent = self
                self._children_name_map["vlan_aware_flexible_xconnect_services"] = "vlan-aware-flexible-xconnect-services"
                self._children_yang_names.add("vlan-aware-flexible-xconnect-services")

                self.vlan_unaware_flexible_xconnect_services = L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices()
                self.vlan_unaware_flexible_xconnect_services.parent = self
                self._children_name_map["vlan_unaware_flexible_xconnect_services"] = "vlan-unaware-flexible-xconnect-services"
                self._children_yang_names.add("vlan-unaware-flexible-xconnect-services")
                self._segment_path = lambda: "flexible-xconnect-service-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/%s" % self._segment_path()


            class VlanAwareFlexibleXconnectServices(Entity):
                """
                List of Vlan\-Aware Flexible XConnect Services
                
                .. attribute:: vlan_aware_flexible_xconnect_service
                
                	Flexible XConnect Service
                	**type**\: list of    :py:class:`VlanAwareFlexibleXconnectService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices, self).__init__()

                    self.yang_name = "vlan-aware-flexible-xconnect-services"
                    self.yang_parent_name = "flexible-xconnect-service-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"vlan-aware-flexible-xconnect-service" : ("vlan_aware_flexible_xconnect_service", L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService)}

                    self.vlan_aware_flexible_xconnect_service = YList(self)
                    self._segment_path = lambda: "vlan-aware-flexible-xconnect-services"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/flexible-xconnect-service-table/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices, [], name, value)


                class VlanAwareFlexibleXconnectService(Entity):
                    """
                    Flexible XConnect Service
                    
                    .. attribute:: eviid  <key>
                    
                    	Ethernet VPN ID
                    	**type**\:  int
                    
                    	**range:** 1..65534
                    
                    .. attribute:: vlan_aware_fxc_attachment_circuits
                    
                    	List of attachment circuits
                    	**type**\:   :py:class:`VlanAwareFxcAttachmentCircuits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService, self).__init__()

                        self.yang_name = "vlan-aware-flexible-xconnect-service"
                        self.yang_parent_name = "vlan-aware-flexible-xconnect-services"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"vlan-aware-fxc-attachment-circuits" : ("vlan_aware_fxc_attachment_circuits", L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits)}
                        self._child_list_classes = {}

                        self.eviid = YLeaf(YType.uint32, "eviid")

                        self.vlan_aware_fxc_attachment_circuits = L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits()
                        self.vlan_aware_fxc_attachment_circuits.parent = self
                        self._children_name_map["vlan_aware_fxc_attachment_circuits"] = "vlan-aware-fxc-attachment-circuits"
                        self._children_yang_names.add("vlan-aware-fxc-attachment-circuits")
                        self._segment_path = lambda: "vlan-aware-flexible-xconnect-service" + "[eviid='" + self.eviid.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/flexible-xconnect-service-table/vlan-aware-flexible-xconnect-services/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService, ['eviid'], name, value)


                    class VlanAwareFxcAttachmentCircuits(Entity):
                        """
                        List of attachment circuits
                        
                        .. attribute:: vlan_aware_fxc_attachment_circuit
                        
                        	Attachment circuit interface
                        	**type**\: list of    :py:class:`VlanAwareFxcAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits, self).__init__()

                            self.yang_name = "vlan-aware-fxc-attachment-circuits"
                            self.yang_parent_name = "vlan-aware-flexible-xconnect-service"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"vlan-aware-fxc-attachment-circuit" : ("vlan_aware_fxc_attachment_circuit", L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit)}

                            self.vlan_aware_fxc_attachment_circuit = YList(self)
                            self._segment_path = lambda: "vlan-aware-fxc-attachment-circuits"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits, [], name, value)


                        class VlanAwareFxcAttachmentCircuit(Entity):
                            """
                            Attachment circuit interface
                            
                            .. attribute:: name  <key>
                            
                            	Name of the attachment circuit interface
                            	**type**\:  str
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.name = YLeaf(YType.str, "name")
                                self._segment_path = lambda: "vlan-aware-fxc-attachment-circuit" + "[name='" + self.name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit, ['name'], name, value)


            class VlanUnawareFlexibleXconnectServices(Entity):
                """
                List of Vlan\-Unaware Flexible XConnect
                Services
                
                .. attribute:: vlan_unaware_flexible_xconnect_service
                
                	Flexible XConnect Service
                	**type**\: list of    :py:class:`VlanUnawareFlexibleXconnectService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices, self).__init__()

                    self.yang_name = "vlan-unaware-flexible-xconnect-services"
                    self.yang_parent_name = "flexible-xconnect-service-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"vlan-unaware-flexible-xconnect-service" : ("vlan_unaware_flexible_xconnect_service", L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService)}

                    self.vlan_unaware_flexible_xconnect_service = YList(self)
                    self._segment_path = lambda: "vlan-unaware-flexible-xconnect-services"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/flexible-xconnect-service-table/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices, [], name, value)


                class VlanUnawareFlexibleXconnectService(Entity):
                    """
                    Flexible XConnect Service
                    
                    .. attribute:: name  <key>
                    
                    	Name of the Flexible XConnect Service
                    	**type**\:  str
                    
                    	**length:** 1..23
                    
                    .. attribute:: vlan_unaware_fxc_attachment_circuits
                    
                    	List of attachment circuits
                    	**type**\:   :py:class:`VlanUnawareFxcAttachmentCircuits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits>`
                    
                    .. attribute:: vlan_unaware_fxc_pseudowire_evpns
                    
                    	List of EVPN Services
                    	**type**\:   :py:class:`VlanUnawareFxcPseudowireEvpns <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService, self).__init__()

                        self.yang_name = "vlan-unaware-flexible-xconnect-service"
                        self.yang_parent_name = "vlan-unaware-flexible-xconnect-services"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"vlan-unaware-fxc-attachment-circuits" : ("vlan_unaware_fxc_attachment_circuits", L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits), "vlan-unaware-fxc-pseudowire-evpns" : ("vlan_unaware_fxc_pseudowire_evpns", L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns)}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.str, "name")

                        self.vlan_unaware_fxc_attachment_circuits = L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits()
                        self.vlan_unaware_fxc_attachment_circuits.parent = self
                        self._children_name_map["vlan_unaware_fxc_attachment_circuits"] = "vlan-unaware-fxc-attachment-circuits"
                        self._children_yang_names.add("vlan-unaware-fxc-attachment-circuits")

                        self.vlan_unaware_fxc_pseudowire_evpns = L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns()
                        self.vlan_unaware_fxc_pseudowire_evpns.parent = self
                        self._children_name_map["vlan_unaware_fxc_pseudowire_evpns"] = "vlan-unaware-fxc-pseudowire-evpns"
                        self._children_yang_names.add("vlan-unaware-fxc-pseudowire-evpns")
                        self._segment_path = lambda: "vlan-unaware-flexible-xconnect-service" + "[name='" + self.name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/flexible-xconnect-service-table/vlan-unaware-flexible-xconnect-services/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService, ['name'], name, value)


                    class VlanUnawareFxcAttachmentCircuits(Entity):
                        """
                        List of attachment circuits
                        
                        .. attribute:: vlan_unaware_fxc_attachment_circuit
                        
                        	Attachment circuit interface
                        	**type**\: list of    :py:class:`VlanUnawareFxcAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits, self).__init__()

                            self.yang_name = "vlan-unaware-fxc-attachment-circuits"
                            self.yang_parent_name = "vlan-unaware-flexible-xconnect-service"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"vlan-unaware-fxc-attachment-circuit" : ("vlan_unaware_fxc_attachment_circuit", L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit)}

                            self.vlan_unaware_fxc_attachment_circuit = YList(self)
                            self._segment_path = lambda: "vlan-unaware-fxc-attachment-circuits"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits, [], name, value)


                        class VlanUnawareFxcAttachmentCircuit(Entity):
                            """
                            Attachment circuit interface
                            
                            .. attribute:: name  <key>
                            
                            	Name of the attachment circuit interface
                            	**type**\:  str
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.name = YLeaf(YType.str, "name")
                                self._segment_path = lambda: "vlan-unaware-fxc-attachment-circuit" + "[name='" + self.name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit, ['name'], name, value)


                    class VlanUnawareFxcPseudowireEvpns(Entity):
                        """
                        List of EVPN Services
                        
                        .. attribute:: vlan_unaware_fxc_pseudowire_evpn
                        
                        	EVPN FXC Service Configuration
                        	**type**\: list of    :py:class:`VlanUnawareFxcPseudowireEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns, self).__init__()

                            self.yang_name = "vlan-unaware-fxc-pseudowire-evpns"
                            self.yang_parent_name = "vlan-unaware-flexible-xconnect-service"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"vlan-unaware-fxc-pseudowire-evpn" : ("vlan_unaware_fxc_pseudowire_evpn", L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn)}

                            self.vlan_unaware_fxc_pseudowire_evpn = YList(self)
                            self._segment_path = lambda: "vlan-unaware-fxc-pseudowire-evpns"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns, [], name, value)


                        class VlanUnawareFxcPseudowireEvpn(Entity):
                            """
                            EVPN FXC Service Configuration
                            
                            .. attribute:: eviid  <key>
                            
                            	Ethernet VPN ID
                            	**type**\:  int
                            
                            	**range:** 1..65534
                            
                            .. attribute:: acid  <key>
                            
                            	AC ID
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.eviid = YLeaf(YType.uint32, "eviid")

                                self.acid = YLeaf(YType.uint32, "acid")
                                self._segment_path = lambda: "vlan-unaware-fxc-pseudowire-evpn" + "[eviid='" + self.eviid.get() + "']" + "[acid='" + self.acid.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn, ['eviid', 'acid'], name, value)


        class G8032Rings(Entity):
            """
            List of G8032 Ring
            
            .. attribute:: g8032_ring
            
            	G8032 Ring
            	**type**\: list of    :py:class:`G8032Ring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Database.G8032Rings, self).__init__()

                self.yang_name = "g8032-rings"
                self.yang_parent_name = "database"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"g8032-ring" : ("g8032_ring", L2Vpn.Database.G8032Rings.G8032Ring)}

                self.g8032_ring = YList(self)
                self._segment_path = lambda: "g8032-rings"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.Database.G8032Rings, [], name, value)


            class G8032Ring(Entity):
                """
                G8032 Ring
                
                .. attribute:: g8032_ring_name  <key>
                
                	Name of the G8032 ring
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: erp_instances
                
                	List of ethernet ring protection instance
                	**type**\:   :py:class:`ErpInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances>`
                
                .. attribute:: erp_port0s
                
                	Ethernet ring protection port0
                	**type**\:   :py:class:`ErpPort0S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S>`
                
                .. attribute:: erp_port1s
                
                	Ethernet ring protection port0
                	**type**\:   :py:class:`ErpPort1S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S>`
                
                .. attribute:: erp_provider_bridge
                
                	Ethernet ring protection provider bridge
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: exclusion_list
                
                	Vlan IDs in the format of a\-b,c,d,e\-f,g ,untagged
                	**type**\:  str
                
                .. attribute:: open_ring
                
                	Specify the G.8032 instance as open ring
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.G8032Rings.G8032Ring, self).__init__()

                    self.yang_name = "g8032-ring"
                    self.yang_parent_name = "g8032-rings"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"erp-instances" : ("erp_instances", L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances), "erp-port0s" : ("erp_port0s", L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S), "erp-port1s" : ("erp_port1s", L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S)}
                    self._child_list_classes = {}

                    self.g8032_ring_name = YLeaf(YType.str, "g8032-ring-name")

                    self.erp_provider_bridge = YLeaf(YType.empty, "erp-provider-bridge")

                    self.exclusion_list = YLeaf(YType.str, "exclusion-list")

                    self.open_ring = YLeaf(YType.empty, "open-ring")

                    self.erp_instances = L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances()
                    self.erp_instances.parent = self
                    self._children_name_map["erp_instances"] = "erp-instances"
                    self._children_yang_names.add("erp-instances")

                    self.erp_port0s = L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S()
                    self.erp_port0s.parent = self
                    self._children_name_map["erp_port0s"] = "erp-port0s"
                    self._children_yang_names.add("erp-port0s")

                    self.erp_port1s = L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S()
                    self.erp_port1s.parent = self
                    self._children_name_map["erp_port1s"] = "erp-port1s"
                    self._children_yang_names.add("erp-port1s")
                    self._segment_path = lambda: "g8032-ring" + "[g8032-ring-name='" + self.g8032_ring_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/g8032-rings/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring, ['g8032_ring_name', 'erp_provider_bridge', 'exclusion_list', 'open_ring'], name, value)


                class ErpInstances(Entity):
                    """
                    List of ethernet ring protection instance
                    
                    .. attribute:: erp_instance
                    
                    	Ethernet ring protection instance
                    	**type**\: list of    :py:class:`ErpInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances, self).__init__()

                        self.yang_name = "erp-instances"
                        self.yang_parent_name = "g8032-ring"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"erp-instance" : ("erp_instance", L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance)}

                        self.erp_instance = YList(self)
                        self._segment_path = lambda: "erp-instances"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances, [], name, value)


                    class ErpInstance(Entity):
                        """
                        Ethernet ring protection instance
                        
                        .. attribute:: erp_instance_id  <key>
                        
                        	ERP instance number
                        	**type**\:  int
                        
                        	**range:** 1..2
                        
                        .. attribute:: aps
                        
                        	Automatic protection switching
                        	**type**\:   :py:class:`Aps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps>`
                        
                        .. attribute:: description
                        
                        	Ethernet ring protection instance description
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: inclusion_list
                        
                        	Associates a set of VLAN IDs with the G .8032 instance
                        	**type**\:  str
                        
                        .. attribute:: profile
                        
                        	Ethernet ring protection instance profile
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: rpl
                        
                        	Ring protection link
                        	**type**\:   :py:class:`Rpl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance, self).__init__()

                            self.yang_name = "erp-instance"
                            self.yang_parent_name = "erp-instances"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"aps" : ("aps", L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps), "rpl" : ("rpl", L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl)}
                            self._child_list_classes = {}

                            self.erp_instance_id = YLeaf(YType.uint32, "erp-instance-id")

                            self.description = YLeaf(YType.str, "description")

                            self.inclusion_list = YLeaf(YType.str, "inclusion-list")

                            self.profile = YLeaf(YType.str, "profile")

                            self.aps = L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps()
                            self.aps.parent = self
                            self._children_name_map["aps"] = "aps"
                            self._children_yang_names.add("aps")

                            self.rpl = L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl()
                            self.rpl.parent = self
                            self._children_name_map["rpl"] = "rpl"
                            self._children_yang_names.add("rpl")
                            self._segment_path = lambda: "erp-instance" + "[erp-instance-id='" + self.erp_instance_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance, ['erp_instance_id', 'description', 'inclusion_list', 'profile'], name, value)


                        class Aps(Entity):
                            """
                            Automatic protection switching
                            
                            .. attribute:: enable
                            
                            	Enable automatic protection switching
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: level
                            
                            	Automatic protection switching level
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: port0
                            
                            	Port0 APS channel in the format of InterfaceName
                            	**type**\:  str
                            
                            .. attribute:: port1
                            
                            	APS channel for ERP port1
                            	**type**\:   :py:class:`Port1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps, self).__init__()

                                self.yang_name = "aps"
                                self.yang_parent_name = "erp-instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"port1" : ("port1", L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1)}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")

                                self.level = YLeaf(YType.uint32, "level")

                                self.port0 = YLeaf(YType.str, "port0")

                                self.port1 = L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1()
                                self.port1.parent = self
                                self._children_name_map["port1"] = "port1"
                                self._children_yang_names.add("port1")
                                self._segment_path = lambda: "aps"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps, ['enable', 'level', 'port0'], name, value)


                            class Port1(Entity):
                                """
                                APS channel for ERP port1
                                
                                .. attribute:: aps_channel
                                
                                	Port1 APS channel in the format of InterfaceName, BDName or XconnectName
                                	**type**\:  str
                                
                                .. attribute:: aps_type
                                
                                	Port1 APS type
                                	**type**\:   :py:class:`Erpaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Erpaps>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1, self).__init__()

                                    self.yang_name = "port1"
                                    self.yang_parent_name = "aps"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.aps_channel = YLeaf(YType.str, "aps-channel")

                                    self.aps_type = YLeaf(YType.enumeration, "aps-type")
                                    self._segment_path = lambda: "port1"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1, ['aps_channel', 'aps_type'], name, value)


                        class Rpl(Entity):
                            """
                            Ring protection link
                            
                            .. attribute:: port
                            
                            	ERP main port number
                            	**type**\:   :py:class:`ErpPort1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.ErpPort1>`
                            
                            .. attribute:: role
                            
                            	RPL role
                            	**type**\:   :py:class:`RplRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.RplRole>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl, self).__init__()

                                self.yang_name = "rpl"
                                self.yang_parent_name = "erp-instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.port = YLeaf(YType.enumeration, "port")

                                self.role = YLeaf(YType.enumeration, "role")
                                self._segment_path = lambda: "rpl"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl, ['port', 'role'], name, value)


                class ErpPort0S(Entity):
                    """
                    Ethernet ring protection port0
                    
                    .. attribute:: erp_port0
                    
                    	Configure ERP main port0
                    	**type**\: list of    :py:class:`ErpPort0 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S, self).__init__()

                        self.yang_name = "erp-port0s"
                        self.yang_parent_name = "g8032-ring"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"erp-port0" : ("erp_port0", L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0)}

                        self.erp_port0 = YList(self)
                        self._segment_path = lambda: "erp-port0s"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S, [], name, value)


                    class ErpPort0(Entity):
                        """
                        Configure ERP main port0
                        
                        .. attribute:: interface_name  <key>
                        
                        	Port0 interface
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: monitor
                        
                        	Ethernet ring protection port0 monitor
                        	**type**\:  str
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.monitor = YLeaf(YType.str, "monitor")
                            self._segment_path = lambda: "erp-port0" + "[interface-name='" + self.interface_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0, ['interface_name', 'monitor'], name, value)


                class ErpPort1S(Entity):
                    """
                    Ethernet ring protection port0
                    
                    .. attribute:: erp_port1
                    
                    	Ethernet ring protection port1
                    	**type**\: list of    :py:class:`ErpPort1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S, self).__init__()

                        self.yang_name = "erp-port1s"
                        self.yang_parent_name = "g8032-ring"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"erp-port1" : ("erp_port1", L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1)}

                        self.erp_port1 = YList(self)
                        self._segment_path = lambda: "erp-port1s"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S, [], name, value)


                    class ErpPort1(Entity):
                        """
                        Ethernet ring protection port1
                        
                        .. attribute:: erp_port_type  <key>
                        
                        	Port1 type
                        	**type**\:   :py:class:`ErpPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.ErpPort>`
                        
                        .. attribute:: interface
                        
                        	interface
                        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface>`
                        
                        .. attribute:: none_or_virtual
                        
                        	none or virtual
                        	**type**\:   :py:class:`NoneOrVirtual <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1, self).__init__()

                            self.yang_name = "erp-port1"
                            self.yang_parent_name = "erp-port1s"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"none-or-virtual" : ("none_or_virtual", L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual)}
                            self._child_list_classes = {"interface" : ("interface", L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface)}

                            self.erp_port_type = YLeaf(YType.enumeration, "erp-port-type")

                            self.none_or_virtual = None
                            self._children_name_map["none_or_virtual"] = "none-or-virtual"
                            self._children_yang_names.add("none-or-virtual")

                            self.interface = YList(self)
                            self._segment_path = lambda: "erp-port1" + "[erp-port-type='" + self.erp_port_type.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1, ['erp_port_type'], name, value)


                        class Interface(Entity):
                            """
                            interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	Port1 interface
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: monitor
                            
                            	Ethernet ring protection port1 monitor
                            	**type**\:  str
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.monitor = YLeaf(YType.str, "monitor")
                                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface, ['interface_name', 'monitor'], name, value)


                        class NoneOrVirtual(Entity):
                            """
                            none or virtual
                            
                            .. attribute:: monitor
                            
                            	Ethernet ring protection port1 monitor
                            	**type**\:  str
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.monitor = YLeaf(YType.str, "monitor")
                                self._segment_path = lambda: "none-or-virtual"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual, ['monitor'], name, value)


        class PseudowireClasses(Entity):
            """
            List of pseudowire classes
            
            .. attribute:: pseudowire_class
            
            	Pseudowire class
            	**type**\: list of    :py:class:`PseudowireClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Database.PseudowireClasses, self).__init__()

                self.yang_name = "pseudowire-classes"
                self.yang_parent_name = "database"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"pseudowire-class" : ("pseudowire_class", L2Vpn.Database.PseudowireClasses.PseudowireClass)}

                self.pseudowire_class = YList(self)
                self._segment_path = lambda: "pseudowire-classes"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.Database.PseudowireClasses, [], name, value)


            class PseudowireClass(Entity):
                """
                Pseudowire class
                
                .. attribute:: name  <key>
                
                	Name of the pseudowire class
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: backup_disable_delay
                
                	Back Up Pseudowire class
                	**type**\:   :py:class:`BackupDisableDelay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay>`
                
                .. attribute:: enable
                
                	Enable pseudowire class
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: l2tpv3_encapsulation
                
                	L2TPv3 encapsulation
                	**type**\:   :py:class:`L2Tpv3Encapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation>`
                
                .. attribute:: mac_withdraw
                
                	Enable backup MAC withdraw
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: mpls_encapsulation
                
                	MPLS encapsulation
                	**type**\:   :py:class:`MplsEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.PseudowireClasses.PseudowireClass, self).__init__()

                    self.yang_name = "pseudowire-class"
                    self.yang_parent_name = "pseudowire-classes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"backup-disable-delay" : ("backup_disable_delay", L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay), "l2tpv3-encapsulation" : ("l2tpv3_encapsulation", L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation), "mpls-encapsulation" : ("mpls_encapsulation", L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.mac_withdraw = YLeaf(YType.empty, "mac-withdraw")

                    self.backup_disable_delay = L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay()
                    self.backup_disable_delay.parent = self
                    self._children_name_map["backup_disable_delay"] = "backup-disable-delay"
                    self._children_yang_names.add("backup-disable-delay")

                    self.l2tpv3_encapsulation = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation()
                    self.l2tpv3_encapsulation.parent = self
                    self._children_name_map["l2tpv3_encapsulation"] = "l2tpv3-encapsulation"
                    self._children_yang_names.add("l2tpv3-encapsulation")

                    self.mpls_encapsulation = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation()
                    self.mpls_encapsulation.parent = self
                    self._children_name_map["mpls_encapsulation"] = "mpls-encapsulation"
                    self._children_yang_names.add("mpls-encapsulation")
                    self._segment_path = lambda: "pseudowire-class" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/pseudowire-classes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass, ['name', 'enable', 'mac_withdraw'], name, value)


                class BackupDisableDelay(Entity):
                    """
                    Back Up Pseudowire class
                    
                    .. attribute:: disable_backup
                    
                    	Disable backup delay
                    	**type**\:  int
                    
                    	**range:** 0..180
                    
                    .. attribute:: type
                    
                    	Delay or Never
                    	**type**\:   :py:class:`BackupDisable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BackupDisable>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay, self).__init__()

                        self.yang_name = "backup-disable-delay"
                        self.yang_parent_name = "pseudowire-class"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.disable_backup = YLeaf(YType.uint32, "disable-backup")

                        self.type = YLeaf(YType.enumeration, "type")
                        self._segment_path = lambda: "backup-disable-delay"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay, ['disable_backup', 'type'], name, value)


                class L2Tpv3Encapsulation(Entity):
                    """
                    L2TPv3 encapsulation
                    
                    .. attribute:: cookie_size
                    
                    	Cookie size
                    	**type**\:   :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                    
                    	**default value**\: zero
                    
                    .. attribute:: df_bit_set
                    
                    	Set the do not fragment bit to 1
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: enable
                    
                    	Enable L2TPv3 encapsulation
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: path_mtu
                    
                    	Path maximum transmission unit
                    	**type**\:   :py:class:`PathMtu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu>`
                    
                    .. attribute:: sequencing
                    
                    	Sequencing
                    	**type**\:   :py:class:`Sequencing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing>`
                    
                    .. attribute:: signaling_protocol
                    
                    	L2TPv3 signaling protocol
                    	**type**\:   :py:class:`SignalingProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol>`
                    
                    .. attribute:: source_address
                    
                    	Source IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: time_to_live
                    
                    	Time to live
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    .. attribute:: transport_mode
                    
                    	Transport mode
                    	**type**\:   :py:class:`TransportMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.TransportMode>`
                    
                    .. attribute:: type_of_service
                    
                    	Type of service
                    	**type**\:   :py:class:`TypeOfService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation, self).__init__()

                        self.yang_name = "l2tpv3-encapsulation"
                        self.yang_parent_name = "pseudowire-class"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"path-mtu" : ("path_mtu", L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu), "sequencing" : ("sequencing", L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing), "signaling-protocol" : ("signaling_protocol", L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol), "type-of-service" : ("type_of_service", L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService)}
                        self._child_list_classes = {}

                        self.cookie_size = YLeaf(YType.enumeration, "cookie-size")

                        self.df_bit_set = YLeaf(YType.empty, "df-bit-set")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.source_address = YLeaf(YType.str, "source-address")

                        self.time_to_live = YLeaf(YType.uint32, "time-to-live")

                        self.transport_mode = YLeaf(YType.enumeration, "transport-mode")

                        self.path_mtu = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu()
                        self.path_mtu.parent = self
                        self._children_name_map["path_mtu"] = "path-mtu"
                        self._children_yang_names.add("path-mtu")

                        self.sequencing = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing()
                        self.sequencing.parent = self
                        self._children_name_map["sequencing"] = "sequencing"
                        self._children_yang_names.add("sequencing")

                        self.signaling_protocol = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol()
                        self.signaling_protocol.parent = self
                        self._children_name_map["signaling_protocol"] = "signaling-protocol"
                        self._children_yang_names.add("signaling-protocol")

                        self.type_of_service = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService()
                        self.type_of_service.parent = self
                        self._children_name_map["type_of_service"] = "type-of-service"
                        self._children_yang_names.add("type-of-service")
                        self._segment_path = lambda: "l2tpv3-encapsulation"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation, ['cookie_size', 'df_bit_set', 'enable', 'source_address', 'time_to_live', 'transport_mode'], name, value)


                    class PathMtu(Entity):
                        """
                        Path maximum transmission unit
                        
                        .. attribute:: enable
                        
                        	Enable path MTU
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: max_path_mtu
                        
                        	Maximum path maximum transmission unit
                        	**type**\:  int
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")

                            self.max_path_mtu = YLeaf(YType.uint32, "max-path-mtu")
                            self._segment_path = lambda: "path-mtu"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu, ['enable', 'max_path_mtu'], name, value)


                    class Sequencing(Entity):
                        """
                        Sequencing
                        
                        .. attribute:: resync_threshold
                        
                        	Out of sequence threshold
                        	**type**\:  int
                        
                        	**range:** 5..65535
                        
                        	**default value**\: 5
                        
                        .. attribute:: sequencing
                        
                        	Sequencing
                        	**type**\:   :py:class:`L2tpv3Sequencing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpv3Sequencing>`
                        
                        	**default value**\: off
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing, self).__init__()

                            self.yang_name = "sequencing"
                            self.yang_parent_name = "l2tpv3-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.resync_threshold = YLeaf(YType.uint32, "resync-threshold")

                            self.sequencing = YLeaf(YType.enumeration, "sequencing")
                            self._segment_path = lambda: "sequencing"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing, ['resync_threshold', 'sequencing'], name, value)


                    class SignalingProtocol(Entity):
                        """
                        L2TPv3 signaling protocol
                        
                        .. attribute:: l2tpv3_class_name
                        
                        	Name of the L2TPv3 class name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: protocol
                        
                        	L2TPv3 signaling protocol
                        	**type**\:   :py:class:`L2tpSignalingProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpSignalingProtocol>`
                        
                        	**default value**\: l2tpv3
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol, self).__init__()

                            self.yang_name = "signaling-protocol"
                            self.yang_parent_name = "l2tpv3-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.l2tpv3_class_name = YLeaf(YType.str, "l2tpv3-class-name")

                            self.protocol = YLeaf(YType.enumeration, "protocol")
                            self._segment_path = lambda: "signaling-protocol"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol, ['l2tpv3_class_name', 'protocol'], name, value)


                    class TypeOfService(Entity):
                        """
                        Type of service
                        
                        .. attribute:: type_of_service_mode
                        
                        	Type of service mode
                        	**type**\:   :py:class:`TypeOfServiceMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.TypeOfServiceMode>`
                        
                        .. attribute:: type_of_service_value
                        
                        	Type of service value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService, self).__init__()

                            self.yang_name = "type-of-service"
                            self.yang_parent_name = "l2tpv3-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.type_of_service_mode = YLeaf(YType.enumeration, "type-of-service-mode")

                            self.type_of_service_value = YLeaf(YType.uint32, "type-of-service-value")
                            self._segment_path = lambda: "type-of-service"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService, ['type_of_service_mode', 'type_of_service_value'], name, value)


                class MplsEncapsulation(Entity):
                    """
                    MPLS encapsulation
                    
                    .. attribute:: control_word
                    
                    	Enable control word
                    	**type**\:   :py:class:`ControlWord <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.ControlWord>`
                    
                    .. attribute:: enable
                    
                    	Enable MPLS encapsulation
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: load_balance_group
                    
                    	Load Balancing
                    	**type**\:   :py:class:`LoadBalanceGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup>`
                    
                    .. attribute:: mpls_redundancy
                    
                    	Redundancy options for MPLS encapsulation
                    	**type**\:   :py:class:`MplsRedundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy>`
                    
                    .. attribute:: preferred_path
                    
                    	Preferred path
                    	**type**\:   :py:class:`PreferredPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath>`
                    
                    .. attribute:: pw_switching_tlv
                    
                    	Pseudowire Switching Point Tlv
                    	**type**\:   :py:class:`PwSwitchingPointTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.PwSwitchingPointTlv>`
                    
                    .. attribute:: sequencing
                    
                    	Sequencing
                    	**type**\:   :py:class:`Sequencing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing>`
                    
                    .. attribute:: signaling_protocol
                    
                    	MPLS signaling protocol
                    	**type**\:   :py:class:`MplsSignalingProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MplsSignalingProtocol>`
                    
                    	**default value**\: ldp
                    
                    .. attribute:: source_address
                    
                    	Source IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: static_tag_rewrite
                    
                    	Static Tag rewrite
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    .. attribute:: transport_mode
                    
                    	Transport mode
                    	**type**\:   :py:class:`TransportMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.TransportMode>`
                    
                    .. attribute:: vccv_type
                    
                    	VCCV verification type
                    	**type**\:   :py:class:`VccvVerification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.VccvVerification>`
                    
                    	**default value**\: lsp-ping
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation, self).__init__()

                        self.yang_name = "mpls-encapsulation"
                        self.yang_parent_name = "pseudowire-class"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"load-balance-group" : ("load_balance_group", L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup), "mpls-redundancy" : ("mpls_redundancy", L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy), "preferred-path" : ("preferred_path", L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath), "sequencing" : ("sequencing", L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing)}
                        self._child_list_classes = {}

                        self.control_word = YLeaf(YType.enumeration, "control-word")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.pw_switching_tlv = YLeaf(YType.enumeration, "pw-switching-tlv")

                        self.signaling_protocol = YLeaf(YType.enumeration, "signaling-protocol")

                        self.source_address = YLeaf(YType.str, "source-address")

                        self.static_tag_rewrite = YLeaf(YType.uint32, "static-tag-rewrite")

                        self.transport_mode = YLeaf(YType.enumeration, "transport-mode")

                        self.vccv_type = YLeaf(YType.enumeration, "vccv-type")

                        self.load_balance_group = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup()
                        self.load_balance_group.parent = self
                        self._children_name_map["load_balance_group"] = "load-balance-group"
                        self._children_yang_names.add("load-balance-group")

                        self.mpls_redundancy = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy()
                        self.mpls_redundancy.parent = self
                        self._children_name_map["mpls_redundancy"] = "mpls-redundancy"
                        self._children_yang_names.add("mpls-redundancy")

                        self.preferred_path = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath()
                        self.preferred_path.parent = self
                        self._children_name_map["preferred_path"] = "preferred-path"
                        self._children_yang_names.add("preferred-path")

                        self.sequencing = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing()
                        self.sequencing.parent = self
                        self._children_name_map["sequencing"] = "sequencing"
                        self._children_yang_names.add("sequencing")
                        self._segment_path = lambda: "mpls-encapsulation"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation, ['control_word', 'enable', 'pw_switching_tlv', 'signaling_protocol', 'source_address', 'static_tag_rewrite', 'transport_mode', 'vccv_type'], name, value)


                    class LoadBalanceGroup(Entity):
                        """
                        Load Balancing
                        
                        .. attribute:: flow_label_load_balance
                        
                        	Enable Flow Label based load balancing
                        	**type**\:   :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance>`
                        
                        .. attribute:: flow_label_load_balance_code
                        
                        	Enable Legacy Flow Label TLV code
                        	**type**\:   :py:class:`FlowLabelTlvCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelTlvCode>`
                        
                        .. attribute:: pw_label_load_balance
                        
                        	Enable PW Label based Load Balancing
                        	**type**\:   :py:class:`LoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.LoadBalance>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup, self).__init__()

                            self.yang_name = "load-balance-group"
                            self.yang_parent_name = "mpls-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"flow-label-load-balance" : ("flow_label_load_balance", L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance)}
                            self._child_list_classes = {}

                            self.flow_label_load_balance_code = YLeaf(YType.enumeration, "flow-label-load-balance-code")

                            self.pw_label_load_balance = YLeaf(YType.enumeration, "pw-label-load-balance")

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
                            	**type**\:   :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalance>`
                            
                            .. attribute:: static
                            
                            	Static Flow Label
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance, self).__init__()

                                self.yang_name = "flow-label-load-balance"
                                self.yang_parent_name = "load-balance-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.flow_label = YLeaf(YType.enumeration, "flow-label")

                                self.static = YLeaf(YType.empty, "static")
                                self._segment_path = lambda: "flow-label-load-balance"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance, ['flow_label', 'static'], name, value)


                    class MplsRedundancy(Entity):
                        """
                        Redundancy options for MPLS encapsulation
                        
                        .. attribute:: redundancy_initial_delay
                        
                        	Initial delay before activating the redundant PW, in seconds
                        	**type**\:  int
                        
                        	**range:** 0..120
                        
                        	**units**\: second
                        
                        .. attribute:: redundancy_one_way
                        
                        	Force one\-way PW redundancy behavior in Redundancy Group
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy, self).__init__()

                            self.yang_name = "mpls-redundancy"
                            self.yang_parent_name = "mpls-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.redundancy_initial_delay = YLeaf(YType.uint32, "redundancy-initial-delay")

                            self.redundancy_one_way = YLeaf(YType.empty, "redundancy-one-way")
                            self._segment_path = lambda: "mpls-redundancy"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy, ['redundancy_initial_delay', 'redundancy_one_way'], name, value)


                    class PreferredPath(Entity):
                        """
                        Preferred path
                        
                        .. attribute:: fallback_disable
                        
                        	Fallback disable
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: interface_tunnel_number
                        
                        	Interface Tunnel number for preferred path
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: srte_policy
                        
                        	Name of the SR TE Policy
                        	**type**\:  str
                        
                        	**length:** 1..60
                        
                        .. attribute:: type
                        
                        	Preferred Path Type
                        	**type**\:   :py:class:`PreferredPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.PreferredPath>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath, self).__init__()

                            self.yang_name = "preferred-path"
                            self.yang_parent_name = "mpls-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.fallback_disable = YLeaf(YType.empty, "fallback-disable")

                            self.interface_tunnel_number = YLeaf(YType.uint32, "interface-tunnel-number")

                            self.srte_policy = YLeaf(YType.str, "srte-policy")

                            self.type = YLeaf(YType.enumeration, "type")
                            self._segment_path = lambda: "preferred-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath, ['fallback_disable', 'interface_tunnel_number', 'srte_policy', 'type'], name, value)


                    class Sequencing(Entity):
                        """
                        Sequencing
                        
                        .. attribute:: resync_threshold
                        
                        	Out of sequence threshold
                        	**type**\:  int
                        
                        	**range:** 5..65535
                        
                        	**default value**\: 5
                        
                        .. attribute:: sequencing
                        
                        	Sequencing
                        	**type**\:   :py:class:`MplsSequencing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MplsSequencing>`
                        
                        	**default value**\: off
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing, self).__init__()

                            self.yang_name = "sequencing"
                            self.yang_parent_name = "mpls-encapsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.resync_threshold = YLeaf(YType.uint32, "resync-threshold")

                            self.sequencing = YLeaf(YType.enumeration, "sequencing")
                            self._segment_path = lambda: "sequencing"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing, ['resync_threshold', 'sequencing'], name, value)


        class Redundancy(Entity):
            """
            Redundancy groups
            
            .. attribute:: enable
            
            	Enable redundancy groups
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: iccp_redundancy_groups
            
            	List of Inter\-Chassis Communication Protocol redundancy groups
            	**type**\:   :py:class:`IccpRedundancyGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.Redundancy.IccpRedundancyGroups>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Database.Redundancy, self).__init__()

                self.yang_name = "redundancy"
                self.yang_parent_name = "database"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"iccp-redundancy-groups" : ("iccp_redundancy_groups", L2Vpn.Database.Redundancy.IccpRedundancyGroups)}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

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
                	**type**\: list of    :py:class:`IccpRedundancyGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.Redundancy.IccpRedundancyGroups, self).__init__()

                    self.yang_name = "iccp-redundancy-groups"
                    self.yang_parent_name = "redundancy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"iccp-redundancy-group" : ("iccp_redundancy_group", L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup)}

                    self.iccp_redundancy_group = YList(self)
                    self._segment_path = lambda: "iccp-redundancy-groups"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/redundancy/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.Redundancy.IccpRedundancyGroups, [], name, value)


                class IccpRedundancyGroup(Entity):
                    """
                    ICCP Redundancy group
                    
                    .. attribute:: group_id  <key>
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 1..4294967295
                    
                    .. attribute:: iccp_interfaces
                    
                    	List of interfaces
                    	**type**\:   :py:class:`IccpInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces>`
                    
                    .. attribute:: multi_homing_node_id
                    
                    	ICCP\-based service multi\-homing node ID
                    	**type**\:  int
                    
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
                        self._child_container_classes = {"iccp-interfaces" : ("iccp_interfaces", L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces)}
                        self._child_list_classes = {}

                        self.group_id = YLeaf(YType.uint32, "group-id")

                        self.multi_homing_node_id = YLeaf(YType.uint32, "multi-homing-node-id")

                        self.iccp_interfaces = L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces()
                        self.iccp_interfaces.parent = self
                        self._children_name_map["iccp_interfaces"] = "iccp-interfaces"
                        self._children_yang_names.add("iccp-interfaces")
                        self._segment_path = lambda: "iccp-redundancy-group" + "[group-id='" + self.group_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/redundancy/iccp-redundancy-groups/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup, ['group_id', 'multi_homing_node_id'], name, value)


                    class IccpInterfaces(Entity):
                        """
                        List of interfaces
                        
                        .. attribute:: iccp_interface
                        
                        	Interface name
                        	**type**\: list of    :py:class:`IccpInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces, self).__init__()

                            self.yang_name = "iccp-interfaces"
                            self.yang_parent_name = "iccp-redundancy-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"iccp-interface" : ("iccp_interface", L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface)}

                            self.iccp_interface = YList(self)
                            self._segment_path = lambda: "iccp-interfaces"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces, [], name, value)


                        class IccpInterface(Entity):
                            """
                            Interface name
                            
                            .. attribute:: interface_name  <key>
                            
                            	Interface name
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: mac_flush_tcn
                            
                            	Enable STP\-TCN MAC flushing
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: primary_vlan_range
                            
                            	Primary VLAN range, in the form of 1\-3,5 ,8\-11
                            	**type**\:  str
                            
                            .. attribute:: recovery_delay
                            
                            	Failure clear recovery delay
                            	**type**\:  int
                            
                            	**range:** 30..3600
                            
                            	**default value**\: 180
                            
                            .. attribute:: secondary_vlan_range
                            
                            	Secondary VLAN range, in the form of 1\-3,5 ,8\-11
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface, self).__init__()

                                self.yang_name = "iccp-interface"
                                self.yang_parent_name = "iccp-interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.mac_flush_tcn = YLeaf(YType.empty, "mac-flush-tcn")

                                self.primary_vlan_range = YLeaf(YType.str, "primary-vlan-range")

                                self.recovery_delay = YLeaf(YType.uint32, "recovery-delay")

                                self.secondary_vlan_range = YLeaf(YType.str, "secondary-vlan-range")
                                self._segment_path = lambda: "iccp-interface" + "[interface-name='" + self.interface_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface, ['interface_name', 'mac_flush_tcn', 'primary_vlan_range', 'recovery_delay', 'secondary_vlan_range'], name, value)


        class XconnectGroups(Entity):
            """
            List of xconnect groups
            
            .. attribute:: xconnect_group
            
            	Xconnect group
            	**type**\: list of    :py:class:`XconnectGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Database.XconnectGroups, self).__init__()

                self.yang_name = "xconnect-groups"
                self.yang_parent_name = "database"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"xconnect-group" : ("xconnect_group", L2Vpn.Database.XconnectGroups.XconnectGroup)}

                self.xconnect_group = YList(self)
                self._segment_path = lambda: "xconnect-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.Database.XconnectGroups, [], name, value)


            class XconnectGroup(Entity):
                """
                Xconnect group
                
                .. attribute:: name  <key>
                
                	Name of the xconnect group
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: mp2mp_xconnects
                
                	List of multi point to multi point xconnects
                	**type**\:   :py:class:`Mp2MpXconnects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects>`
                
                .. attribute:: p2p_xconnects
                
                	List of point to point xconnects
                	**type**\:   :py:class:`P2PXconnects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Database.XconnectGroups.XconnectGroup, self).__init__()

                    self.yang_name = "xconnect-group"
                    self.yang_parent_name = "xconnect-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"mp2mp-xconnects" : ("mp2mp_xconnects", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects), "p2p-xconnects" : ("p2p_xconnects", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.mp2mp_xconnects = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects()
                    self.mp2mp_xconnects.parent = self
                    self._children_name_map["mp2mp_xconnects"] = "mp2mp-xconnects"
                    self._children_yang_names.add("mp2mp-xconnects")

                    self.p2p_xconnects = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects()
                    self.p2p_xconnects.parent = self
                    self._children_name_map["p2p_xconnects"] = "p2p-xconnects"
                    self._children_yang_names.add("p2p-xconnects")
                    self._segment_path = lambda: "xconnect-group" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/database/xconnect-groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup, ['name'], name, value)


                class Mp2MpXconnects(Entity):
                    """
                    List of multi point to multi point xconnects
                    
                    .. attribute:: mp2mp_xconnect
                    
                    	Multi point to multi point xconnect
                    	**type**\: list of    :py:class:`Mp2MpXconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects, self).__init__()

                        self.yang_name = "mp2mp-xconnects"
                        self.yang_parent_name = "xconnect-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"mp2mp-xconnect" : ("mp2mp_xconnect", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect)}

                        self.mp2mp_xconnect = YList(self)
                        self._segment_path = lambda: "mp2mp-xconnects"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects, [], name, value)


                    class Mp2MpXconnect(Entity):
                        """
                        Multi point to multi point xconnect
                        
                        .. attribute:: name  <key>
                        
                        	Name of the multi point to multi point xconnect
                        	**type**\:  str
                        
                        	**length:** 1..26
                        
                        .. attribute:: mp2mp_auto_discovery
                        
                        	auto\-discovery in this MP2MP
                        	**type**\:   :py:class:`Mp2MpAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery>`
                        
                        .. attribute:: mp2mp_control_word
                        
                        	Disable control word
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: mp2mp_interworking
                        
                        	Interworking
                        	**type**\:   :py:class:`Interworking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Interworking>`
                        
                        .. attribute:: mp2mp_shutdown
                        
                        	shutdown this MP2MP VPWS instance
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: mp2mpl2_encapsulation
                        
                        	Configure Layer 2 Encapsulation
                        	**type**\:   :py:class:`L2Encapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Encapsulation>`
                        
                        .. attribute:: mp2mpmtu
                        
                        	Maximum transmission unit for this MP2MP VPWS instance
                        	**type**\:  int
                        
                        	**range:** 64..65535
                        
                        	**units**\: byte
                        
                        .. attribute:: mp2mpvpn_id
                        
                        	VPN Identifier
                        	**type**\:  int
                        
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
                            self._child_container_classes = {"mp2mp-auto-discovery" : ("mp2mp_auto_discovery", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery)}
                            self._child_list_classes = {}

                            self.name = YLeaf(YType.str, "name")

                            self.mp2mp_control_word = YLeaf(YType.empty, "mp2mp-control-word")

                            self.mp2mp_interworking = YLeaf(YType.enumeration, "mp2mp-interworking")

                            self.mp2mp_shutdown = YLeaf(YType.empty, "mp2mp-shutdown")

                            self.mp2mpl2_encapsulation = YLeaf(YType.enumeration, "mp2mpl2-encapsulation")

                            self.mp2mpmtu = YLeaf(YType.uint32, "mp2mpmtu")

                            self.mp2mpvpn_id = YLeaf(YType.uint32, "mp2mpvpn-id")

                            self.mp2mp_auto_discovery = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery()
                            self.mp2mp_auto_discovery.parent = self
                            self._children_name_map["mp2mp_auto_discovery"] = "mp2mp-auto-discovery"
                            self._children_yang_names.add("mp2mp-auto-discovery")
                            self._segment_path = lambda: "mp2mp-xconnect" + "[name='" + self.name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect, ['name', 'mp2mp_control_word', 'mp2mp_interworking', 'mp2mp_shutdown', 'mp2mpl2_encapsulation', 'mp2mpmtu', 'mp2mpvpn_id'], name, value)


                        class Mp2MpAutoDiscovery(Entity):
                            """
                            auto\-discovery in this MP2MP
                            
                            .. attribute:: enable
                            
                            	Enable auto\-discovery
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: mp2mp_route_policy
                            
                            	Route policy
                            	**type**\:   :py:class:`Mp2MpRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy>`
                            
                            .. attribute:: mp2mp_route_targets
                            
                            	Route Target
                            	**type**\:   :py:class:`Mp2MpRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets>`
                            
                            .. attribute:: mp2mp_signaling_protocol
                            
                            	signaling protocol in this MP2MP
                            	**type**\:   :py:class:`Mp2MpSignalingProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol>`
                            
                            .. attribute:: route_distinguisher
                            
                            	Route Distinguisher
                            	**type**\:   :py:class:`RouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery, self).__init__()

                                self.yang_name = "mp2mp-auto-discovery"
                                self.yang_parent_name = "mp2mp-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"mp2mp-route-policy" : ("mp2mp_route_policy", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy), "mp2mp-route-targets" : ("mp2mp_route_targets", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets), "mp2mp-signaling-protocol" : ("mp2mp_signaling_protocol", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol), "route-distinguisher" : ("route_distinguisher", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher)}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")

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

                                self.route_distinguisher = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher()
                                self.route_distinguisher.parent = self
                                self._children_name_map["route_distinguisher"] = "route-distinguisher"
                                self._children_yang_names.add("route-distinguisher")
                                self._segment_path = lambda: "mp2mp-auto-discovery"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery, ['enable'], name, value)


                            class Mp2MpRoutePolicy(Entity):
                                """
                                Route policy
                                
                                .. attribute:: export
                                
                                	Export route policy
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy, self).__init__()

                                    self.yang_name = "mp2mp-route-policy"
                                    self.yang_parent_name = "mp2mp-auto-discovery"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.export = YLeaf(YType.str, "export")
                                    self._segment_path = lambda: "mp2mp-route-policy"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy, ['export'], name, value)


                            class Mp2MpRouteTargets(Entity):
                                """
                                Route Target
                                
                                .. attribute:: mp2mp_route_target
                                
                                	Name of the Route Target
                                	**type**\: list of    :py:class:`Mp2MpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets, self).__init__()

                                    self.yang_name = "mp2mp-route-targets"
                                    self.yang_parent_name = "mp2mp-auto-discovery"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"mp2mp-route-target" : ("mp2mp_route_target", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget)}

                                    self.mp2mp_route_target = YList(self)
                                    self._segment_path = lambda: "mp2mp-route-targets"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets, [], name, value)


                                class Mp2MpRouteTarget(Entity):
                                    """
                                    Name of the Route Target
                                    
                                    .. attribute:: role  <key>
                                    
                                    	Role of the router target type
                                    	**type**\:   :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole>`
                                    
                                    .. attribute:: format  <key>
                                    
                                    	Format of the route target
                                    	**type**\:   :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	ipv4 address
                                    	**type**\: list of    :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address>`
                                    
                                    .. attribute:: two_byte_as_or_four_byte_as
                                    
                                    	two byte as or four byte as
                                    	**type**\: list of    :py:class:`TwoByteAsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget, self).__init__()

                                        self.yang_name = "mp2mp-route-target"
                                        self.yang_parent_name = "mp2mp-route-targets"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"ipv4-address" : ("ipv4_address", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address), "two-byte-as-or-four-byte-as" : ("two_byte_as_or_four_byte_as", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs)}

                                        self.role = YLeaf(YType.enumeration, "role")

                                        self.format = YLeaf(YType.enumeration, "format")

                                        self.ipv4_address = YList(self)
                                        self.two_byte_as_or_four_byte_as = YList(self)
                                        self._segment_path = lambda: "mp2mp-route-target" + "[role='" + self.role.get() + "']" + "[format='" + self.format.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget, ['role', 'format'], name, value)


                                    class Ipv4Address(Entity):
                                        """
                                        ipv4 address
                                        
                                        .. attribute:: address  <key>
                                        
                                        	IPV4 address
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: addr_index  <key>
                                        
                                        	Addr index
                                        	**type**\:  int
                                        
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
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.address = YLeaf(YType.str, "address")

                                            self.addr_index = YLeaf(YType.uint32, "addr-index")
                                            self._segment_path = lambda: "ipv4-address" + "[address='" + self.address.get() + "']" + "[addr-index='" + self.addr_index.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address, ['address', 'addr_index'], name, value)


                                    class TwoByteAsOrFourByteAs(Entity):
                                        """
                                        two byte as or four byte as
                                        
                                        .. attribute:: as_  <key>
                                        
                                        	Two byte or 4 byte AS number
                                        	**type**\:  int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: as_index  <key>
                                        
                                        	AS\:nn (hex or decimal format)
                                        	**type**\:  int
                                        
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
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.as_ = YLeaf(YType.uint32, "as")

                                            self.as_index = YLeaf(YType.uint32, "as-index")
                                            self._segment_path = lambda: "two-byte-as-or-four-byte-as" + "[as='" + self.as_.get() + "']" + "[as-index='" + self.as_index.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs, ['as_', 'as_index'], name, value)


                            class Mp2MpSignalingProtocol(Entity):
                                """
                                signaling protocol in this MP2MP
                                
                                .. attribute:: ce_range
                                
                                	Local Customer Edge Identifier
                                	**type**\:  int
                                
                                	**range:** 11..100
                                
                                .. attribute:: ceids
                                
                                	Local Customer Edge Identifier Table
                                	**type**\:   :py:class:`Ceids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids>`
                                
                                .. attribute:: enable
                                
                                	Enable signaling protocol
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: flow_label_load_balance
                                
                                	Enable Flow Label based load balancing
                                	**type**\:   :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol, self).__init__()

                                    self.yang_name = "mp2mp-signaling-protocol"
                                    self.yang_parent_name = "mp2mp-auto-discovery"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"ceids" : ("ceids", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids), "flow-label-load-balance" : ("flow_label_load_balance", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance)}
                                    self._child_list_classes = {}

                                    self.ce_range = YLeaf(YType.uint32, "ce-range")

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.ceids = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids()
                                    self.ceids.parent = self
                                    self._children_name_map["ceids"] = "ceids"
                                    self._children_yang_names.add("ceids")

                                    self.flow_label_load_balance = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance()
                                    self.flow_label_load_balance.parent = self
                                    self._children_name_map["flow_label_load_balance"] = "flow-label-load-balance"
                                    self._children_yang_names.add("flow-label-load-balance")
                                    self._segment_path = lambda: "mp2mp-signaling-protocol"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol, ['ce_range', 'enable'], name, value)


                                class Ceids(Entity):
                                    """
                                    Local Customer Edge Identifier Table
                                    
                                    .. attribute:: ceid
                                    
                                    	Local Customer Edge Identifier 
                                    	**type**\: list of    :py:class:`Ceid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids, self).__init__()

                                        self.yang_name = "ceids"
                                        self.yang_parent_name = "mp2mp-signaling-protocol"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"ceid" : ("ceid", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid)}

                                        self.ceid = YList(self)
                                        self._segment_path = lambda: "ceids"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids, [], name, value)


                                    class Ceid(Entity):
                                        """
                                        Local Customer Edge Identifier 
                                        
                                        .. attribute:: ce_id  <key>
                                        
                                        	Local Customer Edge Identifier
                                        	**type**\:  int
                                        
                                        	**range:** 1..16384
                                        
                                        .. attribute:: remote_ceid_attachment_circuits
                                        
                                        	AC And Remote Customer Edge Identifier Table
                                        	**type**\:   :py:class:`RemoteCeidAttachmentCircuits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid, self).__init__()

                                            self.yang_name = "ceid"
                                            self.yang_parent_name = "ceids"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"remote-ceid-attachment-circuits" : ("remote_ceid_attachment_circuits", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits)}
                                            self._child_list_classes = {}

                                            self.ce_id = YLeaf(YType.uint32, "ce-id")

                                            self.remote_ceid_attachment_circuits = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits()
                                            self.remote_ceid_attachment_circuits.parent = self
                                            self._children_name_map["remote_ceid_attachment_circuits"] = "remote-ceid-attachment-circuits"
                                            self._children_yang_names.add("remote-ceid-attachment-circuits")
                                            self._segment_path = lambda: "ceid" + "[ce-id='" + self.ce_id.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid, ['ce_id'], name, value)


                                        class RemoteCeidAttachmentCircuits(Entity):
                                            """
                                            AC And Remote Customer Edge Identifier
                                            Table
                                            
                                            .. attribute:: remote_ceid_attachment_circuit
                                            
                                            	AC And Remote Customer Edge Identifier
                                            	**type**\: list of    :py:class:`RemoteCeidAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits, self).__init__()

                                                self.yang_name = "remote-ceid-attachment-circuits"
                                                self.yang_parent_name = "ceid"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"remote-ceid-attachment-circuit" : ("remote_ceid_attachment_circuit", L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit)}

                                                self.remote_ceid_attachment_circuit = YList(self)
                                                self._segment_path = lambda: "remote-ceid-attachment-circuits"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits, [], name, value)


                                            class RemoteCeidAttachmentCircuit(Entity):
                                                """
                                                AC And Remote Customer Edge Identifier
                                                
                                                .. attribute:: name  <key>
                                                
                                                	The name of the Attachment Circuit
                                                	**type**\:  str
                                                
                                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                                
                                                .. attribute:: remote_ce_id  <key>
                                                
                                                	Remote Customer Edge Identifier
                                                	**type**\:  int
                                                
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
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.name = YLeaf(YType.str, "name")

                                                    self.remote_ce_id = YLeaf(YType.uint32, "remote-ce-id")
                                                    self._segment_path = lambda: "remote-ceid-attachment-circuit" + "[name='" + self.name.get() + "']" + "[remote-ce-id='" + self.remote_ce_id.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit, ['name', 'remote_ce_id'], name, value)


                                class FlowLabelLoadBalance(Entity):
                                    """
                                    Enable Flow Label based load balancing
                                    
                                    .. attribute:: flow_label
                                    
                                    	Flow Label load balance type
                                    	**type**\:   :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalance>`
                                    
                                    .. attribute:: static
                                    
                                    	Static Flow Label
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance, self).__init__()

                                        self.yang_name = "flow-label-load-balance"
                                        self.yang_parent_name = "mp2mp-signaling-protocol"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.flow_label = YLeaf(YType.enumeration, "flow-label")

                                        self.static = YLeaf(YType.empty, "static")
                                        self._segment_path = lambda: "flow-label-load-balance"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance, ['flow_label', 'static'], name, value)


                            class RouteDistinguisher(Entity):
                                """
                                Route Distinguisher
                                
                                .. attribute:: addr_index
                                
                                	Addr index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: address
                                
                                	IPV4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: as_
                                
                                	Two byte or 4 byte AS number
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: as_index
                                
                                	AS\:nn (hex or decimal format)
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: type
                                
                                	Router distinguisher type
                                	**type**\:   :py:class:`BgpRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher, self).__init__()

                                    self.yang_name = "route-distinguisher"
                                    self.yang_parent_name = "mp2mp-auto-discovery"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.addr_index = YLeaf(YType.uint32, "addr-index")

                                    self.address = YLeaf(YType.str, "address")

                                    self.as_ = YLeaf(YType.uint32, "as")

                                    self.as_index = YLeaf(YType.uint32, "as-index")

                                    self.type = YLeaf(YType.enumeration, "type")
                                    self._segment_path = lambda: "route-distinguisher"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher, ['addr_index', 'address', 'as_', 'as_index', 'type'], name, value)


                class P2PXconnects(Entity):
                    """
                    List of point to point xconnects
                    
                    .. attribute:: p2p_xconnect
                    
                    	Point to point xconnect
                    	**type**\: list of    :py:class:`P2PXconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects, self).__init__()

                        self.yang_name = "p2p-xconnects"
                        self.yang_parent_name = "xconnect-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"p2p-xconnect" : ("p2p_xconnect", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect)}

                        self.p2p_xconnect = YList(self)
                        self._segment_path = lambda: "p2p-xconnects"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects, [], name, value)


                    class P2PXconnect(Entity):
                        """
                        Point to point xconnect
                        
                        .. attribute:: name  <key>
                        
                        	Name of the point to point xconnect
                        	**type**\:  str
                        
                        	**length:** 1..38
                        
                        .. attribute:: attachment_circuits
                        
                        	List of attachment circuits
                        	**type**\:   :py:class:`AttachmentCircuits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits>`
                        
                        .. attribute:: backup_attachment_circuits
                        
                        	List of backup attachment circuits
                        	**type**\:   :py:class:`BackupAttachmentCircuits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits>`
                        
                        .. attribute:: interworking
                        
                        	Interworking
                        	**type**\:   :py:class:`Interworking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Interworking>`
                        
                        .. attribute:: monitor_sessions
                        
                        	List of Monitor session segments
                        	**type**\:   :py:class:`MonitorSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions>`
                        
                        .. attribute:: p2p_description
                        
                        	cross connect description Name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: pseudowire_evpns
                        
                        	List of EVPN Services
                        	**type**\:   :py:class:`PseudowireEvpns <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns>`
                        
                        .. attribute:: pseudowire_routeds
                        
                        	List of pseudowire\-routed
                        	**type**\:   :py:class:`PseudowireRouteds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds>`
                        
                        .. attribute:: pseudowires
                        
                        	List of pseudowires
                        	**type**\:   :py:class:`Pseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect, self).__init__()

                            self.yang_name = "p2p-xconnect"
                            self.yang_parent_name = "p2p-xconnects"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"attachment-circuits" : ("attachment_circuits", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits), "backup-attachment-circuits" : ("backup_attachment_circuits", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits), "monitor-sessions" : ("monitor_sessions", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions), "pseudowire-evpns" : ("pseudowire_evpns", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns), "pseudowire-routeds" : ("pseudowire_routeds", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds), "pseudowires" : ("pseudowires", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires)}
                            self._child_list_classes = {}

                            self.name = YLeaf(YType.str, "name")

                            self.interworking = YLeaf(YType.enumeration, "interworking")

                            self.p2p_description = YLeaf(YType.str, "p2p-description")

                            self.attachment_circuits = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits()
                            self.attachment_circuits.parent = self
                            self._children_name_map["attachment_circuits"] = "attachment-circuits"
                            self._children_yang_names.add("attachment-circuits")

                            self.backup_attachment_circuits = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits()
                            self.backup_attachment_circuits.parent = self
                            self._children_name_map["backup_attachment_circuits"] = "backup-attachment-circuits"
                            self._children_yang_names.add("backup-attachment-circuits")

                            self.monitor_sessions = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions()
                            self.monitor_sessions.parent = self
                            self._children_name_map["monitor_sessions"] = "monitor-sessions"
                            self._children_yang_names.add("monitor-sessions")

                            self.pseudowire_evpns = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns()
                            self.pseudowire_evpns.parent = self
                            self._children_name_map["pseudowire_evpns"] = "pseudowire-evpns"
                            self._children_yang_names.add("pseudowire-evpns")

                            self.pseudowire_routeds = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds()
                            self.pseudowire_routeds.parent = self
                            self._children_name_map["pseudowire_routeds"] = "pseudowire-routeds"
                            self._children_yang_names.add("pseudowire-routeds")

                            self.pseudowires = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires()
                            self.pseudowires.parent = self
                            self._children_name_map["pseudowires"] = "pseudowires"
                            self._children_yang_names.add("pseudowires")
                            self._segment_path = lambda: "p2p-xconnect" + "[name='" + self.name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect, ['name', 'interworking', 'p2p_description'], name, value)


                        class AttachmentCircuits(Entity):
                            """
                            List of attachment circuits
                            
                            .. attribute:: attachment_circuit
                            
                            	Attachment circuit interface
                            	**type**\: list of    :py:class:`AttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits, self).__init__()

                                self.yang_name = "attachment-circuits"
                                self.yang_parent_name = "p2p-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"attachment-circuit" : ("attachment_circuit", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit)}

                                self.attachment_circuit = YList(self)
                                self._segment_path = lambda: "attachment-circuits"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits, [], name, value)


                            class AttachmentCircuit(Entity):
                                """
                                Attachment circuit interface
                                
                                .. attribute:: name  <key>
                                
                                	Name of the attachment circuit interface
                                	**type**\:  str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: enable
                                
                                	Enable attachment circuit interface
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit, self).__init__()

                                    self.yang_name = "attachment-circuit"
                                    self.yang_parent_name = "attachment-circuits"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.name = YLeaf(YType.str, "name")

                                    self.enable = YLeaf(YType.empty, "enable")
                                    self._segment_path = lambda: "attachment-circuit" + "[name='" + self.name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit, ['name', 'enable'], name, value)


                        class BackupAttachmentCircuits(Entity):
                            """
                            List of backup attachment circuits
                            
                            .. attribute:: backup_attachment_circuit
                            
                            	Backup attachment circuit
                            	**type**\: list of    :py:class:`BackupAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits, self).__init__()

                                self.yang_name = "backup-attachment-circuits"
                                self.yang_parent_name = "p2p-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"backup-attachment-circuit" : ("backup_attachment_circuit", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit)}

                                self.backup_attachment_circuit = YList(self)
                                self._segment_path = lambda: "backup-attachment-circuits"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits, [], name, value)


                            class BackupAttachmentCircuit(Entity):
                                """
                                Backup attachment circuit
                                
                                .. attribute:: interface_name  <key>
                                
                                	Name of the attachment circuit interface
                                	**type**\:  str
                                
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
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.interface_name = YLeaf(YType.str, "interface-name")
                                    self._segment_path = lambda: "backup-attachment-circuit" + "[interface-name='" + self.interface_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit, ['interface_name'], name, value)


                        class MonitorSessions(Entity):
                            """
                            List of Monitor session segments
                            
                            .. attribute:: monitor_session
                            
                            	Monitor session segment
                            	**type**\: list of    :py:class:`MonitorSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions, self).__init__()

                                self.yang_name = "monitor-sessions"
                                self.yang_parent_name = "p2p-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"monitor-session" : ("monitor_session", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession)}

                                self.monitor_session = YList(self)
                                self._segment_path = lambda: "monitor-sessions"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions, [], name, value)


                            class MonitorSession(Entity):
                                """
                                Monitor session segment
                                
                                .. attribute:: name  <key>
                                
                                	Name of the monitor session
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                .. attribute:: enable
                                
                                	Enable monitor session segment 
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession, self).__init__()

                                    self.yang_name = "monitor-session"
                                    self.yang_parent_name = "monitor-sessions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.name = YLeaf(YType.str, "name")

                                    self.enable = YLeaf(YType.empty, "enable")
                                    self._segment_path = lambda: "monitor-session" + "[name='" + self.name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession, ['name', 'enable'], name, value)


                        class PseudowireEvpns(Entity):
                            """
                            List of EVPN Services
                            
                            .. attribute:: pseudowire_evpn
                            
                            	EVPN P2P Service Configuration
                            	**type**\: list of    :py:class:`PseudowireEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns, self).__init__()

                                self.yang_name = "pseudowire-evpns"
                                self.yang_parent_name = "p2p-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"pseudowire-evpn" : ("pseudowire_evpn", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn)}

                                self.pseudowire_evpn = YList(self)
                                self._segment_path = lambda: "pseudowire-evpns"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns, [], name, value)


                            class PseudowireEvpn(Entity):
                                """
                                EVPN P2P Service Configuration
                                
                                .. attribute:: eviid  <key>
                                
                                	Ethernet VPN ID
                                	**type**\:  int
                                
                                	**range:** 1..65534
                                
                                .. attribute:: remote_acid  <key>
                                
                                	Remote AC ID
                                	**type**\:  int
                                
                                	**range:** 1..16777215
                                
                                .. attribute:: source_acid  <key>
                                
                                	Source AC ID
                                	**type**\:  int
                                
                                	**range:** 1..16777215
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn, self).__init__()

                                    self.yang_name = "pseudowire-evpn"
                                    self.yang_parent_name = "pseudowire-evpns"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.eviid = YLeaf(YType.uint32, "eviid")

                                    self.remote_acid = YLeaf(YType.uint32, "remote-acid")

                                    self.source_acid = YLeaf(YType.uint32, "source-acid")
                                    self._segment_path = lambda: "pseudowire-evpn" + "[eviid='" + self.eviid.get() + "']" + "[remote-acid='" + self.remote_acid.get() + "']" + "[source-acid='" + self.source_acid.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn, ['eviid', 'remote_acid', 'source_acid'], name, value)


                        class PseudowireRouteds(Entity):
                            """
                            List of pseudowire\-routed
                            
                            .. attribute:: pseudowire_routed
                            
                            	Pseudowire configuration
                            	**type**\: list of    :py:class:`PseudowireRouted <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds, self).__init__()

                                self.yang_name = "pseudowire-routeds"
                                self.yang_parent_name = "p2p-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"pseudowire-routed" : ("pseudowire_routed", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted)}

                                self.pseudowire_routed = YList(self)
                                self._segment_path = lambda: "pseudowire-routeds"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds, [], name, value)


                            class PseudowireRouted(Entity):
                                """
                                Pseudowire configuration
                                
                                .. attribute:: global_id  <key>
                                
                                	Target Global ID
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: prefix  <key>
                                
                                	Target Prefix
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: acid  <key>
                                
                                	Target AC ID
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: sacid  <key>
                                
                                	Source AC ID
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: class_
                                
                                	Name of the pseudowire class
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: tag_impose
                                
                                	Tag Impose vlan tagged mode
                                	**type**\:  int
                                
                                	**range:** 1..4094
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted, self).__init__()

                                    self.yang_name = "pseudowire-routed"
                                    self.yang_parent_name = "pseudowire-routeds"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.global_id = YLeaf(YType.uint32, "global-id")

                                    self.prefix = YLeaf(YType.str, "prefix")

                                    self.acid = YLeaf(YType.uint32, "acid")

                                    self.sacid = YLeaf(YType.uint32, "sacid")

                                    self.class_ = YLeaf(YType.str, "class")

                                    self.tag_impose = YLeaf(YType.uint32, "tag-impose")
                                    self._segment_path = lambda: "pseudowire-routed" + "[global-id='" + self.global_id.get() + "']" + "[prefix='" + self.prefix.get() + "']" + "[acid='" + self.acid.get() + "']" + "[sacid='" + self.sacid.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted, ['global_id', 'prefix', 'acid', 'sacid', 'class_', 'tag_impose'], name, value)


                        class Pseudowires(Entity):
                            """
                            List of pseudowires
                            
                            .. attribute:: pseudowire
                            
                            	Pseudowire configuration
                            	**type**\: list of    :py:class:`Pseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires, self).__init__()

                                self.yang_name = "pseudowires"
                                self.yang_parent_name = "p2p-xconnect"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"pseudowire" : ("pseudowire", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire)}

                                self.pseudowire = YList(self)
                                self._segment_path = lambda: "pseudowires"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires, [], name, value)


                            class Pseudowire(Entity):
                                """
                                Pseudowire configuration
                                
                                .. attribute:: pseudowire_id  <key>
                                
                                	Pseudowire ID
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: neighbor
                                
                                	keys\: neighbor
                                	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor>`
                                
                                .. attribute:: pseudowire_address
                                
                                	keys\: pseudowire\-address
                                	**type**\: list of    :py:class:`PseudowireAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire, self).__init__()

                                    self.yang_name = "pseudowire"
                                    self.yang_parent_name = "pseudowires"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"neighbor" : ("neighbor", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor), "pseudowire-address" : ("pseudowire_address", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress)}

                                    self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                                    self.neighbor = YList(self)
                                    self.pseudowire_address = YList(self)
                                    self._segment_path = lambda: "pseudowire" + "[pseudowire-id='" + self.pseudowire_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire, ['pseudowire_id'], name, value)


                                class Neighbor(Entity):
                                    """
                                    keys\: neighbor
                                    
                                    .. attribute:: neighbor  <key>
                                    
                                    	Pseudowire IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: backup_pseudowires
                                    
                                    	List of pseudowires
                                    	**type**\:   :py:class:`BackupPseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires>`
                                    
                                    .. attribute:: bandwidth
                                    
                                    	Pseudowire Bandwidth
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: class_
                                    
                                    	Name of the pseudowire class
                                    	**type**\:  str
                                    
                                    	**length:** 1..32
                                    
                                    .. attribute:: l2tp_static
                                    
                                    	Pseudowire L2TPv3 static configuration
                                    	**type**\:   :py:class:`L2TpStatic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic>`
                                    
                                    .. attribute:: l2tp_static_attributes
                                    
                                    	L2TP Static Attributes
                                    	**type**\:   :py:class:`L2TpStaticAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes>`
                                    
                                    .. attribute:: mpls_static_labels
                                    
                                    	MPLS static labels
                                    	**type**\:   :py:class:`MplsStaticLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels>`
                                    
                                    .. attribute:: source_address
                                    
                                    	Value of the Pseudowire source address. Must be IPv6 only
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: tag_impose
                                    
                                    	Tag Impose vlan tagged mode
                                    	**type**\:  int
                                    
                                    	**range:** 1..4094
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor, self).__init__()

                                        self.yang_name = "neighbor"
                                        self.yang_parent_name = "pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"backup-pseudowires" : ("backup_pseudowires", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires), "l2tp-static" : ("l2tp_static", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic), "l2tp-static-attributes" : ("l2tp_static_attributes", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes), "mpls-static-labels" : ("mpls_static_labels", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels)}
                                        self._child_list_classes = {}

                                        self.neighbor = YLeaf(YType.str, "neighbor")

                                        self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                                        self.class_ = YLeaf(YType.str, "class")

                                        self.source_address = YLeaf(YType.str, "source-address")

                                        self.tag_impose = YLeaf(YType.uint32, "tag-impose")

                                        self.backup_pseudowires = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires()
                                        self.backup_pseudowires.parent = self
                                        self._children_name_map["backup_pseudowires"] = "backup-pseudowires"
                                        self._children_yang_names.add("backup-pseudowires")

                                        self.l2tp_static = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic()
                                        self.l2tp_static.parent = self
                                        self._children_name_map["l2tp_static"] = "l2tp-static"
                                        self._children_yang_names.add("l2tp-static")

                                        self.l2tp_static_attributes = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes()
                                        self.l2tp_static_attributes.parent = self
                                        self._children_name_map["l2tp_static_attributes"] = "l2tp-static-attributes"
                                        self._children_yang_names.add("l2tp-static-attributes")

                                        self.mpls_static_labels = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels()
                                        self.mpls_static_labels.parent = self
                                        self._children_name_map["mpls_static_labels"] = "mpls-static-labels"
                                        self._children_yang_names.add("mpls-static-labels")
                                        self._segment_path = lambda: "neighbor" + "[neighbor='" + self.neighbor.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor, ['neighbor', 'bandwidth', 'class_', 'source_address', 'tag_impose'], name, value)


                                    class BackupPseudowires(Entity):
                                        """
                                        List of pseudowires
                                        
                                        .. attribute:: backup_pseudowire
                                        
                                        	Backup pseudowire for the cross connect
                                        	**type**\: list of    :py:class:`BackupPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires, self).__init__()

                                            self.yang_name = "backup-pseudowires"
                                            self.yang_parent_name = "neighbor"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"backup-pseudowire" : ("backup_pseudowire", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire)}

                                            self.backup_pseudowire = YList(self)
                                            self._segment_path = lambda: "backup-pseudowires"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires, [], name, value)


                                        class BackupPseudowire(Entity):
                                            """
                                            Backup pseudowire for the cross connect
                                            
                                            .. attribute:: neighbor  <key>
                                            
                                            	Neighbor IP address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: pseudowire_id  <key>
                                            
                                            	Pseudowire ID
                                            	**type**\:  int
                                            
                                            	**range:** 1..4294967295
                                            
                                            .. attribute:: backup_mpls_static_labels
                                            
                                            	MPLS static labels
                                            	**type**\:   :py:class:`BackupMplsStaticLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels>`
                                            
                                            .. attribute:: backup_pw_class
                                            
                                            	PW class template name to use for the backup PW
                                            	**type**\:  str
                                            
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
                                                self._child_container_classes = {"backup-mpls-static-labels" : ("backup_mpls_static_labels", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels)}
                                                self._child_list_classes = {}

                                                self.neighbor = YLeaf(YType.str, "neighbor")

                                                self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                                                self.backup_pw_class = YLeaf(YType.str, "backup-pw-class")

                                                self.backup_mpls_static_labels = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels()
                                                self.backup_mpls_static_labels.parent = self
                                                self._children_name_map["backup_mpls_static_labels"] = "backup-mpls-static-labels"
                                                self._children_yang_names.add("backup-mpls-static-labels")
                                                self._segment_path = lambda: "backup-pseudowire" + "[neighbor='" + self.neighbor.get() + "']" + "[pseudowire-id='" + self.pseudowire_id.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire, ['neighbor', 'pseudowire_id', 'backup_pw_class'], name, value)


                                            class BackupMplsStaticLabels(Entity):
                                                """
                                                MPLS static labels
                                                
                                                .. attribute:: local_static_label
                                                
                                                	Pseudowire local static label
                                                	**type**\:  int
                                                
                                                	**range:** 16..1048575
                                                
                                                .. attribute:: remote_static_label
                                                
                                                	Pseudowire remote static label
                                                	**type**\:  int
                                                
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
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.local_static_label = YLeaf(YType.uint32, "local-static-label")

                                                    self.remote_static_label = YLeaf(YType.uint32, "remote-static-label")
                                                    self._segment_path = lambda: "backup-mpls-static-labels"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels, ['local_static_label', 'remote_static_label'], name, value)


                                    class L2TpStatic(Entity):
                                        """
                                        Pseudowire L2TPv3 static configuration
                                        
                                        .. attribute:: enable
                                        
                                        	Enable pseudowire L2TPv3 static configuration
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic, self).__init__()

                                            self.yang_name = "l2tp-static"
                                            self.yang_parent_name = "neighbor"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.enable = YLeaf(YType.empty, "enable")
                                            self._segment_path = lambda: "l2tp-static"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic, ['enable'], name, value)


                                    class L2TpStaticAttributes(Entity):
                                        """
                                        L2TP Static Attributes
                                        
                                        .. attribute:: l2tp_local_cookie
                                        
                                        	L2TP local cookie
                                        	**type**\:   :py:class:`L2TpLocalCookie <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie>`
                                        
                                        .. attribute:: l2tp_local_session_id
                                        
                                        	L2TP local session ID
                                        	**type**\:  int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: l2tp_remote_cookie
                                        
                                        	L2TP remote cookie
                                        	**type**\:   :py:class:`L2TpRemoteCookie <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie>`
                                        
                                        .. attribute:: l2tp_remote_session_id
                                        
                                        	L2TP remote session ID
                                        	**type**\:  int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: l2tp_secondary_local_cookie
                                        
                                        	L2TP secondary local cookie
                                        	**type**\:   :py:class:`L2TpSecondaryLocalCookie <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes, self).__init__()

                                            self.yang_name = "l2tp-static-attributes"
                                            self.yang_parent_name = "neighbor"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"l2tp-local-cookie" : ("l2tp_local_cookie", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie), "l2tp-remote-cookie" : ("l2tp_remote_cookie", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie), "l2tp-secondary-local-cookie" : ("l2tp_secondary_local_cookie", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie)}
                                            self._child_list_classes = {}

                                            self.l2tp_local_session_id = YLeaf(YType.uint32, "l2tp-local-session-id")

                                            self.l2tp_remote_session_id = YLeaf(YType.uint32, "l2tp-remote-session-id")

                                            self.l2tp_local_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie()
                                            self.l2tp_local_cookie.parent = self
                                            self._children_name_map["l2tp_local_cookie"] = "l2tp-local-cookie"
                                            self._children_yang_names.add("l2tp-local-cookie")

                                            self.l2tp_remote_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie()
                                            self.l2tp_remote_cookie.parent = self
                                            self._children_name_map["l2tp_remote_cookie"] = "l2tp-remote-cookie"
                                            self._children_yang_names.add("l2tp-remote-cookie")

                                            self.l2tp_secondary_local_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie()
                                            self.l2tp_secondary_local_cookie.parent = self
                                            self._children_name_map["l2tp_secondary_local_cookie"] = "l2tp-secondary-local-cookie"
                                            self._children_yang_names.add("l2tp-secondary-local-cookie")
                                            self._segment_path = lambda: "l2tp-static-attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes, ['l2tp_local_session_id', 'l2tp_remote_session_id'], name, value)


                                        class L2TpLocalCookie(Entity):
                                            """
                                            L2TP local cookie
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher local cookie value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower local cookie value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: size
                                            
                                            	Local cookie size
                                            	**type**\:   :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie, self).__init__()

                                                self.yang_name = "l2tp-local-cookie"
                                                self.yang_parent_name = "l2tp-static-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.higher_value = YLeaf(YType.uint32, "higher-value")

                                                self.lower_value = YLeaf(YType.uint32, "lower-value")

                                                self.size = YLeaf(YType.enumeration, "size")
                                                self._segment_path = lambda: "l2tp-local-cookie"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie, ['higher_value', 'lower_value', 'size'], name, value)


                                        class L2TpRemoteCookie(Entity):
                                            """
                                            L2TP remote cookie
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher remote cookie value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower remote cookie value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: size
                                            
                                            	Remote cookie size
                                            	**type**\:   :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie, self).__init__()

                                                self.yang_name = "l2tp-remote-cookie"
                                                self.yang_parent_name = "l2tp-static-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.higher_value = YLeaf(YType.uint32, "higher-value")

                                                self.lower_value = YLeaf(YType.uint32, "lower-value")

                                                self.size = YLeaf(YType.enumeration, "size")
                                                self._segment_path = lambda: "l2tp-remote-cookie"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie, ['higher_value', 'lower_value', 'size'], name, value)


                                        class L2TpSecondaryLocalCookie(Entity):
                                            """
                                            L2TP secondary local cookie
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher local cookie value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower local cookie value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: size
                                            
                                            	Local cookie size
                                            	**type**\:   :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie, self).__init__()

                                                self.yang_name = "l2tp-secondary-local-cookie"
                                                self.yang_parent_name = "l2tp-static-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.higher_value = YLeaf(YType.uint32, "higher-value")

                                                self.lower_value = YLeaf(YType.uint32, "lower-value")

                                                self.size = YLeaf(YType.enumeration, "size")
                                                self._segment_path = lambda: "l2tp-secondary-local-cookie"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie, ['higher_value', 'lower_value', 'size'], name, value)


                                    class MplsStaticLabels(Entity):
                                        """
                                        MPLS static labels
                                        
                                        .. attribute:: local_static_label
                                        
                                        	Pseudowire local static label
                                        	**type**\:  int
                                        
                                        	**range:** 16..1048575
                                        
                                        .. attribute:: remote_static_label
                                        
                                        	Pseudowire remote static label
                                        	**type**\:  int
                                        
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
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.local_static_label = YLeaf(YType.uint32, "local-static-label")

                                            self.remote_static_label = YLeaf(YType.uint32, "remote-static-label")
                                            self._segment_path = lambda: "mpls-static-labels"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels, ['local_static_label', 'remote_static_label'], name, value)


                                class PseudowireAddress(Entity):
                                    """
                                    keys\: pseudowire\-address
                                    
                                    .. attribute:: pseudowire_address  <key>
                                    
                                    	Pseudowire IPv6 address. A pseudowire can have only one address\: IPv4 or IPv6
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: backup_pseudowires
                                    
                                    	List of pseudowires
                                    	**type**\:   :py:class:`BackupPseudowires <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires>`
                                    
                                    .. attribute:: bandwidth
                                    
                                    	Pseudowire Bandwidth
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: class_
                                    
                                    	Name of the pseudowire class
                                    	**type**\:  str
                                    
                                    	**length:** 1..32
                                    
                                    .. attribute:: l2tp_static
                                    
                                    	Pseudowire L2TPv3 static configuration
                                    	**type**\:   :py:class:`L2TpStatic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic>`
                                    
                                    .. attribute:: l2tp_static_attributes
                                    
                                    	L2TP Static Attributes
                                    	**type**\:   :py:class:`L2TpStaticAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes>`
                                    
                                    .. attribute:: mpls_static_labels
                                    
                                    	MPLS static labels
                                    	**type**\:   :py:class:`MplsStaticLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels>`
                                    
                                    .. attribute:: source_address
                                    
                                    	Value of the Pseudowire source address. Must be IPv6 only
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: tag_impose
                                    
                                    	Tag Impose vlan tagged mode
                                    	**type**\:  int
                                    
                                    	**range:** 1..4094
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2017-06-26'

                                    def __init__(self):
                                        super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress, self).__init__()

                                        self.yang_name = "pseudowire-address"
                                        self.yang_parent_name = "pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"backup-pseudowires" : ("backup_pseudowires", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires), "l2tp-static" : ("l2tp_static", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic), "l2tp-static-attributes" : ("l2tp_static_attributes", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes), "mpls-static-labels" : ("mpls_static_labels", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels)}
                                        self._child_list_classes = {}

                                        self.pseudowire_address = YLeaf(YType.str, "pseudowire-address")

                                        self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                                        self.class_ = YLeaf(YType.str, "class")

                                        self.source_address = YLeaf(YType.str, "source-address")

                                        self.tag_impose = YLeaf(YType.uint32, "tag-impose")

                                        self.backup_pseudowires = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires()
                                        self.backup_pseudowires.parent = self
                                        self._children_name_map["backup_pseudowires"] = "backup-pseudowires"
                                        self._children_yang_names.add("backup-pseudowires")

                                        self.l2tp_static = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic()
                                        self.l2tp_static.parent = self
                                        self._children_name_map["l2tp_static"] = "l2tp-static"
                                        self._children_yang_names.add("l2tp-static")

                                        self.l2tp_static_attributes = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes()
                                        self.l2tp_static_attributes.parent = self
                                        self._children_name_map["l2tp_static_attributes"] = "l2tp-static-attributes"
                                        self._children_yang_names.add("l2tp-static-attributes")

                                        self.mpls_static_labels = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels()
                                        self.mpls_static_labels.parent = self
                                        self._children_name_map["mpls_static_labels"] = "mpls-static-labels"
                                        self._children_yang_names.add("mpls-static-labels")
                                        self._segment_path = lambda: "pseudowire-address" + "[pseudowire-address='" + self.pseudowire_address.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress, ['pseudowire_address', 'bandwidth', 'class_', 'source_address', 'tag_impose'], name, value)


                                    class BackupPseudowires(Entity):
                                        """
                                        List of pseudowires
                                        
                                        .. attribute:: backup_pseudowire
                                        
                                        	Backup pseudowire for the cross connect
                                        	**type**\: list of    :py:class:`BackupPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires, self).__init__()

                                            self.yang_name = "backup-pseudowires"
                                            self.yang_parent_name = "pseudowire-address"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"backup-pseudowire" : ("backup_pseudowire", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire)}

                                            self.backup_pseudowire = YList(self)
                                            self._segment_path = lambda: "backup-pseudowires"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires, [], name, value)


                                        class BackupPseudowire(Entity):
                                            """
                                            Backup pseudowire for the cross connect
                                            
                                            .. attribute:: neighbor  <key>
                                            
                                            	Neighbor IP address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: pseudowire_id  <key>
                                            
                                            	Pseudowire ID
                                            	**type**\:  int
                                            
                                            	**range:** 1..4294967295
                                            
                                            .. attribute:: backup_mpls_static_labels
                                            
                                            	MPLS static labels
                                            	**type**\:   :py:class:`BackupMplsStaticLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels>`
                                            
                                            .. attribute:: backup_pw_class
                                            
                                            	PW class template name to use for the backup PW
                                            	**type**\:  str
                                            
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
                                                self._child_container_classes = {"backup-mpls-static-labels" : ("backup_mpls_static_labels", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels)}
                                                self._child_list_classes = {}

                                                self.neighbor = YLeaf(YType.str, "neighbor")

                                                self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                                                self.backup_pw_class = YLeaf(YType.str, "backup-pw-class")

                                                self.backup_mpls_static_labels = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels()
                                                self.backup_mpls_static_labels.parent = self
                                                self._children_name_map["backup_mpls_static_labels"] = "backup-mpls-static-labels"
                                                self._children_yang_names.add("backup-mpls-static-labels")
                                                self._segment_path = lambda: "backup-pseudowire" + "[neighbor='" + self.neighbor.get() + "']" + "[pseudowire-id='" + self.pseudowire_id.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire, ['neighbor', 'pseudowire_id', 'backup_pw_class'], name, value)


                                            class BackupMplsStaticLabels(Entity):
                                                """
                                                MPLS static labels
                                                
                                                .. attribute:: local_static_label
                                                
                                                	Pseudowire local static label
                                                	**type**\:  int
                                                
                                                	**range:** 16..1048575
                                                
                                                .. attribute:: remote_static_label
                                                
                                                	Pseudowire remote static label
                                                	**type**\:  int
                                                
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
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.local_static_label = YLeaf(YType.uint32, "local-static-label")

                                                    self.remote_static_label = YLeaf(YType.uint32, "remote-static-label")
                                                    self._segment_path = lambda: "backup-mpls-static-labels"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels, ['local_static_label', 'remote_static_label'], name, value)


                                    class L2TpStatic(Entity):
                                        """
                                        Pseudowire L2TPv3 static configuration
                                        
                                        .. attribute:: enable
                                        
                                        	Enable pseudowire L2TPv3 static configuration
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic, self).__init__()

                                            self.yang_name = "l2tp-static"
                                            self.yang_parent_name = "pseudowire-address"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.enable = YLeaf(YType.empty, "enable")
                                            self._segment_path = lambda: "l2tp-static"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic, ['enable'], name, value)


                                    class L2TpStaticAttributes(Entity):
                                        """
                                        L2TP Static Attributes
                                        
                                        .. attribute:: l2tp_local_cookie
                                        
                                        	L2TP local cookie
                                        	**type**\:   :py:class:`L2TpLocalCookie <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie>`
                                        
                                        .. attribute:: l2tp_local_session_id
                                        
                                        	L2TP local session ID
                                        	**type**\:  int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: l2tp_remote_cookie
                                        
                                        	L2TP remote cookie
                                        	**type**\:   :py:class:`L2TpRemoteCookie <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie>`
                                        
                                        .. attribute:: l2tp_remote_session_id
                                        
                                        	L2TP remote session ID
                                        	**type**\:  int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: l2tp_secondary_local_cookie
                                        
                                        	L2TP secondary local cookie
                                        	**type**\:   :py:class:`L2TpSecondaryLocalCookie <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2017-06-26'

                                        def __init__(self):
                                            super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes, self).__init__()

                                            self.yang_name = "l2tp-static-attributes"
                                            self.yang_parent_name = "pseudowire-address"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"l2tp-local-cookie" : ("l2tp_local_cookie", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie), "l2tp-remote-cookie" : ("l2tp_remote_cookie", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie), "l2tp-secondary-local-cookie" : ("l2tp_secondary_local_cookie", L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie)}
                                            self._child_list_classes = {}

                                            self.l2tp_local_session_id = YLeaf(YType.uint32, "l2tp-local-session-id")

                                            self.l2tp_remote_session_id = YLeaf(YType.uint32, "l2tp-remote-session-id")

                                            self.l2tp_local_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie()
                                            self.l2tp_local_cookie.parent = self
                                            self._children_name_map["l2tp_local_cookie"] = "l2tp-local-cookie"
                                            self._children_yang_names.add("l2tp-local-cookie")

                                            self.l2tp_remote_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie()
                                            self.l2tp_remote_cookie.parent = self
                                            self._children_name_map["l2tp_remote_cookie"] = "l2tp-remote-cookie"
                                            self._children_yang_names.add("l2tp-remote-cookie")

                                            self.l2tp_secondary_local_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie()
                                            self.l2tp_secondary_local_cookie.parent = self
                                            self._children_name_map["l2tp_secondary_local_cookie"] = "l2tp-secondary-local-cookie"
                                            self._children_yang_names.add("l2tp-secondary-local-cookie")
                                            self._segment_path = lambda: "l2tp-static-attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes, ['l2tp_local_session_id', 'l2tp_remote_session_id'], name, value)


                                        class L2TpLocalCookie(Entity):
                                            """
                                            L2TP local cookie
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher local cookie value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower local cookie value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: size
                                            
                                            	Local cookie size
                                            	**type**\:   :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie, self).__init__()

                                                self.yang_name = "l2tp-local-cookie"
                                                self.yang_parent_name = "l2tp-static-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.higher_value = YLeaf(YType.uint32, "higher-value")

                                                self.lower_value = YLeaf(YType.uint32, "lower-value")

                                                self.size = YLeaf(YType.enumeration, "size")
                                                self._segment_path = lambda: "l2tp-local-cookie"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie, ['higher_value', 'lower_value', 'size'], name, value)


                                        class L2TpRemoteCookie(Entity):
                                            """
                                            L2TP remote cookie
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher remote cookie value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower remote cookie value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: size
                                            
                                            	Remote cookie size
                                            	**type**\:   :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie, self).__init__()

                                                self.yang_name = "l2tp-remote-cookie"
                                                self.yang_parent_name = "l2tp-static-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.higher_value = YLeaf(YType.uint32, "higher-value")

                                                self.lower_value = YLeaf(YType.uint32, "lower-value")

                                                self.size = YLeaf(YType.enumeration, "size")
                                                self._segment_path = lambda: "l2tp-remote-cookie"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie, ['higher_value', 'lower_value', 'size'], name, value)


                                        class L2TpSecondaryLocalCookie(Entity):
                                            """
                                            L2TP secondary local cookie
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher local cookie value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower local cookie value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: size
                                            
                                            	Local cookie size
                                            	**type**\:   :py:class:`L2tpCookieSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2017-06-26'

                                            def __init__(self):
                                                super(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie, self).__init__()

                                                self.yang_name = "l2tp-secondary-local-cookie"
                                                self.yang_parent_name = "l2tp-static-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.higher_value = YLeaf(YType.uint32, "higher-value")

                                                self.lower_value = YLeaf(YType.uint32, "lower-value")

                                                self.size = YLeaf(YType.enumeration, "size")
                                                self._segment_path = lambda: "l2tp-secondary-local-cookie"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie, ['higher_value', 'lower_value', 'size'], name, value)


                                    class MplsStaticLabels(Entity):
                                        """
                                        MPLS static labels
                                        
                                        .. attribute:: local_static_label
                                        
                                        	Pseudowire local static label
                                        	**type**\:  int
                                        
                                        	**range:** 16..1048575
                                        
                                        .. attribute:: remote_static_label
                                        
                                        	Pseudowire remote static label
                                        	**type**\:  int
                                        
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
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.local_static_label = YLeaf(YType.uint32, "local-static-label")

                                            self.remote_static_label = YLeaf(YType.uint32, "remote-static-label")
                                            self._segment_path = lambda: "mpls-static-labels"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels, ['local_static_label', 'remote_static_label'], name, value)


    class Neighbor(Entity):
        """
        L2VPN neighbor submode
        
        .. attribute:: ldp_flap
        
        	Enable targetted LDP session flap action
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(L2Vpn.Neighbor, self).__init__()

            self.yang_name = "neighbor"
            self.yang_parent_name = "l2vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.ldp_flap = YLeaf(YType.empty, "ldp-flap")
            self._segment_path = lambda: "neighbor"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Vpn.Neighbor, ['ldp_flap'], name, value)


    class Pbb(Entity):
        """
        L2VPN PBB Global
        
        .. attribute:: backbone_source_mac
        
        	Backbone Source MAC
        	**type**\:  str
        
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.backbone_source_mac = YLeaf(YType.str, "backbone-source-mac")
            self._segment_path = lambda: "pbb"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Vpn.Pbb, ['backbone_source_mac'], name, value)


    class PwRouting(Entity):
        """
        Pseudowire\-routing attributes
        
        .. attribute:: pw_routing_bgp
        
        	Enable Autodiscovery BGP Pseudowire\-routing BGP
        	**type**\:   :py:class:`PwRoutingBgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.PwRouting.PwRoutingBgp>`
        
        .. attribute:: pw_routing_global_id
        
        	Pseudowire\-routing Global ID
        	**type**\:  int
        
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
            self._child_container_classes = {"pw-routing-bgp" : ("pw_routing_bgp", L2Vpn.PwRouting.PwRoutingBgp)}
            self._child_list_classes = {}

            self.pw_routing_global_id = YLeaf(YType.uint32, "pw-routing-global-id")

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
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: evpn_route_distinguisher
            
            	Route Distinguisher
            	**type**\:   :py:class:`EvpnRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.PwRouting.PwRoutingBgp, self).__init__()

                self.yang_name = "pw-routing-bgp"
                self.yang_parent_name = "pw-routing"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"evpn-route-distinguisher" : ("evpn_route_distinguisher", L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher)}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

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
                
                .. attribute:: addr_index
                
                	Addr index
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: address
                
                	IPV4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: as_
                
                	Two byte or 4 byte AS number
                	**type**\:  int
                
                	**range:** 1..4294967295
                
                .. attribute:: as_index
                
                	AS\:nn (hex or decimal format)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Router Distinguisher Type
                	**type**\:   :py:class:`BgpRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher, self).__init__()

                    self.yang_name = "evpn-route-distinguisher"
                    self.yang_parent_name = "pw-routing-bgp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.addr_index = YLeaf(YType.uint32, "addr-index")

                    self.address = YLeaf(YType.str, "address")

                    self.as_ = YLeaf(YType.uint32, "as")

                    self.as_index = YLeaf(YType.uint32, "as-index")

                    self.type = YLeaf(YType.enumeration, "type")
                    self._segment_path = lambda: "evpn-route-distinguisher"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/pw-routing/pw-routing-bgp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher, ['addr_index', 'address', 'as_', 'as_index', 'type'], name, value)


    class Snmp(Entity):
        """
        SNMP related configuration
        
        .. attribute:: mib
        
        	MIB related configuration
        	**type**\:   :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Snmp.Mib>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(L2Vpn.Snmp, self).__init__()

            self.yang_name = "snmp"
            self.yang_parent_name = "l2vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"mib" : ("mib", L2Vpn.Snmp.Mib)}
            self._child_list_classes = {}

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
            	**type**\:   :py:class:`MibInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Snmp.Mib.MibInterface>`
            
            .. attribute:: mib_pseudowire
            
            	Pseudowire related configuration for MIB
            	**type**\:   :py:class:`MibPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Snmp.Mib.MibPseudowire>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Snmp.Mib, self).__init__()

                self.yang_name = "mib"
                self.yang_parent_name = "snmp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"mib-interface" : ("mib_interface", L2Vpn.Snmp.Mib.MibInterface), "mib-pseudowire" : ("mib_pseudowire", L2Vpn.Snmp.Mib.MibPseudowire)}
                self._child_list_classes = {}

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
                	**type**\:   :py:class:`Format <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Snmp.Mib.MibInterface.Format>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Snmp.Mib.MibInterface, self).__init__()

                    self.yang_name = "mib-interface"
                    self.yang_parent_name = "mib"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"format" : ("format", L2Vpn.Snmp.Mib.MibInterface.Format)}
                    self._child_list_classes = {}

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
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(L2Vpn.Snmp.Mib.MibInterface.Format, self).__init__()

                        self.yang_name = "format"
                        self.yang_parent_name = "mib-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.external_interface_format = YLeaf(YType.empty, "external-interface-format")
                        self._segment_path = lambda: "format"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/snmp/mib/mib-interface/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Vpn.Snmp.Mib.MibInterface.Format, ['external_interface_format'], name, value)


            class MibPseudowire(Entity):
                """
                Pseudowire related configuration for MIB
                
                .. attribute:: statistics
                
                	Enable pseudowire statistics in MIB output
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2017-06-26'

                def __init__(self):
                    super(L2Vpn.Snmp.Mib.MibPseudowire, self).__init__()

                    self.yang_name = "mib-pseudowire"
                    self.yang_parent_name = "mib"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.statistics = YLeaf(YType.empty, "statistics")
                    self._segment_path = lambda: "mib-pseudowire"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/snmp/mib/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Vpn.Snmp.Mib.MibPseudowire, ['statistics'], name, value)


    class Utility(Entity):
        """
        L2VPN utilities
        
        .. attribute:: logging
        
        	L2VPN logging utility
        	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Utility.Logging>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2017-06-26'

        def __init__(self):
            super(L2Vpn.Utility, self).__init__()

            self.yang_name = "utility"
            self.yang_parent_name = "l2vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"logging" : ("logging", L2Vpn.Utility.Logging)}
            self._child_list_classes = {}

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
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: nsr_state_change
            
            	Enable Non Stop Routing state change logging
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: pseudowire_state_change
            
            	Enable pseudowire state change logging
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: pwhe_replication_state_change
            
            	Enable PW\-HE Replication state change logging
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: vfi
            
            	Enable VFI state change logging
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2017-06-26'

            def __init__(self):
                super(L2Vpn.Utility.Logging, self).__init__()

                self.yang_name = "logging"
                self.yang_parent_name = "utility"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.bridge_domain_state_change = YLeaf(YType.empty, "bridge-domain-state-change")

                self.nsr_state_change = YLeaf(YType.empty, "nsr-state-change")

                self.pseudowire_state_change = YLeaf(YType.empty, "pseudowire-state-change")

                self.pwhe_replication_state_change = YLeaf(YType.empty, "pwhe-replication-state-change")

                self.vfi = YLeaf(YType.empty, "vfi")
                self._segment_path = lambda: "logging"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn/utility/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Vpn.Utility.Logging, ['bridge_domain_state_change', 'nsr_state_change', 'pseudowire_state_change', 'pwhe_replication_state_change', 'vfi'], name, value)

    def clone_ptr(self):
        self._top_entity = L2Vpn()
        return self._top_entity

