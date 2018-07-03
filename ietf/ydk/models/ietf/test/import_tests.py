
import unittest

class ImportTest(unittest.TestCase):


    def test_iana_crypt_hash(self):
        pass


    def test_iana_if_type(self):
        from ydk.models.ietf.iana_if_type import VoiceFXO
        from ydk.models.ietf.iana_if_type import AtmVciEndPt
        from ydk.models.ietf.iana_if_type import PropBWAp2Mp
        from ydk.models.ietf.iana_if_type import PropDocsWirelessDownstream
        from ydk.models.ietf.iana_if_type import V11
        from ydk.models.ietf.iana_if_type import SoftwareLoopback
        from ydk.models.ietf.iana_if_type import Hdlc
        from ydk.models.ietf.iana_if_type import VoiceFGDOS
        from ydk.models.ietf.iana_if_type import FastEtherFX
        from ydk.models.ietf.iana_if_type import DvbTdm
        from ydk.models.ietf.iana_if_type import Nfas
        from ydk.models.ietf.iana_if_type import IfPwType
        from ydk.models.ietf.iana_if_type import L2vlan
        from ydk.models.ietf.iana_if_type import Adsl2plus
        from ydk.models.ietf.iana_if_type import Ieee802154
        from ydk.models.ietf.iana_if_type import VoiceFXS
        from ydk.models.ietf.iana_if_type import DvbRcsMacLayer
        from ydk.models.ietf.iana_if_type import Idsl
        from ydk.models.ietf.iana_if_type import Infiniband
        from ydk.models.ietf.iana_if_type import DdnX25
        from ydk.models.ietf.iana_if_type import WwanPP2
        from ydk.models.ietf.iana_if_type import DocsCableUpstream
        from ydk.models.ietf.iana_if_type import Ethernet3Mbit
        from ydk.models.ietf.iana_if_type import DigitalPowerline
        from ydk.models.ietf.iana_if_type import H323Proxy
        from ydk.models.ietf.iana_if_type import Gtp
        from ydk.models.ietf.iana_if_type import IpOverAtm
        from ydk.models.ietf.iana_if_type import AluEpon
        from ydk.models.ietf.iana_if_type import Imt
        from ydk.models.ietf.iana_if_type import IpSwitch
        from ydk.models.ietf.iana_if_type import Msdsl
        from ydk.models.ietf.iana_if_type import DvbRccMacLayer
        from ydk.models.ietf.iana_if_type import SmdsDxi
        from ydk.models.ietf.iana_if_type import VoiceOverAtm
        from ydk.models.ietf.iana_if_type import Arap
        from ydk.models.ietf.iana_if_type import FastEther
        from ydk.models.ietf.iana_if_type import Mpc
        from ydk.models.ietf.iana_if_type import Linegroup
        from ydk.models.ietf.iana_if_type import Hippi
        from ydk.models.ietf.iana_if_type import Rpr
        from ydk.models.ietf.iana_if_type import Ds1FDL
        from ydk.models.ietf.iana_if_type import SonetVT
        from ydk.models.ietf.iana_if_type import VoiceEncap
        from ydk.models.ietf.iana_if_type import Ss7SigLink
        from ydk.models.ietf.iana_if_type import Arcnet
        from ydk.models.ietf.iana_if_type import ActelisMetaLOOP
        from ydk.models.ietf.iana_if_type import Qllc
        from ydk.models.ietf.iana_if_type import Rfc877x25
        from ydk.models.ietf.iana_if_type import MpegTransport
        from ydk.models.ietf.iana_if_type import X25mlp
        from ydk.models.ietf.iana_if_type import VirtualTg
        from ydk.models.ietf.iana_if_type import HostPad
        from ydk.models.ietf.iana_if_type import StarLan
        from ydk.models.ietf.iana_if_type import Iso88025Dtr
        from ydk.models.ietf.iana_if_type import Ibm370parChan
        from ydk.models.ietf.iana_if_type import Adsl2
        from ydk.models.ietf.iana_if_type import OtnOtu
        from ydk.models.ietf.iana_if_type import PropWirelessP2P
        from ydk.models.ietf.iana_if_type import Interleave
        from ydk.models.ietf.iana_if_type import Isup
        from ydk.models.ietf.iana_if_type import Regular1822
        from ydk.models.ietf.iana_if_type import Gr303RDT
        from ydk.models.ietf.iana_if_type import PropDocsWirelessMaclayer
        from ydk.models.ietf.iana_if_type import Async
        from ydk.models.ietf.iana_if_type import RadioMAC
        from ydk.models.ietf.iana_if_type import OpticalChannelGroup
        from ydk.models.ietf.iana_if_type import SixToFour
        from ydk.models.ietf.iana_if_type import PropDocsWirelessUpstream
        from ydk.models.ietf.iana_if_type import Q2931
        from ydk.models.ietf.iana_if_type import Fddi
        from ydk.models.ietf.iana_if_type import PropCnls
        from ydk.models.ietf.iana_if_type import Aal2
        from ydk.models.ietf.iana_if_type import DvbAsiOut
        from ydk.models.ietf.iana_if_type import AluELP
        from ydk.models.ietf.iana_if_type import CiscoISLvlan
        from ydk.models.ietf.iana_if_type import DocsCableUpstreamRfPort
        from ydk.models.ietf.iana_if_type import Aal5
        from ydk.models.ietf.iana_if_type import FrDlciEndPt
        from ydk.models.ietf.iana_if_type import HippiInterface
        from ydk.models.ietf.iana_if_type import L3ipvlan
        from ydk.models.ietf.iana_if_type import Miox25
        from ydk.models.ietf.iana_if_type import Hssi
        from ydk.models.ietf.iana_if_type import AtmVirtual
        from ydk.models.ietf.iana_if_type import AluGponOnu
        from ydk.models.ietf.iana_if_type import Rfc1483
        from ydk.models.ietf.iana_if_type import Cnr
        from ydk.models.ietf.iana_if_type import SipSig
        from ydk.models.ietf.iana_if_type import Myrinet
        from ydk.models.ietf.iana_if_type import Dlsw
        from ydk.models.ietf.iana_if_type import GigabitEthernet
        from ydk.models.ietf.iana_if_type import X25ple
        from ydk.models.ietf.iana_if_type import Lmp
        from ydk.models.ietf.iana_if_type import OpticalTransport
        from ydk.models.ietf.iana_if_type import Sdlc
        from ydk.models.ietf.iana_if_type import VoiceEM
        from ydk.models.ietf.iana_if_type import X86Laps
        from ydk.models.ietf.iana_if_type import G9982
        from ydk.models.ietf.iana_if_type import Iso88022llc
        from ydk.models.ietf.iana_if_type import DvbAsiIn
        from ydk.models.ietf.iana_if_type import Bgppolicyaccounting
        from ydk.models.ietf.iana_if_type import AluEponOnu
        from ydk.models.ietf.iana_if_type import MfSigLink
        from ydk.models.ietf.iana_if_type import Dcn
        from ydk.models.ietf.iana_if_type import AtmDxi
        from ydk.models.ietf.iana_if_type import VoiceOverFrameRelay
        from ydk.models.ietf.iana_if_type import Gfp
        from ydk.models.ietf.iana_if_type import SonetOverheadChannel
        from ydk.models.ietf.iana_if_type import VmwareVirtualNic
        from ydk.models.ietf.iana_if_type import FcipLink
        from ydk.models.ietf.iana_if_type import IpOverClaw
        from ydk.models.ietf.iana_if_type import Coffee
        from ydk.models.ietf.iana_if_type import Radsl
        from ydk.models.ietf.iana_if_type import Vdsl2
        from ydk.models.ietf.iana_if_type import Rs232
        from ydk.models.ietf.iana_if_type import E1
        from ydk.models.ietf.iana_if_type import ReachDSL
        from ydk.models.ietf.iana_if_type import VoiceOverCable
        from ydk.models.ietf.iana_if_type import Tr008
        from ydk.models.ietf.iana_if_type import VoiceOverIp
        from ydk.models.ietf.iana_if_type import Atm
        from ydk.models.ietf.iana_if_type import Ds3
        from ydk.models.ietf.iana_if_type import Ds0
        from ydk.models.ietf.iana_if_type import Ds1
        from ydk.models.ietf.iana_if_type import Srp
        from ydk.models.ietf.iana_if_type import DocsCableDownstream
        from ydk.models.ietf.iana_if_type import DvbRcsTdma
        from ydk.models.ietf.iana_if_type import G9983
        from ydk.models.ietf.iana_if_type import Plc
        from ydk.models.ietf.iana_if_type import FrameRelayMPI
        from ydk.models.ietf.iana_if_type import Mvl
        from ydk.models.ietf.iana_if_type import PropMultiplexor
        from ydk.models.ietf.iana_if_type import VoiceDID
        from ydk.models.ietf.iana_if_type import CompositeLink
        from ydk.models.ietf.iana_if_type import Proteon10Mbit
        from ydk.models.ietf.iana_if_type import Atmbond
        from ydk.models.ietf.iana_if_type import Frf16MfrBundle
        from ydk.models.ietf.iana_if_type import CctEmul
        from ydk.models.ietf.iana_if_type import MplsTunnel
        from ydk.models.ietf.iana_if_type import Gpon
        from ydk.models.ietf.iana_if_type import Vdsl
        from ydk.models.ietf.iana_if_type import Pos
        from ydk.models.ietf.iana_if_type import Ieee8023adLag
        from ydk.models.ietf.iana_if_type import DocsCableMaclayer
        from ydk.models.ietf.iana_if_type import DocsCableMCmtsDownstream
        from ydk.models.ietf.iana_if_type import Ppp
        from ydk.models.ietf.iana_if_type import FrameRelay
        from ydk.models.ietf.iana_if_type import Eplrs
        from ydk.models.ietf.iana_if_type import VmwareNicTeam
        from ydk.models.ietf.iana_if_type import CableDownstreamRfPort
        from ydk.models.ietf.iana_if_type import MacSecUncontrolledIF
        from ydk.models.ietf.iana_if_type import Iso88023Csmacd
        from ydk.models.ietf.iana_if_type import Usb
        from ydk.models.ietf.iana_if_type import AtmFuni
        from ydk.models.ietf.iana_if_type import TeLink
        from ydk.models.ietf.iana_if_type import Pon622
        from ydk.models.ietf.iana_if_type import Econet
        from ydk.models.ietf.iana_if_type import Tdlc
        from ydk.models.ietf.iana_if_type import Ds0Bundle
        from ydk.models.ietf.iana_if_type import Fast
        from ydk.models.ietf.iana_if_type import Ieee1394
        from ydk.models.ietf.iana_if_type import CblVectaStar
        from ydk.models.ietf.iana_if_type import Rsrb
        from ydk.models.ietf.iana_if_type import FrameRelayInterconnect
        from ydk.models.ietf.iana_if_type import Isdns
        from ydk.models.ietf.iana_if_type import PppMultilinkBundle
        from ydk.models.ietf.iana_if_type import Aflane8025
        from ydk.models.ietf.iana_if_type import Lapb
        from ydk.models.ietf.iana_if_type import Aflane8023
        from ydk.models.ietf.iana_if_type import Lapd
        from ydk.models.ietf.iana_if_type import Isdnu
        from ydk.models.ietf.iana_if_type import Lapf
        from ydk.models.ietf.iana_if_type import CapwapWtpVirtualRadio
        from ydk.models.ietf.iana_if_type import IfVfiType
        from ydk.models.ietf.iana_if_type import X25huntGroup
        from ydk.models.ietf.iana_if_type import Para
        from ydk.models.ietf.iana_if_type import MacSecControlledIF
        from ydk.models.ietf.iana_if_type import Iso88024TokenBus
        from ydk.models.ietf.iana_if_type import LocalTalk
        from ydk.models.ietf.iana_if_type import Hyperchannel
        from ydk.models.ietf.iana_if_type import MediaMailOverIp
        from ydk.models.ietf.iana_if_type import IfGsn
        from ydk.models.ietf.iana_if_type import CapwapDot11Profile
        from ydk.models.ietf.iana_if_type import L3ipxvlan
        from ydk.models.ietf.iana_if_type import AtmSubInterface
        from ydk.models.ietf.iana_if_type import PrimaryISDN
        from ydk.models.ietf.iana_if_type import Proteon80Mbit
        from ydk.models.ietf.iana_if_type import Iso88026Man
        from ydk.models.ietf.iana_if_type import DigitalWrapperOverheadChannel
        from ydk.models.ietf.iana_if_type import DocsCableUpstreamChannel
        from ydk.models.ietf.iana_if_type import OpticalChannel
        from ydk.models.ietf.iana_if_type import EthernetCsmacd
        from ydk.models.ietf.iana_if_type import Bits
        from ydk.models.ietf.iana_if_type import Tunnel
        from ydk.models.ietf.iana_if_type import Hdsl2
        from ydk.models.ietf.iana_if_type import FrameRelayService
        from ydk.models.ietf.iana_if_type import Mpls
        from ydk.models.ietf.iana_if_type import Ieee80211
        from ydk.models.ietf.iana_if_type import Ieee80212
        from ydk.models.ietf.iana_if_type import MocaVersion1
        from ydk.models.ietf.iana_if_type import Sonet
        from ydk.models.ietf.iana_if_type import Escon
        from ydk.models.ietf.iana_if_type import AluEponLogicalLink
        from ydk.models.ietf.iana_if_type import G703at2mb
        from ydk.models.ietf.iana_if_type import Ultra
        from ydk.models.ietf.iana_if_type import DvbRccDownstream
        from ydk.models.ietf.iana_if_type import SipTg
        from ydk.models.ietf.iana_if_type import SmdsIcip
        from ydk.models.ietf.iana_if_type import Bridge
        from ydk.models.ietf.iana_if_type import AtmLogical
        from ydk.models.ietf.iana_if_type import PropPointToPointSerial
        from ydk.models.ietf.iana_if_type import V35
        from ydk.models.ietf.iana_if_type import V36
        from ydk.models.ietf.iana_if_type import V37
        from ydk.models.ietf.iana_if_type import Ip
        from ydk.models.ietf.iana_if_type import Gr303IDT
        from ydk.models.ietf.iana_if_type import BasicISDN
        from ydk.models.ietf.iana_if_type import G703at64k
        from ydk.models.ietf.iana_if_type import ArcnetPlus
        from ydk.models.ietf.iana_if_type import Pip
        from ydk.models.ietf.iana_if_type import Dtm
        from ydk.models.ietf.iana_if_type import Slip
        from ydk.models.ietf.iana_if_type import Hiperlan2
        from ydk.models.ietf.iana_if_type import Adsl
        from ydk.models.ietf.iana_if_type import Ieee80216WMAN
        from ydk.models.ietf.iana_if_type import AtmIma
        from ydk.models.ietf.iana_if_type import Isdn
        from ydk.models.ietf.iana_if_type import CapwapDot11Bss
        from ydk.models.ietf.iana_if_type import Sip
        from ydk.models.ietf.iana_if_type import PdnEtherLoop2
        from ydk.models.ietf.iana_if_type import VoiceEBS
        from ydk.models.ietf.iana_if_type import IpForward
        from ydk.models.ietf.iana_if_type import Iso88025CRFPInt
        from ydk.models.ietf.iana_if_type import PropVirtual
        from ydk.models.ietf.iana_if_type import WwanPP
        from ydk.models.ietf.iana_if_type import Other
        from ydk.models.ietf.iana_if_type import Pon155
        from ydk.models.ietf.iana_if_type import IanaInterfaceType
        from ydk.models.ietf.iana_if_type import Qam
        from ydk.models.ietf.iana_if_type import OtnOdu
        from ydk.models.ietf.iana_if_type import Iso88025Fiber
        from ydk.models.ietf.iana_if_type import Channel
        from ydk.models.ietf.iana_if_type import VoiceEMFGD
        from ydk.models.ietf.iana_if_type import AluGponPhysicalUni
        from ydk.models.ietf.iana_if_type import A12MppSwitch
        from ydk.models.ietf.iana_if_type import Ilan
        from ydk.models.ietf.iana_if_type import PdnEtherLoop1
        from ydk.models.ietf.iana_if_type import X213
        from ydk.models.ietf.iana_if_type import SonetPath
        from ydk.models.ietf.iana_if_type import VoiceFGDEANA
        from ydk.models.ietf.iana_if_type import Iso88025TokenRing
        from ydk.models.ietf.iana_if_type import PropAtm
        from ydk.models.ietf.iana_if_type import AluEponPhysicalUni
        from ydk.models.ietf.iana_if_type import StackToStack
        from ydk.models.ietf.iana_if_type import FrForward
        from ydk.models.ietf.iana_if_type import Homepna
        from ydk.models.ietf.iana_if_type import Sdsl
        from ydk.models.ietf.iana_if_type import VirtualIpAddress
        from ydk.models.ietf.iana_if_type import Bsc
        from ydk.models.ietf.iana_if_type import AtmRadio
        from ydk.models.ietf.iana_if_type import AviciOpticalEther
        from ydk.models.ietf.iana_if_type import G9981
        from ydk.models.ietf.iana_if_type import FibreChannel
        from ydk.models.ietf.iana_if_type import Shdsl
        from ydk.models.ietf.iana_if_type import Eon
        from ydk.models.ietf.iana_if_type import H323Gatekeeper
        from ydk.models.ietf.iana_if_type import Hdh1822
        from ydk.models.ietf.iana_if_type import DvbRccUpstream
        from ydk.models.ietf.iana_if_type import Nsip
        from ydk.models.ietf.iana_if_type import TranspHdlc
        from ydk.models.ietf.iana_if_type import TermPad
        from ydk.models.ietf.iana_if_type import IpOverCdlc
        from ydk.models.ietf.iana_if_type import Ces
        from ydk.models.ietf.iana_if_type import Modem


    def test_ietf_diffserv_action(self):
        from ydk.models.ietf.ietf_diffserv_action import Marking
        from ydk.models.ietf.ietf_diffserv_action import AlwaysDrop
        from ydk.models.ietf.ietf_diffserv_action import TailDrop
        from ydk.models.ietf.ietf_diffserv_action import DropType
        from ydk.models.ietf.ietf_diffserv_action import MeterActionDrop
        from ydk.models.ietf.ietf_diffserv_action import MinRate
        from ydk.models.ietf.ietf_diffserv_action import Meter
        from ydk.models.ietf.ietf_diffserv_action import Priority
        from ydk.models.ietf.ietf_diffserv_action import MaxRate
        from ydk.models.ietf.ietf_diffserv_action import MeterActionType
        from ydk.models.ietf.ietf_diffserv_action import MeterActionSet
        from ydk.models.ietf.ietf_diffserv_action import RandomDetect
        from ydk.models.ietf.ietf_diffserv_action import AlgorithmicDrop


    def test_ietf_diffserv_classifier(self):
        from ydk.models.ietf.ietf_diffserv_classifier import DestinationPort
        from ydk.models.ietf.ietf_diffserv_classifier import Protocol
        from ydk.models.ietf.ietf_diffserv_classifier import DestinationIpAddress
        from ydk.models.ietf.ietf_diffserv_classifier import Dscp
        from ydk.models.ietf.ietf_diffserv_classifier import MatchAllFilter
        from ydk.models.ietf.ietf_diffserv_classifier import SourceIpAddress
        from ydk.models.ietf.ietf_diffserv_classifier import MatchAnyFilter
        from ydk.models.ietf.ietf_diffserv_classifier import SourcePort
        from ydk.models.ietf.ietf_diffserv_classifier import FilterType
        from ydk.models.ietf.ietf_diffserv_classifier import ClassifierEntryFilterOperationType
        from ydk.models.ietf.ietf_diffserv_classifier import Classifiers


    def test_ietf_diffserv_policy(self):
        from ydk.models.ietf.ietf_diffserv_policy import ActionType
        from ydk.models.ietf.ietf_diffserv_policy import Policies


    def test_ietf_diffserv_target(self):
        from ydk.models.ietf.ietf_diffserv_target import Inbound
        from ydk.models.ietf.ietf_diffserv_target import Direction
        from ydk.models.ietf.ietf_diffserv_target import Outbound


    def test_ietf_event_notifications(self):
        from ydk.models.ietf.ietf_event_notifications import ErrorNoSuchOption
        from ydk.models.ietf.ietf_event_notifications import Stream
        from ydk.models.ietf.ietf_event_notifications import ErrorNoSuchSubscription
        from ydk.models.ietf.ietf_event_notifications import NoResources
        from ydk.models.ietf.ietf_event_notifications import Inactive
        from ydk.models.ietf.ietf_event_notifications import Suspended
        from ydk.models.ietf.ietf_event_notifications import Encodings
        from ydk.models.ietf.ietf_event_notifications import EncodeJson
        from ydk.models.ietf.ietf_event_notifications import Transport
        from ydk.models.ietf.ietf_event_notifications import InternalError
        from ydk.models.ietf.ietf_event_notifications import ErrorOther
        from ydk.models.ietf.ietf_event_notifications import Other
        from ydk.models.ietf.ietf_event_notifications import InError
        from ydk.models.ietf.ietf_event_notifications import ErrorInsufficientResources
        from ydk.models.ietf.ietf_event_notifications import Netconf
        from ydk.models.ietf.ietf_event_notifications import ErrorConfiguredSubscription
        from ydk.models.ietf.ietf_event_notifications import SubscriptionResult
        from ydk.models.ietf.ietf_event_notifications import Error
        from ydk.models.ietf.ietf_event_notifications import Active
        from ydk.models.ietf.ietf_event_notifications import NETCONF
        from ydk.models.ietf.ietf_event_notifications import Ok
        from ydk.models.ietf.ietf_event_notifications import SubscriptionStreamStatus
        from ydk.models.ietf.ietf_event_notifications import EncodeXml
        from ydk.models.ietf.ietf_event_notifications import SubscriptionDeleted
        from ydk.models.ietf.ietf_event_notifications import SubscriptionErrors
        from ydk.models.ietf.ietf_event_notifications import PushSource
        from ydk.models.ietf.ietf_event_notifications import EstablishSubscription
        from ydk.models.ietf.ietf_event_notifications import CreateSubscription
        from ydk.models.ietf.ietf_event_notifications import ModifySubscription
        from ydk.models.ietf.ietf_event_notifications import DeleteSubscription
        from ydk.models.ietf.ietf_event_notifications import Streams
        from ydk.models.ietf.ietf_event_notifications import Filters
        from ydk.models.ietf.ietf_event_notifications import SubscriptionConfig
        from ydk.models.ietf.ietf_event_notifications import Subscriptions


    def test_ietf_inet_types(self):
        from ydk.models.ietf.ietf_inet_types import IpVersion


    def test_ietf_interfaces(self):
        from ydk.models.ietf.ietf_interfaces import InterfaceType
        from ydk.models.ietf.ietf_interfaces import Interfaces
        from ydk.models.ietf.ietf_interfaces import InterfacesState


    def test_ietf_interfaces_ext(self):
        pass


    def test_ietf_ip(self):
        from ydk.models.ietf.ietf_ip import NeighborOrigin
        from ydk.models.ietf.ietf_ip import IpAddressOrigin


    def test_ietf_ipv4_unicast_routing(self):
        from ydk.models.ietf.ietf_ipv4_unicast_routing import Ipv4Unicast


    def test_ietf_ipv6_unicast_routing(self):
        from ydk.models.ietf.ietf_ipv6_unicast_routing import Ipv6Unicast


    def test_ietf_key_chain(self):
        from ydk.models.ietf.ietf_key_chain import KeyChains


    def test_ietf_netconf(self):
        from ydk.models.ietf.ietf_netconf import ErrorSeverityType
        from ydk.models.ietf.ietf_netconf import ErrorTagType
        from ydk.models.ietf.ietf_netconf import EditOperationType
        from ydk.models.ietf.ietf_netconf import GetConfig
        from ydk.models.ietf.ietf_netconf import EditConfig
        from ydk.models.ietf.ietf_netconf import CopyConfig
        from ydk.models.ietf.ietf_netconf import DeleteConfig
        from ydk.models.ietf.ietf_netconf import Lock
        from ydk.models.ietf.ietf_netconf import Unlock
        from ydk.models.ietf.ietf_netconf import Get
        from ydk.models.ietf.ietf_netconf import CloseSession
        from ydk.models.ietf.ietf_netconf import KillSession
        from ydk.models.ietf.ietf_netconf import Commit
        from ydk.models.ietf.ietf_netconf import DiscardChanges
        from ydk.models.ietf.ietf_netconf import CancelCommit
        from ydk.models.ietf.ietf_netconf import Validate


    def test_ietf_netconf_acm(self):
        from ydk.models.ietf.ietf_netconf_acm import ActionType
        from ydk.models.ietf.ietf_netconf_acm import Nacm


    def test_ietf_netconf_monitoring(self):
        from ydk.models.ietf.ietf_netconf_monitoring import NetconfBeep
        from ydk.models.ietf.ietf_netconf_monitoring import NetconfSsh
        from ydk.models.ietf.ietf_netconf_monitoring import Rnc
        from ydk.models.ietf.ietf_netconf_monitoring import Yin
        from ydk.models.ietf.ietf_netconf_monitoring import Rng
        from ydk.models.ietf.ietf_netconf_monitoring import Xsd
        from ydk.models.ietf.ietf_netconf_monitoring import NetconfSoapOverBeep
        from ydk.models.ietf.ietf_netconf_monitoring import NetconfTls
        from ydk.models.ietf.ietf_netconf_monitoring import Yang
        from ydk.models.ietf.ietf_netconf_monitoring import SchemaFormat
        from ydk.models.ietf.ietf_netconf_monitoring import NetconfSoapOverHttps
        from ydk.models.ietf.ietf_netconf_monitoring import Transport
        from ydk.models.ietf.ietf_netconf_monitoring import NetconfDatastoreType
        from ydk.models.ietf.ietf_netconf_monitoring import GetSchema
        from ydk.models.ietf.ietf_netconf_monitoring import NetconfState


    def test_ietf_netconf_notifications(self):
        pass


    def test_ietf_netconf_with_defaults(self):
        from ydk.models.ietf.ietf_netconf_with_defaults import WithDefaultsMode


    def test_ietf_ospf(self):
        from ydk.models.ietf.ietf_ospf import IfLinkType
        from ydk.models.ietf.ietf_ospf import AreaType
        from ydk.models.ietf.ietf_ospf import Normal
        from ydk.models.ietf.ietf_ospf import Nssa
        from ydk.models.ietf.ietf_ospf import ShipsInTheNight
        from ydk.models.ietf.ietf_ospf import Ospfv3
        from ydk.models.ietf.ietf_ospf import Stub
        from ydk.models.ietf.ietf_ospf import IfLinkTypeVirtualLink
        from ydk.models.ietf.ietf_ospf import Ospfv2
        from ydk.models.ietf.ietf_ospf import IfLinkTypeNormal
        from ydk.models.ietf.ietf_ospf import IfLinkTypeShamLink
        from ydk.models.ietf.ietf_ospf import OperationMode
        from ydk.models.ietf.ietf_ospf import Ospf
        from ydk.models.ietf.ietf_ospf import NbrStateType
        from ydk.models.ietf.ietf_ospf import IfStateType
        from ydk.models.ietf.ietf_ospf import PacketType
        from ydk.models.ietf.ietf_ospf import RestartExitReasonType
        from ydk.models.ietf.ietf_ospf import NssaTranslatorStateType
        from ydk.models.ietf.ietf_ospf import RestartHelperStatusType
        from ydk.models.ietf.ietf_ospf import RestartStatusType


    def test_ietf_restconf_monitoring(self):
        from ydk.models.ietf.ietf_restconf_monitoring import RestconfState


    def test_ietf_routing(self):
        from ydk.models.ietf.ietf_routing import VrfRoutingInstance
        from ydk.models.ietf.ietf_routing import Direct
        from ydk.models.ietf.ietf_routing import DefaultRoutingInstance
        from ydk.models.ietf.ietf_routing import RoutingProtocol
        from ydk.models.ietf.ietf_routing import Static
        from ydk.models.ietf.ietf_routing import Ipv4
        from ydk.models.ietf.ietf_routing import Ipv6
        from ydk.models.ietf.ietf_routing import RoutingInstance
        from ydk.models.ietf.ietf_routing import AddressFamily
        from ydk.models.ietf.ietf_routing import RoutingState
        from ydk.models.ietf.ietf_routing import Routing
        from ydk.models.ietf.ietf_routing import FibRoute


    def test_ietf_syslog_types(self):
        from ydk.models.ietf.ietf_syslog_types import Cron2
        from ydk.models.ietf.ietf_syslog_types import Cron
        from ydk.models.ietf.ietf_syslog_types import Syslog
        from ydk.models.ietf.ietf_syslog_types import Local4
        from ydk.models.ietf.ietf_syslog_types import Ftp
        from ydk.models.ietf.ietf_syslog_types import Uucp
        from ydk.models.ietf.ietf_syslog_types import Console
        from ydk.models.ietf.ietf_syslog_types import Mail
        from ydk.models.ietf.ietf_syslog_types import Authpriv
        from ydk.models.ietf.ietf_syslog_types import Ntp
        from ydk.models.ietf.ietf_syslog_types import Auth
        from ydk.models.ietf.ietf_syslog_types import User
        from ydk.models.ietf.ietf_syslog_types import Local5
        from ydk.models.ietf.ietf_syslog_types import News
        from ydk.models.ietf.ietf_syslog_types import Local7
        from ydk.models.ietf.ietf_syslog_types import Local6
        from ydk.models.ietf.ietf_syslog_types import Local1
        from ydk.models.ietf.ietf_syslog_types import Local0
        from ydk.models.ietf.ietf_syslog_types import Local3
        from ydk.models.ietf.ietf_syslog_types import Local2
        from ydk.models.ietf.ietf_syslog_types import Audit
        from ydk.models.ietf.ietf_syslog_types import Daemon
        from ydk.models.ietf.ietf_syslog_types import Lpr
        from ydk.models.ietf.ietf_syslog_types import Kern
        from ydk.models.ietf.ietf_syslog_types import SyslogFacility
        from ydk.models.ietf.ietf_syslog_types import Severity


    def test_ietf_yang_library(self):
        from ydk.models.ietf.ietf_yang_library import ModulesState


    def test_ietf_yang_push(self):
        from ydk.models.ietf.ietf_yang_push import CustomStream
        from ydk.models.ietf.ietf_yang_push import YangPush
        from ydk.models.ietf.ietf_yang_push import ErrorDataNotAuthorized
        from ydk.models.ietf.ietf_yang_push import Http2
        from ydk.models.ietf.ietf_yang_push import ChangeType


    def test_ietf_yang_smiv2(self):
        from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentity


    def test_ietf_yang_types(self):
        pass


    def test_policy_types(self):
        from ydk.models.ietf.policy_types import Control
        from ydk.models.ietf.policy_types import InputInterface
        from ydk.models.ietf.policy_types import SrcMac
        from ydk.models.ietf.policy_types import Qos
        from ydk.models.ietf.policy_types import PerfMon
        from ydk.models.ietf.policy_types import Application
        from ydk.models.ietf.policy_types import SecurityGroupName
        from ydk.models.ietf.policy_types import PacketService
        from ydk.models.ietf.policy_types import QosClass
        from ydk.models.ietf.policy_types import Ipv4AclName
        from ydk.models.ietf.policy_types import FlowDlci
        from ydk.models.ietf.policy_types import ControlClass
        from ydk.models.ietf.policy_types import InspectClass
        from ydk.models.ietf.policy_types import AppnavClass
        from ydk.models.ietf.policy_types import Service
        from ydk.models.ietf.policy_types import Dei
        from ydk.models.ietf.policy_types import Prec
        from ydk.models.ietf.policy_types import AccessControlClass
        from ydk.models.ietf.policy_types import PacketLength
        from ydk.models.ietf.policy_types import Ipv4Acl
        from ydk.models.ietf.policy_types import FlowDe
        from ydk.models.ietf.policy_types import FlowIp
        from ydk.models.ietf.policy_types import FlowRecord
        from ydk.models.ietf.policy_types import VlanInner
        from ydk.models.ietf.policy_types import AccessControl
        from ydk.models.ietf.policy_types import Metadata
        from ydk.models.ietf.policy_types import Vlan
        from ydk.models.ietf.policy_types import AtmVci
        from ydk.models.ietf.policy_types import Appnav
        from ydk.models.ietf.policy_types import Inspect
        from ydk.models.ietf.policy_types import ClassMap
        from ydk.models.ietf.policy_types import QosGroup
        from ydk.models.ietf.policy_types import WlanUserPriority
        from ydk.models.ietf.policy_types import IpRtp
        from ydk.models.ietf.policy_types import Ipv6Acl
        from ydk.models.ietf.policy_types import AtmClp
        from ydk.models.ietf.policy_types import DstMac
        from ydk.models.ietf.policy_types import Cos
        from ydk.models.ietf.policy_types import Pbr
        from ydk.models.ietf.policy_types import DeiInner
        from ydk.models.ietf.policy_types import MplsExpTop
        from ydk.models.ietf.policy_types import CosInner
        from ydk.models.ietf.policy_types import Ipv6AclName
        from ydk.models.ietf.policy_types import MplsExpImp
        from ydk.models.ietf.policy_types import SecurityGroupTag
        from ydk.models.ietf.policy_types import ClassType
        from ydk.models.ietf.policy_types import DiscardClass
        from ydk.models.ietf.policy_types import Vpls
        from ydk.models.ietf.policy_types import PolicyType
        from ydk.models.ietf.policy_types import Metric
        from ydk.models.ietf.policy_types import Direction
        from ydk.models.ietf.policy_types import RateUnit


if __name__ == '__main__':
    unittest.main()

