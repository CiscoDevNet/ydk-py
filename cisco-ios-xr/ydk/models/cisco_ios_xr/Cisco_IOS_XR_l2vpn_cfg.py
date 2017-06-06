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

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BackupDisableEnum(Enum):
    """
    BackupDisableEnum

    Backup disable

    .. data:: never = 0

    	Never

    .. data:: delay = 1

    	Delay seconds

    """

    never = 0

    delay = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['BackupDisableEnum']


class BdmacLearnEnum(Enum):
    """
    BdmacLearnEnum

    Bdmac learn

    .. data:: disable_learning = 2

    	Disable Learning

    """

    disable_learning = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['BdmacLearnEnum']


class BgpRouteDistinguisherEnum(Enum):
    """
    BgpRouteDistinguisherEnum

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

    auto = 1

    two_byte_as = 2

    four_byte_as = 3

    ipv4_address = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['BgpRouteDistinguisherEnum']


class BgpRouteTargetEnum(Enum):
    """
    BgpRouteTargetEnum

    Bgp route target

    .. data:: no_stitching = 0

    	RT is default type

    .. data:: stitching = 1

    	RT is for stitching (Golf-L2)

    """

    no_stitching = 0

    stitching = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['BgpRouteTargetEnum']


class BgpRouteTargetFormatEnum(Enum):
    """
    BgpRouteTargetFormatEnum

    Bgp route target format

    .. data:: none = 0

    	No route target

    .. data:: two_byte_as = 1

    	2 Byte AS:nn format

    .. data:: four_byte_as = 2

    	4 byte AS:nn format

    .. data:: ipv4_address = 3

    	IP:nn format

    """

    none = 0

    two_byte_as = 1

    four_byte_as = 2

    ipv4_address = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['BgpRouteTargetFormatEnum']


class BgpRouteTargetRoleEnum(Enum):
    """
    BgpRouteTargetRoleEnum

    Bgp route target role

    .. data:: both = 0

    	Both Import and export roles

    .. data:: import_ = 1

    	Import role

    .. data:: export = 2

    	Export role

    """

    both = 0

    import_ = 1

    export = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['BgpRouteTargetRoleEnum']


class BridgeDomainTransportModeEnum(Enum):
    """
    BridgeDomainTransportModeEnum

    Bridge domain transport mode

    .. data:: vlan_passthrough = 3

    	Vlan tagged passthrough mode

    """

    vlan_passthrough = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['BridgeDomainTransportModeEnum']


class ControlWordEnum(Enum):
    """
    ControlWordEnum

    Control word

    .. data:: enable = 1

    	Enable control word

    .. data:: disable = 2

    	Disable control word

    """

    enable = 1

    disable = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['ControlWordEnum']


class ErpPort1Enum(Enum):
    """
    ErpPort1Enum

    Erp port1

    .. data:: port0 = 0

    	ERP main port 0

    .. data:: port1 = 1

    	ERP main port 1

    """

    port0 = 0

    port1 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['ErpPort1Enum']


class ErpPortEnum(Enum):
    """
    ErpPortEnum

    Erp port

    .. data:: none = 1

    	ERP port type none

    .. data:: virtual = 2

    	ERP port type virtual

    .. data:: interface = 3

    	ERP port type interface

    """

    none = 1

    virtual = 2

    interface = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['ErpPortEnum']


class ErpapsEnum(Enum):
    """
    ErpapsEnum

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

    interface = 1

    bridge_domain = 2

    xconnect = 3

    none = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['ErpapsEnum']


class EthernetSegmentIdentifierEnum(Enum):
    """
    EthernetSegmentIdentifierEnum

    Ethernet segment identifier

    .. data:: type0 = 0

    	ESI type 0

    .. data:: legacy = 128

    	Legacy ESI type

    .. data:: override = 129

    	Override ESI type

    """

    type0 = 0

    legacy = 128

    override = 129


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['EthernetSegmentIdentifierEnum']


class FlowLabelLoadBalanceEnum(Enum):
    """
    FlowLabelLoadBalanceEnum

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

    off = 0

    receive = 1

    transmit = 2

    both = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['FlowLabelLoadBalanceEnum']


class FlowLabelTlvCodeEnum(Enum):
    """
    FlowLabelTlvCodeEnum

    Flow label tlv code

    .. data:: Y_17 = 4

    	Set Flow Label Legacy TLV code (DEPRECATED)

    .. data:: disable = 8

    	Disable Sending Flow Label Legacy TLV

    """

    Y_17 = 4

    disable = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['FlowLabelTlvCodeEnum']


class InterfaceProfileEnum(Enum):
    """
    InterfaceProfileEnum

    Interface profile

    .. data:: snoop = 1

    	Set the snooping

    .. data:: dhcp_protocol = 2

    	disable DHCP protocol

    """

    snoop = 1

    dhcp_protocol = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['InterfaceProfileEnum']


class InterfaceTrafficFloodEnum(Enum):
    """
    InterfaceTrafficFloodEnum

    Interface traffic flood

    .. data:: traffic_flooding = 0

    	Traffic flooding

    .. data:: enable_flooding = 1

    	Enable Flooding

    .. data:: disable_flooding = 2

    	Disable flooding

    """

    traffic_flooding = 0

    enable_flooding = 1

    disable_flooding = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['InterfaceTrafficFloodEnum']


class InterworkingEnum(Enum):
    """
    InterworkingEnum

    Interworking

    .. data:: ethernet = 1

    	Ethernet interworking

    .. data:: ipv4 = 3

    	IPv4 interworking

    """

    ethernet = 1

    ipv4 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['InterworkingEnum']


class L2EncapsulationEnum(Enum):
    """
    L2EncapsulationEnum

    L2 encapsulation

    .. data:: vlan = 4

    	Vlan tagged mode

    .. data:: ethernet = 5

    	Ethernet port mode

    """

    vlan = 4

    ethernet = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2EncapsulationEnum']


class L2TpCookieSizeEnum(Enum):
    """
    L2TpCookieSizeEnum

    L2tp cookie size

    .. data:: zero = 0

    	Cookie size is zero bytes

    .. data:: four = 4

    	Cookie size is four bytes

    .. data:: eight = 8

    	Cookie size is eight bytes

    """

    zero = 0

    four = 4

    eight = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2TpCookieSizeEnum']


class L2TpSignalingProtocolEnum(Enum):
    """
    L2TpSignalingProtocolEnum

    L2tp signaling protocol

    .. data:: none = 1

    	No signaling

    .. data:: l2tpv3 = 2

    	L2TPv3

    """

    none = 1

    l2tpv3 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2TpSignalingProtocolEnum']


class L2Tpv3SequencingEnum(Enum):
    """
    L2Tpv3SequencingEnum

    L2tpv3 sequencing

    .. data:: off = 0

    	Sequencing is off

    .. data:: both = 4

    	Sequencing on both transmit and receive side

    """

    off = 0

    both = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2Tpv3SequencingEnum']


class L2VpnCapabilityModeEnum(Enum):
    """
    L2VpnCapabilityModeEnum

    L2vpn capability mode

    .. data:: high_mode = 1

    	Compute global capability as the highest node

    	capability

    .. data:: single_mode = 2

    	Disable global capability re-computation

    """

    high_mode = 1

    single_mode = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2VpnCapabilityModeEnum']


class L2VpnLoggingEnum(Enum):
    """
    L2VpnLoggingEnum

    L2vpn logging

    .. data:: enable = 1

    	enable logging

    .. data:: disable = 2

    	disable logging

    """

    enable = 1

    disable = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2VpnLoggingEnum']


class L2VpnVerificationEnum(Enum):
    """
    L2VpnVerificationEnum

    L2vpn verification

    .. data:: enable = 1

    	enable verification

    .. data:: disable = 2

    	disable verification

    """

    enable = 1

    disable = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2VpnVerificationEnum']


class LdpVplsIdEnum(Enum):
    """
    LdpVplsIdEnum

    Ldp vpls id

    .. data:: two_byte_as = 10

    	VPLS-ID in 2 byte AS:nn format

    .. data:: ipv4_address = 266

    	VPLS-ID in IPv4 IP:nn format

    """

    two_byte_as = 10

    ipv4_address = 266


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['LdpVplsIdEnum']


class LoadBalanceEnum(Enum):
    """
    LoadBalanceEnum

    Load balance

    .. data:: source_dest_mac = 1

    	Source and Destination MAC hashing

    .. data:: source_dest_ip = 2

    	Source and Destination IP hashing

    .. data:: pseudowire_label = 4

    	PW Label hashing

    """

    source_dest_mac = 1

    source_dest_ip = 2

    pseudowire_label = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['LoadBalanceEnum']


class MacAgingEnum(Enum):
    """
    MacAgingEnum

    Mac aging

    .. data:: absolute = 1

    	Absolute aging type

    .. data:: inactivity = 2

    	Inactivity aging type

    """

    absolute = 1

    inactivity = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MacAgingEnum']


class MacLearnEnum(Enum):
    """
    MacLearnEnum

    Mac learn

    .. data:: default_learning = 0

    	Mac Learning

    .. data:: enable_learning = 1

    	Enable Learning

    .. data:: disable_learning = 2

    	Disable Learning

    """

    default_learning = 0

    enable_learning = 1

    disable_learning = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MacLearnEnum']


class MacLimitActionEnum(Enum):
    """
    MacLimitActionEnum

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

    none = 0

    flood = 1

    no_flood = 2

    shutdown = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MacLimitActionEnum']


class MacNotificationEnum(Enum):
    """
    MacNotificationEnum

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

    no_notif = 0

    syslog = 1

    trap = 2

    syslog_snmp = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MacNotificationEnum']


class MacSecureActionEnum(Enum):
    """
    MacSecureActionEnum

    Mac secure action

    .. data:: restrict = 1

    	MAC Secure Action Restrict

    .. data:: none = 2

    	No Action

    .. data:: shutdown = 3

    	MAC Secure Action Shutdown

    """

    restrict = 1

    none = 2

    shutdown = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MacSecureActionEnum']


class MacWithdrawBehaviorEnum(Enum):
    """
    MacWithdrawBehaviorEnum

    Mac withdraw behavior

    .. data:: legacy = 1

    	MAC Withdrawal sent on state-down (legacy)

    .. data:: optimized = 2

    	Optimized MAC Withdrawal

    """

    legacy = 1

    optimized = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MacWithdrawBehaviorEnum']


class MplsSequencingEnum(Enum):
    """
    MplsSequencingEnum

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

    off = 0

    transmit = 1

    receive = 2

    both = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MplsSequencingEnum']


class MplsSignalingProtocolEnum(Enum):
    """
    MplsSignalingProtocolEnum

    Mpls signaling protocol

    .. data:: none = 1

    	No signaling

    .. data:: ldp = 4

    	LDP

    """

    none = 1

    ldp = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MplsSignalingProtocolEnum']


class PortDownFlushEnum(Enum):
    """
    PortDownFlushEnum

    Port down flush

    .. data:: port_down_flush = 0

    	MAC Port Down Flush

    .. data:: enable_port_down_flush = 1

    	Enable Port Down Flush

    .. data:: disable_port_down_flush = 2

    	Disable Port Down Flush

    """

    port_down_flush = 0

    enable_port_down_flush = 1

    disable_port_down_flush = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['PortDownFlushEnum']


class PreferredPathEnum(Enum):
    """
    PreferredPathEnum

    Preferred path

    .. data:: te_tunnel = 2

    	TE Tunnel

    .. data:: ip_tunnel = 3

    	IP Tunnel

    .. data:: tp_tunnel = 4

    	TP Tunnel

    """

    te_tunnel = 2

    ip_tunnel = 3

    tp_tunnel = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['PreferredPathEnum']


class PwSwitchingPointTlvEnum(Enum):
    """
    PwSwitchingPointTlvEnum

    Pw switching point tlv

    .. data:: hide = 2

    	Hide TLV

    """

    hide = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['PwSwitchingPointTlvEnum']


class RplRoleEnum(Enum):
    """
    RplRoleEnum

    Rpl role

    .. data:: owner = 1

    	ERP RPL owner

    .. data:: neighbor = 2

    	ERP RPL neighbor

    .. data:: next_neighbor = 3

    	ERP RPL next neighbor

    """

    owner = 1

    neighbor = 2

    next_neighbor = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['RplRoleEnum']


class StormControlEnum(Enum):
    """
    StormControlEnum

    Storm control

    .. data:: unicast = 1

    	Unknown-unicast Storm Control

    .. data:: multicast = 2

    	Multicast Storm Control

    .. data:: broadcast = 4

    	Broadcast Storm Control

    """

    unicast = 1

    multicast = 2

    broadcast = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['StormControlEnum']


class TransportModeEnum(Enum):
    """
    TransportModeEnum

    Transport mode

    .. data:: ethernet = 1

    	Ethernet port mode

    .. data:: vlan = 2

    	Vlan tagged mode

    .. data:: vlan_passthrough = 3

    	Vlan tagged passthrough mode

    """

    ethernet = 1

    vlan = 2

    vlan_passthrough = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['TransportModeEnum']


class TypeOfServiceModeEnum(Enum):
    """
    TypeOfServiceModeEnum

    Type of service mode

    .. data:: none = 0

    	Do not reflect the type of service

    .. data:: reflect = 1

    	Reflect the type of service

    """

    none = 0

    reflect = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['TypeOfServiceModeEnum']


class VccvVerificationEnum(Enum):
    """
    VccvVerificationEnum

    Vccv verification

    .. data:: none = 0

    	No connectivity verification over VCCV

    .. data:: lsp_ping = 2

    	LSP Ping over VCCV

    """

    none = 0

    lsp_ping = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['VccvVerificationEnum']



class L2Vpn(object):
    """
    L2VPN configuration
    
    .. attribute:: auto_discovery
    
    	Global auto\-discovery attributes
    	**type**\:   :py:class:`AutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.AutoDiscovery>`
    
    .. attribute:: capability
    
    	L2VPN Capability Mode
    	**type**\:   :py:class:`L2VpnCapabilityModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnCapabilityModeEnum>`
    
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
    	**type**\:   :py:class:`LoadBalanceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.LoadBalanceEnum>`
    
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
    _revision = '2015-11-09'

    def __init__(self):
        self.auto_discovery = L2Vpn.AutoDiscovery()
        self.auto_discovery.parent = self
        self.capability = None
        self.database = L2Vpn.Database()
        self.database.parent = self
        self.enable = None
        self.l2vpn_router_id = None
        self.load_balance = None
        self.mspw_description = None
        self.mtu_mismatch_ignore = None
        self.neighbor = L2Vpn.Neighbor()
        self.neighbor.parent = self
        self.nsr = None
        self.pbb = L2Vpn.Pbb()
        self.pbb.parent = self
        self.pw_grouping = None
        self.pw_routing = L2Vpn.PwRouting()
        self.pw_routing.parent = self
        self.pw_status_disable = None
        self.pwoam_refresh = None
        self.snmp = L2Vpn.Snmp()
        self.snmp.parent = self
        self.tcn_propagation = None
        self.utility = L2Vpn.Utility()
        self.utility.parent = self


    class PwRouting(object):
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
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.pw_routing_bgp = L2Vpn.PwRouting.PwRoutingBgp()
            self.pw_routing_bgp.parent = self
            self.pw_routing_global_id = None


        class PwRoutingBgp(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.evpn_route_distinguisher = L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher()
                self.evpn_route_distinguisher.parent = self


            class EvpnRouteDistinguisher(object):
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
                	**type**\:   :py:class:`BgpRouteDistinguisherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisherEnum>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.addr_index = None
                    self.address = None
                    self.as_ = None
                    self.as_index = None
                    self.type = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:pw-routing/Cisco-IOS-XR-l2vpn-cfg:pw-routing-bgp/Cisco-IOS-XR-l2vpn-cfg:evpn-route-distinguisher'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.addr_index is not None:
                        return True

                    if self.address is not None:
                        return True

                    if self.as_ is not None:
                        return True

                    if self.as_index is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:pw-routing/Cisco-IOS-XR-l2vpn-cfg:pw-routing-bgp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.evpn_route_distinguisher is not None and self.evpn_route_distinguisher._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2Vpn.PwRouting.PwRoutingBgp']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:pw-routing'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.pw_routing_bgp is not None and self.pw_routing_bgp._has_data():
                return True

            if self.pw_routing_global_id is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2Vpn.PwRouting']['meta_info']


    class Neighbor(object):
        """
        L2VPN neighbor submode
        
        .. attribute:: ldp_flap
        
        	Enable targetted LDP session flap action
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ldp_flap = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:neighbor'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.ldp_flap is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2Vpn.Neighbor']['meta_info']


    class Database(object):
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
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.bridge_domain_groups = L2Vpn.Database.BridgeDomainGroups()
            self.bridge_domain_groups.parent = self
            self.flexible_xconnect_service_table = L2Vpn.Database.FlexibleXconnectServiceTable()
            self.flexible_xconnect_service_table.parent = self
            self.g8032_rings = L2Vpn.Database.G8032Rings()
            self.g8032_rings.parent = self
            self.pseudowire_classes = L2Vpn.Database.PseudowireClasses()
            self.pseudowire_classes.parent = self
            self.redundancy = L2Vpn.Database.Redundancy()
            self.redundancy.parent = self
            self.xconnect_groups = L2Vpn.Database.XconnectGroups()
            self.xconnect_groups.parent = self


        class G8032Rings(object):
            """
            List of G8032 Ring
            
            .. attribute:: g8032_ring
            
            	G8032 Ring
            	**type**\: list of    :py:class:`G8032Ring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.g8032_ring = YList()
                self.g8032_ring.parent = self
                self.g8032_ring.name = 'g8032_ring'


            class G8032Ring(object):
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.g8032_ring_name = None
                    self.erp_instances = L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances()
                    self.erp_instances.parent = self
                    self.erp_port0s = L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S()
                    self.erp_port0s.parent = self
                    self.erp_port1s = L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S()
                    self.erp_port1s.parent = self
                    self.erp_provider_bridge = None
                    self.exclusion_list = None
                    self.open_ring = None


                class ErpPort0S(object):
                    """
                    Ethernet ring protection port0
                    
                    .. attribute:: erp_port0
                    
                    	Configure ERP main port0
                    	**type**\: list of    :py:class:`ErpPort0 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.erp_port0 = YList()
                        self.erp_port0.parent = self
                        self.erp_port0.name = 'erp_port0'


                    class ErpPort0(object):
                        """
                        Configure ERP main port0
                        
                        .. attribute:: interface_name  <key>
                        
                        	Port0 interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: monitor
                        
                        	Ethernet ring protection port0 monitor
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.monitor = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:erp-port0[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.monitor is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:erp-port0s'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.erp_port0 is not None:
                            for child_ref in self.erp_port0:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S']['meta_info']


                class ErpInstances(object):
                    """
                    List of ethernet ring protection instance
                    
                    .. attribute:: erp_instance
                    
                    	Ethernet ring protection instance
                    	**type**\: list of    :py:class:`ErpInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.erp_instance = YList()
                        self.erp_instance.parent = self
                        self.erp_instance.name = 'erp_instance'


                    class ErpInstance(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.erp_instance_id = None
                            self.aps = L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps()
                            self.aps.parent = self
                            self.description = None
                            self.inclusion_list = None
                            self.profile = None
                            self.rpl = L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl()
                            self.rpl.parent = self


                        class Rpl(object):
                            """
                            Ring protection link
                            
                            .. attribute:: port
                            
                            	ERP main port number
                            	**type**\:   :py:class:`ErpPort1Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.ErpPort1Enum>`
                            
                            .. attribute:: role
                            
                            	RPL role
                            	**type**\:   :py:class:`RplRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.RplRoleEnum>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.port = None
                                self.role = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:rpl'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.port is not None:
                                    return True

                                if self.role is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl']['meta_info']


                        class Aps(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.level = None
                                self.port0 = None
                                self.port1 = L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1()
                                self.port1.parent = self


                            class Port1(object):
                                """
                                APS channel for ERP port1
                                
                                .. attribute:: aps_channel
                                
                                	Port1 APS channel in the format of InterfaceName, BDName or XconnectName
                                	**type**\:  str
                                
                                .. attribute:: aps_type
                                
                                	Port1 APS type
                                	**type**\:   :py:class:`ErpapsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.ErpapsEnum>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aps_channel = None
                                    self.aps_type = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:port1'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.aps_channel is not None:
                                        return True

                                    if self.aps_type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:aps'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.level is not None:
                                    return True

                                if self.port0 is not None:
                                    return True

                                if self.port1 is not None and self.port1._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.erp_instance_id is None:
                                raise YPYModelError('Key property erp_instance_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:erp-instance[Cisco-IOS-XR-l2vpn-cfg:erp-instance-id = ' + str(self.erp_instance_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.erp_instance_id is not None:
                                return True

                            if self.aps is not None and self.aps._has_data():
                                return True

                            if self.description is not None:
                                return True

                            if self.inclusion_list is not None:
                                return True

                            if self.profile is not None:
                                return True

                            if self.rpl is not None and self.rpl._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:erp-instances'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.erp_instance is not None:
                            for child_ref in self.erp_instance:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances']['meta_info']


                class ErpPort1S(object):
                    """
                    Ethernet ring protection port0
                    
                    .. attribute:: erp_port1
                    
                    	Ethernet ring protection port1
                    	**type**\: list of    :py:class:`ErpPort1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.erp_port1 = YList()
                        self.erp_port1.parent = self
                        self.erp_port1.name = 'erp_port1'


                    class ErpPort1(object):
                        """
                        Ethernet ring protection port1
                        
                        .. attribute:: erp_port_type  <key>
                        
                        	Port1 type
                        	**type**\:   :py:class:`ErpPortEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.ErpPortEnum>`
                        
                        .. attribute:: interface
                        
                        	interface
                        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface>`
                        
                        .. attribute:: none_or_virtual
                        
                        	none or virtual
                        	**type**\:   :py:class:`NoneOrVirtual <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.erp_port_type = None
                            self.interface = YList()
                            self.interface.parent = self
                            self.interface.name = 'interface'
                            self.none_or_virtual = None


                        class NoneOrVirtual(object):
                            """
                            none or virtual
                            
                            .. attribute:: monitor
                            
                            	Ethernet ring protection port1 monitor
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.monitor = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:none-or-virtual'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self._is_presence:
                                    return True
                                if self.monitor is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual']['meta_info']


                        class Interface(object):
                            """
                            interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	Port1 interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: monitor
                            
                            	Ethernet ring protection port1 monitor
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None
                                self.monitor = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYModelError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.interface_name is not None:
                                    return True

                                if self.monitor is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.erp_port_type is None:
                                raise YPYModelError('Key property erp_port_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:erp-port1[Cisco-IOS-XR-l2vpn-cfg:erp-port-type = ' + str(self.erp_port_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.erp_port_type is not None:
                                return True

                            if self.interface is not None:
                                for child_ref in self.interface:
                                    if child_ref._has_data():
                                        return True

                            if self.none_or_virtual is not None and self.none_or_virtual._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:erp-port1s'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.erp_port1 is not None:
                            for child_ref in self.erp_port1:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S']['meta_info']

                @property
                def _common_path(self):
                    if self.g8032_ring_name is None:
                        raise YPYModelError('Key property g8032_ring_name is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:g8032-rings/Cisco-IOS-XR-l2vpn-cfg:g8032-ring[Cisco-IOS-XR-l2vpn-cfg:g8032-ring-name = ' + str(self.g8032_ring_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.g8032_ring_name is not None:
                        return True

                    if self.erp_instances is not None and self.erp_instances._has_data():
                        return True

                    if self.erp_port0s is not None and self.erp_port0s._has_data():
                        return True

                    if self.erp_port1s is not None and self.erp_port1s._has_data():
                        return True

                    if self.erp_provider_bridge is not None:
                        return True

                    if self.exclusion_list is not None:
                        return True

                    if self.open_ring is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2Vpn.Database.G8032Rings.G8032Ring']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:g8032-rings'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.g8032_ring is not None:
                    for child_ref in self.g8032_ring:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2Vpn.Database.G8032Rings']['meta_info']


        class XconnectGroups(object):
            """
            List of xconnect groups
            
            .. attribute:: xconnect_group
            
            	Xconnect group
            	**type**\: list of    :py:class:`XconnectGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.xconnect_group = YList()
                self.xconnect_group.parent = self
                self.xconnect_group.name = 'xconnect_group'


            class XconnectGroup(object):
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.mp2mp_xconnects = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects()
                    self.mp2mp_xconnects.parent = self
                    self.p2p_xconnects = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects()
                    self.p2p_xconnects.parent = self


                class P2PXconnects(object):
                    """
                    List of point to point xconnects
                    
                    .. attribute:: p2p_xconnect
                    
                    	Point to point xconnect
                    	**type**\: list of    :py:class:`P2PXconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.p2p_xconnect = YList()
                        self.p2p_xconnect.parent = self
                        self.p2p_xconnect.name = 'p2p_xconnect'


                    class P2PXconnect(object):
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
                        	**type**\:   :py:class:`InterworkingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterworkingEnum>`
                        
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.attachment_circuits = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits()
                            self.attachment_circuits.parent = self
                            self.backup_attachment_circuits = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits()
                            self.backup_attachment_circuits.parent = self
                            self.interworking = None
                            self.monitor_sessions = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions()
                            self.monitor_sessions.parent = self
                            self.p2p_description = None
                            self.pseudowire_evpns = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns()
                            self.pseudowire_evpns.parent = self
                            self.pseudowire_routeds = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds()
                            self.pseudowire_routeds.parent = self
                            self.pseudowires = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires()
                            self.pseudowires.parent = self


                        class BackupAttachmentCircuits(object):
                            """
                            List of backup attachment circuits
                            
                            .. attribute:: backup_attachment_circuit
                            
                            	Backup attachment circuit
                            	**type**\: list of    :py:class:`BackupAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.backup_attachment_circuit = YList()
                                self.backup_attachment_circuit.parent = self
                                self.backup_attachment_circuit.name = 'backup_attachment_circuit'


                            class BackupAttachmentCircuit(object):
                                """
                                Backup attachment circuit
                                
                                .. attribute:: interface_name  <key>
                                
                                	Name of the attachment circuit interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYModelError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-attachment-circuit[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.interface_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-attachment-circuits'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.backup_attachment_circuit is not None:
                                    for child_ref in self.backup_attachment_circuit:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits']['meta_info']


                        class PseudowireEvpns(object):
                            """
                            List of EVPN Services
                            
                            .. attribute:: pseudowire_evpn
                            
                            	EVPN P2P Service Configuration
                            	**type**\: list of    :py:class:`PseudowireEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.pseudowire_evpn = YList()
                                self.pseudowire_evpn.parent = self
                                self.pseudowire_evpn.name = 'pseudowire_evpn'


                            class PseudowireEvpn(object):
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.eviid = None
                                    self.remote_acid = None
                                    self.source_acid = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.eviid is None:
                                        raise YPYModelError('Key property eviid is None')
                                    if self.remote_acid is None:
                                        raise YPYModelError('Key property remote_acid is None')
                                    if self.source_acid is None:
                                        raise YPYModelError('Key property source_acid is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-evpn[Cisco-IOS-XR-l2vpn-cfg:eviid = ' + str(self.eviid) + '][Cisco-IOS-XR-l2vpn-cfg:remote-acid = ' + str(self.remote_acid) + '][Cisco-IOS-XR-l2vpn-cfg:source-acid = ' + str(self.source_acid) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.eviid is not None:
                                        return True

                                    if self.remote_acid is not None:
                                        return True

                                    if self.source_acid is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-evpns'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.pseudowire_evpn is not None:
                                    for child_ref in self.pseudowire_evpn:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns']['meta_info']


                        class Pseudowires(object):
                            """
                            List of pseudowires
                            
                            .. attribute:: pseudowire
                            
                            	Pseudowire configuration
                            	**type**\: list of    :py:class:`Pseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.pseudowire = YList()
                                self.pseudowire.parent = self
                                self.pseudowire.name = 'pseudowire'


                            class Pseudowire(object):
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.pseudowire_id = None
                                    self.neighbor = YList()
                                    self.neighbor.parent = self
                                    self.neighbor.name = 'neighbor'
                                    self.pseudowire_address = YList()
                                    self.pseudowire_address.parent = self
                                    self.pseudowire_address.name = 'pseudowire_address'


                                class Neighbor(object):
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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.neighbor = None
                                        self.backup_pseudowires = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires()
                                        self.backup_pseudowires.parent = self
                                        self.bandwidth = None
                                        self.class_ = None
                                        self.l2tp_static = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic()
                                        self.l2tp_static.parent = self
                                        self.l2tp_static_attributes = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes()
                                        self.l2tp_static_attributes.parent = self
                                        self.mpls_static_labels = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels()
                                        self.mpls_static_labels.parent = self
                                        self.source_address = None
                                        self.tag_impose = None


                                    class MplsStaticLabels(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.local_static_label = None
                                            self.remote_static_label = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mpls-static-labels'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.local_static_label is not None:
                                                return True

                                            if self.remote_static_label is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels']['meta_info']


                                    class BackupPseudowires(object):
                                        """
                                        List of pseudowires
                                        
                                        .. attribute:: backup_pseudowire
                                        
                                        	Backup pseudowire for the cross connect
                                        	**type**\: list of    :py:class:`BackupPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.backup_pseudowire = YList()
                                            self.backup_pseudowire.parent = self
                                            self.backup_pseudowire.name = 'backup_pseudowire'


                                        class BackupPseudowire(object):
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
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.neighbor = None
                                                self.pseudowire_id = None
                                                self.backup_mpls_static_labels = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels()
                                                self.backup_mpls_static_labels.parent = self
                                                self.backup_pw_class = None


                                            class BackupMplsStaticLabels(object):
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
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.local_static_label = None
                                                    self.remote_static_label = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-mpls-static-labels'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if self.local_static_label is not None:
                                                        return True

                                                    if self.remote_static_label is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.neighbor is None:
                                                    raise YPYModelError('Key property neighbor is None')
                                                if self.pseudowire_id is None:
                                                    raise YPYModelError('Key property pseudowire_id is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-pseudowire[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + '][Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.neighbor is not None:
                                                    return True

                                                if self.pseudowire_id is not None:
                                                    return True

                                                if self.backup_mpls_static_labels is not None and self.backup_mpls_static_labels._has_data():
                                                    return True

                                                if self.backup_pw_class is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-pseudowires'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.backup_pseudowire is not None:
                                                for child_ref in self.backup_pseudowire:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires']['meta_info']


                                    class L2TpStaticAttributes(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.l2tp_local_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie()
                                            self.l2tp_local_cookie.parent = self
                                            self.l2tp_local_session_id = None
                                            self.l2tp_remote_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie()
                                            self.l2tp_remote_cookie.parent = self
                                            self.l2tp_remote_session_id = None
                                            self.l2tp_secondary_local_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie()
                                            self.l2tp_secondary_local_cookie.parent = self


                                        class L2TpRemoteCookie(object):
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
                                            	**type**\:   :py:class:`L2TpCookieSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2TpCookieSizeEnum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.higher_value = None
                                                self.lower_value = None
                                                self.size = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-remote-cookie'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.higher_value is not None:
                                                    return True

                                                if self.lower_value is not None:
                                                    return True

                                                if self.size is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie']['meta_info']


                                        class L2TpSecondaryLocalCookie(object):
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
                                            	**type**\:   :py:class:`L2TpCookieSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2TpCookieSizeEnum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.higher_value = None
                                                self.lower_value = None
                                                self.size = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-secondary-local-cookie'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.higher_value is not None:
                                                    return True

                                                if self.lower_value is not None:
                                                    return True

                                                if self.size is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie']['meta_info']


                                        class L2TpLocalCookie(object):
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
                                            	**type**\:   :py:class:`L2TpCookieSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2TpCookieSizeEnum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.higher_value = None
                                                self.lower_value = None
                                                self.size = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-local-cookie'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.higher_value is not None:
                                                    return True

                                                if self.lower_value is not None:
                                                    return True

                                                if self.size is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-static-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.l2tp_local_cookie is not None and self.l2tp_local_cookie._has_data():
                                                return True

                                            if self.l2tp_local_session_id is not None:
                                                return True

                                            if self.l2tp_remote_cookie is not None and self.l2tp_remote_cookie._has_data():
                                                return True

                                            if self.l2tp_remote_session_id is not None:
                                                return True

                                            if self.l2tp_secondary_local_cookie is not None and self.l2tp_secondary_local_cookie._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes']['meta_info']


                                    class L2TpStatic(object):
                                        """
                                        Pseudowire L2TPv3 static configuration
                                        
                                        .. attribute:: enable
                                        
                                        	Enable pseudowire L2TPv3 static configuration
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.enable = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-static'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.enable is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.neighbor is None:
                                            raise YPYModelError('Key property neighbor is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:neighbor[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.neighbor is not None:
                                            return True

                                        if self.backup_pseudowires is not None and self.backup_pseudowires._has_data():
                                            return True

                                        if self.bandwidth is not None:
                                            return True

                                        if self.class_ is not None:
                                            return True

                                        if self.l2tp_static is not None and self.l2tp_static._has_data():
                                            return True

                                        if self.l2tp_static_attributes is not None and self.l2tp_static_attributes._has_data():
                                            return True

                                        if self.mpls_static_labels is not None and self.mpls_static_labels._has_data():
                                            return True

                                        if self.source_address is not None:
                                            return True

                                        if self.tag_impose is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor']['meta_info']


                                class PseudowireAddress(object):
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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.pseudowire_address = None
                                        self.backup_pseudowires = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires()
                                        self.backup_pseudowires.parent = self
                                        self.bandwidth = None
                                        self.class_ = None
                                        self.l2tp_static = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic()
                                        self.l2tp_static.parent = self
                                        self.l2tp_static_attributes = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes()
                                        self.l2tp_static_attributes.parent = self
                                        self.mpls_static_labels = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels()
                                        self.mpls_static_labels.parent = self
                                        self.source_address = None
                                        self.tag_impose = None


                                    class MplsStaticLabels(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.local_static_label = None
                                            self.remote_static_label = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mpls-static-labels'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.local_static_label is not None:
                                                return True

                                            if self.remote_static_label is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels']['meta_info']


                                    class BackupPseudowires(object):
                                        """
                                        List of pseudowires
                                        
                                        .. attribute:: backup_pseudowire
                                        
                                        	Backup pseudowire for the cross connect
                                        	**type**\: list of    :py:class:`BackupPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.backup_pseudowire = YList()
                                            self.backup_pseudowire.parent = self
                                            self.backup_pseudowire.name = 'backup_pseudowire'


                                        class BackupPseudowire(object):
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
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.neighbor = None
                                                self.pseudowire_id = None
                                                self.backup_mpls_static_labels = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels()
                                                self.backup_mpls_static_labels.parent = self
                                                self.backup_pw_class = None


                                            class BackupMplsStaticLabels(object):
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
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.local_static_label = None
                                                    self.remote_static_label = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-mpls-static-labels'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if self.local_static_label is not None:
                                                        return True

                                                    if self.remote_static_label is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.neighbor is None:
                                                    raise YPYModelError('Key property neighbor is None')
                                                if self.pseudowire_id is None:
                                                    raise YPYModelError('Key property pseudowire_id is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-pseudowire[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + '][Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.neighbor is not None:
                                                    return True

                                                if self.pseudowire_id is not None:
                                                    return True

                                                if self.backup_mpls_static_labels is not None and self.backup_mpls_static_labels._has_data():
                                                    return True

                                                if self.backup_pw_class is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-pseudowires'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.backup_pseudowire is not None:
                                                for child_ref in self.backup_pseudowire:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires']['meta_info']


                                    class L2TpStaticAttributes(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.l2tp_local_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie()
                                            self.l2tp_local_cookie.parent = self
                                            self.l2tp_local_session_id = None
                                            self.l2tp_remote_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie()
                                            self.l2tp_remote_cookie.parent = self
                                            self.l2tp_remote_session_id = None
                                            self.l2tp_secondary_local_cookie = L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie()
                                            self.l2tp_secondary_local_cookie.parent = self


                                        class L2TpRemoteCookie(object):
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
                                            	**type**\:   :py:class:`L2TpCookieSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2TpCookieSizeEnum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.higher_value = None
                                                self.lower_value = None
                                                self.size = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-remote-cookie'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.higher_value is not None:
                                                    return True

                                                if self.lower_value is not None:
                                                    return True

                                                if self.size is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie']['meta_info']


                                        class L2TpSecondaryLocalCookie(object):
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
                                            	**type**\:   :py:class:`L2TpCookieSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2TpCookieSizeEnum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.higher_value = None
                                                self.lower_value = None
                                                self.size = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-secondary-local-cookie'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.higher_value is not None:
                                                    return True

                                                if self.lower_value is not None:
                                                    return True

                                                if self.size is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie']['meta_info']


                                        class L2TpLocalCookie(object):
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
                                            	**type**\:   :py:class:`L2TpCookieSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2TpCookieSizeEnum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.higher_value = None
                                                self.lower_value = None
                                                self.size = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-local-cookie'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.higher_value is not None:
                                                    return True

                                                if self.lower_value is not None:
                                                    return True

                                                if self.size is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-static-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.l2tp_local_cookie is not None and self.l2tp_local_cookie._has_data():
                                                return True

                                            if self.l2tp_local_session_id is not None:
                                                return True

                                            if self.l2tp_remote_cookie is not None and self.l2tp_remote_cookie._has_data():
                                                return True

                                            if self.l2tp_remote_session_id is not None:
                                                return True

                                            if self.l2tp_secondary_local_cookie is not None and self.l2tp_secondary_local_cookie._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes']['meta_info']


                                    class L2TpStatic(object):
                                        """
                                        Pseudowire L2TPv3 static configuration
                                        
                                        .. attribute:: enable
                                        
                                        	Enable pseudowire L2TPv3 static configuration
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.enable = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-static'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.enable is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.pseudowire_address is None:
                                            raise YPYModelError('Key property pseudowire_address is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-address[Cisco-IOS-XR-l2vpn-cfg:pseudowire-address = ' + str(self.pseudowire_address) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.pseudowire_address is not None:
                                            return True

                                        if self.backup_pseudowires is not None and self.backup_pseudowires._has_data():
                                            return True

                                        if self.bandwidth is not None:
                                            return True

                                        if self.class_ is not None:
                                            return True

                                        if self.l2tp_static is not None and self.l2tp_static._has_data():
                                            return True

                                        if self.l2tp_static_attributes is not None and self.l2tp_static_attributes._has_data():
                                            return True

                                        if self.mpls_static_labels is not None and self.mpls_static_labels._has_data():
                                            return True

                                        if self.source_address is not None:
                                            return True

                                        if self.tag_impose is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.pseudowire_id is None:
                                        raise YPYModelError('Key property pseudowire_id is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire[Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.pseudowire_id is not None:
                                        return True

                                    if self.neighbor is not None:
                                        for child_ref in self.neighbor:
                                            if child_ref._has_data():
                                                return True

                                    if self.pseudowire_address is not None:
                                        for child_ref in self.pseudowire_address:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowires'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.pseudowire is not None:
                                    for child_ref in self.pseudowire:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires']['meta_info']


                        class MonitorSessions(object):
                            """
                            List of Monitor session segments
                            
                            .. attribute:: monitor_session
                            
                            	Monitor session segment
                            	**type**\: list of    :py:class:`MonitorSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.monitor_session = YList()
                                self.monitor_session.parent = self
                                self.monitor_session.name = 'monitor_session'


                            class MonitorSession(object):
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.name = None
                                    self.enable = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.name is None:
                                        raise YPYModelError('Key property name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:monitor-session[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.name is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:monitor-sessions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.monitor_session is not None:
                                    for child_ref in self.monitor_session:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions']['meta_info']


                        class PseudowireRouteds(object):
                            """
                            List of pseudowire\-routed
                            
                            .. attribute:: pseudowire_routed
                            
                            	Pseudowire configuration
                            	**type**\: list of    :py:class:`PseudowireRouted <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.pseudowire_routed = YList()
                                self.pseudowire_routed.parent = self
                                self.pseudowire_routed.name = 'pseudowire_routed'


                            class PseudowireRouted(object):
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.global_id = None
                                    self.prefix = None
                                    self.acid = None
                                    self.sacid = None
                                    self.class_ = None
                                    self.tag_impose = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.global_id is None:
                                        raise YPYModelError('Key property global_id is None')
                                    if self.prefix is None:
                                        raise YPYModelError('Key property prefix is None')
                                    if self.acid is None:
                                        raise YPYModelError('Key property acid is None')
                                    if self.sacid is None:
                                        raise YPYModelError('Key property sacid is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-routed[Cisco-IOS-XR-l2vpn-cfg:global-id = ' + str(self.global_id) + '][Cisco-IOS-XR-l2vpn-cfg:prefix = ' + str(self.prefix) + '][Cisco-IOS-XR-l2vpn-cfg:acid = ' + str(self.acid) + '][Cisco-IOS-XR-l2vpn-cfg:sacid = ' + str(self.sacid) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.global_id is not None:
                                        return True

                                    if self.prefix is not None:
                                        return True

                                    if self.acid is not None:
                                        return True

                                    if self.sacid is not None:
                                        return True

                                    if self.class_ is not None:
                                        return True

                                    if self.tag_impose is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-routeds'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.pseudowire_routed is not None:
                                    for child_ref in self.pseudowire_routed:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds']['meta_info']


                        class AttachmentCircuits(object):
                            """
                            List of attachment circuits
                            
                            .. attribute:: attachment_circuit
                            
                            	Attachment circuit interface
                            	**type**\: list of    :py:class:`AttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.attachment_circuit = YList()
                                self.attachment_circuit.parent = self
                                self.attachment_circuit.name = 'attachment_circuit'


                            class AttachmentCircuit(object):
                                """
                                Attachment circuit interface
                                
                                .. attribute:: name  <key>
                                
                                	Name of the attachment circuit interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: enable
                                
                                	Enable attachment circuit interface
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.name = None
                                    self.enable = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.name is None:
                                        raise YPYModelError('Key property name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:attachment-circuit[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.name is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:attachment-circuits'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.attachment_circuit is not None:
                                    for child_ref in self.attachment_circuit:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:p2p-xconnect[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            if self.attachment_circuits is not None and self.attachment_circuits._has_data():
                                return True

                            if self.backup_attachment_circuits is not None and self.backup_attachment_circuits._has_data():
                                return True

                            if self.interworking is not None:
                                return True

                            if self.monitor_sessions is not None and self.monitor_sessions._has_data():
                                return True

                            if self.p2p_description is not None:
                                return True

                            if self.pseudowire_evpns is not None and self.pseudowire_evpns._has_data():
                                return True

                            if self.pseudowire_routeds is not None and self.pseudowire_routeds._has_data():
                                return True

                            if self.pseudowires is not None and self.pseudowires._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:p2p-xconnects'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.p2p_xconnect is not None:
                            for child_ref in self.p2p_xconnect:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects']['meta_info']


                class Mp2MpXconnects(object):
                    """
                    List of multi point to multi point xconnects
                    
                    .. attribute:: mp2mp_xconnect
                    
                    	Multi point to multi point xconnect
                    	**type**\: list of    :py:class:`Mp2MpXconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mp2mp_xconnect = YList()
                        self.mp2mp_xconnect.parent = self
                        self.mp2mp_xconnect.name = 'mp2mp_xconnect'


                    class Mp2MpXconnect(object):
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
                        	**type**\:   :py:class:`InterworkingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterworkingEnum>`
                        
                        .. attribute:: mp2mp_shutdown
                        
                        	shutdown this MP2MP VPWS instance
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: mp2mpl2_encapsulation
                        
                        	Configure Layer 2 Encapsulation
                        	**type**\:   :py:class:`L2EncapsulationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2EncapsulationEnum>`
                        
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.mp2mp_auto_discovery = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery()
                            self.mp2mp_auto_discovery.parent = self
                            self.mp2mp_control_word = None
                            self.mp2mp_interworking = None
                            self.mp2mp_shutdown = None
                            self.mp2mpl2_encapsulation = None
                            self.mp2mpmtu = None
                            self.mp2mpvpn_id = None


                        class Mp2MpAutoDiscovery(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.mp2mp_route_policy = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy()
                                self.mp2mp_route_policy.parent = self
                                self.mp2mp_route_targets = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets()
                                self.mp2mp_route_targets.parent = self
                                self.mp2mp_signaling_protocol = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol()
                                self.mp2mp_signaling_protocol.parent = self
                                self.route_distinguisher = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher()
                                self.route_distinguisher.parent = self


                            class RouteDistinguisher(object):
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
                                	**type**\:   :py:class:`BgpRouteDistinguisherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisherEnum>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.addr_index = None
                                    self.address = None
                                    self.as_ = None
                                    self.as_index = None
                                    self.type = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:route-distinguisher'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.addr_index is not None:
                                        return True

                                    if self.address is not None:
                                        return True

                                    if self.as_ is not None:
                                        return True

                                    if self.as_index is not None:
                                        return True

                                    if self.type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher']['meta_info']


                            class Mp2MpRoutePolicy(object):
                                """
                                Route policy
                                
                                .. attribute:: export
                                
                                	Export route policy
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.export = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-route-policy'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.export is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy']['meta_info']


                            class Mp2MpRouteTargets(object):
                                """
                                Route Target
                                
                                .. attribute:: mp2mp_route_target
                                
                                	Name of the Route Target
                                	**type**\: list of    :py:class:`Mp2MpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mp2mp_route_target = YList()
                                    self.mp2mp_route_target.parent = self
                                    self.mp2mp_route_target.name = 'mp2mp_route_target'


                                class Mp2MpRouteTarget(object):
                                    """
                                    Name of the Route Target
                                    
                                    .. attribute:: role  <key>
                                    
                                    	Role of the router target type
                                    	**type**\:   :py:class:`BgpRouteTargetRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRoleEnum>`
                                    
                                    .. attribute:: format  <key>
                                    
                                    	Format of the route target
                                    	**type**\:   :py:class:`BgpRouteTargetFormatEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormatEnum>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	ipv4 address
                                    	**type**\: list of    :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address>`
                                    
                                    .. attribute:: two_byte_as_or_four_byte_as
                                    
                                    	two byte as or four byte as
                                    	**type**\: list of    :py:class:`TwoByteAsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.role = None
                                        self.format = None
                                        self.ipv4_address = YList()
                                        self.ipv4_address.parent = self
                                        self.ipv4_address.name = 'ipv4_address'
                                        self.two_byte_as_or_four_byte_as = YList()
                                        self.two_byte_as_or_four_byte_as.parent = self
                                        self.two_byte_as_or_four_byte_as.name = 'two_byte_as_or_four_byte_as'


                                    class TwoByteAsOrFourByteAs(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.as_ = None
                                            self.as_index = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.as_ is None:
                                                raise YPYModelError('Key property as_ is None')
                                            if self.as_index is None:
                                                raise YPYModelError('Key property as_index is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:two-byte-as-or-four-byte-as[Cisco-IOS-XR-l2vpn-cfg:as = ' + str(self.as_) + '][Cisco-IOS-XR-l2vpn-cfg:as-index = ' + str(self.as_index) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.as_ is not None:
                                                return True

                                            if self.as_index is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs']['meta_info']


                                    class Ipv4Address(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.address = None
                                            self.addr_index = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.address is None:
                                                raise YPYModelError('Key property address is None')
                                            if self.addr_index is None:
                                                raise YPYModelError('Key property addr_index is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ipv4-address[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-l2vpn-cfg:addr-index = ' + str(self.addr_index) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.address is not None:
                                                return True

                                            if self.addr_index is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.role is None:
                                            raise YPYModelError('Key property role is None')
                                        if self.format is None:
                                            raise YPYModelError('Key property format is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-route-target[Cisco-IOS-XR-l2vpn-cfg:role = ' + str(self.role) + '][Cisco-IOS-XR-l2vpn-cfg:format = ' + str(self.format) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.role is not None:
                                            return True

                                        if self.format is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            for child_ref in self.ipv4_address:
                                                if child_ref._has_data():
                                                    return True

                                        if self.two_byte_as_or_four_byte_as is not None:
                                            for child_ref in self.two_byte_as_or_four_byte_as:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-route-targets'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.mp2mp_route_target is not None:
                                        for child_ref in self.mp2mp_route_target:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets']['meta_info']


                            class Mp2MpSignalingProtocol(object):
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ce_range = None
                                    self.ceids = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids()
                                    self.ceids.parent = self
                                    self.enable = None
                                    self.flow_label_load_balance = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance()
                                    self.flow_label_load_balance.parent = self


                                class FlowLabelLoadBalance(object):
                                    """
                                    Enable Flow Label based load balancing
                                    
                                    .. attribute:: flow_label
                                    
                                    	Flow Label load balance type
                                    	**type**\:   :py:class:`FlowLabelLoadBalanceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalanceEnum>`
                                    
                                    .. attribute:: static
                                    
                                    	Static Flow Label
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.flow_label = None
                                        self.static = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:flow-label-load-balance'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.flow_label is not None:
                                            return True

                                        if self.static is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance']['meta_info']


                                class Ceids(object):
                                    """
                                    Local Customer Edge Identifier Table
                                    
                                    .. attribute:: ceid
                                    
                                    	Local Customer Edge Identifier 
                                    	**type**\: list of    :py:class:`Ceid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.ceid = YList()
                                        self.ceid.parent = self
                                        self.ceid.name = 'ceid'


                                    class Ceid(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.ce_id = None
                                            self.remote_ceid_attachment_circuits = L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits()
                                            self.remote_ceid_attachment_circuits.parent = self


                                        class RemoteCeidAttachmentCircuits(object):
                                            """
                                            AC And Remote Customer Edge Identifier
                                            Table
                                            
                                            .. attribute:: remote_ceid_attachment_circuit
                                            
                                            	AC And Remote Customer Edge Identifier
                                            	**type**\: list of    :py:class:`RemoteCeidAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.remote_ceid_attachment_circuit = YList()
                                                self.remote_ceid_attachment_circuit.parent = self
                                                self.remote_ceid_attachment_circuit.name = 'remote_ceid_attachment_circuit'


                                            class RemoteCeidAttachmentCircuit(object):
                                                """
                                                AC And Remote Customer Edge Identifier
                                                
                                                .. attribute:: name  <key>
                                                
                                                	The name of the Attachment Circuit
                                                	**type**\:  str
                                                
                                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                                
                                                .. attribute:: remote_ce_id  <key>
                                                
                                                	Remote Customer Edge Identifier
                                                	**type**\:  int
                                                
                                                	**range:** 1..16384
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.name = None
                                                    self.remote_ce_id = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.name is None:
                                                        raise YPYModelError('Key property name is None')
                                                    if self.remote_ce_id is None:
                                                        raise YPYModelError('Key property remote_ce_id is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:remote-ceid-attachment-circuit[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + '][Cisco-IOS-XR-l2vpn-cfg:remote-ce-id = ' + str(self.remote_ce_id) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if self.name is not None:
                                                        return True

                                                    if self.remote_ce_id is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:remote-ceid-attachment-circuits'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.remote_ceid_attachment_circuit is not None:
                                                    for child_ref in self.remote_ceid_attachment_circuit:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.ce_id is None:
                                                raise YPYModelError('Key property ce_id is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ceid[Cisco-IOS-XR-l2vpn-cfg:ce-id = ' + str(self.ce_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.ce_id is not None:
                                                return True

                                            if self.remote_ceid_attachment_circuits is not None and self.remote_ceid_attachment_circuits._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ceids'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.ceid is not None:
                                            for child_ref in self.ceid:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-signaling-protocol'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.ce_range is not None:
                                        return True

                                    if self.ceids is not None and self.ceids._has_data():
                                        return True

                                    if self.enable is not None:
                                        return True

                                    if self.flow_label_load_balance is not None and self.flow_label_load_balance._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-auto-discovery'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.mp2mp_route_policy is not None and self.mp2mp_route_policy._has_data():
                                    return True

                                if self.mp2mp_route_targets is not None and self.mp2mp_route_targets._has_data():
                                    return True

                                if self.mp2mp_signaling_protocol is not None and self.mp2mp_signaling_protocol._has_data():
                                    return True

                                if self.route_distinguisher is not None and self.route_distinguisher._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-xconnect[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            if self.mp2mp_auto_discovery is not None and self.mp2mp_auto_discovery._has_data():
                                return True

                            if self.mp2mp_control_word is not None:
                                return True

                            if self.mp2mp_interworking is not None:
                                return True

                            if self.mp2mp_shutdown is not None:
                                return True

                            if self.mp2mpl2_encapsulation is not None:
                                return True

                            if self.mp2mpmtu is not None:
                                return True

                            if self.mp2mpvpn_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-xconnects'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.mp2mp_xconnect is not None:
                            for child_ref in self.mp2mp_xconnect:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:xconnect-groups/Cisco-IOS-XR-l2vpn-cfg:xconnect-group[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.mp2mp_xconnects is not None and self.mp2mp_xconnects._has_data():
                        return True

                    if self.p2p_xconnects is not None and self.p2p_xconnects._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:xconnect-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.xconnect_group is not None:
                    for child_ref in self.xconnect_group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2Vpn.Database.XconnectGroups']['meta_info']


        class BridgeDomainGroups(object):
            """
            List of bridge  groups
            
            .. attribute:: bridge_domain_group
            
            	Bridge group
            	**type**\: list of    :py:class:`BridgeDomainGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bridge_domain_group = YList()
                self.bridge_domain_group.parent = self
                self.bridge_domain_group.name = 'bridge_domain_group'


            class BridgeDomainGroup(object):
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.bridge_domains = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains()
                    self.bridge_domains.parent = self


                class BridgeDomains(object):
                    """
                    List of Bridge Domain
                    
                    .. attribute:: bridge_domain
                    
                    	bridge domain
                    	**type**\: list of    :py:class:`BridgeDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bridge_domain = YList()
                        self.bridge_domain.parent = self
                        self.bridge_domain.name = 'bridge_domain'


                    class BridgeDomain(object):
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
                        	**type**\:   :py:class:`BridgeDomainTransportModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BridgeDomainTransportModeEnum>`
                        
                        .. attribute:: vfis
                        
                        	Specify the virtual forwarding interface name
                        	**type**\:   :py:class:`Vfis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.access_vfis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis()
                            self.access_vfis.parent = self
                            self.bd_attachment_circuits = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits()
                            self.bd_attachment_circuits.parent = self
                            self.bd_pseudowire_evpns = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns()
                            self.bd_pseudowire_evpns.parent = self
                            self.bd_pseudowires = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires()
                            self.bd_pseudowires.parent = self
                            self.bd_storm_controls = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls()
                            self.bd_storm_controls.parent = self
                            self.bridge_description = None
                            self.bridge_domain_evis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis()
                            self.bridge_domain_evis.parent = self
                            self.bridge_domain_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac()
                            self.bridge_domain_mac.parent = self
                            self.bridge_domain_mtu = None
                            self.bridge_domain_pbb = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb()
                            self.bridge_domain_pbb.parent = self
                            self.coupled_mode = None
                            self.dai = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai()
                            self.dai.parent = self
                            self.dhcp = None
                            self.flooding = None
                            self.flooding_unknown_unicast = None
                            self.igmp_snooping = None
                            self.igmp_snooping_disable = None
                            self.ip_source_guard = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard()
                            self.ip_source_guard.parent = self
                            self.member_vnis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis()
                            self.member_vnis.parent = self
                            self.mld_snooping = None
                            self.nv_satellite = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite()
                            self.nv_satellite.parent = self
                            self.routed_interfaces = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces()
                            self.routed_interfaces.parent = self
                            self.shutdown = None
                            self.transport_mode = None
                            self.vfis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis()
                            self.vfis.parent = self


                        class BdStormControls(object):
                            """
                            Storm Control
                            
                            .. attribute:: bd_storm_control
                            
                            	Storm Control Type
                            	**type**\: list of    :py:class:`BdStormControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bd_storm_control = YList()
                                self.bd_storm_control.parent = self
                                self.bd_storm_control.name = 'bd_storm_control'


                            class BdStormControl(object):
                                """
                                Storm Control Type
                                
                                .. attribute:: sctype  <key>
                                
                                	Storm Control Type
                                	**type**\:   :py:class:`StormControlEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.StormControlEnum>`
                                
                                .. attribute:: storm_control_unit
                                
                                	Specify units for Storm Control Configuration
                                	**type**\:   :py:class:`StormControlUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.sctype = None
                                    self.storm_control_unit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit()
                                    self.storm_control_unit.parent = self


                                class StormControlUnit(object):
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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.kbits_per_sec = None
                                        self.pkts_per_sec = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:storm-control-unit'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.kbits_per_sec is not None:
                                            return True

                                        if self.pkts_per_sec is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.sctype is None:
                                        raise YPYModelError('Key property sctype is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-storm-control[Cisco-IOS-XR-l2vpn-cfg:sctype = ' + str(self.sctype) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.sctype is not None:
                                        return True

                                    if self.storm_control_unit is not None and self.storm_control_unit._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-storm-controls'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.bd_storm_control is not None:
                                    for child_ref in self.bd_storm_control:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls']['meta_info']


                        class MemberVnis(object):
                            """
                            Bridge Domain VxLAN Network Identifier
                            Table
                            
                            .. attribute:: member_vni
                            
                            	Bridge Domain Member VxLAN Network Identifier 
                            	**type**\: list of    :py:class:`MemberVni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.member_vni = YList()
                                self.member_vni.parent = self
                                self.member_vni.name = 'member_vni'


                            class MemberVni(object):
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.vni = None
                                    self.member_vni_static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses()
                                    self.member_vni_static_mac_addresses.parent = self


                                class MemberVniStaticMacAddresses(object):
                                    """
                                    Static Mac Address Table
                                    
                                    .. attribute:: member_vni_static_mac_address
                                    
                                    	Static Mac Address Configuration
                                    	**type**\: list of    :py:class:`MemberVniStaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.member_vni_static_mac_address = YList()
                                        self.member_vni_static_mac_address.parent = self
                                        self.member_vni_static_mac_address.name = 'member_vni_static_mac_address'


                                    class MemberVniStaticMacAddress(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.mac_address = None
                                            self.next_hop_ip = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.mac_address is None:
                                                raise YPYModelError('Key property mac_address is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:member-vni-static-mac-address[Cisco-IOS-XR-l2vpn-cfg:mac-address = ' + str(self.mac_address) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.mac_address is not None:
                                                return True

                                            if self.next_hop_ip is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:member-vni-static-mac-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.member_vni_static_mac_address is not None:
                                            for child_ref in self.member_vni_static_mac_address:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.vni is None:
                                        raise YPYModelError('Key property vni is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:member-vni[Cisco-IOS-XR-l2vpn-cfg:vni = ' + str(self.vni) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.vni is not None:
                                        return True

                                    if self.member_vni_static_mac_addresses is not None and self.member_vni_static_mac_addresses._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:member-vnis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.member_vni is not None:
                                    for child_ref in self.member_vni:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis']['meta_info']


                        class BridgeDomainMac(object):
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
                            	**type**\:   :py:class:`BdmacLearnEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BdmacLearnEnum>`
                            
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
                            	**type**\:   :py:class:`MacWithdrawBehaviorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacWithdrawBehaviorEnum>`
                            
                            .. attribute:: bd_mac_withdraw_relay
                            
                            	Mac withdraw sent from access PW to access PW
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: mac_secure
                            
                            	MAC Secure
                            	**type**\:   :py:class:`MacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bd_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging()
                                self.bd_mac_aging.parent = self
                                self.bd_mac_filters = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters()
                                self.bd_mac_filters.parent = self
                                self.bd_mac_learn = None
                                self.bd_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit()
                                self.bd_mac_limit.parent = self
                                self.bd_mac_port_down_flush = None
                                self.bd_mac_withdraw = None
                                self.bd_mac_withdraw_access_pw_disable = None
                                self.bd_mac_withdraw_behavior = None
                                self.bd_mac_withdraw_relay = None
                                self.mac_secure = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure()
                                self.mac_secure.parent = self


                            class BdMacLimit(object):
                                """
                                MAC\-Limit configuration commands
                                
                                .. attribute:: bd_mac_limit_action
                                
                                	MAC address limit enforcement action
                                	**type**\:   :py:class:`MacLimitActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitActionEnum>`
                                
                                .. attribute:: bd_mac_limit_max
                                
                                	Number of MAC addresses after which MAC limit action is taken
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: bd_mac_limit_notif
                                
                                	Mac Address Limit Notification
                                	**type**\:   :py:class:`MacNotificationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotificationEnum>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bd_mac_limit_action = None
                                    self.bd_mac_limit_max = None
                                    self.bd_mac_limit_notif = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-mac-limit'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.bd_mac_limit_action is not None:
                                        return True

                                    if self.bd_mac_limit_max is not None:
                                        return True

                                    if self.bd_mac_limit_notif is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit']['meta_info']


                            class BdMacFilters(object):
                                """
                                Filter Mac Address
                                
                                .. attribute:: bd_mac_filter
                                
                                	Static MAC address
                                	**type**\: list of    :py:class:`BdMacFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bd_mac_filter = YList()
                                    self.bd_mac_filter.parent = self
                                    self.bd_mac_filter.name = 'bd_mac_filter'


                                class BdMacFilter(object):
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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.drop = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.address is None:
                                            raise YPYModelError('Key property address is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-mac-filter[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.drop is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-mac-filters'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.bd_mac_filter is not None:
                                        for child_ref in self.bd_mac_filter:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters']['meta_info']


                            class MacSecure(object):
                                """
                                MAC Secure
                                
                                .. attribute:: action
                                
                                	MAC secure enforcement action
                                	**type**\:   :py:class:`MacSecureActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacSecureActionEnum>`
                                
                                .. attribute:: enable
                                
                                	Enable MAC Secure
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: logging
                                
                                	MAC Secure Logging
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.action = None
                                    self.enable = None
                                    self.logging = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mac-secure'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.action is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    if self.logging is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure']['meta_info']


                            class BdMacAging(object):
                                """
                                MAC\-Aging configuration commands
                                
                                .. attribute:: bd_mac_aging_time
                                
                                	Mac Aging Time
                                	**type**\:  int
                                
                                	**range:** 300..30000
                                
                                .. attribute:: bd_mac_aging_type
                                
                                	MAC address aging type
                                	**type**\:   :py:class:`MacAgingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAgingEnum>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bd_mac_aging_time = None
                                    self.bd_mac_aging_type = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-mac-aging'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.bd_mac_aging_time is not None:
                                        return True

                                    if self.bd_mac_aging_type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-mac'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.bd_mac_aging is not None and self.bd_mac_aging._has_data():
                                    return True

                                if self.bd_mac_filters is not None and self.bd_mac_filters._has_data():
                                    return True

                                if self.bd_mac_learn is not None:
                                    return True

                                if self.bd_mac_limit is not None and self.bd_mac_limit._has_data():
                                    return True

                                if self.bd_mac_port_down_flush is not None:
                                    return True

                                if self.bd_mac_withdraw is not None:
                                    return True

                                if self.bd_mac_withdraw_access_pw_disable is not None:
                                    return True

                                if self.bd_mac_withdraw_behavior is not None:
                                    return True

                                if self.bd_mac_withdraw_relay is not None:
                                    return True

                                if self.mac_secure is not None and self.mac_secure._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac']['meta_info']


                        class NvSatellite(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.offload_ipv4_multicast_enable = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:nv-satellite'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.offload_ipv4_multicast_enable is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite']['meta_info']


                        class BridgeDomainPbb(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.pbb_core = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore()
                                self.pbb_core.parent = self
                                self.pbb_edges = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges()
                                self.pbb_edges.parent = self


                            class PbbEdges(object):
                                """
                                PBB Edge
                                
                                .. attribute:: pbb_edge
                                
                                	Configure BD as PBB Edge with ISID and associated PBB Core BD
                                	**type**\: list of    :py:class:`PbbEdge <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.pbb_edge = YList()
                                    self.pbb_edge.parent = self
                                    self.pbb_edge.name = 'pbb_edge'


                                class PbbEdge(object):
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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.isid = None
                                        self.core_bd_name = None
                                        self.pbb_edge_dhcp_profile = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile()
                                        self.pbb_edge_dhcp_profile.parent = self
                                        self.pbb_edge_igmp_profile = None
                                        self.pbb_edge_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac()
                                        self.pbb_edge_mac.parent = self
                                        self.pbb_edge_split_horizon_group = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup()
                                        self.pbb_edge_split_horizon_group.parent = self
                                        self.pbb_static_mac_mappings = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings()
                                        self.pbb_static_mac_mappings.parent = self
                                        self.unknown_unicast_bmac = None


                                    class PbbEdgeSplitHorizonGroup(object):
                                        """
                                        Split Horizon Group
                                        
                                        .. attribute:: disable
                                        
                                        	Disable split horizon group
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.disable = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge-split-horizon-group'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.disable is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup']['meta_info']


                                    class PbbStaticMacMappings(object):
                                        """
                                        PBB Static Mac Address Mapping Table
                                        
                                        .. attribute:: pbb_static_mac_mapping
                                        
                                        	PBB Static Mac Address Mapping Configuration
                                        	**type**\: list of    :py:class:`PbbStaticMacMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.pbb_static_mac_mapping = YList()
                                            self.pbb_static_mac_mapping.parent = self
                                            self.pbb_static_mac_mapping.name = 'pbb_static_mac_mapping'


                                        class PbbStaticMacMapping(object):
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
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.pbb_static_mac_mapping_bmac = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.address is None:
                                                    raise YPYModelError('Key property address is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-static-mac-mapping[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.address is not None:
                                                    return True

                                                if self.pbb_static_mac_mapping_bmac is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-static-mac-mappings'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.pbb_static_mac_mapping is not None:
                                                for child_ref in self.pbb_static_mac_mapping:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings']['meta_info']


                                    class PbbEdgeDhcpProfile(object):
                                        """
                                        Attach a DHCP profile
                                        
                                        .. attribute:: dhcp_snooping_id
                                        
                                        	Disable DHCP snooping
                                        	**type**\:  str
                                        
                                        .. attribute:: profile_id
                                        
                                        	Set the snooping profile
                                        	**type**\:   :py:class:`InterfaceProfileEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfileEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.dhcp_snooping_id = None
                                            self.profile_id = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge-dhcp-profile'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.dhcp_snooping_id is not None:
                                                return True

                                            if self.profile_id is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile']['meta_info']


                                    class PbbEdgeMac(object):
                                        """
                                        MAC configuration commands
                                        
                                        .. attribute:: pbb_edge_mac_aging
                                        
                                        	MAC\-Aging configuration commands
                                        	**type**\:   :py:class:`PbbEdgeMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging>`
                                        
                                        .. attribute:: pbb_edge_mac_learning
                                        
                                        	Enable Mac Learning
                                        	**type**\:   :py:class:`MacLearnEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLearnEnum>`
                                        
                                        .. attribute:: pbb_edge_mac_limit
                                        
                                        	MAC\-Limit configuration commands
                                        	**type**\:   :py:class:`PbbEdgeMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit>`
                                        
                                        .. attribute:: pbb_edge_mac_secure
                                        
                                        	MAC Secure
                                        	**type**\:   :py:class:`PbbEdgeMacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.pbb_edge_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging()
                                            self.pbb_edge_mac_aging.parent = self
                                            self.pbb_edge_mac_learning = None
                                            self.pbb_edge_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit()
                                            self.pbb_edge_mac_limit.parent = self
                                            self.pbb_edge_mac_secure = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure()
                                            self.pbb_edge_mac_secure.parent = self


                                        class PbbEdgeMacLimit(object):
                                            """
                                            MAC\-Limit configuration commands
                                            
                                            .. attribute:: pbb_edge_mac_limit_action
                                            
                                            	MAC address limit enforcement action
                                            	**type**\:   :py:class:`MacLimitActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitActionEnum>`
                                            
                                            .. attribute:: pbb_edge_mac_limit_max
                                            
                                            	Number of MAC addresses after which MAC limit action is taken
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: pbb_edge_mac_limit_notif
                                            
                                            	MAC address limit notification action
                                            	**type**\:   :py:class:`MacNotificationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotificationEnum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.pbb_edge_mac_limit_action = None
                                                self.pbb_edge_mac_limit_max = None
                                                self.pbb_edge_mac_limit_notif = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge-mac-limit'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.pbb_edge_mac_limit_action is not None:
                                                    return True

                                                if self.pbb_edge_mac_limit_max is not None:
                                                    return True

                                                if self.pbb_edge_mac_limit_notif is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit']['meta_info']


                                        class PbbEdgeMacAging(object):
                                            """
                                            MAC\-Aging configuration commands
                                            
                                            .. attribute:: pbb_edge_mac_aging_time
                                            
                                            	Mac Aging Time
                                            	**type**\:  int
                                            
                                            	**range:** 300..30000
                                            
                                            .. attribute:: pbb_edge_mac_aging_type
                                            
                                            	MAC address aging type
                                            	**type**\:   :py:class:`MacAgingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAgingEnum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.pbb_edge_mac_aging_time = None
                                                self.pbb_edge_mac_aging_type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge-mac-aging'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.pbb_edge_mac_aging_time is not None:
                                                    return True

                                                if self.pbb_edge_mac_aging_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging']['meta_info']


                                        class PbbEdgeMacSecure(object):
                                            """
                                            MAC Secure
                                            
                                            .. attribute:: accept_shutdown
                                            
                                            	Accept Virtual instance port to be shutdown on mac violation
                                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                            
                                            .. attribute:: action
                                            
                                            	MAC secure enforcement action
                                            	**type**\:   :py:class:`MacSecureActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacSecureActionEnum>`
                                            
                                            .. attribute:: disable
                                            
                                            	Disable Virtual instance port MAC Secure
                                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                            
                                            .. attribute:: enable
                                            
                                            	Enable MAC Secure
                                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                            
                                            .. attribute:: logging
                                            
                                            	MAC Secure Logging
                                            	**type**\:   :py:class:`L2VpnLoggingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnLoggingEnum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.accept_shutdown = None
                                                self.action = None
                                                self.disable = None
                                                self.enable = None
                                                self.logging = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge-mac-secure'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.accept_shutdown is not None:
                                                    return True

                                                if self.action is not None:
                                                    return True

                                                if self.disable is not None:
                                                    return True

                                                if self.enable is not None:
                                                    return True

                                                if self.logging is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge-mac'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.pbb_edge_mac_aging is not None and self.pbb_edge_mac_aging._has_data():
                                                return True

                                            if self.pbb_edge_mac_learning is not None:
                                                return True

                                            if self.pbb_edge_mac_limit is not None and self.pbb_edge_mac_limit._has_data():
                                                return True

                                            if self.pbb_edge_mac_secure is not None and self.pbb_edge_mac_secure._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.isid is None:
                                            raise YPYModelError('Key property isid is None')
                                        if self.core_bd_name is None:
                                            raise YPYModelError('Key property core_bd_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge[Cisco-IOS-XR-l2vpn-cfg:isid = ' + str(self.isid) + '][Cisco-IOS-XR-l2vpn-cfg:core-bd-name = ' + str(self.core_bd_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.isid is not None:
                                            return True

                                        if self.core_bd_name is not None:
                                            return True

                                        if self.pbb_edge_dhcp_profile is not None and self.pbb_edge_dhcp_profile._has_data():
                                            return True

                                        if self.pbb_edge_igmp_profile is not None:
                                            return True

                                        if self.pbb_edge_mac is not None and self.pbb_edge_mac._has_data():
                                            return True

                                        if self.pbb_edge_split_horizon_group is not None and self.pbb_edge_split_horizon_group._has_data():
                                            return True

                                        if self.pbb_static_mac_mappings is not None and self.pbb_static_mac_mappings._has_data():
                                            return True

                                        if self.unknown_unicast_bmac is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edges'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.pbb_edge is not None:
                                        for child_ref in self.pbb_edge:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges']['meta_info']


                            class PbbCore(object):
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.enable = None
                                    self.pbb_core_dhcp_profile = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile()
                                    self.pbb_core_dhcp_profile.parent = self
                                    self.pbb_core_evis = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis()
                                    self.pbb_core_evis.parent = self
                                    self.pbb_core_igmp_profile = None
                                    self.pbb_core_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac()
                                    self.pbb_core_mac.parent = self
                                    self.pbb_core_mmrp_flood_optimization = None
                                    self.vlan_id = None


                                class PbbCoreMac(object):
                                    """
                                    MAC configuration commands
                                    
                                    .. attribute:: pbb_core_mac_aging
                                    
                                    	MAC\-Aging configuration commands
                                    	**type**\:   :py:class:`PbbCoreMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging>`
                                    
                                    .. attribute:: pbb_core_mac_learning
                                    
                                    	Enable Mac Learning
                                    	**type**\:   :py:class:`MacLearnEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLearnEnum>`
                                    
                                    .. attribute:: pbb_core_mac_limit
                                    
                                    	MAC\-Limit configuration commands
                                    	**type**\:   :py:class:`PbbCoreMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.pbb_core_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging()
                                        self.pbb_core_mac_aging.parent = self
                                        self.pbb_core_mac_learning = None
                                        self.pbb_core_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit()
                                        self.pbb_core_mac_limit.parent = self


                                    class PbbCoreMacAging(object):
                                        """
                                        MAC\-Aging configuration commands
                                        
                                        .. attribute:: pbb_core_mac_aging_time
                                        
                                        	Mac Aging Time
                                        	**type**\:  int
                                        
                                        	**range:** 300..30000
                                        
                                        .. attribute:: pbb_core_mac_aging_type
                                        
                                        	MAC address aging type
                                        	**type**\:   :py:class:`MacAgingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAgingEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.pbb_core_mac_aging_time = None
                                            self.pbb_core_mac_aging_type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-core-mac-aging'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.pbb_core_mac_aging_time is not None:
                                                return True

                                            if self.pbb_core_mac_aging_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging']['meta_info']


                                    class PbbCoreMacLimit(object):
                                        """
                                        MAC\-Limit configuration commands
                                        
                                        .. attribute:: pbb_core_mac_limit_action
                                        
                                        	MAC address limit enforcement action
                                        	**type**\:   :py:class:`MacLimitActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitActionEnum>`
                                        
                                        .. attribute:: pbb_core_mac_limit_max
                                        
                                        	Number of MAC addresses after which MAC limit action is taken
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pbb_core_mac_limit_notif
                                        
                                        	MAC address limit notification action
                                        	**type**\:   :py:class:`MacNotificationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotificationEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.pbb_core_mac_limit_action = None
                                            self.pbb_core_mac_limit_max = None
                                            self.pbb_core_mac_limit_notif = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-core-mac-limit'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.pbb_core_mac_limit_action is not None:
                                                return True

                                            if self.pbb_core_mac_limit_max is not None:
                                                return True

                                            if self.pbb_core_mac_limit_notif is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-core-mac'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.pbb_core_mac_aging is not None and self.pbb_core_mac_aging._has_data():
                                            return True

                                        if self.pbb_core_mac_learning is not None:
                                            return True

                                        if self.pbb_core_mac_limit is not None and self.pbb_core_mac_limit._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac']['meta_info']


                                class PbbCoreEvis(object):
                                    """
                                    PBB Core EVI Table
                                    
                                    .. attribute:: pbb_core_evi
                                    
                                    	PBB Core EVI
                                    	**type**\: list of    :py:class:`PbbCoreEvi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.pbb_core_evi = YList()
                                        self.pbb_core_evi.parent = self
                                        self.pbb_core_evi.name = 'pbb_core_evi'


                                    class PbbCoreEvi(object):
                                        """
                                        PBB Core EVI
                                        
                                        .. attribute:: eviid  <key>
                                        
                                        	Ethernet VPN ID
                                        	**type**\:  int
                                        
                                        	**range:** 1..4294967295
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.eviid = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.eviid is None:
                                                raise YPYModelError('Key property eviid is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-core-evi[Cisco-IOS-XR-l2vpn-cfg:eviid = ' + str(self.eviid) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.eviid is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-core-evis'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.pbb_core_evi is not None:
                                            for child_ref in self.pbb_core_evi:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis']['meta_info']


                                class PbbCoreDhcpProfile(object):
                                    """
                                    Attach a DHCP profile
                                    
                                    .. attribute:: dhcp_snooping_id
                                    
                                    	Disable DHCP snooping
                                    	**type**\:  str
                                    
                                    .. attribute:: profile_id
                                    
                                    	Set the snooping profile
                                    	**type**\:   :py:class:`InterfaceProfileEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfileEnum>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.dhcp_snooping_id = None
                                        self.profile_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-core-dhcp-profile'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.dhcp_snooping_id is not None:
                                            return True

                                        if self.profile_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-core'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.enable is not None:
                                        return True

                                    if self.pbb_core_dhcp_profile is not None and self.pbb_core_dhcp_profile._has_data():
                                        return True

                                    if self.pbb_core_evis is not None and self.pbb_core_evis._has_data():
                                        return True

                                    if self.pbb_core_igmp_profile is not None:
                                        return True

                                    if self.pbb_core_mac is not None and self.pbb_core_mac._has_data():
                                        return True

                                    if self.pbb_core_mmrp_flood_optimization is not None:
                                        return True

                                    if self.vlan_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-pbb'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.pbb_core is not None and self.pbb_core._has_data():
                                    return True

                                if self.pbb_edges is not None and self.pbb_edges._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb']['meta_info']


                        class BridgeDomainEvis(object):
                            """
                            Bridge Domain EVI Table
                            
                            .. attribute:: bridge_domain_evi
                            
                            	Bridge Domain EVI
                            	**type**\: list of    :py:class:`BridgeDomainEvi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bridge_domain_evi = YList()
                                self.bridge_domain_evi.parent = self
                                self.bridge_domain_evi.name = 'bridge_domain_evi'


                            class BridgeDomainEvi(object):
                                """
                                Bridge Domain EVI
                                
                                .. attribute:: eviid  <key>
                                
                                	Ethernet VPN ID
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.eviid = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.eviid is None:
                                        raise YPYModelError('Key property eviid is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-evi[Cisco-IOS-XR-l2vpn-cfg:eviid = ' + str(self.eviid) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.eviid is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-evis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.bridge_domain_evi is not None:
                                    for child_ref in self.bridge_domain_evi:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis']['meta_info']


                        class AccessVfis(object):
                            """
                            Specify the access virtual forwarding
                            interface name
                            
                            .. attribute:: access_vfi
                            
                            	Name of the Acess Virtual Forwarding Interface
                            	**type**\: list of    :py:class:`AccessVfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.access_vfi = YList()
                                self.access_vfi.parent = self
                                self.access_vfi.name = 'access_vfi'


                            class AccessVfi(object):
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
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.name = None
                                    self.access_vfi_pseudowires = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires()
                                    self.access_vfi_pseudowires.parent = self


                                class AccessVfiPseudowires(object):
                                    """
                                    List of pseudowires
                                    
                                    .. attribute:: access_vfi_pseudowire
                                    
                                    	Pseudowire configuration
                                    	**type**\: list of    :py:class:`AccessVfiPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.access_vfi_pseudowire = YList()
                                        self.access_vfi_pseudowire.parent = self
                                        self.access_vfi_pseudowire.name = 'access_vfi_pseudowire'


                                    class AccessVfiPseudowire(object):
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
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.neighbor = None
                                            self.pseudowire_id = None
                                            self.access_vfi_pseudowire_static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses()
                                            self.access_vfi_pseudowire_static_mac_addresses.parent = self


                                        class AccessVfiPseudowireStaticMacAddresses(object):
                                            """
                                            Static Mac Address Table
                                            
                                            .. attribute:: access_vfi_pseudowire_static_mac_address
                                            
                                            	Static Mac Address Configuration
                                            	**type**\: list of    :py:class:`AccessVfiPseudowireStaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.access_vfi_pseudowire_static_mac_address = YList()
                                                self.access_vfi_pseudowire_static_mac_address.parent = self
                                                self.access_vfi_pseudowire_static_mac_address.name = 'access_vfi_pseudowire_static_mac_address'


                                            class AccessVfiPseudowireStaticMacAddress(object):
                                                """
                                                Static Mac Address Configuration
                                                
                                                .. attribute:: address  <key>
                                                
                                                	Static MAC address
                                                	**type**\:  str
                                                
                                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.address = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.address is None:
                                                        raise YPYModelError('Key property address is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:access-vfi-pseudowire-static-mac-address[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if self.address is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:access-vfi-pseudowire-static-mac-addresses'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.access_vfi_pseudowire_static_mac_address is not None:
                                                    for child_ref in self.access_vfi_pseudowire_static_mac_address:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.neighbor is None:
                                                raise YPYModelError('Key property neighbor is None')
                                            if self.pseudowire_id is None:
                                                raise YPYModelError('Key property pseudowire_id is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:access-vfi-pseudowire[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + '][Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.neighbor is not None:
                                                return True

                                            if self.pseudowire_id is not None:
                                                return True

                                            if self.access_vfi_pseudowire_static_mac_addresses is not None and self.access_vfi_pseudowire_static_mac_addresses._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:access-vfi-pseudowires'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.access_vfi_pseudowire is not None:
                                            for child_ref in self.access_vfi_pseudowire:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.name is None:
                                        raise YPYModelError('Key property name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:access-vfi[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.name is not None:
                                        return True

                                    if self.access_vfi_pseudowires is not None and self.access_vfi_pseudowires._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:access-vfis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.access_vfi is not None:
                                    for child_ref in self.access_vfi:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis']['meta_info']


                        class BdPseudowires(object):
                            """
                            List of pseudowires
                            
                            .. attribute:: bd_pseudowire
                            
                            	Pseudowire configuration
                            	**type**\: list of    :py:class:`BdPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bd_pseudowire = YList()
                                self.bd_pseudowire.parent = self
                                self.bd_pseudowire.name = 'bd_pseudowire'


                            class BdPseudowire(object):
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
                                	**type**\:   :py:class:`InterfaceTrafficFloodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFloodEnum>`
                                
                                .. attribute:: pseudowire_flooding_unknown_unicast
                                
                                	Bridge\-domain Pseudowire flooding Unknown Unicast
                                	**type**\:   :py:class:`InterfaceTrafficFloodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFloodEnum>`
                                
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.neighbor = None
                                    self.pseudowire_id = None
                                    self.bd_pw_class = None
                                    self.bd_pw_mpls_static_labels = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels()
                                    self.bd_pw_mpls_static_labels.parent = self
                                    self.bd_pw_split_horizon = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon()
                                    self.bd_pw_split_horizon.parent = self
                                    self.bd_pw_static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses()
                                    self.bd_pw_static_mac_addresses.parent = self
                                    self.bdpw_storm_control_types = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes()
                                    self.bdpw_storm_control_types.parent = self
                                    self.bridge_domain_backup_pseudowires = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires()
                                    self.bridge_domain_backup_pseudowires.parent = self
                                    self.pseudowire_dai = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai()
                                    self.pseudowire_dai.parent = self
                                    self.pseudowire_flooding = None
                                    self.pseudowire_flooding_unknown_unicast = None
                                    self.pseudowire_igmp_snoop = None
                                    self.pseudowire_ip_source_guard = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard()
                                    self.pseudowire_ip_source_guard.parent = self
                                    self.pseudowire_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac()
                                    self.pseudowire_mac.parent = self
                                    self.pseudowire_mld_snoop = None
                                    self.pseudowire_profile = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile()
                                    self.pseudowire_profile.parent = self


                                class PseudowireDai(object):
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
                                    	**type**\:   :py:class:`L2VpnLoggingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnLoggingEnum>`
                                    
                                    .. attribute:: pseudowire_dai_address_validation
                                    
                                    	Address Validation
                                    	**type**\:   :py:class:`PseudowireDaiAddressValidation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.disable = None
                                        self.enable = None
                                        self.logging = None
                                        self.pseudowire_dai_address_validation = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation()
                                        self.pseudowire_dai_address_validation.parent = self


                                    class PseudowireDaiAddressValidation(object):
                                        """
                                        Address Validation
                                        
                                        .. attribute:: destination_mac_verification
                                        
                                        	Destination MAC Verification
                                        	**type**\:   :py:class:`L2VpnVerificationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnVerificationEnum>`
                                        
                                        .. attribute:: ipv4_verification
                                        
                                        	IPv4 Verification
                                        	**type**\:   :py:class:`L2VpnVerificationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnVerificationEnum>`
                                        
                                        .. attribute:: source_mac_verification
                                        
                                        	Source MAC Verification
                                        	**type**\:   :py:class:`L2VpnVerificationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnVerificationEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.destination_mac_verification = None
                                            self.ipv4_verification = None
                                            self.source_mac_verification = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-dai-address-validation'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.destination_mac_verification is not None:
                                                return True

                                            if self.ipv4_verification is not None:
                                                return True

                                            if self.source_mac_verification is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-dai'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.disable is not None:
                                            return True

                                        if self.enable is not None:
                                            return True

                                        if self.logging is not None:
                                            return True

                                        if self.pseudowire_dai_address_validation is not None and self.pseudowire_dai_address_validation._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai']['meta_info']


                                class BdpwStormControlTypes(object):
                                    """
                                    Storm Control
                                    
                                    .. attribute:: bdpw_storm_control_type
                                    
                                    	Storm Control Type
                                    	**type**\: list of    :py:class:`BdpwStormControlType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bdpw_storm_control_type = YList()
                                        self.bdpw_storm_control_type.parent = self
                                        self.bdpw_storm_control_type.name = 'bdpw_storm_control_type'


                                    class BdpwStormControlType(object):
                                        """
                                        Storm Control Type
                                        
                                        .. attribute:: sctype  <key>
                                        
                                        	Storm Control Type
                                        	**type**\:   :py:class:`StormControlEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.StormControlEnum>`
                                        
                                        .. attribute:: storm_control_unit
                                        
                                        	Specify units for Storm Control Configuration
                                        	**type**\:   :py:class:`StormControlUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.sctype = None
                                            self.storm_control_unit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit()
                                            self.storm_control_unit.parent = self


                                        class StormControlUnit(object):
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
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.kbits_per_sec = None
                                                self.pkts_per_sec = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:storm-control-unit'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.kbits_per_sec is not None:
                                                    return True

                                                if self.pkts_per_sec is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.sctype is None:
                                                raise YPYModelError('Key property sctype is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bdpw-storm-control-type[Cisco-IOS-XR-l2vpn-cfg:sctype = ' + str(self.sctype) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.sctype is not None:
                                                return True

                                            if self.storm_control_unit is not None and self.storm_control_unit._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bdpw-storm-control-types'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.bdpw_storm_control_type is not None:
                                            for child_ref in self.bdpw_storm_control_type:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes']['meta_info']


                                class PseudowireProfile(object):
                                    """
                                    Attach a DHCP profile
                                    
                                    .. attribute:: dhcp_snooping_id
                                    
                                    	Disable DHCP snooping
                                    	**type**\:  str
                                    
                                    .. attribute:: profile_id
                                    
                                    	Set the snooping profile
                                    	**type**\:   :py:class:`InterfaceProfileEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfileEnum>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.dhcp_snooping_id = None
                                        self.profile_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-profile'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.dhcp_snooping_id is not None:
                                            return True

                                        if self.profile_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile']['meta_info']


                                class BdPwStaticMacAddresses(object):
                                    """
                                    Static Mac Address Table
                                    
                                    .. attribute:: bd_pw_static_mac_address
                                    
                                    	Static Mac Address Configuration
                                    	**type**\: list of    :py:class:`BdPwStaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bd_pw_static_mac_address = YList()
                                        self.bd_pw_static_mac_address.parent = self
                                        self.bd_pw_static_mac_address.name = 'bd_pw_static_mac_address'


                                    class BdPwStaticMacAddress(object):
                                        """
                                        Static Mac Address Configuration
                                        
                                        .. attribute:: address  <key>
                                        
                                        	Static MAC address
                                        	**type**\:  str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.address = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.address is None:
                                                raise YPYModelError('Key property address is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pw-static-mac-address[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.address is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pw-static-mac-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.bd_pw_static_mac_address is not None:
                                            for child_ref in self.bd_pw_static_mac_address:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses']['meta_info']


                                class PseudowireIpSourceGuard(object):
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
                                    	**type**\:   :py:class:`L2VpnLoggingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnLoggingEnum>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.disable = None
                                        self.enable = None
                                        self.logging = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-ip-source-guard'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.disable is not None:
                                            return True

                                        if self.enable is not None:
                                            return True

                                        if self.logging is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard']['meta_info']


                                class PseudowireMac(object):
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
                                    	**type**\:   :py:class:`MacLearnEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLearnEnum>`
                                    
                                    .. attribute:: pseudowire_mac_limit
                                    
                                    	MAC\-Limit configuration commands
                                    	**type**\:   :py:class:`PseudowireMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit>`
                                    
                                    .. attribute:: pseudowire_mac_port_down_flush
                                    
                                    	Enable/Disable MAC Flush When Port goes down
                                    	**type**\:   :py:class:`PortDownFlushEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.PortDownFlushEnum>`
                                    
                                    .. attribute:: pseudowire_mac_secure
                                    
                                    	MAC Secure
                                    	**type**\:   :py:class:`PseudowireMacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.enable = None
                                        self.pseudowire_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging()
                                        self.pseudowire_mac_aging.parent = self
                                        self.pseudowire_mac_learning = None
                                        self.pseudowire_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit()
                                        self.pseudowire_mac_limit.parent = self
                                        self.pseudowire_mac_port_down_flush = None
                                        self.pseudowire_mac_secure = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure()
                                        self.pseudowire_mac_secure.parent = self


                                    class PseudowireMacSecure(object):
                                        """
                                        MAC Secure
                                        
                                        .. attribute:: action
                                        
                                        	MAC secure enforcement action
                                        	**type**\:   :py:class:`MacSecureActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacSecureActionEnum>`
                                        
                                        .. attribute:: disable
                                        
                                        	Disable L2 Pseudowire MAC Secure
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable MAC Secure
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: logging
                                        
                                        	MAC Secure Logging
                                        	**type**\:   :py:class:`L2VpnLoggingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnLoggingEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.action = None
                                            self.disable = None
                                            self.enable = None
                                            self.logging = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-mac-secure'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.action is not None:
                                                return True

                                            if self.disable is not None:
                                                return True

                                            if self.enable is not None:
                                                return True

                                            if self.logging is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure']['meta_info']


                                    class PseudowireMacAging(object):
                                        """
                                        MAC\-Aging configuration commands
                                        
                                        .. attribute:: pseudowire_mac_aging_time
                                        
                                        	MAC Aging Time
                                        	**type**\:  int
                                        
                                        	**range:** 300..30000
                                        
                                        .. attribute:: pseudowire_mac_aging_type
                                        
                                        	MAC address aging type
                                        	**type**\:   :py:class:`MacAgingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAgingEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.pseudowire_mac_aging_time = None
                                            self.pseudowire_mac_aging_type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-mac-aging'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.pseudowire_mac_aging_time is not None:
                                                return True

                                            if self.pseudowire_mac_aging_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging']['meta_info']


                                    class PseudowireMacLimit(object):
                                        """
                                        MAC\-Limit configuration commands
                                        
                                        .. attribute:: pseudowire_mac_limit_action
                                        
                                        	Bridge Access Pseudowire MAC address limit enforcement action
                                        	**type**\:   :py:class:`MacLimitActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitActionEnum>`
                                        
                                        .. attribute:: pseudowire_mac_limit_max
                                        
                                        	Number of MAC addresses on a Bridge Access Pseudowire after which MAC limit action is taken
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pseudowire_mac_limit_notif
                                        
                                        	MAC address limit notification action in a Bridge Access Pseudowire
                                        	**type**\:   :py:class:`MacNotificationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotificationEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.pseudowire_mac_limit_action = None
                                            self.pseudowire_mac_limit_max = None
                                            self.pseudowire_mac_limit_notif = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-mac-limit'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.pseudowire_mac_limit_action is not None:
                                                return True

                                            if self.pseudowire_mac_limit_max is not None:
                                                return True

                                            if self.pseudowire_mac_limit_notif is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-mac'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.enable is not None:
                                            return True

                                        if self.pseudowire_mac_aging is not None and self.pseudowire_mac_aging._has_data():
                                            return True

                                        if self.pseudowire_mac_learning is not None:
                                            return True

                                        if self.pseudowire_mac_limit is not None and self.pseudowire_mac_limit._has_data():
                                            return True

                                        if self.pseudowire_mac_port_down_flush is not None:
                                            return True

                                        if self.pseudowire_mac_secure is not None and self.pseudowire_mac_secure._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac']['meta_info']


                                class BdPwSplitHorizon(object):
                                    """
                                    Split Horizon
                                    
                                    .. attribute:: bd_pw_split_horizon_group
                                    
                                    	Split Horizon Group
                                    	**type**\:   :py:class:`BdPwSplitHorizonGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bd_pw_split_horizon_group = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup()
                                        self.bd_pw_split_horizon_group.parent = self


                                    class BdPwSplitHorizonGroup(object):
                                        """
                                        Split Horizon Group
                                        
                                        .. attribute:: enable
                                        
                                        	Enable split horizon group
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.enable = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pw-split-horizon-group'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.enable is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pw-split-horizon'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.bd_pw_split_horizon_group is not None and self.bd_pw_split_horizon_group._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon']['meta_info']


                                class BdPwMplsStaticLabels(object):
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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.local_static_label = None
                                        self.remote_static_label = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pw-mpls-static-labels'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.local_static_label is not None:
                                            return True

                                        if self.remote_static_label is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels']['meta_info']


                                class BridgeDomainBackupPseudowires(object):
                                    """
                                    List of pseudowires
                                    
                                    .. attribute:: bridge_domain_backup_pseudowire
                                    
                                    	Backup pseudowire configuration
                                    	**type**\: list of    :py:class:`BridgeDomainBackupPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bridge_domain_backup_pseudowire = YList()
                                        self.bridge_domain_backup_pseudowire.parent = self
                                        self.bridge_domain_backup_pseudowire.name = 'bridge_domain_backup_pseudowire'


                                    class BridgeDomainBackupPseudowire(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.neighbor = None
                                            self.pseudowire_id = None
                                            self.bridge_domain_backup_pw_class = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.neighbor is None:
                                                raise YPYModelError('Key property neighbor is None')
                                            if self.pseudowire_id is None:
                                                raise YPYModelError('Key property pseudowire_id is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-backup-pseudowire[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + '][Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.neighbor is not None:
                                                return True

                                            if self.pseudowire_id is not None:
                                                return True

                                            if self.bridge_domain_backup_pw_class is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-backup-pseudowires'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.bridge_domain_backup_pseudowire is not None:
                                            for child_ref in self.bridge_domain_backup_pseudowire:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.neighbor is None:
                                        raise YPYModelError('Key property neighbor is None')
                                    if self.pseudowire_id is None:
                                        raise YPYModelError('Key property pseudowire_id is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pseudowire[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + '][Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.neighbor is not None:
                                        return True

                                    if self.pseudowire_id is not None:
                                        return True

                                    if self.bd_pw_class is not None:
                                        return True

                                    if self.bd_pw_mpls_static_labels is not None and self.bd_pw_mpls_static_labels._has_data():
                                        return True

                                    if self.bd_pw_split_horizon is not None and self.bd_pw_split_horizon._has_data():
                                        return True

                                    if self.bd_pw_static_mac_addresses is not None and self.bd_pw_static_mac_addresses._has_data():
                                        return True

                                    if self.bdpw_storm_control_types is not None and self.bdpw_storm_control_types._has_data():
                                        return True

                                    if self.bridge_domain_backup_pseudowires is not None and self.bridge_domain_backup_pseudowires._has_data():
                                        return True

                                    if self.pseudowire_dai is not None and self.pseudowire_dai._has_data():
                                        return True

                                    if self.pseudowire_flooding is not None:
                                        return True

                                    if self.pseudowire_flooding_unknown_unicast is not None:
                                        return True

                                    if self.pseudowire_igmp_snoop is not None:
                                        return True

                                    if self.pseudowire_ip_source_guard is not None and self.pseudowire_ip_source_guard._has_data():
                                        return True

                                    if self.pseudowire_mac is not None and self.pseudowire_mac._has_data():
                                        return True

                                    if self.pseudowire_mld_snoop is not None:
                                        return True

                                    if self.pseudowire_profile is not None and self.pseudowire_profile._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pseudowires'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.bd_pseudowire is not None:
                                    for child_ref in self.bd_pseudowire:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires']['meta_info']


                        class Vfis(object):
                            """
                            Specify the virtual forwarding interface
                            name
                            
                            .. attribute:: vfi
                            
                            	Name of the Virtual Forwarding Interface
                            	**type**\: list of    :py:class:`Vfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.vfi = YList()
                                self.vfi.parent = self
                                self.vfi.name = 'vfi'


                            class Vfi(object):
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.name = None
                                    self.bgp_auto_discovery = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery()
                                    self.bgp_auto_discovery.parent = self
                                    self.multicast_p2mp = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp()
                                    self.multicast_p2mp.parent = self
                                    self.vfi_pseudowires = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires()
                                    self.vfi_pseudowires.parent = self
                                    self.vfi_shutdown = None
                                    self.vpnid = None


                                class MulticastP2Mp(object):
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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.enable = None
                                        self.signalings = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings()
                                        self.signalings.parent = self
                                        self.transports = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports()
                                        self.transports.parent = self


                                    class Transports(object):
                                        """
                                        Multicast P2MP Transport
                                        
                                        .. attribute:: transport
                                        
                                        	Multicast P2MP Transport Type
                                        	**type**\: list of    :py:class:`Transport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.transport = YList()
                                            self.transport.parent = self
                                            self.transport.name = 'transport'


                                        class Transport(object):
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
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.transport_name = None
                                                self.attribute_set_name = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.transport_name is None:
                                                    raise YPYModelError('Key property transport_name is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:transport[Cisco-IOS-XR-l2vpn-cfg:transport-name = ' + str(self.transport_name) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.transport_name is not None:
                                                    return True

                                                if self.attribute_set_name is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:transports'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.transport is not None:
                                                for child_ref in self.transport:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports']['meta_info']


                                    class Signalings(object):
                                        """
                                        Multicast P2MP Signaling Type
                                        
                                        .. attribute:: signaling
                                        
                                        	Multicast P2MP Signaling Type
                                        	**type**\: list of    :py:class:`Signaling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.signaling = YList()
                                            self.signaling.parent = self
                                            self.signaling.name = 'signaling'


                                        class Signaling(object):
                                            """
                                            Multicast P2MP Signaling Type
                                            
                                            .. attribute:: signaling_name  <key>
                                            
                                            	Signaling Type
                                            	**type**\:  str
                                            
                                            	**pattern:** (BGP)
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.signaling_name = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.signaling_name is None:
                                                    raise YPYModelError('Key property signaling_name is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:signaling[Cisco-IOS-XR-l2vpn-cfg:signaling-name = ' + str(self.signaling_name) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.signaling_name is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:signalings'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.signaling is not None:
                                                for child_ref in self.signaling:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:multicast-p2mp'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.enable is not None:
                                            return True

                                        if self.signalings is not None and self.signalings._has_data():
                                            return True

                                        if self.transports is not None and self.transports._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp']['meta_info']


                                class VfiPseudowires(object):
                                    """
                                    List of pseudowires
                                    
                                    .. attribute:: vfi_pseudowire
                                    
                                    	Pseudowire configuration
                                    	**type**\: list of    :py:class:`VfiPseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.vfi_pseudowire = YList()
                                        self.vfi_pseudowire.parent = self
                                        self.vfi_pseudowire.name = 'vfi_pseudowire'


                                    class VfiPseudowire(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.neighbor = None
                                            self.pseudowire_id = None
                                            self.pseudowire_static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses()
                                            self.pseudowire_static_mac_addresses.parent = self
                                            self.vfi_pw_class = None
                                            self.vfi_pw_dhcp_snoop = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop()
                                            self.vfi_pw_dhcp_snoop.parent = self
                                            self.vfi_pw_igmp_snoop = None
                                            self.vfi_pw_mld_snoop = None
                                            self.vfi_pw_mpls_static_labels = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels()
                                            self.vfi_pw_mpls_static_labels.parent = self


                                        class VfiPwDhcpSnoop(object):
                                            """
                                            Attach a DHCP Snooping profile
                                            
                                            .. attribute:: dhcp_snooping_id
                                            
                                            	Disable DHCP snooping
                                            	**type**\:  str
                                            
                                            .. attribute:: profile_id
                                            
                                            	Set the snooping profile
                                            	**type**\:   :py:class:`InterfaceProfileEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfileEnum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.dhcp_snooping_id = None
                                                self.profile_id = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vfi-pw-dhcp-snoop'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.dhcp_snooping_id is not None:
                                                    return True

                                                if self.profile_id is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop']['meta_info']


                                        class VfiPwMplsStaticLabels(object):
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
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.local_static_label = None
                                                self.remote_static_label = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vfi-pw-mpls-static-labels'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.local_static_label is not None:
                                                    return True

                                                if self.remote_static_label is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels']['meta_info']


                                        class PseudowireStaticMacAddresses(object):
                                            """
                                            Static Mac Address Table
                                            
                                            .. attribute:: pseudowire_static_mac_address
                                            
                                            	Static Mac Address Configuration
                                            	**type**\: list of    :py:class:`PseudowireStaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.pseudowire_static_mac_address = YList()
                                                self.pseudowire_static_mac_address.parent = self
                                                self.pseudowire_static_mac_address.name = 'pseudowire_static_mac_address'


                                            class PseudowireStaticMacAddress(object):
                                                """
                                                Static Mac Address Configuration
                                                
                                                .. attribute:: address  <key>
                                                
                                                	Static MAC address
                                                	**type**\:  str
                                                
                                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.address = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.address is None:
                                                        raise YPYModelError('Key property address is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-static-mac-address[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if self.address is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-static-mac-addresses'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.pseudowire_static_mac_address is not None:
                                                    for child_ref in self.pseudowire_static_mac_address:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.neighbor is None:
                                                raise YPYModelError('Key property neighbor is None')
                                            if self.pseudowire_id is None:
                                                raise YPYModelError('Key property pseudowire_id is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vfi-pseudowire[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + '][Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.neighbor is not None:
                                                return True

                                            if self.pseudowire_id is not None:
                                                return True

                                            if self.pseudowire_static_mac_addresses is not None and self.pseudowire_static_mac_addresses._has_data():
                                                return True

                                            if self.vfi_pw_class is not None:
                                                return True

                                            if self.vfi_pw_dhcp_snoop is not None and self.vfi_pw_dhcp_snoop._has_data():
                                                return True

                                            if self.vfi_pw_igmp_snoop is not None:
                                                return True

                                            if self.vfi_pw_mld_snoop is not None:
                                                return True

                                            if self.vfi_pw_mpls_static_labels is not None and self.vfi_pw_mpls_static_labels._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vfi-pseudowires'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.vfi_pseudowire is not None:
                                            for child_ref in self.vfi_pseudowire:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires']['meta_info']


                                class BgpAutoDiscovery(object):
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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.ad_control_word = None
                                        self.bgp_route_policy = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy()
                                        self.bgp_route_policy.parent = self
                                        self.bgp_signaling_protocol = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol()
                                        self.bgp_signaling_protocol.parent = self
                                        self.enable = None
                                        self.ldp_signaling_protocol = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol()
                                        self.ldp_signaling_protocol.parent = self
                                        self.route_distinguisher = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher()
                                        self.route_distinguisher.parent = self
                                        self.route_targets = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets()
                                        self.route_targets.parent = self
                                        self.table_policy = None


                                    class LdpSignalingProtocol(object):
                                        """
                                        Signaling Protocol LDP in this VFI
                                        configuration
                                        
                                        .. attribute:: enable
                                        
                                        	Enable LDP as Signaling Protocol .Deletion of this object also causes deletion of all objects under LDPSignalingProtocol
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: flow_label_load_balance
                                        
                                        	Enable Flow Label based load balancing
                                        	**type**\:   :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance>`
                                        
                                        .. attribute:: vplsid
                                        
                                        	VPLS ID
                                        	**type**\:   :py:class:`Vplsid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.Vplsid>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.enable = None
                                            self.flow_label_load_balance = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance()
                                            self.flow_label_load_balance.parent = self
                                            self.vplsid = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.Vplsid()
                                            self.vplsid.parent = self


                                        class Vplsid(object):
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
                                            	**type**\:   :py:class:`LdpVplsIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.LdpVplsIdEnum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.address_index = None
                                                self.as_ = None
                                                self.as_index = None
                                                self.type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vplsid'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.address is not None:
                                                    return True

                                                if self.address_index is not None:
                                                    return True

                                                if self.as_ is not None:
                                                    return True

                                                if self.as_index is not None:
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.Vplsid']['meta_info']


                                        class FlowLabelLoadBalance(object):
                                            """
                                            Enable Flow Label based load balancing
                                            
                                            .. attribute:: flow_label
                                            
                                            	Flow Label load balance type
                                            	**type**\:   :py:class:`FlowLabelLoadBalanceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalanceEnum>`
                                            
                                            .. attribute:: static
                                            
                                            	Static Flow Label
                                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.flow_label = None
                                                self.static = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:flow-label-load-balance'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.flow_label is not None:
                                                    return True

                                                if self.static is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ldp-signaling-protocol'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.enable is not None:
                                                return True

                                            if self.flow_label_load_balance is not None and self.flow_label_load_balance._has_data():
                                                return True

                                            if self.vplsid is not None and self.vplsid._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol']['meta_info']


                                    class BgpRoutePolicy(object):
                                        """
                                        Route policy
                                        
                                        .. attribute:: export
                                        
                                        	Export route policy
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.export = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bgp-route-policy'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.export is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy']['meta_info']


                                    class RouteDistinguisher(object):
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
                                        	**type**\:   :py:class:`BgpRouteDistinguisherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisherEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.addr_index = None
                                            self.address = None
                                            self.as_ = None
                                            self.as_index = None
                                            self.type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:route-distinguisher'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.addr_index is not None:
                                                return True

                                            if self.address is not None:
                                                return True

                                            if self.as_ is not None:
                                                return True

                                            if self.as_index is not None:
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher']['meta_info']


                                    class BgpSignalingProtocol(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.enable = None
                                            self.flow_label_load_balance = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance()
                                            self.flow_label_load_balance.parent = self
                                            self.ve_range = None
                                            self.veid = None


                                        class FlowLabelLoadBalance(object):
                                            """
                                            Enable Flow Label based load balancing
                                            
                                            .. attribute:: flow_label
                                            
                                            	Flow Label load balance type
                                            	**type**\:   :py:class:`FlowLabelLoadBalanceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalanceEnum>`
                                            
                                            .. attribute:: static
                                            
                                            	Static Flow Label
                                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.flow_label = None
                                                self.static = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:flow-label-load-balance'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.flow_label is not None:
                                                    return True

                                                if self.static is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bgp-signaling-protocol'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.enable is not None:
                                                return True

                                            if self.flow_label_load_balance is not None and self.flow_label_load_balance._has_data():
                                                return True

                                            if self.ve_range is not None:
                                                return True

                                            if self.veid is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol']['meta_info']


                                    class RouteTargets(object):
                                        """
                                        Route Target
                                        
                                        .. attribute:: route_target
                                        
                                        	Name of the Route Target
                                        	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.route_target = YList()
                                            self.route_target.parent = self
                                            self.route_target.name = 'route_target'


                                        class RouteTarget(object):
                                            """
                                            Name of the Route Target
                                            
                                            .. attribute:: role  <key>
                                            
                                            	Role of the router target type
                                            	**type**\:   :py:class:`BgpRouteTargetRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRoleEnum>`
                                            
                                            .. attribute:: format  <key>
                                            
                                            	Format of the route target
                                            	**type**\:   :py:class:`BgpRouteTargetFormatEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormatEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	ipv4 address
                                            	**type**\: list of    :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address>`
                                            
                                            .. attribute:: two_byte_as_or_four_byte_as
                                            
                                            	two byte as or four byte as
                                            	**type**\: list of    :py:class:`TwoByteAsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.role = None
                                                self.format = None
                                                self.ipv4_address = YList()
                                                self.ipv4_address.parent = self
                                                self.ipv4_address.name = 'ipv4_address'
                                                self.two_byte_as_or_four_byte_as = YList()
                                                self.two_byte_as_or_four_byte_as.parent = self
                                                self.two_byte_as_or_four_byte_as.name = 'two_byte_as_or_four_byte_as'


                                            class TwoByteAsOrFourByteAs(object):
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
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.as_ = None
                                                    self.as_index = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.as_ is None:
                                                        raise YPYModelError('Key property as_ is None')
                                                    if self.as_index is None:
                                                        raise YPYModelError('Key property as_index is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:two-byte-as-or-four-byte-as[Cisco-IOS-XR-l2vpn-cfg:as = ' + str(self.as_) + '][Cisco-IOS-XR-l2vpn-cfg:as-index = ' + str(self.as_index) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if self.as_ is not None:
                                                        return True

                                                    if self.as_index is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs']['meta_info']


                                            class Ipv4Address(object):
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
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.address = None
                                                    self.addr_index = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.address is None:
                                                        raise YPYModelError('Key property address is None')
                                                    if self.addr_index is None:
                                                        raise YPYModelError('Key property addr_index is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ipv4-address[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-l2vpn-cfg:addr-index = ' + str(self.addr_index) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if self.address is not None:
                                                        return True

                                                    if self.addr_index is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.role is None:
                                                    raise YPYModelError('Key property role is None')
                                                if self.format is None:
                                                    raise YPYModelError('Key property format is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:route-target[Cisco-IOS-XR-l2vpn-cfg:role = ' + str(self.role) + '][Cisco-IOS-XR-l2vpn-cfg:format = ' + str(self.format) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.role is not None:
                                                    return True

                                                if self.format is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    for child_ref in self.ipv4_address:
                                                        if child_ref._has_data():
                                                            return True

                                                if self.two_byte_as_or_four_byte_as is not None:
                                                    for child_ref in self.two_byte_as_or_four_byte_as:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:route-targets'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.route_target is not None:
                                                for child_ref in self.route_target:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bgp-auto-discovery'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.ad_control_word is not None:
                                            return True

                                        if self.bgp_route_policy is not None and self.bgp_route_policy._has_data():
                                            return True

                                        if self.bgp_signaling_protocol is not None and self.bgp_signaling_protocol._has_data():
                                            return True

                                        if self.enable is not None:
                                            return True

                                        if self.ldp_signaling_protocol is not None and self.ldp_signaling_protocol._has_data():
                                            return True

                                        if self.route_distinguisher is not None and self.route_distinguisher._has_data():
                                            return True

                                        if self.route_targets is not None and self.route_targets._has_data():
                                            return True

                                        if self.table_policy is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.name is None:
                                        raise YPYModelError('Key property name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vfi[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.name is not None:
                                        return True

                                    if self.bgp_auto_discovery is not None and self.bgp_auto_discovery._has_data():
                                        return True

                                    if self.multicast_p2mp is not None and self.multicast_p2mp._has_data():
                                        return True

                                    if self.vfi_pseudowires is not None and self.vfi_pseudowires._has_data():
                                        return True

                                    if self.vfi_shutdown is not None:
                                        return True

                                    if self.vpnid is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vfis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.vfi is not None:
                                    for child_ref in self.vfi:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis']['meta_info']


                        class BdAttachmentCircuits(object):
                            """
                            Attachment Circuit table
                            
                            .. attribute:: bd_attachment_circuit
                            
                            	Name of the Attachment Circuit
                            	**type**\: list of    :py:class:`BdAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bd_attachment_circuit = YList()
                                self.bd_attachment_circuit.parent = self
                                self.bd_attachment_circuit.name = 'bd_attachment_circuit'


                            class BdAttachmentCircuit(object):
                                """
                                Name of the Attachment Circuit
                                
                                .. attribute:: name  <key>
                                
                                	The name of the Attachment Circuit
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: bdac_storm_control_types
                                
                                	Storm Control
                                	**type**\:   :py:class:`BdacStormControlTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes>`
                                
                                .. attribute:: interface_dai
                                
                                	L2 Interface Dynamic ARP Inspection
                                	**type**\:   :py:class:`InterfaceDai <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai>`
                                
                                .. attribute:: interface_flooding
                                
                                	Enable or Disable Flooding
                                	**type**\:   :py:class:`InterfaceTrafficFloodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFloodEnum>`
                                
                                .. attribute:: interface_flooding_unknown_unicast
                                
                                	Enable or Disable Unknown Unicast Flooding
                                	**type**\:   :py:class:`InterfaceTrafficFloodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFloodEnum>`
                                
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.name = None
                                    self.bdac_storm_control_types = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes()
                                    self.bdac_storm_control_types.parent = self
                                    self.interface_dai = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai()
                                    self.interface_dai.parent = self
                                    self.interface_flooding = None
                                    self.interface_flooding_unknown_unicast = None
                                    self.interface_igmp_snoop = None
                                    self.interface_ip_source_guard = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard()
                                    self.interface_ip_source_guard.parent = self
                                    self.interface_mac = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac()
                                    self.interface_mac.parent = self
                                    self.interface_mld_snoop = None
                                    self.interface_profile = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile()
                                    self.interface_profile.parent = self
                                    self.split_horizon = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon()
                                    self.split_horizon.parent = self
                                    self.static_mac_addresses = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses()
                                    self.static_mac_addresses.parent = self


                                class InterfaceIpSourceGuard(object):
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
                                    	**type**\:   :py:class:`L2VpnLoggingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnLoggingEnum>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.disable = None
                                        self.enable = None
                                        self.logging = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-ip-source-guard'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.disable is not None:
                                            return True

                                        if self.enable is not None:
                                            return True

                                        if self.logging is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard']['meta_info']


                                class InterfaceDai(object):
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
                                    	**type**\:   :py:class:`L2VpnLoggingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnLoggingEnum>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.disable = None
                                        self.enable = None
                                        self.interface_dai_address_validation = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation()
                                        self.interface_dai_address_validation.parent = self
                                        self.logging = None


                                    class InterfaceDaiAddressValidation(object):
                                        """
                                        Address Validation
                                        
                                        .. attribute:: destination_mac_verification
                                        
                                        	Destination MAC Verification
                                        	**type**\:   :py:class:`L2VpnVerificationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnVerificationEnum>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable Address Validation
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: ipv4_verification
                                        
                                        	IPv4 Verification
                                        	**type**\:   :py:class:`L2VpnVerificationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnVerificationEnum>`
                                        
                                        .. attribute:: source_mac_verification
                                        
                                        	Source MAC Verification
                                        	**type**\:   :py:class:`L2VpnVerificationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnVerificationEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.destination_mac_verification = None
                                            self.enable = None
                                            self.ipv4_verification = None
                                            self.source_mac_verification = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-dai-address-validation'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.destination_mac_verification is not None:
                                                return True

                                            if self.enable is not None:
                                                return True

                                            if self.ipv4_verification is not None:
                                                return True

                                            if self.source_mac_verification is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-dai'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.disable is not None:
                                            return True

                                        if self.enable is not None:
                                            return True

                                        if self.interface_dai_address_validation is not None and self.interface_dai_address_validation._has_data():
                                            return True

                                        if self.logging is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai']['meta_info']


                                class InterfaceProfile(object):
                                    """
                                    Attach a DHCP profile
                                    
                                    .. attribute:: dhcp_snooping_id
                                    
                                    	Disable DHCP snooping
                                    	**type**\:  str
                                    
                                    .. attribute:: profile_id
                                    
                                    	Set the snooping profile
                                    	**type**\:   :py:class:`InterfaceProfileEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfileEnum>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.dhcp_snooping_id = None
                                        self.profile_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-profile'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.dhcp_snooping_id is not None:
                                            return True

                                        if self.profile_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile']['meta_info']


                                class BdacStormControlTypes(object):
                                    """
                                    Storm Control
                                    
                                    .. attribute:: bdac_storm_control_type
                                    
                                    	Storm Control Type
                                    	**type**\: list of    :py:class:`BdacStormControlType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bdac_storm_control_type = YList()
                                        self.bdac_storm_control_type.parent = self
                                        self.bdac_storm_control_type.name = 'bdac_storm_control_type'


                                    class BdacStormControlType(object):
                                        """
                                        Storm Control Type
                                        
                                        .. attribute:: sctype  <key>
                                        
                                        	Storm Control Type
                                        	**type**\:   :py:class:`StormControlEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.StormControlEnum>`
                                        
                                        .. attribute:: storm_control_unit
                                        
                                        	Specify units for Storm Control Configuration
                                        	**type**\:   :py:class:`StormControlUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.sctype = None
                                            self.storm_control_unit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit()
                                            self.storm_control_unit.parent = self


                                        class StormControlUnit(object):
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
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.kbits_per_sec = None
                                                self.pkts_per_sec = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:storm-control-unit'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.kbits_per_sec is not None:
                                                    return True

                                                if self.pkts_per_sec is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.sctype is None:
                                                raise YPYModelError('Key property sctype is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bdac-storm-control-type[Cisco-IOS-XR-l2vpn-cfg:sctype = ' + str(self.sctype) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.sctype is not None:
                                                return True

                                            if self.storm_control_unit is not None and self.storm_control_unit._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bdac-storm-control-types'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.bdac_storm_control_type is not None:
                                            for child_ref in self.bdac_storm_control_type:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes']['meta_info']


                                class SplitHorizon(object):
                                    """
                                    Split Horizon
                                    
                                    .. attribute:: split_horizon_group_id
                                    
                                    	Split Horizon Group ID
                                    	**type**\:   :py:class:`SplitHorizonGroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.split_horizon_group_id = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId()
                                        self.split_horizon_group_id.parent = self


                                    class SplitHorizonGroupId(object):
                                        """
                                        Split Horizon Group ID
                                        
                                        .. attribute:: enable
                                        
                                        	Enable split horizon group
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.enable = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:split-horizon-group-id'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.enable is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:split-horizon'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.split_horizon_group_id is not None and self.split_horizon_group_id._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon']['meta_info']


                                class StaticMacAddresses(object):
                                    """
                                    Static Mac Address Table
                                    
                                    .. attribute:: static_mac_address
                                    
                                    	Static Mac Address Configuration
                                    	**type**\: list of    :py:class:`StaticMacAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.static_mac_address = YList()
                                        self.static_mac_address.parent = self
                                        self.static_mac_address.name = 'static_mac_address'


                                    class StaticMacAddress(object):
                                        """
                                        Static Mac Address Configuration
                                        
                                        .. attribute:: address  <key>
                                        
                                        	Static MAC address
                                        	**type**\:  str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.address = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.address is None:
                                                raise YPYModelError('Key property address is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:static-mac-address[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.address is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:static-mac-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.static_mac_address is not None:
                                            for child_ref in self.static_mac_address:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses']['meta_info']


                                class InterfaceMac(object):
                                    """
                                    MAC configuration commands
                                    
                                    .. attribute:: interface_mac_aging
                                    
                                    	MAC\-Aging configuration commands
                                    	**type**\:   :py:class:`InterfaceMacAging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging>`
                                    
                                    .. attribute:: interface_mac_learning
                                    
                                    	Enable Mac Learning
                                    	**type**\:   :py:class:`MacLearnEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLearnEnum>`
                                    
                                    .. attribute:: interface_mac_limit
                                    
                                    	MAC\-Limit configuration commands
                                    	**type**\:   :py:class:`InterfaceMacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit>`
                                    
                                    .. attribute:: interface_mac_port_down_flush
                                    
                                    	Enable/Disable MAC Flush When Port goes down
                                    	**type**\:   :py:class:`PortDownFlushEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.PortDownFlushEnum>`
                                    
                                    .. attribute:: interface_mac_secure
                                    
                                    	MAC Secure
                                    	**type**\:   :py:class:`InterfaceMacSecure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.interface_mac_aging = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging()
                                        self.interface_mac_aging.parent = self
                                        self.interface_mac_learning = None
                                        self.interface_mac_limit = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit()
                                        self.interface_mac_limit.parent = self
                                        self.interface_mac_port_down_flush = None
                                        self.interface_mac_secure = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure()
                                        self.interface_mac_secure.parent = self


                                    class InterfaceMacAging(object):
                                        """
                                        MAC\-Aging configuration commands
                                        
                                        .. attribute:: interface_mac_aging_time
                                        
                                        	Mac Aging Time
                                        	**type**\:  int
                                        
                                        	**range:** 300..30000
                                        
                                        .. attribute:: interface_mac_aging_type
                                        
                                        	MAC address aging type
                                        	**type**\:   :py:class:`MacAgingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacAgingEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.interface_mac_aging_time = None
                                            self.interface_mac_aging_type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-mac-aging'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.interface_mac_aging_time is not None:
                                                return True

                                            if self.interface_mac_aging_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging']['meta_info']


                                    class InterfaceMacSecure(object):
                                        """
                                        MAC Secure
                                        
                                        .. attribute:: action
                                        
                                        	MAC secure enforcement action
                                        	**type**\:   :py:class:`MacSecureActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacSecureActionEnum>`
                                        
                                        .. attribute:: disable
                                        
                                        	Disable L2 Interface MAC Secure
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable MAC Secure
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: logging
                                        
                                        	MAC Secure Logging
                                        	**type**\:   :py:class:`L2VpnLoggingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2VpnLoggingEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.action = None
                                            self.disable = None
                                            self.enable = None
                                            self.logging = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-mac-secure'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.action is not None:
                                                return True

                                            if self.disable is not None:
                                                return True

                                            if self.enable is not None:
                                                return True

                                            if self.logging is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure']['meta_info']


                                    class InterfaceMacLimit(object):
                                        """
                                        MAC\-Limit configuration commands
                                        
                                        .. attribute:: interface_mac_limit_action
                                        
                                        	Interface MAC address limit enforcement action
                                        	**type**\:   :py:class:`MacLimitActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacLimitActionEnum>`
                                        
                                        .. attribute:: interface_mac_limit_max
                                        
                                        	Number of MAC addresses on an Interface after which MAC limit action is taken
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: interface_mac_limit_notif
                                        
                                        	MAC address limit notification action in a Interface
                                        	**type**\:   :py:class:`MacNotificationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MacNotificationEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.interface_mac_limit_action = None
                                            self.interface_mac_limit_max = None
                                            self.interface_mac_limit_notif = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-mac-limit'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.interface_mac_limit_action is not None:
                                                return True

                                            if self.interface_mac_limit_max is not None:
                                                return True

                                            if self.interface_mac_limit_notif is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-mac'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.interface_mac_aging is not None and self.interface_mac_aging._has_data():
                                            return True

                                        if self.interface_mac_learning is not None:
                                            return True

                                        if self.interface_mac_limit is not None and self.interface_mac_limit._has_data():
                                            return True

                                        if self.interface_mac_port_down_flush is not None:
                                            return True

                                        if self.interface_mac_secure is not None and self.interface_mac_secure._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.name is None:
                                        raise YPYModelError('Key property name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-attachment-circuit[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.name is not None:
                                        return True

                                    if self.bdac_storm_control_types is not None and self.bdac_storm_control_types._has_data():
                                        return True

                                    if self.interface_dai is not None and self.interface_dai._has_data():
                                        return True

                                    if self.interface_flooding is not None:
                                        return True

                                    if self.interface_flooding_unknown_unicast is not None:
                                        return True

                                    if self.interface_igmp_snoop is not None:
                                        return True

                                    if self.interface_ip_source_guard is not None and self.interface_ip_source_guard._has_data():
                                        return True

                                    if self.interface_mac is not None and self.interface_mac._has_data():
                                        return True

                                    if self.interface_mld_snoop is not None:
                                        return True

                                    if self.interface_profile is not None and self.interface_profile._has_data():
                                        return True

                                    if self.split_horizon is not None and self.split_horizon._has_data():
                                        return True

                                    if self.static_mac_addresses is not None and self.static_mac_addresses._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-attachment-circuits'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.bd_attachment_circuit is not None:
                                    for child_ref in self.bd_attachment_circuit:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits']['meta_info']


                        class BdPseudowireEvpns(object):
                            """
                            List of EVPN pseudowires
                            
                            .. attribute:: bd_pseudowire_evpn
                            
                            	EVPN Pseudowire configuration
                            	**type**\: list of    :py:class:`BdPseudowireEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bd_pseudowire_evpn = YList()
                                self.bd_pseudowire_evpn.parent = self
                                self.bd_pseudowire_evpn.name = 'bd_pseudowire_evpn'


                            class BdPseudowireEvpn(object):
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.eviid = None
                                    self.acid = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.eviid is None:
                                        raise YPYModelError('Key property eviid is None')
                                    if self.acid is None:
                                        raise YPYModelError('Key property acid is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pseudowire-evpn[Cisco-IOS-XR-l2vpn-cfg:eviid = ' + str(self.eviid) + '][Cisco-IOS-XR-l2vpn-cfg:acid = ' + str(self.acid) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.eviid is not None:
                                        return True

                                    if self.acid is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pseudowire-evpns'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.bd_pseudowire_evpn is not None:
                                    for child_ref in self.bd_pseudowire_evpn:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns']['meta_info']


                        class IpSourceGuard(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.logging = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ip-source-guard'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.logging is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard']['meta_info']


                        class Dai(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.dai_address_validation = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation()
                                self.dai_address_validation.parent = self
                                self.enable = None
                                self.logging = None


                            class DaiAddressValidation(object):
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.destination_mac_verification = None
                                    self.enable = None
                                    self.ipv4_verification = None
                                    self.source_mac_verification = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:dai-address-validation'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.destination_mac_verification is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    if self.ipv4_verification is not None:
                                        return True

                                    if self.source_mac_verification is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:dai'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.dai_address_validation is not None and self.dai_address_validation._has_data():
                                    return True

                                if self.enable is not None:
                                    return True

                                if self.logging is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai']['meta_info']


                        class RoutedInterfaces(object):
                            """
                            Bridge Domain Routed Interface Table
                            
                            .. attribute:: routed_interface
                            
                            	Bridge Domain Routed Interface
                            	**type**\: list of    :py:class:`RoutedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.routed_interface = YList()
                                self.routed_interface.parent = self
                                self.routed_interface.name = 'routed_interface'


                            class RoutedInterface(object):
                                """
                                Bridge Domain Routed Interface
                                
                                .. attribute:: interface_name  <key>
                                
                                	The name of the Routed Interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: routed_interface_split_horizon_group
                                
                                	Routed interface split horizon group
                                	**type**\:   :py:class:`RoutedInterfaceSplitHorizonGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None
                                    self.routed_interface_split_horizon_group = L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup()
                                    self.routed_interface_split_horizon_group.parent = self


                                class RoutedInterfaceSplitHorizonGroup(object):
                                    """
                                    Routed interface split horizon group
                                    
                                    .. attribute:: routed_interface_split_horizon_group_core
                                    
                                    	Configure BVI under SHG 1
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.routed_interface_split_horizon_group_core = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:routed-interface-split-horizon-group'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.routed_interface_split_horizon_group_core is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYModelError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:routed-interface[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.interface_name is not None:
                                        return True

                                    if self.routed_interface_split_horizon_group is not None and self.routed_interface_split_horizon_group._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:routed-interfaces'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.routed_interface is not None:
                                    for child_ref in self.routed_interface:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domain[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            if self.access_vfis is not None and self.access_vfis._has_data():
                                return True

                            if self.bd_attachment_circuits is not None and self.bd_attachment_circuits._has_data():
                                return True

                            if self.bd_pseudowire_evpns is not None and self.bd_pseudowire_evpns._has_data():
                                return True

                            if self.bd_pseudowires is not None and self.bd_pseudowires._has_data():
                                return True

                            if self.bd_storm_controls is not None and self.bd_storm_controls._has_data():
                                return True

                            if self.bridge_description is not None:
                                return True

                            if self.bridge_domain_evis is not None and self.bridge_domain_evis._has_data():
                                return True

                            if self.bridge_domain_mac is not None and self.bridge_domain_mac._has_data():
                                return True

                            if self.bridge_domain_mtu is not None:
                                return True

                            if self.bridge_domain_pbb is not None and self.bridge_domain_pbb._has_data():
                                return True

                            if self.coupled_mode is not None:
                                return True

                            if self.dai is not None and self.dai._has_data():
                                return True

                            if self.dhcp is not None:
                                return True

                            if self.flooding is not None:
                                return True

                            if self.flooding_unknown_unicast is not None:
                                return True

                            if self.igmp_snooping is not None:
                                return True

                            if self.igmp_snooping_disable is not None:
                                return True

                            if self.ip_source_guard is not None and self.ip_source_guard._has_data():
                                return True

                            if self.member_vnis is not None and self.member_vnis._has_data():
                                return True

                            if self.mld_snooping is not None:
                                return True

                            if self.nv_satellite is not None and self.nv_satellite._has_data():
                                return True

                            if self.routed_interfaces is not None and self.routed_interfaces._has_data():
                                return True

                            if self.shutdown is not None:
                                return True

                            if self.transport_mode is not None:
                                return True

                            if self.vfis is not None and self.vfis._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domains'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.bridge_domain is not None:
                            for child_ref in self.bridge_domain:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-groups/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-group[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.bridge_domains is not None and self.bridge_domains._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.bridge_domain_group is not None:
                    for child_ref in self.bridge_domain_group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2Vpn.Database.BridgeDomainGroups']['meta_info']


        class PseudowireClasses(object):
            """
            List of pseudowire classes
            
            .. attribute:: pseudowire_class
            
            	Pseudowire class
            	**type**\: list of    :py:class:`PseudowireClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.pseudowire_class = YList()
                self.pseudowire_class.parent = self
                self.pseudowire_class.name = 'pseudowire_class'


            class PseudowireClass(object):
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.backup_disable_delay = L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay()
                    self.backup_disable_delay.parent = self
                    self.enable = None
                    self.l2tpv3_encapsulation = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation()
                    self.l2tpv3_encapsulation.parent = self
                    self.mac_withdraw = None
                    self.mpls_encapsulation = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation()
                    self.mpls_encapsulation.parent = self


                class L2Tpv3Encapsulation(object):
                    """
                    L2TPv3 encapsulation
                    
                    .. attribute:: cookie_size
                    
                    	Cookie size
                    	**type**\:   :py:class:`L2TpCookieSizeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2TpCookieSizeEnum>`
                    
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
                    	**type**\:   :py:class:`TransportModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.TransportModeEnum>`
                    
                    .. attribute:: type_of_service
                    
                    	Type of service
                    	**type**\:   :py:class:`TypeOfService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.cookie_size = None
                        self.df_bit_set = None
                        self.enable = None
                        self.path_mtu = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu()
                        self.path_mtu.parent = self
                        self.sequencing = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing()
                        self.sequencing.parent = self
                        self.signaling_protocol = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol()
                        self.signaling_protocol.parent = self
                        self.source_address = None
                        self.time_to_live = None
                        self.transport_mode = None
                        self.type_of_service = L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService()
                        self.type_of_service.parent = self


                    class Sequencing(object):
                        """
                        Sequencing
                        
                        .. attribute:: resync_threshold
                        
                        	Out of sequence threshold
                        	**type**\:  int
                        
                        	**range:** 5..65535
                        
                        	**default value**\: 5
                        
                        .. attribute:: sequencing
                        
                        	Sequencing
                        	**type**\:   :py:class:`L2Tpv3SequencingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Tpv3SequencingEnum>`
                        
                        	**default value**\: off
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.resync_threshold = None
                            self.sequencing = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:sequencing'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.resync_threshold is not None:
                                return True

                            if self.sequencing is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing']['meta_info']


                    class TypeOfService(object):
                        """
                        Type of service
                        
                        .. attribute:: type_of_service_mode
                        
                        	Type of service mode
                        	**type**\:   :py:class:`TypeOfServiceModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.TypeOfServiceModeEnum>`
                        
                        .. attribute:: type_of_service_value
                        
                        	Type of service value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.type_of_service_mode = None
                            self.type_of_service_value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:type-of-service'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.type_of_service_mode is not None:
                                return True

                            if self.type_of_service_value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService']['meta_info']


                    class SignalingProtocol(object):
                        """
                        L2TPv3 signaling protocol
                        
                        .. attribute:: l2tpv3_class_name
                        
                        	Name of the L2TPv3 class name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: protocol
                        
                        	L2TPv3 signaling protocol
                        	**type**\:   :py:class:`L2TpSignalingProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2TpSignalingProtocolEnum>`
                        
                        	**default value**\: l2tpv3
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.l2tpv3_class_name = None
                            self.protocol = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:signaling-protocol'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.l2tpv3_class_name is not None:
                                return True

                            if self.protocol is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol']['meta_info']


                    class PathMtu(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.enable = None
                            self.max_path_mtu = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:path-mtu'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.enable is not None:
                                return True

                            if self.max_path_mtu is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tpv3-encapsulation'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.cookie_size is not None:
                            return True

                        if self.df_bit_set is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.path_mtu is not None and self.path_mtu._has_data():
                            return True

                        if self.sequencing is not None and self.sequencing._has_data():
                            return True

                        if self.signaling_protocol is not None and self.signaling_protocol._has_data():
                            return True

                        if self.source_address is not None:
                            return True

                        if self.time_to_live is not None:
                            return True

                        if self.transport_mode is not None:
                            return True

                        if self.type_of_service is not None and self.type_of_service._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation']['meta_info']


                class BackupDisableDelay(object):
                    """
                    Back Up Pseudowire class
                    
                    .. attribute:: disable_backup
                    
                    	Disable backup delay
                    	**type**\:  int
                    
                    	**range:** 0..180
                    
                    .. attribute:: type
                    
                    	Delay or Never
                    	**type**\:   :py:class:`BackupDisableEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BackupDisableEnum>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.disable_backup = None
                        self.type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-disable-delay'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.disable_backup is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay']['meta_info']


                class MplsEncapsulation(object):
                    """
                    MPLS encapsulation
                    
                    .. attribute:: control_word
                    
                    	Enable control word
                    	**type**\:   :py:class:`ControlWordEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.ControlWordEnum>`
                    
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
                    	**type**\:   :py:class:`PwSwitchingPointTlvEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.PwSwitchingPointTlvEnum>`
                    
                    .. attribute:: sequencing
                    
                    	Sequencing
                    	**type**\:   :py:class:`Sequencing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing>`
                    
                    .. attribute:: signaling_protocol
                    
                    	MPLS signaling protocol
                    	**type**\:   :py:class:`MplsSignalingProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MplsSignalingProtocolEnum>`
                    
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
                    	**type**\:   :py:class:`TransportModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.TransportModeEnum>`
                    
                    .. attribute:: vccv_type
                    
                    	VCCV verification type
                    	**type**\:   :py:class:`VccvVerificationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.VccvVerificationEnum>`
                    
                    	**default value**\: lsp-ping
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.control_word = None
                        self.enable = None
                        self.load_balance_group = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup()
                        self.load_balance_group.parent = self
                        self.mpls_redundancy = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy()
                        self.mpls_redundancy.parent = self
                        self.preferred_path = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath()
                        self.preferred_path.parent = self
                        self.pw_switching_tlv = None
                        self.sequencing = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing()
                        self.sequencing.parent = self
                        self.signaling_protocol = None
                        self.source_address = None
                        self.static_tag_rewrite = None
                        self.transport_mode = None
                        self.vccv_type = None


                    class Sequencing(object):
                        """
                        Sequencing
                        
                        .. attribute:: resync_threshold
                        
                        	Out of sequence threshold
                        	**type**\:  int
                        
                        	**range:** 5..65535
                        
                        	**default value**\: 5
                        
                        .. attribute:: sequencing
                        
                        	Sequencing
                        	**type**\:   :py:class:`MplsSequencingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.MplsSequencingEnum>`
                        
                        	**default value**\: off
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.resync_threshold = None
                            self.sequencing = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:sequencing'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.resync_threshold is not None:
                                return True

                            if self.sequencing is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing']['meta_info']


                    class MplsRedundancy(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.redundancy_initial_delay = None
                            self.redundancy_one_way = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mpls-redundancy'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.redundancy_initial_delay is not None:
                                return True

                            if self.redundancy_one_way is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy']['meta_info']


                    class PreferredPath(object):
                        """
                        Preferred path
                        
                        .. attribute:: fallback_disable
                        
                        	Fallback disable
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: interface_tunnel_number
                        
                        	Interface Tunnel number for preferred path
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: type
                        
                        	Preferred Path Type
                        	**type**\:   :py:class:`PreferredPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.PreferredPathEnum>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.fallback_disable = None
                            self.interface_tunnel_number = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:preferred-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.fallback_disable is not None:
                                return True

                            if self.interface_tunnel_number is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath']['meta_info']


                    class LoadBalanceGroup(object):
                        """
                        Load Balancing
                        
                        .. attribute:: flow_label_load_balance
                        
                        	Enable Flow Label based load balancing
                        	**type**\:   :py:class:`FlowLabelLoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance>`
                        
                        .. attribute:: flow_label_load_balance_code
                        
                        	Enable Legacy Flow Label TLV code
                        	**type**\:   :py:class:`FlowLabelTlvCodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelTlvCodeEnum>`
                        
                        .. attribute:: pw_label_load_balance
                        
                        	Enable PW Label based Load Balancing
                        	**type**\:   :py:class:`LoadBalanceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.LoadBalanceEnum>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.flow_label_load_balance = L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance()
                            self.flow_label_load_balance.parent = self
                            self.flow_label_load_balance_code = None
                            self.pw_label_load_balance = None


                        class FlowLabelLoadBalance(object):
                            """
                            Enable Flow Label based load balancing
                            
                            .. attribute:: flow_label
                            
                            	Flow Label load balance type
                            	**type**\:   :py:class:`FlowLabelLoadBalanceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalanceEnum>`
                            
                            .. attribute:: static
                            
                            	Static Flow Label
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.flow_label = None
                                self.static = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:flow-label-load-balance'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.flow_label is not None:
                                    return True

                                if self.static is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:load-balance-group'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.flow_label_load_balance is not None and self.flow_label_load_balance._has_data():
                                return True

                            if self.flow_label_load_balance_code is not None:
                                return True

                            if self.pw_label_load_balance is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mpls-encapsulation'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.control_word is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.load_balance_group is not None and self.load_balance_group._has_data():
                            return True

                        if self.mpls_redundancy is not None and self.mpls_redundancy._has_data():
                            return True

                        if self.preferred_path is not None and self.preferred_path._has_data():
                            return True

                        if self.pw_switching_tlv is not None:
                            return True

                        if self.sequencing is not None and self.sequencing._has_data():
                            return True

                        if self.signaling_protocol is not None:
                            return True

                        if self.source_address is not None:
                            return True

                        if self.static_tag_rewrite is not None:
                            return True

                        if self.transport_mode is not None:
                            return True

                        if self.vccv_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:pseudowire-classes/Cisco-IOS-XR-l2vpn-cfg:pseudowire-class[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.backup_disable_delay is not None and self.backup_disable_delay._has_data():
                        return True

                    if self.enable is not None:
                        return True

                    if self.l2tpv3_encapsulation is not None and self.l2tpv3_encapsulation._has_data():
                        return True

                    if self.mac_withdraw is not None:
                        return True

                    if self.mpls_encapsulation is not None and self.mpls_encapsulation._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:pseudowire-classes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.pseudowire_class is not None:
                    for child_ref in self.pseudowire_class:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2Vpn.Database.PseudowireClasses']['meta_info']


        class FlexibleXconnectServiceTable(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vlan_aware_flexible_xconnect_services = L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices()
                self.vlan_aware_flexible_xconnect_services.parent = self
                self.vlan_unaware_flexible_xconnect_services = L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices()
                self.vlan_unaware_flexible_xconnect_services.parent = self


            class VlanUnawareFlexibleXconnectServices(object):
                """
                List of Vlan\-Unaware Flexible XConnect
                Services
                
                .. attribute:: vlan_unaware_flexible_xconnect_service
                
                	Flexible XConnect Service
                	**type**\: list of    :py:class:`VlanUnawareFlexibleXconnectService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.vlan_unaware_flexible_xconnect_service = YList()
                    self.vlan_unaware_flexible_xconnect_service.parent = self
                    self.vlan_unaware_flexible_xconnect_service.name = 'vlan_unaware_flexible_xconnect_service'


                class VlanUnawareFlexibleXconnectService(object):
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.vlan_unaware_fxc_attachment_circuits = L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits()
                        self.vlan_unaware_fxc_attachment_circuits.parent = self
                        self.vlan_unaware_fxc_pseudowire_evpns = L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns()
                        self.vlan_unaware_fxc_pseudowire_evpns.parent = self


                    class VlanUnawareFxcAttachmentCircuits(object):
                        """
                        List of attachment circuits
                        
                        .. attribute:: vlan_unaware_fxc_attachment_circuit
                        
                        	Attachment circuit interface
                        	**type**\: list of    :py:class:`VlanUnawareFxcAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vlan_unaware_fxc_attachment_circuit = YList()
                            self.vlan_unaware_fxc_attachment_circuit.parent = self
                            self.vlan_unaware_fxc_attachment_circuit.name = 'vlan_unaware_fxc_attachment_circuit'


                        class VlanUnawareFxcAttachmentCircuit(object):
                            """
                            Attachment circuit interface
                            
                            .. attribute:: name  <key>
                            
                            	Name of the attachment circuit interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.name is None:
                                    raise YPYModelError('Key property name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vlan-unaware-fxc-attachment-circuit[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vlan-unaware-fxc-attachment-circuits'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.vlan_unaware_fxc_attachment_circuit is not None:
                                for child_ref in self.vlan_unaware_fxc_attachment_circuit:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits']['meta_info']


                    class VlanUnawareFxcPseudowireEvpns(object):
                        """
                        List of EVPN Services
                        
                        .. attribute:: vlan_unaware_fxc_pseudowire_evpn
                        
                        	EVPN FXC Service Configuration
                        	**type**\: list of    :py:class:`VlanUnawareFxcPseudowireEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vlan_unaware_fxc_pseudowire_evpn = YList()
                            self.vlan_unaware_fxc_pseudowire_evpn.parent = self
                            self.vlan_unaware_fxc_pseudowire_evpn.name = 'vlan_unaware_fxc_pseudowire_evpn'


                        class VlanUnawareFxcPseudowireEvpn(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.eviid = None
                                self.acid = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.eviid is None:
                                    raise YPYModelError('Key property eviid is None')
                                if self.acid is None:
                                    raise YPYModelError('Key property acid is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vlan-unaware-fxc-pseudowire-evpn[Cisco-IOS-XR-l2vpn-cfg:eviid = ' + str(self.eviid) + '][Cisco-IOS-XR-l2vpn-cfg:acid = ' + str(self.acid) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.eviid is not None:
                                    return True

                                if self.acid is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vlan-unaware-fxc-pseudowire-evpns'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.vlan_unaware_fxc_pseudowire_evpn is not None:
                                for child_ref in self.vlan_unaware_fxc_pseudowire_evpn:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns']['meta_info']

                    @property
                    def _common_path(self):
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:flexible-xconnect-service-table/Cisco-IOS-XR-l2vpn-cfg:vlan-unaware-flexible-xconnect-services/Cisco-IOS-XR-l2vpn-cfg:vlan-unaware-flexible-xconnect-service[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        if self.vlan_unaware_fxc_attachment_circuits is not None and self.vlan_unaware_fxc_attachment_circuits._has_data():
                            return True

                        if self.vlan_unaware_fxc_pseudowire_evpns is not None and self.vlan_unaware_fxc_pseudowire_evpns._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:flexible-xconnect-service-table/Cisco-IOS-XR-l2vpn-cfg:vlan-unaware-flexible-xconnect-services'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vlan_unaware_flexible_xconnect_service is not None:
                        for child_ref in self.vlan_unaware_flexible_xconnect_service:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices']['meta_info']


            class VlanAwareFlexibleXconnectServices(object):
                """
                List of Vlan\-Aware Flexible XConnect Services
                
                .. attribute:: vlan_aware_flexible_xconnect_service
                
                	Flexible XConnect Service
                	**type**\: list of    :py:class:`VlanAwareFlexibleXconnectService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.vlan_aware_flexible_xconnect_service = YList()
                    self.vlan_aware_flexible_xconnect_service.parent = self
                    self.vlan_aware_flexible_xconnect_service.name = 'vlan_aware_flexible_xconnect_service'


                class VlanAwareFlexibleXconnectService(object):
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.eviid = None
                        self.vlan_aware_fxc_attachment_circuits = L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits()
                        self.vlan_aware_fxc_attachment_circuits.parent = self


                    class VlanAwareFxcAttachmentCircuits(object):
                        """
                        List of attachment circuits
                        
                        .. attribute:: vlan_aware_fxc_attachment_circuit
                        
                        	Attachment circuit interface
                        	**type**\: list of    :py:class:`VlanAwareFxcAttachmentCircuit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vlan_aware_fxc_attachment_circuit = YList()
                            self.vlan_aware_fxc_attachment_circuit.parent = self
                            self.vlan_aware_fxc_attachment_circuit.name = 'vlan_aware_fxc_attachment_circuit'


                        class VlanAwareFxcAttachmentCircuit(object):
                            """
                            Attachment circuit interface
                            
                            .. attribute:: name  <key>
                            
                            	Name of the attachment circuit interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.name is None:
                                    raise YPYModelError('Key property name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vlan-aware-fxc-attachment-circuit[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vlan-aware-fxc-attachment-circuits'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.vlan_aware_fxc_attachment_circuit is not None:
                                for child_ref in self.vlan_aware_fxc_attachment_circuit:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits']['meta_info']

                    @property
                    def _common_path(self):
                        if self.eviid is None:
                            raise YPYModelError('Key property eviid is None')

                        return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:flexible-xconnect-service-table/Cisco-IOS-XR-l2vpn-cfg:vlan-aware-flexible-xconnect-services/Cisco-IOS-XR-l2vpn-cfg:vlan-aware-flexible-xconnect-service[Cisco-IOS-XR-l2vpn-cfg:eviid = ' + str(self.eviid) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.eviid is not None:
                            return True

                        if self.vlan_aware_fxc_attachment_circuits is not None and self.vlan_aware_fxc_attachment_circuits._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:flexible-xconnect-service-table/Cisco-IOS-XR-l2vpn-cfg:vlan-aware-flexible-xconnect-services'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vlan_aware_flexible_xconnect_service is not None:
                        for child_ref in self.vlan_aware_flexible_xconnect_service:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:flexible-xconnect-service-table'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vlan_aware_flexible_xconnect_services is not None and self.vlan_aware_flexible_xconnect_services._has_data():
                    return True

                if self.vlan_unaware_flexible_xconnect_services is not None and self.vlan_unaware_flexible_xconnect_services._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2Vpn.Database.FlexibleXconnectServiceTable']['meta_info']


        class Redundancy(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.iccp_redundancy_groups = L2Vpn.Database.Redundancy.IccpRedundancyGroups()
                self.iccp_redundancy_groups.parent = self


            class IccpRedundancyGroups(object):
                """
                List of Inter\-Chassis Communication Protocol
                redundancy groups
                
                .. attribute:: iccp_redundancy_group
                
                	ICCP Redundancy group
                	**type**\: list of    :py:class:`IccpRedundancyGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.iccp_redundancy_group = YList()
                    self.iccp_redundancy_group.parent = self
                    self.iccp_redundancy_group.name = 'iccp_redundancy_group'


                class IccpRedundancyGroup(object):
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.group_id = None
                        self.iccp_interfaces = L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces()
                        self.iccp_interfaces.parent = self
                        self.multi_homing_node_id = None


                    class IccpInterfaces(object):
                        """
                        List of interfaces
                        
                        .. attribute:: iccp_interface
                        
                        	Interface name
                        	**type**\: list of    :py:class:`IccpInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.iccp_interface = YList()
                            self.iccp_interface.parent = self
                            self.iccp_interface.name = 'iccp_interface'


                        class IccpInterface(object):
                            """
                            Interface name
                            
                            .. attribute:: interface_name  <key>
                            
                            	Interface name
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None
                                self.mac_flush_tcn = None
                                self.primary_vlan_range = None
                                self.recovery_delay = None
                                self.secondary_vlan_range = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYModelError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:iccp-interface[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.interface_name is not None:
                                    return True

                                if self.mac_flush_tcn is not None:
                                    return True

                                if self.primary_vlan_range is not None:
                                    return True

                                if self.recovery_delay is not None:
                                    return True

                                if self.secondary_vlan_range is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:iccp-interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.iccp_interface is not None:
                                for child_ref in self.iccp_interface:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces']['meta_info']

                    @property
                    def _common_path(self):
                        if self.group_id is None:
                            raise YPYModelError('Key property group_id is None')

                        return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:redundancy/Cisco-IOS-XR-l2vpn-cfg:iccp-redundancy-groups/Cisco-IOS-XR-l2vpn-cfg:iccp-redundancy-group[Cisco-IOS-XR-l2vpn-cfg:group-id = ' + str(self.group_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.group_id is not None:
                            return True

                        if self.iccp_interfaces is not None and self.iccp_interfaces._has_data():
                            return True

                        if self.multi_homing_node_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:redundancy/Cisco-IOS-XR-l2vpn-cfg:iccp-redundancy-groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.iccp_redundancy_group is not None:
                        for child_ref in self.iccp_redundancy_group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2Vpn.Database.Redundancy.IccpRedundancyGroups']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:redundancy'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.iccp_redundancy_groups is not None and self.iccp_redundancy_groups._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2Vpn.Database.Redundancy']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.bridge_domain_groups is not None and self.bridge_domain_groups._has_data():
                return True

            if self.flexible_xconnect_service_table is not None and self.flexible_xconnect_service_table._has_data():
                return True

            if self.g8032_rings is not None and self.g8032_rings._has_data():
                return True

            if self.pseudowire_classes is not None and self.pseudowire_classes._has_data():
                return True

            if self.redundancy is not None and self.redundancy._has_data():
                return True

            if self.xconnect_groups is not None and self.xconnect_groups._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2Vpn.Database']['meta_info']


    class Pbb(object):
        """
        L2VPN PBB Global
        
        .. attribute:: backbone_source_mac
        
        	Backbone Source MAC
        	**type**\:  str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.backbone_source_mac = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:pbb'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.backbone_source_mac is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2Vpn.Pbb']['meta_info']


    class AutoDiscovery(object):
        """
        Global auto\-discovery attributes
        
        .. attribute:: bgp_signaling
        
        	Global bgp signaling attributes
        	**type**\:   :py:class:`BgpSignaling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.AutoDiscovery.BgpSignaling>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.bgp_signaling = L2Vpn.AutoDiscovery.BgpSignaling()
            self.bgp_signaling.parent = self


        class BgpSignaling(object):
            """
            Global bgp signaling attributes
            
            .. attribute:: mtu_mismatch_ignore
            
            	Ignore MTU mismatch for auto\-discovered pseudowires
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.mtu_mismatch_ignore = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:auto-discovery/Cisco-IOS-XR-l2vpn-cfg:bgp-signaling'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.mtu_mismatch_ignore is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2Vpn.AutoDiscovery.BgpSignaling']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:auto-discovery'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.bgp_signaling is not None and self.bgp_signaling._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2Vpn.AutoDiscovery']['meta_info']


    class Utility(object):
        """
        L2VPN utilities
        
        .. attribute:: logging
        
        	L2VPN logging utility
        	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Utility.Logging>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.logging = L2Vpn.Utility.Logging()
            self.logging.parent = self


        class Logging(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bridge_domain_state_change = None
                self.nsr_state_change = None
                self.pseudowire_state_change = None
                self.pwhe_replication_state_change = None
                self.vfi = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:utility/Cisco-IOS-XR-l2vpn-cfg:logging'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.bridge_domain_state_change is not None:
                    return True

                if self.nsr_state_change is not None:
                    return True

                if self.pseudowire_state_change is not None:
                    return True

                if self.pwhe_replication_state_change is not None:
                    return True

                if self.vfi is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2Vpn.Utility.Logging']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:utility'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.logging is not None and self.logging._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2Vpn.Utility']['meta_info']


    class Snmp(object):
        """
        SNMP related configuration
        
        .. attribute:: mib
        
        	MIB related configuration
        	**type**\:   :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Snmp.Mib>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.mib = L2Vpn.Snmp.Mib()
            self.mib.parent = self


        class Mib(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.mib_interface = L2Vpn.Snmp.Mib.MibInterface()
                self.mib_interface.parent = self
                self.mib_pseudowire = L2Vpn.Snmp.Mib.MibPseudowire()
                self.mib_pseudowire.parent = self


            class MibInterface(object):
                """
                Interface related configuration for MIB
                
                .. attribute:: format
                
                	MIB interface name output format
                	**type**\:   :py:class:`Format <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.L2Vpn.Snmp.Mib.MibInterface.Format>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.format = L2Vpn.Snmp.Mib.MibInterface.Format()
                    self.format.parent = self


                class Format(object):
                    """
                    MIB interface name output format
                    
                    .. attribute:: external_interface_format
                    
                    	Set MIB interface name output in slash format (/)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.external_interface_format = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:snmp/Cisco-IOS-XR-l2vpn-cfg:mib/Cisco-IOS-XR-l2vpn-cfg:mib-interface/Cisco-IOS-XR-l2vpn-cfg:format'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.external_interface_format is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2Vpn.Snmp.Mib.MibInterface.Format']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:snmp/Cisco-IOS-XR-l2vpn-cfg:mib/Cisco-IOS-XR-l2vpn-cfg:mib-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.format is not None and self.format._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2Vpn.Snmp.Mib.MibInterface']['meta_info']


            class MibPseudowire(object):
                """
                Pseudowire related configuration for MIB
                
                .. attribute:: statistics
                
                	Enable pseudowire statistics in MIB output
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.statistics = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:snmp/Cisco-IOS-XR-l2vpn-cfg:mib/Cisco-IOS-XR-l2vpn-cfg:mib-pseudowire'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.statistics is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2Vpn.Snmp.Mib.MibPseudowire']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:snmp/Cisco-IOS-XR-l2vpn-cfg:mib'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.mib_interface is not None and self.mib_interface._has_data():
                    return True

                if self.mib_pseudowire is not None and self.mib_pseudowire._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2Vpn.Snmp.Mib']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:snmp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.mib is not None and self.mib._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2Vpn.Snmp']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.auto_discovery is not None and self.auto_discovery._has_data():
            return True

        if self.capability is not None:
            return True

        if self.database is not None and self.database._has_data():
            return True

        if self.enable is not None:
            return True

        if self.l2vpn_router_id is not None:
            return True

        if self.load_balance is not None:
            return True

        if self.mspw_description is not None:
            return True

        if self.mtu_mismatch_ignore is not None:
            return True

        if self.neighbor is not None and self.neighbor._has_data():
            return True

        if self.nsr is not None:
            return True

        if self.pbb is not None and self.pbb._has_data():
            return True

        if self.pw_grouping is not None:
            return True

        if self.pw_routing is not None and self.pw_routing._has_data():
            return True

        if self.pw_status_disable is not None:
            return True

        if self.pwoam_refresh is not None:
            return True

        if self.snmp is not None and self.snmp._has_data():
            return True

        if self.tcn_propagation is not None:
            return True

        if self.utility is not None and self.utility._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2Vpn']['meta_info']


class GenericInterfaceLists(object):
    """
    generic interface lists
    
    .. attribute:: generic_interface
    
    	Bridge group
    	**type**\: list of    :py:class:`GenericInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.GenericInterfaceLists.GenericInterface>`
    
    

    """

    _prefix = 'l2vpn-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.generic_interface = YList()
        self.generic_interface.parent = self
        self.generic_interface.name = 'generic_interface'


    class GenericInterface(object):
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
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.generic_interface_list_name = None
            self.enable = None
            self.interfaces = GenericInterfaceLists.GenericInterface.Interfaces()
            self.interfaces.parent = self


        class Interfaces(object):
            """
            Interface table
            
            .. attribute:: interface
            
            	Interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.GenericInterfaceLists.GenericInterface.Interfaces.Interface>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                Interface
                
                .. attribute:: interface_name  <key>
                
                	Name of the interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: enable
                
                	Enable interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.enable = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.enable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['GenericInterfaceLists.GenericInterface.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['GenericInterfaceLists.GenericInterface.Interfaces']['meta_info']

        @property
        def _common_path(self):
            if self.generic_interface_list_name is None:
                raise YPYModelError('Key property generic_interface_list_name is None')

            return '/Cisco-IOS-XR-l2vpn-cfg:generic-interface-lists/Cisco-IOS-XR-l2vpn-cfg:generic-interface[Cisco-IOS-XR-l2vpn-cfg:generic-interface-list-name = ' + str(self.generic_interface_list_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.generic_interface_list_name is not None:
                return True

            if self.enable is not None:
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['GenericInterfaceLists.GenericInterface']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-l2vpn-cfg:generic-interface-lists'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.generic_interface is not None:
            for child_ref in self.generic_interface:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['GenericInterfaceLists']['meta_info']


class Evpn(object):
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
    _revision = '2015-11-09'

    def __init__(self):
        self.enable = None
        self.evpn_tables = Evpn.EvpnTables()
        self.evpn_tables.parent = self


    class EvpnTables(object):
        """
        EVPN submodes
        
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
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: evpn_timers
        
        	Enter EVPN timers configuration submode
        	**type**\:   :py:class:`EvpnTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnTimers>`
        
        .. attribute:: evpn_virtual_access_pws
        
        	Virtual Access Pseudowire interfaces
        	**type**\:   :py:class:`EvpnVirtualAccessPws <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws>`
        
        .. attribute:: evpn_virtual_access_vfis
        
        	Virtual Access VFI interfaces
        	**type**\:   :py:class:`EvpnVirtualAccessVfis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis>`
        
        .. attribute:: evpnbgp_auto_discovery
        
        	Enable Autodiscovery BGP in EVPN
        	**type**\:   :py:class:`EvpnbgpAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnbgpAutoDiscovery>`
        
        .. attribute:: evpnevis
        
        	Enter EVPN EVI configuration submode
        	**type**\:   :py:class:`Evpnevis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.evpn_interfaces = Evpn.EvpnTables.EvpnInterfaces()
            self.evpn_interfaces.parent = self
            self.evpn_load_balancing = Evpn.EvpnTables.EvpnLoadBalancing()
            self.evpn_load_balancing.parent = self
            self.evpn_logging = Evpn.EvpnTables.EvpnLogging()
            self.evpn_logging.parent = self
            self.evpn_source_interface = None
            self.evpn_timers = Evpn.EvpnTables.EvpnTimers()
            self.evpn_timers.parent = self
            self.evpn_virtual_access_pws = Evpn.EvpnTables.EvpnVirtualAccessPws()
            self.evpn_virtual_access_pws.parent = self
            self.evpn_virtual_access_vfis = Evpn.EvpnTables.EvpnVirtualAccessVfis()
            self.evpn_virtual_access_vfis.parent = self
            self.evpnbgp_auto_discovery = Evpn.EvpnTables.EvpnbgpAutoDiscovery()
            self.evpnbgp_auto_discovery.parent = self
            self.evpnevis = Evpn.EvpnTables.Evpnevis()
            self.evpnevis.parent = self


        class EvpnTimers(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.evpn_peering = None
                self.evpn_recovery = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-timers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.evpn_peering is not None:
                    return True

                if self.evpn_recovery is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.EvpnTimers']['meta_info']


        class Evpnevis(object):
            """
            Enter EVPN EVI configuration submode
            
            .. attribute:: evpnevi
            
            	Enter EVPN EVI configuration submode
            	**type**\: list of    :py:class:`Evpnevi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.evpnevi = YList()
                self.evpnevi.parent = self
                self.evpnevi.name = 'evpnevi'


            class Evpnevi(object):
                """
                Enter EVPN EVI configuration submode
                
                .. attribute:: eviid  <key>
                
                	EVI ID
                	**type**\:  int
                
                	**range:** 1..65534
                
                .. attribute:: evi_advertise_mac
                
                	Advertise MAC only routes
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evi_load_balancing
                
                	Enter EVI Loadbalancing configuration submode
                	**type**\:   :py:class:`EviLoadBalancing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing>`
                
                .. attribute:: evi_reorig_disable
                
                	Disable route re\-origination
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evi_stitching
                
                	Enable RT stitching for MPLS fabric
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evi_unknown_unicast_flooding_disable
                
                	Disable Unknown Unicast Flooding on this EVI
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evpn_evi_cw_disable
                
                	CW disable for EVPN EVI
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: evpnevi_description
                
                	Description for EVPN EVI
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: evpnevibgp_auto_discovery
                
                	Enable Autodiscovery BGP in EVPN EVI
                	**type**\:   :py:class:`EvpnevibgpAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.eviid = None
                    self.evi_advertise_mac = None
                    self.evi_load_balancing = Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing()
                    self.evi_load_balancing.parent = self
                    self.evi_reorig_disable = None
                    self.evi_stitching = None
                    self.evi_unknown_unicast_flooding_disable = None
                    self.evpn_evi_cw_disable = None
                    self.evpnevi_description = None
                    self.evpnevibgp_auto_discovery = Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery()
                    self.evpnevibgp_auto_discovery.parent = self


                class EviLoadBalancing(object):
                    """
                    Enter EVI Loadbalancing configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable EVI Loadbalancing
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evi_flow_label
                    
                    	Enable Flow Label based load balancing
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.evi_flow_label = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evi-load-balancing'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable is not None:
                            return True

                        if self.evi_flow_label is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing']['meta_info']


                class EvpnevibgpAutoDiscovery(object):
                    """
                    Enable Autodiscovery BGP in EVPN EVI
                    
                    .. attribute:: enable
                    
                    	Enable Autodiscovery BGP
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: evpn_route_distinguisher
                    
                    	Route Distinguisher
                    	**type**\:   :py:class:`EvpnRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteDistinguisher>`
                    
                    .. attribute:: evpn_route_targets
                    
                    	Route Target
                    	**type**\:   :py:class:`EvpnRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets>`
                    
                    .. attribute:: table_policy
                    
                    	Table Policy for installation of forwarding data to L2FIB
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.evpn_route_distinguisher = Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteDistinguisher()
                        self.evpn_route_distinguisher.parent = self
                        self.evpn_route_targets = Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets()
                        self.evpn_route_targets.parent = self
                        self.table_policy = None


                    class EvpnRouteTargets(object):
                        """
                        Route Target
                        
                        .. attribute:: evpn_route_target_as
                        
                        	Name of the Route Target
                        	**type**\: list of    :py:class:`EvpnRouteTargetAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs>`
                        
                        .. attribute:: evpn_route_target_ipv4_address
                        
                        	Name of the Route Target
                        	**type**\: list of    :py:class:`EvpnRouteTargetIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address>`
                        
                        .. attribute:: evpn_route_target_none
                        
                        	Name of the Route Target
                        	**type**\: list of    :py:class:`EvpnRouteTargetNone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.evpn_route_target_as = YList()
                            self.evpn_route_target_as.parent = self
                            self.evpn_route_target_as.name = 'evpn_route_target_as'
                            self.evpn_route_target_ipv4_address = YList()
                            self.evpn_route_target_ipv4_address.parent = self
                            self.evpn_route_target_ipv4_address.name = 'evpn_route_target_ipv4_address'
                            self.evpn_route_target_none = YList()
                            self.evpn_route_target_none.parent = self
                            self.evpn_route_target_none.name = 'evpn_route_target_none'


                        class EvpnRouteTargetAs(object):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  <key>
                            
                            	Format of the route target
                            	**type**\:   :py:class:`BgpRouteTargetFormatEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormatEnum>`
                            
                            .. attribute:: role  <key>
                            
                            	Role of the router target type
                            	**type**\:   :py:class:`BgpRouteTargetRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRoleEnum>`
                            
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
                            	**type**\:   :py:class:`BgpRouteTargetEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetEnum>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.format = None
                                self.role = None
                                self.as_ = None
                                self.as_index = None
                                self.stitching = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.format is None:
                                    raise YPYModelError('Key property format is None')
                                if self.role is None:
                                    raise YPYModelError('Key property role is None')
                                if self.as_ is None:
                                    raise YPYModelError('Key property as_ is None')
                                if self.as_index is None:
                                    raise YPYModelError('Key property as_index is None')
                                if self.stitching is None:
                                    raise YPYModelError('Key property stitching is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-route-target-as[Cisco-IOS-XR-l2vpn-cfg:format = ' + str(self.format) + '][Cisco-IOS-XR-l2vpn-cfg:role = ' + str(self.role) + '][Cisco-IOS-XR-l2vpn-cfg:as = ' + str(self.as_) + '][Cisco-IOS-XR-l2vpn-cfg:as-index = ' + str(self.as_index) + '][Cisco-IOS-XR-l2vpn-cfg:stitching = ' + str(self.stitching) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.format is not None:
                                    return True

                                if self.role is not None:
                                    return True

                                if self.as_ is not None:
                                    return True

                                if self.as_index is not None:
                                    return True

                                if self.stitching is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs']['meta_info']


                        class EvpnRouteTargetNone(object):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  <key>
                            
                            	Format of the route target
                            	**type**\:   :py:class:`BgpRouteTargetFormatEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormatEnum>`
                            
                            .. attribute:: role  <key>
                            
                            	Role of the router target type
                            	**type**\:   :py:class:`BgpRouteTargetRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRoleEnum>`
                            
                            .. attribute:: stitching  <key>
                            
                            	whether RT is Stitching RT
                            	**type**\:   :py:class:`BgpRouteTargetEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetEnum>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.format = None
                                self.role = None
                                self.stitching = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.format is None:
                                    raise YPYModelError('Key property format is None')
                                if self.role is None:
                                    raise YPYModelError('Key property role is None')
                                if self.stitching is None:
                                    raise YPYModelError('Key property stitching is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-route-target-none[Cisco-IOS-XR-l2vpn-cfg:format = ' + str(self.format) + '][Cisco-IOS-XR-l2vpn-cfg:role = ' + str(self.role) + '][Cisco-IOS-XR-l2vpn-cfg:stitching = ' + str(self.stitching) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.format is not None:
                                    return True

                                if self.role is not None:
                                    return True

                                if self.stitching is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone']['meta_info']


                        class EvpnRouteTargetIpv4Address(object):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format  <key>
                            
                            	Format of the route target
                            	**type**\:   :py:class:`BgpRouteTargetFormatEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormatEnum>`
                            
                            .. attribute:: role  <key>
                            
                            	Role of the router target type
                            	**type**\:   :py:class:`BgpRouteTargetRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRoleEnum>`
                            
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
                            	**type**\:   :py:class:`BgpRouteTargetEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetEnum>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.format = None
                                self.role = None
                                self.address = None
                                self.addr_index = None
                                self.stitching = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.format is None:
                                    raise YPYModelError('Key property format is None')
                                if self.role is None:
                                    raise YPYModelError('Key property role is None')
                                if self.address is None:
                                    raise YPYModelError('Key property address is None')
                                if self.addr_index is None:
                                    raise YPYModelError('Key property addr_index is None')
                                if self.stitching is None:
                                    raise YPYModelError('Key property stitching is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-route-target-ipv4-address[Cisco-IOS-XR-l2vpn-cfg:format = ' + str(self.format) + '][Cisco-IOS-XR-l2vpn-cfg:role = ' + str(self.role) + '][Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-l2vpn-cfg:addr-index = ' + str(self.addr_index) + '][Cisco-IOS-XR-l2vpn-cfg:stitching = ' + str(self.stitching) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.format is not None:
                                    return True

                                if self.role is not None:
                                    return True

                                if self.address is not None:
                                    return True

                                if self.addr_index is not None:
                                    return True

                                if self.stitching is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-route-targets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.evpn_route_target_as is not None:
                                for child_ref in self.evpn_route_target_as:
                                    if child_ref._has_data():
                                        return True

                            if self.evpn_route_target_ipv4_address is not None:
                                for child_ref in self.evpn_route_target_ipv4_address:
                                    if child_ref._has_data():
                                        return True

                            if self.evpn_route_target_none is not None:
                                for child_ref in self.evpn_route_target_none:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets']['meta_info']


                    class EvpnRouteDistinguisher(object):
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
                        	**type**\:   :py:class:`BgpRouteDistinguisherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisherEnum>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.addr_index = None
                            self.address = None
                            self.as_ = None
                            self.as_index = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-route-distinguisher'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.addr_index is not None:
                                return True

                            if self.address is not None:
                                return True

                            if self.as_ is not None:
                                return True

                            if self.as_index is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteDistinguisher']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpnevibgp-auto-discovery'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable is not None:
                            return True

                        if self.evpn_route_distinguisher is not None and self.evpn_route_distinguisher._has_data():
                            return True

                        if self.evpn_route_targets is not None and self.evpn_route_targets._has_data():
                            return True

                        if self.table_policy is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery']['meta_info']

                @property
                def _common_path(self):
                    if self.eviid is None:
                        raise YPYModelError('Key property eviid is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpnevis/Cisco-IOS-XR-l2vpn-cfg:evpnevi[Cisco-IOS-XR-l2vpn-cfg:eviid = ' + str(self.eviid) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.eviid is not None:
                        return True

                    if self.evi_advertise_mac is not None:
                        return True

                    if self.evi_load_balancing is not None and self.evi_load_balancing._has_data():
                        return True

                    if self.evi_reorig_disable is not None:
                        return True

                    if self.evi_stitching is not None:
                        return True

                    if self.evi_unknown_unicast_flooding_disable is not None:
                        return True

                    if self.evpn_evi_cw_disable is not None:
                        return True

                    if self.evpnevi_description is not None:
                        return True

                    if self.evpnevibgp_auto_discovery is not None and self.evpnevibgp_auto_discovery._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpnevis'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.evpnevi is not None:
                    for child_ref in self.evpnevi:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.Evpnevis']['meta_info']


        class EvpnVirtualAccessVfis(object):
            """
            Virtual Access VFI interfaces
            
            .. attribute:: evpn_virtual_access_vfi
            
            	Virtual Access VFI
            	**type**\: list of    :py:class:`EvpnVirtualAccessVfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.evpn_virtual_access_vfi = YList()
                self.evpn_virtual_access_vfi.parent = self
                self.evpn_virtual_access_vfi.name = 'evpn_virtual_access_vfi'


            class EvpnVirtualAccessVfi(object):
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.evpn_virtual_access_vfi_timers = Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers()
                    self.evpn_virtual_access_vfi_timers.parent = self
                    self.evpn_virtual_ethernet_segment = Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment()
                    self.evpn_virtual_ethernet_segment.parent = self


                class EvpnVirtualAccessVfiTimers(object):
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.evpn_virtual_access_vfi_peering = None
                        self.evpn_virtual_access_vfi_recovery = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-virtual-access-vfi-timers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable is not None:
                            return True

                        if self.evpn_virtual_access_vfi_peering is not None:
                            return True

                        if self.evpn_virtual_access_vfi_recovery is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers']['meta_info']


                class EvpnVirtualEthernetSegment(object):
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
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.es_import_route_target = None
                        self.identifier = None


                    class Identifier(object):
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
                        	**type**\:   :py:class:`EthernetSegmentIdentifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EthernetSegmentIdentifierEnum>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.bytes01 = None
                            self.bytes23 = None
                            self.bytes45 = None
                            self.bytes67 = None
                            self.bytes89 = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:identifier'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.bytes01 is not None:
                                return True

                            if self.bytes23 is not None:
                                return True

                            if self.bytes45 is not None:
                                return True

                            if self.bytes67 is not None:
                                return True

                            if self.bytes89 is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.Identifier']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-virtual-ethernet-segment'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable is not None:
                            return True

                        if self.es_import_route_target is not None:
                            return True

                        if self.identifier is not None and self.identifier._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-virtual-access-vfis/Cisco-IOS-XR-l2vpn-cfg:evpn-virtual-access-vfi[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.evpn_virtual_access_vfi_timers is not None and self.evpn_virtual_access_vfi_timers._has_data():
                        return True

                    if self.evpn_virtual_ethernet_segment is not None and self.evpn_virtual_ethernet_segment._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-virtual-access-vfis'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.evpn_virtual_access_vfi is not None:
                    for child_ref in self.evpn_virtual_access_vfi:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis']['meta_info']


        class EvpnLoadBalancing(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.evpn_flow_label = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-load-balancing'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.evpn_flow_label is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.EvpnLoadBalancing']['meta_info']


        class EvpnbgpAutoDiscovery(object):
            """
            Enable Autodiscovery BGP in EVPN
            
            .. attribute:: enable
            
            	Enable Autodiscovery BGP
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: evpn_route_distinguisher
            
            	Route Distinguisher
            	**type**\:   :py:class:`EvpnRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnbgpAutoDiscovery.EvpnRouteDistinguisher>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.evpn_route_distinguisher = Evpn.EvpnTables.EvpnbgpAutoDiscovery.EvpnRouteDistinguisher()
                self.evpn_route_distinguisher.parent = self


            class EvpnRouteDistinguisher(object):
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
                	**type**\:   :py:class:`BgpRouteDistinguisherEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisherEnum>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.addr_index = None
                    self.address = None
                    self.as_ = None
                    self.as_index = None
                    self.type = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpnbgp-auto-discovery/Cisco-IOS-XR-l2vpn-cfg:evpn-route-distinguisher'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.addr_index is not None:
                        return True

                    if self.address is not None:
                        return True

                    if self.as_ is not None:
                        return True

                    if self.as_index is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['Evpn.EvpnTables.EvpnbgpAutoDiscovery.EvpnRouteDistinguisher']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpnbgp-auto-discovery'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.evpn_route_distinguisher is not None and self.evpn_route_distinguisher._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.EvpnbgpAutoDiscovery']['meta_info']


        class EvpnLogging(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.evpn_df_election = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-logging'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.evpn_df_election is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.EvpnLogging']['meta_info']


        class EvpnInterfaces(object):
            """
            Attachment Circuit interfaces
            
            .. attribute:: evpn_interface
            
            	Attachment circuit interface
            	**type**\: list of    :py:class:`EvpnInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.evpn_interface = YList()
                self.evpn_interface.parent = self
                self.evpn_interface.name = 'evpn_interface'


            class EvpnInterface(object):
                """
                Attachment circuit interface
                
                .. attribute:: interface_name  <key>
                
                	Name of the attachment circuit interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: evpn_interface_ethernet_segment
                
                	Enter Ethernet Segment configuration submode
                	**type**\:   :py:class:`EvpnInterfaceEthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment>`
                
                .. attribute:: evpnac_timers
                
                	Enter Interface\-specific timers configuration submode
                	**type**\:   :py:class:`EvpnacTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers>`
                
                .. attribute:: mac_flush
                
                	Enable MVRP MAC Flush mode
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.evpn_interface_ethernet_segment = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment()
                    self.evpn_interface_ethernet_segment.parent = self
                    self.evpnac_timers = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers()
                    self.evpnac_timers.parent = self
                    self.mac_flush = None


                class EvpnInterfaceEthernetSegment(object):
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
                    	**type**\:   :py:class:`Identifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.Identifier>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: load_balancing_single_active
                    
                    	Enable single\-active load balancing mode
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: manual_service_carving
                    
                    	Enter Manual service carving configuration submode
                    	**type**\:   :py:class:`ManualServiceCarving <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.backbone_source_mac = None
                        self.enable = None
                        self.es_import_route_target = None
                        self.force_single_homed = None
                        self.identifier = None
                        self.load_balancing_single_active = None
                        self.manual_service_carving = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving()
                        self.manual_service_carving.parent = self


                    class ManualServiceCarving(object):
                        """
                        Enter Manual service carving configuration
                        submode
                        
                        .. attribute:: enable
                        
                        	Enable Manual service carving
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: service_list
                        
                        	Manual service carving primary,secondary lists
                        	**type**\:   :py:class:`ServiceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving.ServiceList>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.enable = None
                            self.service_list = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving.ServiceList()
                            self.service_list.parent = self


                        class ServiceList(object):
                            """
                            Manual service carving primary,secondary
                            lists
                            
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.primary = None
                                self.secondary = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:service-list'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.primary is not None:
                                    return True

                                if self.secondary is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving.ServiceList']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:manual-service-carving'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.enable is not None:
                                return True

                            if self.service_list is not None and self.service_list._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving']['meta_info']


                    class Identifier(object):
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
                        	**type**\:   :py:class:`EthernetSegmentIdentifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EthernetSegmentIdentifierEnum>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.bytes01 = None
                            self.bytes23 = None
                            self.bytes45 = None
                            self.bytes67 = None
                            self.bytes89 = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:identifier'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.bytes01 is not None:
                                return True

                            if self.bytes23 is not None:
                                return True

                            if self.bytes45 is not None:
                                return True

                            if self.bytes67 is not None:
                                return True

                            if self.bytes89 is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.Identifier']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-interface-ethernet-segment'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.backbone_source_mac is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.es_import_route_target is not None:
                            return True

                        if self.force_single_homed is not None:
                            return True

                        if self.identifier is not None and self.identifier._has_data():
                            return True

                        if self.load_balancing_single_active is not None:
                            return True

                        if self.manual_service_carving is not None and self.manual_service_carving._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment']['meta_info']


                class EvpnacTimers(object):
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.evpnac_peering = None
                        self.evpnac_recovery = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpnac-timers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable is not None:
                            return True

                        if self.evpnac_peering is not None:
                            return True

                        if self.evpnac_recovery is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-interfaces/Cisco-IOS-XR-l2vpn-cfg:evpn-interface[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.evpn_interface_ethernet_segment is not None and self.evpn_interface_ethernet_segment._has_data():
                        return True

                    if self.evpnac_timers is not None and self.evpnac_timers._has_data():
                        return True

                    if self.mac_flush is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.evpn_interface is not None:
                    for child_ref in self.evpn_interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces']['meta_info']


        class EvpnVirtualAccessPws(object):
            """
            Virtual Access Pseudowire interfaces
            
            .. attribute:: evpn_virtual_access_pw
            
            	Virtual Access Pseudowire
            	**type**\: list of    :py:class:`EvpnVirtualAccessPw <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.evpn_virtual_access_pw = YList()
                self.evpn_virtual_access_pw.parent = self
                self.evpn_virtual_access_pw.name = 'evpn_virtual_access_pw'


            class EvpnVirtualAccessPw(object):
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.neighbor = None
                    self.pseudowire_id = None
                    self.evpn_virtual_access_pw_timers = Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers()
                    self.evpn_virtual_access_pw_timers.parent = self
                    self.evpn_virtual_ethernet_segment = Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment()
                    self.evpn_virtual_ethernet_segment.parent = self


                class EvpnVirtualAccessPwTimers(object):
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.evpn_virtual_access_pw_peering = None
                        self.evpn_virtual_access_pw_recovery = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-virtual-access-pw-timers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable is not None:
                            return True

                        if self.evpn_virtual_access_pw_peering is not None:
                            return True

                        if self.evpn_virtual_access_pw_recovery is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers']['meta_info']


                class EvpnVirtualEthernetSegment(object):
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
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.es_import_route_target = None
                        self.identifier = None


                    class Identifier(object):
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
                        	**type**\:   :py:class:`EthernetSegmentIdentifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg.EthernetSegmentIdentifierEnum>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.bytes01 = None
                            self.bytes23 = None
                            self.bytes45 = None
                            self.bytes67 = None
                            self.bytes89 = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:identifier'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.bytes01 is not None:
                                return True

                            if self.bytes23 is not None:
                                return True

                            if self.bytes45 is not None:
                                return True

                            if self.bytes67 is not None:
                                return True

                            if self.bytes89 is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.Identifier']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-virtual-ethernet-segment'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable is not None:
                            return True

                        if self.es_import_route_target is not None:
                            return True

                        if self.identifier is not None and self.identifier._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment']['meta_info']

                @property
                def _common_path(self):
                    if self.neighbor is None:
                        raise YPYModelError('Key property neighbor is None')
                    if self.pseudowire_id is None:
                        raise YPYModelError('Key property pseudowire_id is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-virtual-access-pws/Cisco-IOS-XR-l2vpn-cfg:evpn-virtual-access-pw[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + '][Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.neighbor is not None:
                        return True

                    if self.pseudowire_id is not None:
                        return True

                    if self.evpn_virtual_access_pw_timers is not None and self.evpn_virtual_access_pw_timers._has_data():
                        return True

                    if self.evpn_virtual_ethernet_segment is not None and self.evpn_virtual_ethernet_segment._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-virtual-access-pws'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.evpn_virtual_access_pw is not None:
                    for child_ref in self.evpn_virtual_access_pw:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.evpn_interfaces is not None and self.evpn_interfaces._has_data():
                return True

            if self.evpn_load_balancing is not None and self.evpn_load_balancing._has_data():
                return True

            if self.evpn_logging is not None and self.evpn_logging._has_data():
                return True

            if self.evpn_source_interface is not None:
                return True

            if self.evpn_timers is not None and self.evpn_timers._has_data():
                return True

            if self.evpn_virtual_access_pws is not None and self.evpn_virtual_access_pws._has_data():
                return True

            if self.evpn_virtual_access_vfis is not None and self.evpn_virtual_access_vfis._has_data():
                return True

            if self.evpnbgp_auto_discovery is not None and self.evpnbgp_auto_discovery._has_data():
                return True

            if self.evpnevis is not None and self.evpnevis._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['Evpn.EvpnTables']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-l2vpn-cfg:evpn'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.enable is not None:
            return True

        if self.evpn_tables is not None and self.evpn_tables._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['Evpn']['meta_info']


