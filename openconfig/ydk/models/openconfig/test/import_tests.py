
import unittest

class ImportTest(unittest.TestCase):


    def test_cisco_xr_openconfig_interfaces_types(self):
        pass


    def test_openconfig_bgp(self):
        from ydk.models.openconfig.openconfig_bgp import Bgp


    def test_openconfig_bgp_common(self):
        pass


    def test_openconfig_bgp_common_multiprotocol(self):
        pass


    def test_openconfig_bgp_common_structure(self):
        pass


    def test_openconfig_bgp_global(self):
        pass


    def test_openconfig_bgp_neighbor(self):
        pass


    def test_openconfig_bgp_peer_group(self):
        pass


    def test_openconfig_bgp_policy(self):
        from ydk.models.openconfig.openconfig_bgp_policy import BgpSetCommunityOptionType
        from ydk.models.openconfig.openconfig_bgp_policy import BgpSetMedType
        from ydk.models.openconfig.openconfig_bgp_policy import BgpNextHopType


    def test_openconfig_bgp_types(self):
        from ydk.models.openconfig.openconfig_bgp_types import IPV6UNICAST
        from ydk.models.openconfig.openconfig_bgp_types import IPV4UNICAST
        from ydk.models.openconfig.openconfig_bgp_types import L3VPNIPV6MULTICAST
        from ydk.models.openconfig.openconfig_bgp_types import PRIVATEASREPLACEALL
        from ydk.models.openconfig.openconfig_bgp_types import L3VPNIPV6UNICAST
        from ydk.models.openconfig.openconfig_bgp_types import REMOVEPRIVATEASOPTION
        from ydk.models.openconfig.openconfig_bgp_types import BGPCAPABILITY
        from ydk.models.openconfig.openconfig_bgp_types import L3VPNIPV4MULTICAST
        from ydk.models.openconfig.openconfig_bgp_types import NOADVERTISE
        from ydk.models.openconfig.openconfig_bgp_types import IPV4LABELEDUNICAST
        from ydk.models.openconfig.openconfig_bgp_types import MPBGP
        from ydk.models.openconfig.openconfig_bgp_types import NOEXPORT
        from ydk.models.openconfig.openconfig_bgp_types import NOEXPORTSUBCONFED
        from ydk.models.openconfig.openconfig_bgp_types import BGPWELLKNOWNSTDCOMMUNITY
        from ydk.models.openconfig.openconfig_bgp_types import IPV6LABELEDUNICAST
        from ydk.models.openconfig.openconfig_bgp_types import NOPEER
        from ydk.models.openconfig.openconfig_bgp_types import PRIVATEASREMOVEALL
        from ydk.models.openconfig.openconfig_bgp_types import ASN32
        from ydk.models.openconfig.openconfig_bgp_types import ROUTEREFRESH
        from ydk.models.openconfig.openconfig_bgp_types import L3VPNIPV4UNICAST
        from ydk.models.openconfig.openconfig_bgp_types import GRACEFULRESTART
        from ydk.models.openconfig.openconfig_bgp_types import L2VPNVPLS
        from ydk.models.openconfig.openconfig_bgp_types import AFISAFITYPE
        from ydk.models.openconfig.openconfig_bgp_types import L2VPNEVPN
        from ydk.models.openconfig.openconfig_bgp_types import ADDPATHS
        from ydk.models.openconfig.openconfig_bgp_types import PeerType
        from ydk.models.openconfig.openconfig_bgp_types import BgpOriginAttrType
        from ydk.models.openconfig.openconfig_bgp_types import CommunityType
        from ydk.models.openconfig.openconfig_bgp_types import BgpSessionDirection


    def test_openconfig_channel_monitor(self):
        from ydk.models.openconfig.openconfig_channel_monitor import ChannelMonitors


    def test_openconfig_extensions(self):
        pass


    def test_openconfig_if_aggregate(self):
        from ydk.models.openconfig.openconfig_if_aggregate import AggregationType


    def test_openconfig_if_ethernet(self):
        from ydk.models.openconfig.openconfig_if_ethernet import ETHERNETSPEED
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED50GB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED100MB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED25GB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED10MB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED40GB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED100GB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEEDUNKNOWN
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED1GB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED10GB


    def test_openconfig_if_ip(self):
        from ydk.models.openconfig.openconfig_if_ip import IpAddressOrigin
        from ydk.models.openconfig.openconfig_if_ip import NeighborOrigin


    def test_openconfig_interfaces(self):
        from ydk.models.openconfig.openconfig_interfaces import Interfaces


    def test_openconfig_lacp(self):
        from ydk.models.openconfig.openconfig_lacp import LacpPeriodType
        from ydk.models.openconfig.openconfig_lacp import LacpTimeoutType
        from ydk.models.openconfig.openconfig_lacp import LacpActivityType
        from ydk.models.openconfig.openconfig_lacp import LacpSynchronizationType
        from ydk.models.openconfig.openconfig_lacp import Lacp


    def test_openconfig_local_routing(self):
        from ydk.models.openconfig.openconfig_local_routing import DROP
        from ydk.models.openconfig.openconfig_local_routing import LOCALLINK
        from ydk.models.openconfig.openconfig_local_routing import LOCALDEFINEDNEXTHOP
        from ydk.models.openconfig.openconfig_local_routing import LocalRoutes


    def test_openconfig_mpls(self):
        from ydk.models.openconfig.openconfig_mpls import ExplicitlyDefined
        from ydk.models.openconfig.openconfig_mpls import LocallyComputed
        from ydk.models.openconfig.openconfig_mpls import ExternallyQueried
        from ydk.models.openconfig.openconfig_mpls import PathComputationMethod
        from ydk.models.openconfig.openconfig_mpls import TeMetricType
        from ydk.models.openconfig.openconfig_mpls import MplsSrlgFloodingType
        from ydk.models.openconfig.openconfig_mpls import CspfTieBreaking
        from ydk.models.openconfig.openconfig_mpls import MplsHopType
        from ydk.models.openconfig.openconfig_mpls import TeBandwidthType
        from ydk.models.openconfig.openconfig_mpls import Mpls


    def test_openconfig_mpls_igp(self):
        pass


    def test_openconfig_mpls_ldp(self):
        pass


    def test_openconfig_mpls_rsvp(self):
        pass


    def test_openconfig_mpls_sr(self):
        pass


    def test_openconfig_mpls_static(self):
        pass


    def test_openconfig_mpls_te(self):
        pass


    def test_openconfig_mpls_types(self):
        from ydk.models.openconfig.openconfig_mpls_types import ADMINUP
        from ydk.models.openconfig.openconfig_mpls_types import PathSetupRsvp
        from ydk.models.openconfig.openconfig_mpls_types import LinkNodeProtectionRequested
        from ydk.models.openconfig.openconfig_mpls_types import PathSetupSr
        from ydk.models.openconfig.openconfig_mpls_types import TRANSIT
        from ydk.models.openconfig.openconfig_mpls_types import ProtectionType
        from ydk.models.openconfig.openconfig_mpls_types import P2MP
        from ydk.models.openconfig.openconfig_mpls_types import PathSetupLdp
        from ydk.models.openconfig.openconfig_mpls_types import DOWN
        from ydk.models.openconfig.openconfig_mpls_types import PathSetupProtocol
        from ydk.models.openconfig.openconfig_mpls_types import ADMINDOWN
        from ydk.models.openconfig.openconfig_mpls_types import EGRESS
        from ydk.models.openconfig.openconfig_mpls_types import INGRESS
        from ydk.models.openconfig.openconfig_mpls_types import EXPLICIT
        from ydk.models.openconfig.openconfig_mpls_types import NullLabelType
        from ydk.models.openconfig.openconfig_mpls_types import UP
        from ydk.models.openconfig.openconfig_mpls_types import LspRole
        from ydk.models.openconfig.openconfig_mpls_types import Unprotected
        from ydk.models.openconfig.openconfig_mpls_types import IMPLICIT
        from ydk.models.openconfig.openconfig_mpls_types import LspOperStatus
        from ydk.models.openconfig.openconfig_mpls_types import TunnelAdminStatus
        from ydk.models.openconfig.openconfig_mpls_types import P2P
        from ydk.models.openconfig.openconfig_mpls_types import LinkProtectionRequested
        from ydk.models.openconfig.openconfig_mpls_types import TunnelType
        from ydk.models.openconfig.openconfig_mpls_types import TunnelType
        from ydk.models.openconfig.openconfig_mpls_types import MplsLabel


    def test_openconfig_optical_amplifier(self):
        from ydk.models.openconfig.openconfig_optical_amplifier import BACKWARDRAMAN
        from ydk.models.openconfig.openconfig_optical_amplifier import OPTICALAMPLIFIERTYPE
        from ydk.models.openconfig.openconfig_optical_amplifier import FORWARDRAMAN
        from ydk.models.openconfig.openconfig_optical_amplifier import CONSTANTGAIN
        from ydk.models.openconfig.openconfig_optical_amplifier import MIDGAINRANGE
        from ydk.models.openconfig.openconfig_optical_amplifier import OPTICALAMPLIFIERMODE
        from ydk.models.openconfig.openconfig_optical_amplifier import LOWGAINRANGE
        from ydk.models.openconfig.openconfig_optical_amplifier import HYBRID
        from ydk.models.openconfig.openconfig_optical_amplifier import EDFA
        from ydk.models.openconfig.openconfig_optical_amplifier import CONSTANTPOWER
        from ydk.models.openconfig.openconfig_optical_amplifier import FIXEDGAINRANGE
        from ydk.models.openconfig.openconfig_optical_amplifier import HIGHGAINRANGE
        from ydk.models.openconfig.openconfig_optical_amplifier import GAINRANGE
        from ydk.models.openconfig.openconfig_optical_amplifier import OpticalAmplifier


    def test_openconfig_platform(self):
        from ydk.models.openconfig.openconfig_platform import Components


    def test_openconfig_platform_transceiver(self):
        pass


    def test_openconfig_platform_types(self):
        from ydk.models.openconfig.openconfig_platform_types import OPENCONFIGHARDWARECOMPONENT
        from ydk.models.openconfig.openconfig_platform_types import SENSOR
        from ydk.models.openconfig.openconfig_platform_types import CHASSIS
        from ydk.models.openconfig.openconfig_platform_types import FAN
        from ydk.models.openconfig.openconfig_platform_types import OPENCONFIGSOFTWARECOMPONENT
        from ydk.models.openconfig.openconfig_platform_types import BACKPLANE
        from ydk.models.openconfig.openconfig_platform_types import CPU
        from ydk.models.openconfig.openconfig_platform_types import OPERATINGSYSTEM
        from ydk.models.openconfig.openconfig_platform_types import TRANSCEIVER
        from ydk.models.openconfig.openconfig_platform_types import MODULE
        from ydk.models.openconfig.openconfig_platform_types import LINECARD
        from ydk.models.openconfig.openconfig_platform_types import PORT
        from ydk.models.openconfig.openconfig_platform_types import POWERSUPPLY


    def test_openconfig_policy_types(self):
        from ydk.models.openconfig.openconfig_policy_types import ATTRIBUTELE
        from ydk.models.openconfig.openconfig_policy_types import BGP
        from ydk.models.openconfig.openconfig_policy_types import ATTRIBUTECOMPARISON
        from ydk.models.openconfig.openconfig_policy_types import LOCALAGGREGATE
        from ydk.models.openconfig.openconfig_policy_types import ATTRIBUTEGE
        from ydk.models.openconfig.openconfig_policy_types import ATTRIBUTEEQ
        from ydk.models.openconfig.openconfig_policy_types import INSTALLPROTOCOLTYPE
        from ydk.models.openconfig.openconfig_policy_types import ISIS
        from ydk.models.openconfig.openconfig_policy_types import OSPF
        from ydk.models.openconfig.openconfig_policy_types import OSPF3
        from ydk.models.openconfig.openconfig_policy_types import DIRECTLYCONNECTED
        from ydk.models.openconfig.openconfig_policy_types import STATIC
        from ydk.models.openconfig.openconfig_policy_types import MatchSetOptionsType
        from ydk.models.openconfig.openconfig_policy_types import MatchSetOptionsRestrictedType


    def test_openconfig_rib_bgp(self):
        from ydk.models.openconfig.openconfig_rib_bgp import BgpRib


    def test_openconfig_rib_bgp_types(self):
        from ydk.models.openconfig.openconfig_rib_bgp_types import NEXTHOPCOSTHIGHER
        from ydk.models.openconfig.openconfig_rib_bgp_types import HIGHERROUTERID
        from ydk.models.openconfig.openconfig_rib_bgp_types import INVALIDORIGINATOR
        from ydk.models.openconfig.openconfig_rib_bgp_types import ORIGINTYPEHIGHER
        from ydk.models.openconfig.openconfig_rib_bgp_types import INVALIDCLUSTERLOOP
        from ydk.models.openconfig.openconfig_rib_bgp_types import BGPNOTSELECTEDPOLICY
        from ydk.models.openconfig.openconfig_rib_bgp_types import PREFEREXTERNAL
        from ydk.models.openconfig.openconfig_rib_bgp_types import ASPATHLONGER
        from ydk.models.openconfig.openconfig_rib_bgp_types import LOCALPREFLOWER
        from ydk.models.openconfig.openconfig_rib_bgp_types import INVALIDROUTEREASON
        from ydk.models.openconfig.openconfig_rib_bgp_types import INVALIDASLOOP
        from ydk.models.openconfig.openconfig_rib_bgp_types import HIGHERPEERADDRESS
        from ydk.models.openconfig.openconfig_rib_bgp_types import REJECTEDIMPORTPOLICY
        from ydk.models.openconfig.openconfig_rib_bgp_types import BGPNOTSELECTEDBESTPATH
        from ydk.models.openconfig.openconfig_rib_bgp_types import MEDHIGHER
        from ydk.models.openconfig.openconfig_rib_bgp_types import INVALIDCONFED


    def test_openconfig_routing_policy(self):
        from ydk.models.openconfig.openconfig_routing_policy import DefaultPolicyType
        from ydk.models.openconfig.openconfig_routing_policy import RoutingPolicy


    def test_openconfig_telemetry(self):
        from ydk.models.openconfig.openconfig_telemetry import TelemetryStreamProtocol
        from ydk.models.openconfig.openconfig_telemetry import TelemetrySystem


    def test_openconfig_terminal_device(self):
        from ydk.models.openconfig.openconfig_terminal_device import TerminalDevice


    def test_openconfig_transport_line_common(self):
        from ydk.models.openconfig.openconfig_transport_line_common import INGRESS
        from ydk.models.openconfig.openconfig_transport_line_common import EGRESS
        from ydk.models.openconfig.openconfig_transport_line_common import ADD
        from ydk.models.openconfig.openconfig_transport_line_common import MONITOR
        from ydk.models.openconfig.openconfig_transport_line_common import OPTICALLINEPORTTYPE
        from ydk.models.openconfig.openconfig_transport_line_common import DROP


    def test_openconfig_transport_line_protection(self):
        from ydk.models.openconfig.openconfig_transport_line_protection import APSPATHS
        from ydk.models.openconfig.openconfig_transport_line_protection import SECONDARY
        from ydk.models.openconfig.openconfig_transport_line_protection import PRIMARY
        from ydk.models.openconfig.openconfig_transport_line_protection import Aps


    def test_openconfig_transport_types(self):
        from ydk.models.openconfig.openconfig_transport_types import P1S12D2
        from ydk.models.openconfig.openconfig_transport_types import PROTETHERNET
        from ydk.models.openconfig.openconfig_transport_types import ETH4X10GBASELR
        from ydk.models.openconfig.openconfig_transport_types import PROTOTU1E
        from ydk.models.openconfig.openconfig_transport_types import TRANSCEIVERFORMFACTORTYPE
        from ydk.models.openconfig.openconfig_transport_types import VSR20003R2
        from ydk.models.openconfig.openconfig_transport_types import ETH10GBASEZR
        from ydk.models.openconfig.openconfig_transport_types import VSR20003R3
        from ydk.models.openconfig.openconfig_transport_types import ETHERNETPMDTYPE
        from ydk.models.openconfig.openconfig_transport_types import PROT100GE
        from ydk.models.openconfig.openconfig_transport_types import CFP2
        from ydk.models.openconfig.openconfig_transport_types import PROT100GMLG
        from ydk.models.openconfig.openconfig_transport_types import SCCONNECTOR
        from ydk.models.openconfig.openconfig_transport_types import P1L12D2
        from ydk.models.openconfig.openconfig_transport_types import ETH4X10GBASESR
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE40G
        from ydk.models.openconfig.openconfig_transport_types import TRIBUTARYPROTOCOLTYPE
        from ydk.models.openconfig.openconfig_transport_types import QSFP28
        from ydk.models.openconfig.openconfig_transport_types import PROTODU2E
        from ydk.models.openconfig.openconfig_transport_types import PROTOC768
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE10G
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASESR10
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASEPSM4
        from ydk.models.openconfig.openconfig_transport_types import LOGICALELEMENTPROTOCOLTYPE
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASECWDM4
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASELR4
        from ydk.models.openconfig.openconfig_transport_types import PROTOTU2
        from ydk.models.openconfig.openconfig_transport_types import ETH100GAOC
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE2DOT5G
        from ydk.models.openconfig.openconfig_transport_types import PROTOTU4
        from ydk.models.openconfig.openconfig_transport_types import SFP
        from ydk.models.openconfig.openconfig_transport_types import PROTSTM256
        from ydk.models.openconfig.openconfig_transport_types import PROTOTN
        from ydk.models.openconfig.openconfig_transport_types import OTNAPPLICATIONCODE
        from ydk.models.openconfig.openconfig_transport_types import PROTOTUCN
        from ydk.models.openconfig.openconfig_transport_types import OTHER
        from ydk.models.openconfig.openconfig_transport_types import PROT1GE
        from ydk.models.openconfig.openconfig_transport_types import SONETUNDEFINED
        from ydk.models.openconfig.openconfig_transport_types import PROTSTM64
        from ydk.models.openconfig.openconfig_transport_types import ETH40GBASECR4
        from ydk.models.openconfig.openconfig_transport_types import CFP2ACO
        from ydk.models.openconfig.openconfig_transport_types import PROTOTU3
        from ydk.models.openconfig.openconfig_transport_types import NONPLUGGABLE
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE100G
        from ydk.models.openconfig.openconfig_transport_types import ETH10GBASESR
        from ydk.models.openconfig.openconfig_transport_types import ETH10GBASEER
        from ydk.models.openconfig.openconfig_transport_types import PROTOC192
        from ydk.models.openconfig.openconfig_transport_types import PROTODU4
        from ydk.models.openconfig.openconfig_transport_types import OTNUNDEFINED
        from ydk.models.openconfig.openconfig_transport_types import PROTODU2
        from ydk.models.openconfig.openconfig_transport_types import PROT10GEWAN
        from ydk.models.openconfig.openconfig_transport_types import PROTOTU2E
        from ydk.models.openconfig.openconfig_transport_types import CFP
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASEER4
        from ydk.models.openconfig.openconfig_transport_types import OPTICALCHANNEL
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE1G
        from ydk.models.openconfig.openconfig_transport_types import ETH100GACC
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASECLR4
        from ydk.models.openconfig.openconfig_transport_types import ETH40GBASESR4
        from ydk.models.openconfig.openconfig_transport_types import CFP4
        from ydk.models.openconfig.openconfig_transport_types import ETHUNDEFINED
        from ydk.models.openconfig.openconfig_transport_types import LCCONNECTOR
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASECR4
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASESR4
        from ydk.models.openconfig.openconfig_transport_types import ETH40GBASELR4
        from ydk.models.openconfig.openconfig_transport_types import PROT40GE
        from ydk.models.openconfig.openconfig_transport_types import ETH10GBASELRM
        from ydk.models.openconfig.openconfig_transport_types import SONETAPPLICATIONCODE
        from ydk.models.openconfig.openconfig_transport_types import XFP
        from ydk.models.openconfig.openconfig_transport_types import SFPPLUS
        from ydk.models.openconfig.openconfig_transport_types import PROTODU3
        from ydk.models.openconfig.openconfig_transport_types import MPOCONNECTOR
        from ydk.models.openconfig.openconfig_transport_types import PROTSTM16
        from ydk.models.openconfig.openconfig_transport_types import ETH40GBASEPSM4
        from ydk.models.openconfig.openconfig_transport_types import VSR20003R5
        from ydk.models.openconfig.openconfig_transport_types import PROTOC48
        from ydk.models.openconfig.openconfig_transport_types import P1L12D1
        from ydk.models.openconfig.openconfig_transport_types import TRIBUTARYRATECLASSTYPE
        from ydk.models.openconfig.openconfig_transport_types import QSFP
        from ydk.models.openconfig.openconfig_transport_types import FIBERCONNECTORTYPE
        from ydk.models.openconfig.openconfig_transport_types import PROT10GELAN
        from ydk.models.openconfig.openconfig_transport_types import X2
        from ydk.models.openconfig.openconfig_transport_types import ETH40GBASEER4
        from ydk.models.openconfig.openconfig_transport_types import ETH10GBASELR
        from ydk.models.openconfig.openconfig_transport_types import AdminStateType
        from ydk.models.openconfig.openconfig_transport_types import LoopbackModeType


    def test_openconfig_types(self):
        from ydk.models.openconfig.openconfig_types import L2ETHERNET
        from ydk.models.openconfig.openconfig_types import IPV6
        from ydk.models.openconfig.openconfig_types import ADDRESSFAMILY
        from ydk.models.openconfig.openconfig_types import IPV4
        from ydk.models.openconfig.openconfig_types import MPLS


    def test_openconfig_vlan(self):
        from ydk.models.openconfig.openconfig_vlan import Vlans


    def test_openconfig_vlan_types(self):
        from ydk.models.openconfig.openconfig_vlan_types import TPID0x8A88
        from ydk.models.openconfig.openconfig_vlan_types import TPID0X9200
        from ydk.models.openconfig.openconfig_vlan_types import TPID0x8100
        from ydk.models.openconfig.openconfig_vlan_types import TPID0x9100
        from ydk.models.openconfig.openconfig_vlan_types import TPIDTYPES
        from ydk.models.openconfig.openconfig_vlan_types import VlanModeType


if __name__ == '__main__':
    unittest.main()

