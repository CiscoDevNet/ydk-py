
import unittest

class ImportTest(unittest.TestCase):


    def test_openconfig_aaa(self):
        from ydk.models.openconfig.openconfig_aaa import TACACS
        from ydk.models.openconfig.openconfig_aaa import RADIUS


    def test_openconfig_aaa_radius(self):
        pass


    def test_openconfig_aaa_tacacs(self):
        pass


    def test_openconfig_aaa_types(self):
        from ydk.models.openconfig.openconfig_aaa_types import AAASERVERTYPE
        from ydk.models.openconfig.openconfig_aaa_types import SYSTEMDEFINEDROLES
        from ydk.models.openconfig.openconfig_aaa_types import SYSTEMROLEADMIN
        from ydk.models.openconfig.openconfig_aaa_types import AAAACCOUNTINGEVENTTYPE
        from ydk.models.openconfig.openconfig_aaa_types import AAAACCOUNTINGEVENTCOMMAND
        from ydk.models.openconfig.openconfig_aaa_types import AAAACCOUNTINGEVENTLOGIN
        from ydk.models.openconfig.openconfig_aaa_types import AAAAUTHORIZATIONEVENTTYPE
        from ydk.models.openconfig.openconfig_aaa_types import AAAAUTHORIZATIONEVENTCOMMAND
        from ydk.models.openconfig.openconfig_aaa_types import AAAAUTHORIZATIONEVENTCONFIG
        from ydk.models.openconfig.openconfig_aaa_types import AAAMETHODTYPE
        from ydk.models.openconfig.openconfig_aaa_types import TACACSALL
        from ydk.models.openconfig.openconfig_aaa_types import RADIUSALL
        from ydk.models.openconfig.openconfig_aaa_types import LOCAL


    def test_openconfig_acl(self):
        from ydk.models.openconfig.openconfig_acl import ACLTYPE
        from ydk.models.openconfig.openconfig_acl import ACLIPV4
        from ydk.models.openconfig.openconfig_acl import ACLIPV6
        from ydk.models.openconfig.openconfig_acl import ACLL2
        from ydk.models.openconfig.openconfig_acl import ACLMIXED
        from ydk.models.openconfig.openconfig_acl import FORWARDINGACTION
        from ydk.models.openconfig.openconfig_acl import ACCEPT
        from ydk.models.openconfig.openconfig_acl import DROP
        from ydk.models.openconfig.openconfig_acl import REJECT
        from ydk.models.openconfig.openconfig_acl import LOGACTION
        from ydk.models.openconfig.openconfig_acl import LOGSYSLOG
        from ydk.models.openconfig.openconfig_acl import LOGNONE
        from ydk.models.openconfig.openconfig_acl import ACLCOUNTERCAPABILITY
        from ydk.models.openconfig.openconfig_acl import INTERFACEONLY
        from ydk.models.openconfig.openconfig_acl import AGGREGATEONLY
        from ydk.models.openconfig.openconfig_acl import INTERFACEAGGREGATE
        from ydk.models.openconfig.openconfig_acl import Acl


    def test_openconfig_aft(self):
        pass


    def test_openconfig_aft_common(self):
        pass


    def test_openconfig_aft_ethernet(self):
        pass


    def test_openconfig_aft_ipv4(self):
        pass


    def test_openconfig_aft_ipv6(self):
        pass


    def test_openconfig_aft_mpls(self):
        pass


    def test_openconfig_aft_network_instance(self):
        pass


    def test_openconfig_aft_pf(self):
        pass


    def test_openconfig_aft_types(self):
        from ydk.models.openconfig.openconfig_aft_types import EncapsulationHeaderType


    def test_openconfig_alarm_types(self):
        from ydk.models.openconfig.openconfig_alarm_types import OPENCONFIGALARMTYPEID
        from ydk.models.openconfig.openconfig_alarm_types import AIS
        from ydk.models.openconfig.openconfig_alarm_types import EQPT
        from ydk.models.openconfig.openconfig_alarm_types import LOS
        from ydk.models.openconfig.openconfig_alarm_types import OTS
        from ydk.models.openconfig.openconfig_alarm_types import OPENCONFIGALARMSEVERITY
        from ydk.models.openconfig.openconfig_alarm_types import UNKNOWN
        from ydk.models.openconfig.openconfig_alarm_types import MINOR
        from ydk.models.openconfig.openconfig_alarm_types import WARNING
        from ydk.models.openconfig.openconfig_alarm_types import MAJOR
        from ydk.models.openconfig.openconfig_alarm_types import CRITICAL


    def test_openconfig_alarms(self):
        pass


    def test_openconfig_bfd(self):
        from ydk.models.openconfig.openconfig_bfd import BfdSessionState
        from ydk.models.openconfig.openconfig_bfd import BfdDiagnosticCode
        from ydk.models.openconfig.openconfig_bfd import Bfd


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
        from ydk.models.openconfig.openconfig_bgp_policy import BgpNextHopType
        from ydk.models.openconfig.openconfig_bgp_policy import BgpSetMedType


    def test_openconfig_bgp_types(self):
        from ydk.models.openconfig.openconfig_bgp_types import BGPCAPABILITY
        from ydk.models.openconfig.openconfig_bgp_types import MPBGP
        from ydk.models.openconfig.openconfig_bgp_types import ROUTEREFRESH
        from ydk.models.openconfig.openconfig_bgp_types import ASN32
        from ydk.models.openconfig.openconfig_bgp_types import GRACEFULRESTART
        from ydk.models.openconfig.openconfig_bgp_types import ADDPATHS
        from ydk.models.openconfig.openconfig_bgp_types import AFISAFITYPE
        from ydk.models.openconfig.openconfig_bgp_types import IPV4UNICAST
        from ydk.models.openconfig.openconfig_bgp_types import IPV6UNICAST
        from ydk.models.openconfig.openconfig_bgp_types import IPV4LABELEDUNICAST
        from ydk.models.openconfig.openconfig_bgp_types import IPV6LABELEDUNICAST
        from ydk.models.openconfig.openconfig_bgp_types import L3VPNIPV4UNICAST
        from ydk.models.openconfig.openconfig_bgp_types import L3VPNIPV6UNICAST
        from ydk.models.openconfig.openconfig_bgp_types import L3VPNIPV4MULTICAST
        from ydk.models.openconfig.openconfig_bgp_types import L3VPNIPV6MULTICAST
        from ydk.models.openconfig.openconfig_bgp_types import L2VPNVPLS
        from ydk.models.openconfig.openconfig_bgp_types import L2VPNEVPN
        from ydk.models.openconfig.openconfig_bgp_types import BGPWELLKNOWNSTDCOMMUNITY
        from ydk.models.openconfig.openconfig_bgp_types import NOEXPORT
        from ydk.models.openconfig.openconfig_bgp_types import NOADVERTISE
        from ydk.models.openconfig.openconfig_bgp_types import NOEXPORTSUBCONFED
        from ydk.models.openconfig.openconfig_bgp_types import NOPEER
        from ydk.models.openconfig.openconfig_bgp_types import REMOVEPRIVATEASOPTION
        from ydk.models.openconfig.openconfig_bgp_types import PRIVATEASREMOVEALL
        from ydk.models.openconfig.openconfig_bgp_types import PRIVATEASREPLACEALL
        from ydk.models.openconfig.openconfig_bgp_types import BgpSessionDirection
        from ydk.models.openconfig.openconfig_bgp_types import BgpOriginAttrType
        from ydk.models.openconfig.openconfig_bgp_types import PeerType
        from ydk.models.openconfig.openconfig_bgp_types import CommunityType
        from ydk.models.openconfig.openconfig_bgp_types import AsPathSegmentType


    def test_openconfig_channel_monitor(self):
        from ydk.models.openconfig.openconfig_channel_monitor import ChannelMonitors


    def test_openconfig_extensions(self):
        pass


    def test_openconfig_if_aggregate(self):
        from ydk.models.openconfig.openconfig_if_aggregate import AggregationType


    def test_openconfig_if_ethernet(self):
        from ydk.models.openconfig.openconfig_if_ethernet import ETHERNETSPEED
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED10MB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED100MB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED1GB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED10GB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED25GB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED40GB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED50GB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEED100GB
        from ydk.models.openconfig.openconfig_if_ethernet import SPEEDUNKNOWN


    def test_openconfig_if_ip(self):
        from ydk.models.openconfig.openconfig_if_ip import IpAddressOrigin
        from ydk.models.openconfig.openconfig_if_ip import NeighborOrigin


    def test_openconfig_if_ip_ext(self):
        pass


    def test_openconfig_if_types(self):
        from ydk.models.openconfig.openconfig_if_types import INTERFACETYPE
        from ydk.models.openconfig.openconfig_if_types import IFETHERNET
        from ydk.models.openconfig.openconfig_if_types import IFAGGREGATE
        from ydk.models.openconfig.openconfig_if_types import IFLOOPBACK
        from ydk.models.openconfig.openconfig_if_types import IFROUTEDVLAN
        from ydk.models.openconfig.openconfig_if_types import IFSONET
        from ydk.models.openconfig.openconfig_if_types import IFTUNNELGRE4
        from ydk.models.openconfig.openconfig_if_types import IFTUNNELGRE6


    def test_openconfig_inet_types(self):
        from ydk.models.openconfig.openconfig_inet_types import IpVersion


    def test_openconfig_interfaces(self):
        from ydk.models.openconfig.openconfig_interfaces import Interfaces


    def test_openconfig_isis(self):
        from ydk.models.openconfig.openconfig_isis import IsisMetricFlags


    def test_openconfig_isis_lsdb_types(self):
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISISTLVTYPE
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISISSUBTLVTYPE
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYSUBTLVSTYPE
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPREACHABILITYSUBTLVSTYPE
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ROUTERCAPABILITYSUBTLVSTYPE
        from ydk.models.openconfig.openconfig_isis_lsdb_types import AREAADDRESSES
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IISNEIGHBORS
        from ydk.models.openconfig.openconfig_isis_lsdb_types import INSTANCEID
        from ydk.models.openconfig.openconfig_isis_lsdb_types import AUTHENTICATION
        from ydk.models.openconfig.openconfig_isis_lsdb_types import PURGEOI
        from ydk.models.openconfig.openconfig_isis_lsdb_types import LSPBUFFERSIZE
        from ydk.models.openconfig.openconfig_isis_lsdb_types import EXTENDEDISREACHABILITY
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISNEIGHBORATTRIBUTE
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISISALIASID
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPV4INTERNALREACHABILITY
        from ydk.models.openconfig.openconfig_isis_lsdb_types import NLPID
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPV4EXTERNALREACHABILITY
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPV4INTERFACEADDRESSES
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPV4TEROUTERID
        from ydk.models.openconfig.openconfig_isis_lsdb_types import EXTENDEDIPV4REACHABILITY
        from ydk.models.openconfig.openconfig_isis_lsdb_types import DYNAMICNAME
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPV4SRLG
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPV6SRLG
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPV6TEROUTERID
        from ydk.models.openconfig.openconfig_isis_lsdb_types import MTISN
        from ydk.models.openconfig.openconfig_isis_lsdb_types import MTISNEIGHBORATTRIBUTE
        from ydk.models.openconfig.openconfig_isis_lsdb_types import MULTITOPOLOGY
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPV6INTERFACEADDRESSES
        from ydk.models.openconfig.openconfig_isis_lsdb_types import MTIPV4REACHABILITY
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPV6REACHABILITY
        from ydk.models.openconfig.openconfig_isis_lsdb_types import MTIPV6REACHABILITY
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ROUTERCAPABILITY
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYADMINGROUP
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYLINKID
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYIPV4INTERFACEADDRESS
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYIPV4NEIGHBORADDRESS
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYMAXLINKBANDWIDTH
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYMAXRESERVABLEBANDWIDTH
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYUNRESERVEDBANDWIDTH
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYIPV6INTERFACEADDRESS
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYIPV6NEIGHBORADDRESS
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYEXTENDEDADMINGROUP
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYTEDEFAULTMETRIC
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYLINKATTRIBUTES
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYLINKPROTECTIONTYPE
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYBANDWIDTHCONSTRAINTS
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYUNCONSTRAINEDLSP
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYADJSID
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYADJLANSID
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYLINKDELAY
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYMINMAXLINKDELAY
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYLINKDELAYVARIATION
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYLINKLOSS
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYRESIDUALBANDWIDTH
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYAVAILABLEBANDWIDTH
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ISREACHABILITYUTILIZEDBANDWIDTH
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPREACHABILITYTAG
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPREACHABILITYTAG64
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPREACHABILITYPREFIXSID
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPREACHABILITYPREFIXFLAGS
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPREACHABILITYIPV4ROUTERID
        from ydk.models.openconfig.openconfig_isis_lsdb_types import IPREACHABILITYIPV6ROUTERID
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ROUTERCAPABILITYSRCAPABILITY
        from ydk.models.openconfig.openconfig_isis_lsdb_types import ROUTERCAPABILITYSRALGORITHM


    def test_openconfig_isis_lsp(self):
        pass


    def test_openconfig_isis_policy(self):
        pass


    def test_openconfig_isis_routing(self):
        pass


    def test_openconfig_isis_types(self):
        from ydk.models.openconfig.openconfig_isis_types import OVERLOADRESETTRIGGERTYPE
        from ydk.models.openconfig.openconfig_isis_types import WAITFORBGP
        from ydk.models.openconfig.openconfig_isis_types import WAITFORSYSTEM
        from ydk.models.openconfig.openconfig_isis_types import MTTYPE
        from ydk.models.openconfig.openconfig_isis_types import SAFITYPE
        from ydk.models.openconfig.openconfig_isis_types import AFITYPE
        from ydk.models.openconfig.openconfig_isis_types import AFISAFITYPE
        from ydk.models.openconfig.openconfig_isis_types import IPV4UNICAST
        from ydk.models.openconfig.openconfig_isis_types import IPV6MULTICAST
        from ydk.models.openconfig.openconfig_isis_types import IPV4MULTICAST
        from ydk.models.openconfig.openconfig_isis_types import IPV6UNICAST
        from ydk.models.openconfig.openconfig_isis_types import UNICAST
        from ydk.models.openconfig.openconfig_isis_types import MULTICAST
        from ydk.models.openconfig.openconfig_isis_types import IPV4
        from ydk.models.openconfig.openconfig_isis_types import IPV6
        from ydk.models.openconfig.openconfig_isis_types import LevelType
        from ydk.models.openconfig.openconfig_isis_types import AdaptiveTimerType
        from ydk.models.openconfig.openconfig_isis_types import HelloPaddingType
        from ydk.models.openconfig.openconfig_isis_types import CircuitType
        from ydk.models.openconfig.openconfig_isis_types import MetricType
        from ydk.models.openconfig.openconfig_isis_types import MetricStyle
        from ydk.models.openconfig.openconfig_isis_types import IsisInterfaceAdjState


    def test_openconfig_lacp(self):
        from ydk.models.openconfig.openconfig_lacp import LacpActivityType
        from ydk.models.openconfig.openconfig_lacp import LacpTimeoutType
        from ydk.models.openconfig.openconfig_lacp import LacpSynchronizationType
        from ydk.models.openconfig.openconfig_lacp import LacpPeriodType
        from ydk.models.openconfig.openconfig_lacp import Lacp


    def test_openconfig_lldp(self):
        from ydk.models.openconfig.openconfig_lldp import Lldp


    def test_openconfig_lldp_types(self):
        from ydk.models.openconfig.openconfig_lldp_types import LLDPSYSTEMCAPABILITY
        from ydk.models.openconfig.openconfig_lldp_types import OTHER
        from ydk.models.openconfig.openconfig_lldp_types import REPEATER
        from ydk.models.openconfig.openconfig_lldp_types import MACBRIDGE
        from ydk.models.openconfig.openconfig_lldp_types import WLANACCESSPOINT
        from ydk.models.openconfig.openconfig_lldp_types import ROUTER
        from ydk.models.openconfig.openconfig_lldp_types import TELEPHONE
        from ydk.models.openconfig.openconfig_lldp_types import DOCSISCABLEDEVICE
        from ydk.models.openconfig.openconfig_lldp_types import STATIONONLY
        from ydk.models.openconfig.openconfig_lldp_types import CVLAN
        from ydk.models.openconfig.openconfig_lldp_types import SVLAN
        from ydk.models.openconfig.openconfig_lldp_types import TWOPORTMACRELAY
        from ydk.models.openconfig.openconfig_lldp_types import LLDPTLV
        from ydk.models.openconfig.openconfig_lldp_types import CHASSISID
        from ydk.models.openconfig.openconfig_lldp_types import PORTID
        from ydk.models.openconfig.openconfig_lldp_types import PORTDESCRIPTION
        from ydk.models.openconfig.openconfig_lldp_types import SYSTEMNAME
        from ydk.models.openconfig.openconfig_lldp_types import SYSTEMDESCRIPTION
        from ydk.models.openconfig.openconfig_lldp_types import SYSTEMCAPABILITIES
        from ydk.models.openconfig.openconfig_lldp_types import MANAGEMENTADDRESS
        from ydk.models.openconfig.openconfig_lldp_types import ChassisIdType
        from ydk.models.openconfig.openconfig_lldp_types import PortIdType


    def test_openconfig_local_routing(self):
        from ydk.models.openconfig.openconfig_local_routing import LOCALDEFINEDNEXTHOP
        from ydk.models.openconfig.openconfig_local_routing import DROP
        from ydk.models.openconfig.openconfig_local_routing import LOCALLINK
        from ydk.models.openconfig.openconfig_local_routing import LocalRoutes


    def test_openconfig_mpls(self):
        from ydk.models.openconfig.openconfig_mpls import TeBandwidthType
        from ydk.models.openconfig.openconfig_mpls import MplsSrlgFloodingType
        from ydk.models.openconfig.openconfig_mpls import MplsHopType
        from ydk.models.openconfig.openconfig_mpls import TeMetricType
        from ydk.models.openconfig.openconfig_mpls import CspfTieBreaking
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
        from ydk.models.openconfig.openconfig_mpls_types import PATHCOMPUTATIONMETHOD
        from ydk.models.openconfig.openconfig_mpls_types import LOCALLYCOMPUTED
        from ydk.models.openconfig.openconfig_mpls_types import EXTERNALLYQUERIED
        from ydk.models.openconfig.openconfig_mpls_types import EXPLICITLYDEFINED
        from ydk.models.openconfig.openconfig_mpls_types import PATHSETUPPROTOCOL
        from ydk.models.openconfig.openconfig_mpls_types import PATHSETUPRSVP
        from ydk.models.openconfig.openconfig_mpls_types import PATHSETUPSR
        from ydk.models.openconfig.openconfig_mpls_types import PATHSETUPLDP
        from ydk.models.openconfig.openconfig_mpls_types import PROTECTIONTYPE
        from ydk.models.openconfig.openconfig_mpls_types import UNPROTECTED
        from ydk.models.openconfig.openconfig_mpls_types import LINKPROTECTIONREQUIRED
        from ydk.models.openconfig.openconfig_mpls_types import LINKNODEPROTECTIONREQUESTED
        from ydk.models.openconfig.openconfig_mpls_types import LSPROLE
        from ydk.models.openconfig.openconfig_mpls_types import INGRESS
        from ydk.models.openconfig.openconfig_mpls_types import EGRESS
        from ydk.models.openconfig.openconfig_mpls_types import TRANSIT
        from ydk.models.openconfig.openconfig_mpls_types import TUNNELTYPE
        from ydk.models.openconfig.openconfig_mpls_types import P2P
        from ydk.models.openconfig.openconfig_mpls_types import P2MP
        from ydk.models.openconfig.openconfig_mpls_types import LSPOPERSTATUS
        from ydk.models.openconfig.openconfig_mpls_types import DOWN
        from ydk.models.openconfig.openconfig_mpls_types import UP
        from ydk.models.openconfig.openconfig_mpls_types import TUNNELADMINSTATUS
        from ydk.models.openconfig.openconfig_mpls_types import ADMINDOWN
        from ydk.models.openconfig.openconfig_mpls_types import ADMINUP
        from ydk.models.openconfig.openconfig_mpls_types import NULLLABELTYPE
        from ydk.models.openconfig.openconfig_mpls_types import EXPLICIT
        from ydk.models.openconfig.openconfig_mpls_types import IMPLICIT
        from ydk.models.openconfig.openconfig_mpls_types import LSPMETRICTYPE
        from ydk.models.openconfig.openconfig_mpls_types import LSPMETRICRELATIVE
        from ydk.models.openconfig.openconfig_mpls_types import LSPMETRICABSOLUTE
        from ydk.models.openconfig.openconfig_mpls_types import LSPMETRICINHERITED
        from ydk.models.openconfig.openconfig_mpls_types import MplsLabel
        from ydk.models.openconfig.openconfig_mpls_types import TunnelType


    def test_openconfig_network_instance(self):
        from ydk.models.openconfig.openconfig_network_instance import NetworkInstances


    def test_openconfig_network_instance_l2(self):
        pass


    def test_openconfig_network_instance_l3(self):
        pass


    def test_openconfig_network_instance_types(self):
        from ydk.models.openconfig.openconfig_network_instance_types import NETWORKINSTANCETYPE
        from ydk.models.openconfig.openconfig_network_instance_types import DEFAULTINSTANCE
        from ydk.models.openconfig.openconfig_network_instance_types import L3VRF
        from ydk.models.openconfig.openconfig_network_instance_types import L2VSI
        from ydk.models.openconfig.openconfig_network_instance_types import L2P2P
        from ydk.models.openconfig.openconfig_network_instance_types import L2L3
        from ydk.models.openconfig.openconfig_network_instance_types import ENDPOINTTYPE
        from ydk.models.openconfig.openconfig_network_instance_types import LOCAL
        from ydk.models.openconfig.openconfig_network_instance_types import REMOTE
        from ydk.models.openconfig.openconfig_network_instance_types import LABELALLOCATIONMODE
        from ydk.models.openconfig.openconfig_network_instance_types import PERPREFIX
        from ydk.models.openconfig.openconfig_network_instance_types import PERNEXTHOP
        from ydk.models.openconfig.openconfig_network_instance_types import INSTANCELABEL
        from ydk.models.openconfig.openconfig_network_instance_types import ENCAPSULATION
        from ydk.models.openconfig.openconfig_network_instance_types import MPLS
        from ydk.models.openconfig.openconfig_network_instance_types import VXLAN
        from ydk.models.openconfig.openconfig_network_instance_types import SIGNALLINGPROTOCOL
        from ydk.models.openconfig.openconfig_network_instance_types import LDP
        from ydk.models.openconfig.openconfig_network_instance_types import BGPVPLS
        from ydk.models.openconfig.openconfig_network_instance_types import BGPEVPN


    def test_openconfig_optical_amplifier(self):
        from ydk.models.openconfig.openconfig_optical_amplifier import OPTICALAMPLIFIERTYPE
        from ydk.models.openconfig.openconfig_optical_amplifier import EDFA
        from ydk.models.openconfig.openconfig_optical_amplifier import FORWARDRAMAN
        from ydk.models.openconfig.openconfig_optical_amplifier import BACKWARDRAMAN
        from ydk.models.openconfig.openconfig_optical_amplifier import HYBRID
        from ydk.models.openconfig.openconfig_optical_amplifier import GAINRANGE
        from ydk.models.openconfig.openconfig_optical_amplifier import LOWGAINRANGE
        from ydk.models.openconfig.openconfig_optical_amplifier import MIDGAINRANGE
        from ydk.models.openconfig.openconfig_optical_amplifier import HIGHGAINRANGE
        from ydk.models.openconfig.openconfig_optical_amplifier import FIXEDGAINRANGE
        from ydk.models.openconfig.openconfig_optical_amplifier import OPTICALAMPLIFIERMODE
        from ydk.models.openconfig.openconfig_optical_amplifier import CONSTANTPOWER
        from ydk.models.openconfig.openconfig_optical_amplifier import CONSTANTGAIN
        from ydk.models.openconfig.openconfig_optical_amplifier import FIBERTYPEPROFILE
        from ydk.models.openconfig.openconfig_optical_amplifier import DSF
        from ydk.models.openconfig.openconfig_optical_amplifier import LEAF
        from ydk.models.openconfig.openconfig_optical_amplifier import SSMF
        from ydk.models.openconfig.openconfig_optical_amplifier import TWC
        from ydk.models.openconfig.openconfig_optical_amplifier import TWRS
        from ydk.models.openconfig.openconfig_optical_amplifier import OpticalAmplifier


    def test_openconfig_packet_match(self):
        pass


    def test_openconfig_packet_match_types(self):
        from ydk.models.openconfig.openconfig_packet_match_types import ETHERTYPE
        from ydk.models.openconfig.openconfig_packet_match_types import ETHERTYPEIPV4
        from ydk.models.openconfig.openconfig_packet_match_types import ETHERTYPEARP
        from ydk.models.openconfig.openconfig_packet_match_types import ETHERTYPEVLAN
        from ydk.models.openconfig.openconfig_packet_match_types import ETHERTYPEIPV6
        from ydk.models.openconfig.openconfig_packet_match_types import ETHERTYPEMPLS
        from ydk.models.openconfig.openconfig_packet_match_types import ETHERTYPELLDP
        from ydk.models.openconfig.openconfig_packet_match_types import ETHERTYPEROCE
        from ydk.models.openconfig.openconfig_packet_match_types import IPPROTOCOL
        from ydk.models.openconfig.openconfig_packet_match_types import IPTCP
        from ydk.models.openconfig.openconfig_packet_match_types import IPUDP
        from ydk.models.openconfig.openconfig_packet_match_types import IPICMP
        from ydk.models.openconfig.openconfig_packet_match_types import IPIGMP
        from ydk.models.openconfig.openconfig_packet_match_types import IPPIM
        from ydk.models.openconfig.openconfig_packet_match_types import IPRSVP
        from ydk.models.openconfig.openconfig_packet_match_types import IPGRE
        from ydk.models.openconfig.openconfig_packet_match_types import IPAUTH
        from ydk.models.openconfig.openconfig_packet_match_types import IPL2TP
        from ydk.models.openconfig.openconfig_packet_match_types import TCPFLAGS
        from ydk.models.openconfig.openconfig_packet_match_types import TCPSYN
        from ydk.models.openconfig.openconfig_packet_match_types import TCPFIN
        from ydk.models.openconfig.openconfig_packet_match_types import TCPRST
        from ydk.models.openconfig.openconfig_packet_match_types import TCPPSH
        from ydk.models.openconfig.openconfig_packet_match_types import TCPACK
        from ydk.models.openconfig.openconfig_packet_match_types import TCPURG
        from ydk.models.openconfig.openconfig_packet_match_types import TCPECE
        from ydk.models.openconfig.openconfig_packet_match_types import TCPCWR
        from ydk.models.openconfig.openconfig_packet_match_types import PortNumRange


    def test_openconfig_platform(self):
        from ydk.models.openconfig.openconfig_platform import Components


    def test_openconfig_platform_cpu(self):
        pass


    def test_openconfig_platform_ext(self):
        pass


    def test_openconfig_platform_fan(self):
        pass


    def test_openconfig_platform_linecard(self):
        pass


    def test_openconfig_platform_port(self):
        pass


    def test_openconfig_platform_psu(self):
        pass


    def test_openconfig_platform_transceiver(self):
        pass


    def test_openconfig_platform_types(self):
        from ydk.models.openconfig.openconfig_platform_types import OPENCONFIGHARDWARECOMPONENT
        from ydk.models.openconfig.openconfig_platform_types import OPENCONFIGSOFTWARECOMPONENT
        from ydk.models.openconfig.openconfig_platform_types import CHASSIS
        from ydk.models.openconfig.openconfig_platform_types import BACKPLANE
        from ydk.models.openconfig.openconfig_platform_types import FABRIC
        from ydk.models.openconfig.openconfig_platform_types import POWERSUPPLY
        from ydk.models.openconfig.openconfig_platform_types import FAN
        from ydk.models.openconfig.openconfig_platform_types import SENSOR
        from ydk.models.openconfig.openconfig_platform_types import FRU
        from ydk.models.openconfig.openconfig_platform_types import LINECARD
        from ydk.models.openconfig.openconfig_platform_types import CONTROLLERCARD
        from ydk.models.openconfig.openconfig_platform_types import PORT
        from ydk.models.openconfig.openconfig_platform_types import TRANSCEIVER
        from ydk.models.openconfig.openconfig_platform_types import CPU
        from ydk.models.openconfig.openconfig_platform_types import STORAGE
        from ydk.models.openconfig.openconfig_platform_types import INTEGRATEDCIRCUIT
        from ydk.models.openconfig.openconfig_platform_types import OPERATINGSYSTEM
        from ydk.models.openconfig.openconfig_platform_types import COMPONENTOPERSTATUS
        from ydk.models.openconfig.openconfig_platform_types import ACTIVE
        from ydk.models.openconfig.openconfig_platform_types import INACTIVE
        from ydk.models.openconfig.openconfig_platform_types import DISABLED
        from ydk.models.openconfig.openconfig_platform_types import FECMODETYPE
        from ydk.models.openconfig.openconfig_platform_types import FECENABLED
        from ydk.models.openconfig.openconfig_platform_types import FECDISABLED
        from ydk.models.openconfig.openconfig_platform_types import FECAUTO
        from ydk.models.openconfig.openconfig_platform_types import FECSTATUSTYPE
        from ydk.models.openconfig.openconfig_platform_types import FECSTATUSLOCKED
        from ydk.models.openconfig.openconfig_platform_types import FECSTATUSUNLOCKED
        from ydk.models.openconfig.openconfig_platform_types import ComponentPowerType


    def test_openconfig_policy_types(self):
        from ydk.models.openconfig.openconfig_policy_types import ATTRIBUTECOMPARISON
        from ydk.models.openconfig.openconfig_policy_types import ATTRIBUTEEQ
        from ydk.models.openconfig.openconfig_policy_types import ATTRIBUTEGE
        from ydk.models.openconfig.openconfig_policy_types import ATTRIBUTELE
        from ydk.models.openconfig.openconfig_policy_types import INSTALLPROTOCOLTYPE
        from ydk.models.openconfig.openconfig_policy_types import BGP
        from ydk.models.openconfig.openconfig_policy_types import ISIS
        from ydk.models.openconfig.openconfig_policy_types import OSPF
        from ydk.models.openconfig.openconfig_policy_types import OSPF3
        from ydk.models.openconfig.openconfig_policy_types import STATIC
        from ydk.models.openconfig.openconfig_policy_types import DIRECTLYCONNECTED
        from ydk.models.openconfig.openconfig_policy_types import LOCALAGGREGATE
        from ydk.models.openconfig.openconfig_policy_types import MatchSetOptionsType
        from ydk.models.openconfig.openconfig_policy_types import MatchSetOptionsRestrictedType


    def test_openconfig_procmon(self):
        pass


    def test_openconfig_rib_bgp(self):
        from ydk.models.openconfig.openconfig_rib_bgp import BgpRib


    def test_openconfig_rib_bgp_types(self):
        from ydk.models.openconfig.openconfig_rib_bgp_types import INVALIDROUTEREASON
        from ydk.models.openconfig.openconfig_rib_bgp_types import INVALIDCLUSTERLOOP
        from ydk.models.openconfig.openconfig_rib_bgp_types import INVALIDASLOOP
        from ydk.models.openconfig.openconfig_rib_bgp_types import INVALIDORIGINATOR
        from ydk.models.openconfig.openconfig_rib_bgp_types import INVALIDCONFED
        from ydk.models.openconfig.openconfig_rib_bgp_types import BGPNOTSELECTEDBESTPATH
        from ydk.models.openconfig.openconfig_rib_bgp_types import LOCALPREFLOWER
        from ydk.models.openconfig.openconfig_rib_bgp_types import ASPATHLONGER
        from ydk.models.openconfig.openconfig_rib_bgp_types import ORIGINTYPEHIGHER
        from ydk.models.openconfig.openconfig_rib_bgp_types import MEDHIGHER
        from ydk.models.openconfig.openconfig_rib_bgp_types import PREFEREXTERNAL
        from ydk.models.openconfig.openconfig_rib_bgp_types import NEXTHOPCOSTHIGHER
        from ydk.models.openconfig.openconfig_rib_bgp_types import HIGHERROUTERID
        from ydk.models.openconfig.openconfig_rib_bgp_types import HIGHERPEERADDRESS
        from ydk.models.openconfig.openconfig_rib_bgp_types import BGPNOTSELECTEDPOLICY
        from ydk.models.openconfig.openconfig_rib_bgp_types import REJECTEDIMPORTPOLICY


    def test_openconfig_routing_policy(self):
        from ydk.models.openconfig.openconfig_routing_policy import DefaultPolicyType
        from ydk.models.openconfig.openconfig_routing_policy import PolicyResultType
        from ydk.models.openconfig.openconfig_routing_policy import RoutingPolicy


    def test_openconfig_rsvp_sr_ext(self):
        pass


    def test_openconfig_segment_routing(self):
        from ydk.models.openconfig.openconfig_segment_routing import SrDataplaneType
        from ydk.models.openconfig.openconfig_segment_routing import MplsLabel


    def test_openconfig_system(self):
        from ydk.models.openconfig.openconfig_system import NTPAUTHTYPE
        from ydk.models.openconfig.openconfig_system import NTPAUTHMD5
        from ydk.models.openconfig.openconfig_system import System


    def test_openconfig_system_logging(self):
        from ydk.models.openconfig.openconfig_system_logging import SYSLOGFACILITY
        from ydk.models.openconfig.openconfig_system_logging import ALL
        from ydk.models.openconfig.openconfig_system_logging import KERNEL
        from ydk.models.openconfig.openconfig_system_logging import USER
        from ydk.models.openconfig.openconfig_system_logging import MAIL
        from ydk.models.openconfig.openconfig_system_logging import SYSTEMDAEMON
        from ydk.models.openconfig.openconfig_system_logging import AUTH
        from ydk.models.openconfig.openconfig_system_logging import SYSLOG
        from ydk.models.openconfig.openconfig_system_logging import AUTHPRIV
        from ydk.models.openconfig.openconfig_system_logging import NTP
        from ydk.models.openconfig.openconfig_system_logging import AUDIT
        from ydk.models.openconfig.openconfig_system_logging import CONSOLE
        from ydk.models.openconfig.openconfig_system_logging import LOCAL0
        from ydk.models.openconfig.openconfig_system_logging import LOCAL1
        from ydk.models.openconfig.openconfig_system_logging import LOCAL2
        from ydk.models.openconfig.openconfig_system_logging import LOCAL3
        from ydk.models.openconfig.openconfig_system_logging import LOCAL4
        from ydk.models.openconfig.openconfig_system_logging import LOCAL5
        from ydk.models.openconfig.openconfig_system_logging import LOCAL6
        from ydk.models.openconfig.openconfig_system_logging import LOCAL7
        from ydk.models.openconfig.openconfig_system_logging import LOGDESTINATIONTYPE
        from ydk.models.openconfig.openconfig_system_logging import DESTCONSOLE
        from ydk.models.openconfig.openconfig_system_logging import DESTBUFFER
        from ydk.models.openconfig.openconfig_system_logging import DESTFILE
        from ydk.models.openconfig.openconfig_system_logging import DESTREMOTE
        from ydk.models.openconfig.openconfig_system_logging import SyslogSeverity


    def test_openconfig_system_management(self):
        pass


    def test_openconfig_system_terminal(self):
        pass


    def test_openconfig_telemetry(self):
        from ydk.models.openconfig.openconfig_telemetry import TelemetryStreamProtocol
        from ydk.models.openconfig.openconfig_telemetry import TelemetrySystem


    def test_openconfig_terminal_device(self):
        from ydk.models.openconfig.openconfig_terminal_device import TerminalDevice


    def test_openconfig_transport_line_common(self):
        from ydk.models.openconfig.openconfig_transport_line_common import OPTICALLINEPORTTYPE
        from ydk.models.openconfig.openconfig_transport_line_common import INGRESS
        from ydk.models.openconfig.openconfig_transport_line_common import EGRESS
        from ydk.models.openconfig.openconfig_transport_line_common import ADD
        from ydk.models.openconfig.openconfig_transport_line_common import DROP
        from ydk.models.openconfig.openconfig_transport_line_common import MONITOR


    def test_openconfig_transport_line_protection(self):
        from ydk.models.openconfig.openconfig_transport_line_protection import APSPATHS
        from ydk.models.openconfig.openconfig_transport_line_protection import PRIMARY
        from ydk.models.openconfig.openconfig_transport_line_protection import SECONDARY
        from ydk.models.openconfig.openconfig_transport_line_protection import Aps


    def test_openconfig_transport_types(self):
        from ydk.models.openconfig.openconfig_transport_types import FRAMEMAPPINGPROTOCOL
        from ydk.models.openconfig.openconfig_transport_types import AMP
        from ydk.models.openconfig.openconfig_transport_types import GMP
        from ydk.models.openconfig.openconfig_transport_types import BMP
        from ydk.models.openconfig.openconfig_transport_types import CBR
        from ydk.models.openconfig.openconfig_transport_types import GFPT
        from ydk.models.openconfig.openconfig_transport_types import GFPF
        from ydk.models.openconfig.openconfig_transport_types import TRIBUTARYSLOTGRANULARITY
        from ydk.models.openconfig.openconfig_transport_types import TRIBSLOT1DOT25G
        from ydk.models.openconfig.openconfig_transport_types import TRIBSLOT2DOT5G
        from ydk.models.openconfig.openconfig_transport_types import TRIBSLOT5G
        from ydk.models.openconfig.openconfig_transport_types import TRIBUTARYPROTOCOLTYPE
        from ydk.models.openconfig.openconfig_transport_types import PROT1GE
        from ydk.models.openconfig.openconfig_transport_types import PROTOC48
        from ydk.models.openconfig.openconfig_transport_types import PROTSTM16
        from ydk.models.openconfig.openconfig_transport_types import PROT10GELAN
        from ydk.models.openconfig.openconfig_transport_types import PROT10GEWAN
        from ydk.models.openconfig.openconfig_transport_types import PROTOC192
        from ydk.models.openconfig.openconfig_transport_types import PROTSTM64
        from ydk.models.openconfig.openconfig_transport_types import PROTOTU2
        from ydk.models.openconfig.openconfig_transport_types import PROTOTU2E
        from ydk.models.openconfig.openconfig_transport_types import PROTOTU1E
        from ydk.models.openconfig.openconfig_transport_types import PROTODU2
        from ydk.models.openconfig.openconfig_transport_types import PROTODU2E
        from ydk.models.openconfig.openconfig_transport_types import PROT40GE
        from ydk.models.openconfig.openconfig_transport_types import PROTOC768
        from ydk.models.openconfig.openconfig_transport_types import PROTSTM256
        from ydk.models.openconfig.openconfig_transport_types import PROTOTU3
        from ydk.models.openconfig.openconfig_transport_types import PROTODU3
        from ydk.models.openconfig.openconfig_transport_types import PROT100GE
        from ydk.models.openconfig.openconfig_transport_types import PROT100GMLG
        from ydk.models.openconfig.openconfig_transport_types import PROTOTU4
        from ydk.models.openconfig.openconfig_transport_types import PROTOTUCN
        from ydk.models.openconfig.openconfig_transport_types import PROTODUCN
        from ydk.models.openconfig.openconfig_transport_types import PROTODU4
        from ydk.models.openconfig.openconfig_transport_types import TRANSCEIVERFORMFACTORTYPE
        from ydk.models.openconfig.openconfig_transport_types import CFP
        from ydk.models.openconfig.openconfig_transport_types import CFP2
        from ydk.models.openconfig.openconfig_transport_types import CFP2ACO
        from ydk.models.openconfig.openconfig_transport_types import CFP4
        from ydk.models.openconfig.openconfig_transport_types import QSFP
        from ydk.models.openconfig.openconfig_transport_types import QSFPPLUS
        from ydk.models.openconfig.openconfig_transport_types import QSFP28
        from ydk.models.openconfig.openconfig_transport_types import CPAK
        from ydk.models.openconfig.openconfig_transport_types import SFP
        from ydk.models.openconfig.openconfig_transport_types import SFPPLUS
        from ydk.models.openconfig.openconfig_transport_types import XFP
        from ydk.models.openconfig.openconfig_transport_types import X2
        from ydk.models.openconfig.openconfig_transport_types import NONPLUGGABLE
        from ydk.models.openconfig.openconfig_transport_types import OTHER
        from ydk.models.openconfig.openconfig_transport_types import FIBERCONNECTORTYPE
        from ydk.models.openconfig.openconfig_transport_types import SCCONNECTOR
        from ydk.models.openconfig.openconfig_transport_types import LCCONNECTOR
        from ydk.models.openconfig.openconfig_transport_types import MPOCONNECTOR
        from ydk.models.openconfig.openconfig_transport_types import ETHERNETPMDTYPE
        from ydk.models.openconfig.openconfig_transport_types import ETH10GBASELRM
        from ydk.models.openconfig.openconfig_transport_types import ETH10GBASELR
        from ydk.models.openconfig.openconfig_transport_types import ETH10GBASEZR
        from ydk.models.openconfig.openconfig_transport_types import ETH10GBASEER
        from ydk.models.openconfig.openconfig_transport_types import ETH10GBASESR
        from ydk.models.openconfig.openconfig_transport_types import ETH40GBASECR4
        from ydk.models.openconfig.openconfig_transport_types import ETH40GBASESR4
        from ydk.models.openconfig.openconfig_transport_types import ETH40GBASELR4
        from ydk.models.openconfig.openconfig_transport_types import ETH40GBASEER4
        from ydk.models.openconfig.openconfig_transport_types import ETH40GBASEPSM4
        from ydk.models.openconfig.openconfig_transport_types import ETH4X10GBASELR
        from ydk.models.openconfig.openconfig_transport_types import ETH4X10GBASESR
        from ydk.models.openconfig.openconfig_transport_types import ETH100GAOC
        from ydk.models.openconfig.openconfig_transport_types import ETH100GACC
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASESR10
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASESR4
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASELR4
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASEER4
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASECWDM4
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASECLR4
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASEPSM4
        from ydk.models.openconfig.openconfig_transport_types import ETH100GBASECR4
        from ydk.models.openconfig.openconfig_transport_types import ETHUNDEFINED
        from ydk.models.openconfig.openconfig_transport_types import SONETAPPLICATIONCODE
        from ydk.models.openconfig.openconfig_transport_types import VSR20003R2
        from ydk.models.openconfig.openconfig_transport_types import VSR20003R3
        from ydk.models.openconfig.openconfig_transport_types import VSR20003R5
        from ydk.models.openconfig.openconfig_transport_types import SONETUNDEFINED
        from ydk.models.openconfig.openconfig_transport_types import OTNAPPLICATIONCODE
        from ydk.models.openconfig.openconfig_transport_types import P1L12D1
        from ydk.models.openconfig.openconfig_transport_types import P1S12D2
        from ydk.models.openconfig.openconfig_transport_types import P1L12D2
        from ydk.models.openconfig.openconfig_transport_types import OTNUNDEFINED
        from ydk.models.openconfig.openconfig_transport_types import TRIBUTARYRATECLASSTYPE
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE1G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE2DOT5G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE10G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE40G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE100G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE150G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE200G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE250G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE300G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE400G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE500G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE600G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE700G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE800G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE900G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE1000G
        from ydk.models.openconfig.openconfig_transport_types import TRIBRATE1100G
        from ydk.models.openconfig.openconfig_transport_types import LOGICALELEMENTPROTOCOLTYPE
        from ydk.models.openconfig.openconfig_transport_types import PROTETHERNET
        from ydk.models.openconfig.openconfig_transport_types import PROTOTN
        from ydk.models.openconfig.openconfig_transport_types import OPTICALCHANNEL
        from ydk.models.openconfig.openconfig_transport_types import FIBERJUMPERTYPE
        from ydk.models.openconfig.openconfig_transport_types import FIBERJUMPERSIMPLEX
        from ydk.models.openconfig.openconfig_transport_types import FIBERJUMPERMULTIFIBERSTRAND
        from ydk.models.openconfig.openconfig_transport_types import OPTICALPORTTYPE
        from ydk.models.openconfig.openconfig_transport_types import INGRESS
        from ydk.models.openconfig.openconfig_transport_types import EGRESS
        from ydk.models.openconfig.openconfig_transport_types import ADD
        from ydk.models.openconfig.openconfig_transport_types import DROP
        from ydk.models.openconfig.openconfig_transport_types import MONITOR
        from ydk.models.openconfig.openconfig_transport_types import TERMINALCLIENT
        from ydk.models.openconfig.openconfig_transport_types import TERMINALLINE
        from ydk.models.openconfig.openconfig_transport_types import AdminStateType
        from ydk.models.openconfig.openconfig_transport_types import LoopbackModeType


    def test_openconfig_types(self):
        from ydk.models.openconfig.openconfig_types import ADDRESSFAMILY
        from ydk.models.openconfig.openconfig_types import IPV4
        from ydk.models.openconfig.openconfig_types import IPV6
        from ydk.models.openconfig.openconfig_types import MPLS
        from ydk.models.openconfig.openconfig_types import L2ETHERNET


    def test_openconfig_vlan(self):
        from ydk.models.openconfig.openconfig_vlan import Vlans


    def test_openconfig_vlan_types(self):
        from ydk.models.openconfig.openconfig_vlan_types import TPIDTYPES
        from ydk.models.openconfig.openconfig_vlan_types import TPID0x8100
        from ydk.models.openconfig.openconfig_vlan_types import TPID0x8A88
        from ydk.models.openconfig.openconfig_vlan_types import TPID0x9100
        from ydk.models.openconfig.openconfig_vlan_types import TPID0X9200
        from ydk.models.openconfig.openconfig_vlan_types import VlanModeType


    def test_openconfig_yang_types(self):
        pass


if __name__ == '__main__':
    unittest.main()

