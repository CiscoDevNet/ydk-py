""" Cisco_IOS_XE_ios_common_oper 

This module contains a collection of YANG definitions
for some common IOS structures
Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IosEncapsType(Enum):
    """
    IosEncapsType (Enum Class)

    Encaps Type

    .. data:: ios_encaps_type_null = 0

    	undefined -- error

    .. data:: ios_encaps_type_arpa = 1

    	Ethernet - DDN style

    .. data:: ios_encaps_type_sap = 2

    	Ethernet

    .. data:: ios_encaps_type_snap = 3

    	802.2 SNAP types

    .. data:: ios_encaps_type_1822 = 4

    	DDN - 1822 (obsolete)

    .. data:: ios_encaps_type_hdlc = 5

    	Serial - raw HDLC

    .. data:: ios_encaps_type_unused2 = 6

    	Unused Placeholder (3MB)

    .. data:: ios_encaps_type_unused1 = 7

    	Unused Placeholder (HDH)

    .. data:: ios_encaps_type_lapb = 8

    	Serial - LAPB

    .. data:: ios_encaps_type_x25 = 9

    	Serial - X.25

    .. data:: ios_encaps_type_hub = 10

    	HUB fiber optic

    .. data:: ios_encaps_type_novell_ether = 11

    	Novell style XNS on Ethernet

    .. data:: ios_encaps_type_unsupported = 12

    	Unsupported protocols

    .. data:: ios_encaps_type_3com_tr = 13

    	3Com XNS over TR 802.2 0x80

    .. data:: ios_encaps_type_ub_tr = 14

    	Ungermann-Bass XNS over TR SNAP

    .. data:: ios_encaps_type_apollo = 15

    	Apollo domain packets

    .. data:: ios_encaps_type_ppp = 16

    	Serial PPP

    .. data:: ios_encaps_type_unused4 = 17

    	Unused Placeholder (ISO3)

    .. data:: ios_encaps_type_vines_tr = 18

    	ISO1 with Vines demux byte

    .. data:: ios_encaps_type_ethertalk = 19

    	AppleTalk phase 1 on ethernet

    .. data:: ios_encaps_type_frame_relay = 20

    	Frame Relay

    .. data:: ios_encaps_type_smds = 21

    	Switched Multimegabit Data Service (SMDS)

    .. data:: ios_encaps_type_mac = 22

    	MAC level packets

    .. data:: ios_encaps_type_ultra_iso2 = 23

    	Ultranet

    .. data:: ios_encaps_type_ultra_iso1 = 24

    	Ultranet-Hello

    .. data:: ios_encaps_type_stun = 25

    	Serial - serial tunnelling

    .. data:: ios_encaps_type_bridge = 26

    	Packet in bridge encapsulation

    .. data:: ios_encaps_type_llc2 = 27

    	LLC 2

    .. data:: ios_encaps_type_sdlcp = 28

    	Serial - SDLC (primary)

    .. data:: ios_encaps_type_sdlcs = 29

    	Serial - SDLC (secondary)

    .. data:: ios_encaps_type_slip = 30

    	Async SLIP encapsulation

    .. data:: ios_encaps_type_tunnel = 31

    	Standard Tunnel Interface

    .. data:: ios_encaps_type_bridge_encaps = 32

    	Bridge encap on local gen packs

    .. data:: ios_encaps_type_atm = 33

    	ATM interface encaps

    .. data:: ios_encaps_type_atm_dxi = 34

    	ATM DXI implementation

    .. data:: ios_encaps_type_fr_ietf = 35

    	Frame Relay with IETF encaps

    .. data:: ios_encaps_type_smds_dxi = 36

    	SMDS DXI implementation

    .. data:: ios_encaps_type_atm_dxi_ietf = 37

    	atm-dxi with IETF encaps

    .. data:: ios_encaps_type_channel = 38

    	IBM Channel

    .. data:: ios_encaps_type_sdlc = 39

    	CLSI compliant SDLC

    .. data:: ios_encaps_type_sde = 40

    	802.10 Secure Data Exchange

    .. data:: ios_encaps_type_bstun = 41

    	block serial tunnel

    .. data:: ios_encaps_type_dialer = 42

    	Dialer encapsulation

    .. data:: ios_encaps_type_novell_fddi = 43

    	Novell style XNS on FDDI

    .. data:: ios_encaps_type_v120 = 44

    	V120 ISDN->ASYNC encaps

    .. data:: ios_encaps_type_isl = 45

    	Inter Switch Link - vLANs on FEIP

    .. data:: ios_encaps_type_loop = 46

    	loopback interface

    .. data:: ios_encaps_type_channel_ilan = 47

    	IBM Channel internal LAN

    .. data:: ios_encaps_type_serial_autodetect = 48

    	Autodetected for Serials

    .. data:: ios_encaps_type_cpp = 49

    	Combinet proprietary protocol

    .. data:: ios_encaps_type_ndlc = 50

    	NCIA DLC

    .. data:: ios_encaps_type_lapd = 51

    	ISDN Q.921

    .. data:: ios_encaps_type_ftc_trunk = 52

    	StrataCom IPX/Fastpad protocol

    .. data:: ios_encaps_type_atmces_t1 = 53

    	ATM T1 Circuit Emulation.

    .. data:: ios_encaps_type_atmces_e1 = 54

    	ATM E1 Circuit Emulation.

    .. data:: ios_encaps_type_voice = 55

    	Packetized Voice

    .. data:: ios_encaps_type_alc = 56

    	ALC (P1024B) sync protocol

    .. data:: ios_encaps_type_uts = 57

    	UTS (P1024C) sync protocol

    .. data:: ios_encaps_type_trisl = 58

    	Token Ring Inter-Switch Link (TRISL)

    .. data:: ios_encaps_type_mcns = 59

    	Cable - MCNS

    .. data:: ios_encaps_type_atmces = 60

    	ATM circuit emulation service

    .. data:: ios_encaps_type_trans = 61

    	for transparent mode

    .. data:: ios_encaps_type_clear_channel = 62

    	TDM clear channel

    .. data:: ios_encaps_type_tc_atm = 63

    	Tag Controlled ATM interface

    .. data:: ios_encaps_type_fr_ppp = 64

    	PPP over Frame Relay

    .. data:: ios_encaps_type_dot1q = 65

    	IEEE 802.1Q

    .. data:: ios_encaps_type_funi = 66

    	Frame based user network interface

    .. data:: ios_encaps_type_lapbta = 67

    	LAPB terminal adapter

    .. data:: ios_encaps_type_docsis = 68

    	Cable Modem

    .. data:: ios_encaps_type_np_inband = 69

    	NextPort DSP modem in-band message

    .. data:: ios_encaps_type_ss7_mtp2 = 70

    	SS7 MTP-2 over serial/TDM interface

    .. data:: ios_encaps_type_gtp = 71

    	General Packet Radio Service (GPRS)

    .. data:: ios_encaps_type_isl_switchport = 72

    	ISL SW encap pkt sent on swch prt

    .. data:: ios_encaps_type_srp = 73

    	Spatial Reuse Protocol

    .. data:: ios_encaps_type_ppp_etype = 74

    	PPP hdr w/Ethertype protocol type

    .. data:: ios_encaps_type_atm_ppp = 75

    	PPP over ATM

    .. data:: ios_encaps_type_mfr = 76

    	Multilink Frame Relay

    .. data:: ios_encaps_type_srp2 = 77

    	SRP version 2

    .. data:: ios_encaps_type_fr_extended = 78

    	Frame Relay extended addressing

    .. data:: ios_encaps_type_pppoe = 79

    	PPP Over Ethernet

    .. data:: ios_encaps_type_ouni_sdcc = 80

    	OIF UNI SDCC per OIF2000.125

    .. data:: ios_encaps_type_multiservice = 81

    	encap type for multiservice i/f

    .. data:: ios_encaps_type_container = 82

    	Container

    .. data:: ios_encaps_type_dot1ad = 83

    	Dot1ad ether type

    .. data:: ios_encaps_type_cem = 84

    	Circuit Emulation Type

    .. data:: ios_encaps_type_dot1ah = 85

    	IEEE 802.1ah Ether type

    .. data:: ios_encaps_type_ptp = 86

    	PTP type

    .. data:: ios_encaps_type_ssl = 87

    	For SSLVPN

    .. data:: ios_encaps_type_lisp = 88

    	Locator/ID Separation Protocol (LISP)

    .. data:: ios_encaps_type_dsp_spa = 89

    	DSP-based SPA

    .. data:: ios_encaps_type_t101 = 90

    	IEC-60870-5-101 for Async Serial interface

    .. data:: ios_encaps_type_crypto = 91

    	Crypto

    .. data:: ios_encaps_type_rawtcp = 92

    	Raw socket TCP for Async line interface

    .. data:: ios_encaps_type_async = 93

    	Async line raw data

    .. data:: ios_encaps_type_cmd = 94

    	Cisco Meta Data (CMD) EtherType=0x8909 encap

    .. data:: ios_encaps_type_scada = 95

    	SCADA for Async Serial Interface

    .. data:: ios_encaps_type_rawudp = 96

    	Raw socket UDP for Async line interface

    .. data:: ios_encaps_type_relay_line = 97

    	Line relay for Async line interface

    .. data:: ios_encaps_type_rawmpls = 98

    	Raw socket over MPLS for Async line interface

    	Market want to call it trans. It's a little conflict

    	TRANSPARENT

    .. data:: ios_encaps_type_arpa_nid = 99

    	if NID added after ARPA we add a new type

    """

    ios_encaps_type_null = Enum.YLeaf(0, "ios-encaps-type-null")

    ios_encaps_type_arpa = Enum.YLeaf(1, "ios-encaps-type-arpa")

    ios_encaps_type_sap = Enum.YLeaf(2, "ios-encaps-type-sap")

    ios_encaps_type_snap = Enum.YLeaf(3, "ios-encaps-type-snap")

    ios_encaps_type_1822 = Enum.YLeaf(4, "ios-encaps-type-1822")

    ios_encaps_type_hdlc = Enum.YLeaf(5, "ios-encaps-type-hdlc")

    ios_encaps_type_unused2 = Enum.YLeaf(6, "ios-encaps-type-unused2")

    ios_encaps_type_unused1 = Enum.YLeaf(7, "ios-encaps-type-unused1")

    ios_encaps_type_lapb = Enum.YLeaf(8, "ios-encaps-type-lapb")

    ios_encaps_type_x25 = Enum.YLeaf(9, "ios-encaps-type-x25")

    ios_encaps_type_hub = Enum.YLeaf(10, "ios-encaps-type-hub")

    ios_encaps_type_novell_ether = Enum.YLeaf(11, "ios-encaps-type-novell-ether")

    ios_encaps_type_unsupported = Enum.YLeaf(12, "ios-encaps-type-unsupported")

    ios_encaps_type_3com_tr = Enum.YLeaf(13, "ios-encaps-type-3com-tr")

    ios_encaps_type_ub_tr = Enum.YLeaf(14, "ios-encaps-type-ub-tr")

    ios_encaps_type_apollo = Enum.YLeaf(15, "ios-encaps-type-apollo")

    ios_encaps_type_ppp = Enum.YLeaf(16, "ios-encaps-type-ppp")

    ios_encaps_type_unused4 = Enum.YLeaf(17, "ios-encaps-type-unused4")

    ios_encaps_type_vines_tr = Enum.YLeaf(18, "ios-encaps-type-vines-tr")

    ios_encaps_type_ethertalk = Enum.YLeaf(19, "ios-encaps-type-ethertalk")

    ios_encaps_type_frame_relay = Enum.YLeaf(20, "ios-encaps-type-frame-relay")

    ios_encaps_type_smds = Enum.YLeaf(21, "ios-encaps-type-smds")

    ios_encaps_type_mac = Enum.YLeaf(22, "ios-encaps-type-mac")

    ios_encaps_type_ultra_iso2 = Enum.YLeaf(23, "ios-encaps-type-ultra-iso2")

    ios_encaps_type_ultra_iso1 = Enum.YLeaf(24, "ios-encaps-type-ultra-iso1")

    ios_encaps_type_stun = Enum.YLeaf(25, "ios-encaps-type-stun")

    ios_encaps_type_bridge = Enum.YLeaf(26, "ios-encaps-type-bridge")

    ios_encaps_type_llc2 = Enum.YLeaf(27, "ios-encaps-type-llc2")

    ios_encaps_type_sdlcp = Enum.YLeaf(28, "ios-encaps-type-sdlcp")

    ios_encaps_type_sdlcs = Enum.YLeaf(29, "ios-encaps-type-sdlcs")

    ios_encaps_type_slip = Enum.YLeaf(30, "ios-encaps-type-slip")

    ios_encaps_type_tunnel = Enum.YLeaf(31, "ios-encaps-type-tunnel")

    ios_encaps_type_bridge_encaps = Enum.YLeaf(32, "ios-encaps-type-bridge-encaps")

    ios_encaps_type_atm = Enum.YLeaf(33, "ios-encaps-type-atm")

    ios_encaps_type_atm_dxi = Enum.YLeaf(34, "ios-encaps-type-atm-dxi")

    ios_encaps_type_fr_ietf = Enum.YLeaf(35, "ios-encaps-type-fr-ietf")

    ios_encaps_type_smds_dxi = Enum.YLeaf(36, "ios-encaps-type-smds-dxi")

    ios_encaps_type_atm_dxi_ietf = Enum.YLeaf(37, "ios-encaps-type-atm-dxi-ietf")

    ios_encaps_type_channel = Enum.YLeaf(38, "ios-encaps-type-channel")

    ios_encaps_type_sdlc = Enum.YLeaf(39, "ios-encaps-type-sdlc")

    ios_encaps_type_sde = Enum.YLeaf(40, "ios-encaps-type-sde")

    ios_encaps_type_bstun = Enum.YLeaf(41, "ios-encaps-type-bstun")

    ios_encaps_type_dialer = Enum.YLeaf(42, "ios-encaps-type-dialer")

    ios_encaps_type_novell_fddi = Enum.YLeaf(43, "ios-encaps-type-novell-fddi")

    ios_encaps_type_v120 = Enum.YLeaf(44, "ios-encaps-type-v120")

    ios_encaps_type_isl = Enum.YLeaf(45, "ios-encaps-type-isl")

    ios_encaps_type_loop = Enum.YLeaf(46, "ios-encaps-type-loop")

    ios_encaps_type_channel_ilan = Enum.YLeaf(47, "ios-encaps-type-channel-ilan")

    ios_encaps_type_serial_autodetect = Enum.YLeaf(48, "ios-encaps-type-serial-autodetect")

    ios_encaps_type_cpp = Enum.YLeaf(49, "ios-encaps-type-cpp")

    ios_encaps_type_ndlc = Enum.YLeaf(50, "ios-encaps-type-ndlc")

    ios_encaps_type_lapd = Enum.YLeaf(51, "ios-encaps-type-lapd")

    ios_encaps_type_ftc_trunk = Enum.YLeaf(52, "ios-encaps-type-ftc-trunk")

    ios_encaps_type_atmces_t1 = Enum.YLeaf(53, "ios-encaps-type-atmces-t1")

    ios_encaps_type_atmces_e1 = Enum.YLeaf(54, "ios-encaps-type-atmces-e1")

    ios_encaps_type_voice = Enum.YLeaf(55, "ios-encaps-type-voice")

    ios_encaps_type_alc = Enum.YLeaf(56, "ios-encaps-type-alc")

    ios_encaps_type_uts = Enum.YLeaf(57, "ios-encaps-type-uts")

    ios_encaps_type_trisl = Enum.YLeaf(58, "ios-encaps-type-trisl")

    ios_encaps_type_mcns = Enum.YLeaf(59, "ios-encaps-type-mcns")

    ios_encaps_type_atmces = Enum.YLeaf(60, "ios-encaps-type-atmces")

    ios_encaps_type_trans = Enum.YLeaf(61, "ios-encaps-type-trans")

    ios_encaps_type_clear_channel = Enum.YLeaf(62, "ios-encaps-type-clear-channel")

    ios_encaps_type_tc_atm = Enum.YLeaf(63, "ios-encaps-type-tc-atm")

    ios_encaps_type_fr_ppp = Enum.YLeaf(64, "ios-encaps-type-fr-ppp")

    ios_encaps_type_dot1q = Enum.YLeaf(65, "ios-encaps-type-dot1q")

    ios_encaps_type_funi = Enum.YLeaf(66, "ios-encaps-type-funi")

    ios_encaps_type_lapbta = Enum.YLeaf(67, "ios-encaps-type-lapbta")

    ios_encaps_type_docsis = Enum.YLeaf(68, "ios-encaps-type-docsis")

    ios_encaps_type_np_inband = Enum.YLeaf(69, "ios-encaps-type-np-inband")

    ios_encaps_type_ss7_mtp2 = Enum.YLeaf(70, "ios-encaps-type-ss7-mtp2")

    ios_encaps_type_gtp = Enum.YLeaf(71, "ios-encaps-type-gtp")

    ios_encaps_type_isl_switchport = Enum.YLeaf(72, "ios-encaps-type-isl-switchport")

    ios_encaps_type_srp = Enum.YLeaf(73, "ios-encaps-type-srp")

    ios_encaps_type_ppp_etype = Enum.YLeaf(74, "ios-encaps-type-ppp-etype")

    ios_encaps_type_atm_ppp = Enum.YLeaf(75, "ios-encaps-type-atm-ppp")

    ios_encaps_type_mfr = Enum.YLeaf(76, "ios-encaps-type-mfr")

    ios_encaps_type_srp2 = Enum.YLeaf(77, "ios-encaps-type-srp2")

    ios_encaps_type_fr_extended = Enum.YLeaf(78, "ios-encaps-type-fr-extended")

    ios_encaps_type_pppoe = Enum.YLeaf(79, "ios-encaps-type-pppoe")

    ios_encaps_type_ouni_sdcc = Enum.YLeaf(80, "ios-encaps-type-ouni-sdcc")

    ios_encaps_type_multiservice = Enum.YLeaf(81, "ios-encaps-type-multiservice")

    ios_encaps_type_container = Enum.YLeaf(82, "ios-encaps-type-container")

    ios_encaps_type_dot1ad = Enum.YLeaf(83, "ios-encaps-type-dot1ad")

    ios_encaps_type_cem = Enum.YLeaf(84, "ios-encaps-type-cem")

    ios_encaps_type_dot1ah = Enum.YLeaf(85, "ios-encaps-type-dot1ah")

    ios_encaps_type_ptp = Enum.YLeaf(86, "ios-encaps-type-ptp")

    ios_encaps_type_ssl = Enum.YLeaf(87, "ios-encaps-type-ssl")

    ios_encaps_type_lisp = Enum.YLeaf(88, "ios-encaps-type-lisp")

    ios_encaps_type_dsp_spa = Enum.YLeaf(89, "ios-encaps-type-dsp-spa")

    ios_encaps_type_t101 = Enum.YLeaf(90, "ios-encaps-type-t101")

    ios_encaps_type_crypto = Enum.YLeaf(91, "ios-encaps-type-crypto")

    ios_encaps_type_rawtcp = Enum.YLeaf(92, "ios-encaps-type-rawtcp")

    ios_encaps_type_async = Enum.YLeaf(93, "ios-encaps-type-async")

    ios_encaps_type_cmd = Enum.YLeaf(94, "ios-encaps-type-cmd")

    ios_encaps_type_scada = Enum.YLeaf(95, "ios-encaps-type-scada")

    ios_encaps_type_rawudp = Enum.YLeaf(96, "ios-encaps-type-rawudp")

    ios_encaps_type_relay_line = Enum.YLeaf(97, "ios-encaps-type-relay-line")

    ios_encaps_type_rawmpls = Enum.YLeaf(98, "ios-encaps-type-rawmpls")

    ios_encaps_type_arpa_nid = Enum.YLeaf(99, "ios-encaps-type-arpa-nid")


class IosLinktype(Enum):
    """
    IosLinktype (Enum Class)

    Link Type

    .. data:: ios_linktype_illegal = 0

    	invalid link type

    .. data:: ios_linktype_arp = 1

    	IP ARP

    .. data:: ios_linktype_rarp = 2

    	Reverse ARP

    .. data:: ios_linktype_xarp = 3

    	Xerox ARP

    .. data:: ios_linktype_probe = 4

    	HP's 802 version of ARP

    .. data:: ios_linktype_loop = 5

    	Ethernet loopback

    .. data:: ios_linktype_address = 6

    	cisco Systems Serial ARP

    .. data:: ios_linktype_ip = 7

    	Internet Protocol (IP)

    .. data:: ios_linktype_pup = 8

    	Xerox PARC Universal Protocol (PUP)

    .. data:: ios_linktype_9_unused = 9

    	Available Unused Slot

    .. data:: ios_linktype_xns = 10

    	XNS protocol (Xerox original)

    .. data:: ios_linktype_novell = 11

    	Novell IPX

    .. data:: ios_linktype_apollo = 12

    	Apollo Domain

    .. data:: ios_linktype_vines = 13

    	Banyan Vines IP

    .. data:: ios_linktype_pad = 14

    	X.2[89] PAD protocol

    .. data:: ios_linktype_x25 = 15

    	X.25 for purists

    .. data:: ios_linktype_appletalk = 16

    	AppleTalk - Extended DDP

    .. data:: ios_linktype_aarp = 17

    	Appletalk ARP

    .. data:: ios_linktype_dec_spanning = 18

    	DEC spanning tree

    .. data:: ios_linktype_ieee_spanning = 19

    	IEEE spanning tree BPDU

    .. data:: ios_linktype_nbf = 20

    	NBF NetBios Frames

    .. data:: ios_linktype_21_unused = 21

    	Unused Link Type

    .. data:: ios_linktype_decnet = 22

    	DECnet Phase IV node unicast

    .. data:: ios_linktype_decnet_router_l1 = 23

    	(Old) DECnet PhaseIV router multicast

    .. data:: ios_linktype_decnet_node = 24

    	DECnet Phase IV node multicast

    .. data:: ios_linktype_clns = 25

    	OSI 8473 ES-IS 9542, etc.

    .. data:: ios_linktype_clns_all_es = 26

    	ES-IS Multicast - all end systems

    .. data:: ios_linktype_clns_all_is = 27

    	ES-IS Multicast - all intermed.

    .. data:: ios_linktype_clns_bcast = 28

    	CLNS & ES-IS Broadcasts

    .. data:: ios_linktype_xot = 29

    	X.25 over TCP

    .. data:: ios_linktype_ppp = 30

    	Protocol PPP

    .. data:: ios_linktype_lat = 31

    	DEC LAT terminal protocol

    .. data:: ios_linktype_vines_echo = 32

    	Banyan Vines Echo Protocol

    .. data:: ios_linktype_vines_loop = 33

    	Banyan Vines Loopback Protocol

    .. data:: ios_linktype_atalk_short = 34

    	AppleTalk short DDP

    .. data:: ios_linktype_mop_boot = 35

    	DEC MOP booting protocol

    .. data:: ios_linktype_mop_console = 36

    	DEC MOP console protocol

    .. data:: ios_linktype_rsrb = 37

    	RSRB raw

    .. data:: ios_linktype_bridge = 38

    	transparent bridge traffic

    .. data:: ios_linktype_stun = 39

    	Stunnel

    .. data:: ios_linktype_fr_arp = 40

    	Frame Relay

    .. data:: ios_linktype_smds_arp = 41

    	SMDS own ARP

    .. data:: ios_linktype_mac = 42

    	MAC packets

    .. data:: ios_linktype_ibmnm = 43

    	IBM Network Management packets

    .. data:: ios_linktype_uarp = 44

    	Ultranet

    .. data:: ios_linktype_ultra_hello = 45

    	Ultranet

    .. data:: ios_linktype_x25service = 46

    	X.25 services

    .. data:: ios_linktype_uncompressed_tcp = 47

    	Uncompressed TCP/IP

    .. data:: ios_linktype_compressed_tcp = 48

    	Compressed TCP/IP

    .. data:: ios_linktype_llc2 = 49

    	LLC type II

    .. data:: ios_linktype_cmns = 50

    	CMNS--X.25 over non-serial media

    .. data:: ios_linktype_isis_all_l1_is = 51

    	ISIS - All Level 1 ISes

    .. data:: ios_linktype_isis_all_l2_is = 52

    	ISIS - All Level 2 ISes

    .. data:: ios_linktype_fr_switch = 53

    	FR switching over IP tunnel

    .. data:: ios_linktype_decnet_prime_router = 54

    	Ph-IV Prime all routers

    .. data:: ios_linktype_srb = 55

    	source route bridge traffic

    .. data:: ios_linktype_qllc = 56

    	qllc (SNA over X.25)

    .. data:: ios_linktype_x25_multi_enc = 57

    	X.25 multiprotocol encapsulation

    .. data:: ios_linktype_lex = 58

    	Lan Extension Protocol

    .. data:: ios_linktype_lex_rcmd = 59

    	Lex-NCP + LEX Remote commands

    .. data:: ios_linktype_decnet_router_l2 = 60

    	DECnet PhaseIV L2 router multcast

    .. data:: ios_linktype_cls = 61

    	Frames from RSRB vring->CLS vring

    .. data:: ios_linktype_snapshot = 62

    	Start dialing, don't send frame

    .. data:: ios_linktype_dlsw = 63

    	Data Link Switching traffic

    .. data:: ios_linktype_sde = 64

    	802.10 Secure Data Exchange

    .. data:: ios_linktype_cdp = 65

    	Cisco Discovery Protocol

    .. data:: ios_linktype_ppp_compression = 66

    	Compression Control Protocol PPP

    .. data:: ios_linktype_nmp = 67

    	Local LNM packet traffic

    .. data:: ios_linktype_bstun = 68

    	block serial tunnel

    .. data:: ios_linktype_ipc = 69

    	Out-of-band IPC

    .. data:: ios_linktype_love = 70

    	CIP statistics

    .. data:: ios_linktype_cfgack = 71

    	CIP asynchronous cfg acks

    .. data:: ios_linktype_appn_anr = 72

    	APPN HPR ANR traffic

    .. data:: ios_linktype_multilink = 73

    	Multilink protocol

    .. data:: ios_linktype_nhrp = 74

    	Next Hop Resolution Protocol (NHRP)

    .. data:: ios_linktype_mac_exp = 75

    	MAC frames are express buffered

    .. data:: ios_linktype_cgmp = 76

    	Cisco Group Management Protocol

    .. data:: ios_linktype_vtp = 77

    	Cisco VLAN Transport Protocol

    .. data:: ios_linktype_cpp = 78

    	Combinet proprietary encaps

    .. data:: ios_linktype_ipv6 = 79

    	IP version 6

    .. data:: ios_linktype_atm = 80

    	Asynchronous Transfer Mode (ATM)

    .. data:: ios_linktype_isl = 81

    	Cisco Inter Switch Link

    .. data:: ios_linktype_bap = 82

    	Bandwidth Allocation Protocol

    .. data:: ios_linktype_compressed_rtp = 83

    	Compressed RTP-UDP-IP

    .. data:: ios_linktype_compressed_udp = 84

    	Compressed UDP-IP

    .. data:: ios_linktype_uncompressed_udp = 85

    	Unompressed RTP-UDP-IP

    .. data:: ios_linktype_context_status = 86

    	RTP context error

    .. data:: ios_linktype_fr_switch_serial = 87

    	FR switching over serial line

    	internal packet identification only

    .. data:: ios_linktype_c5_ibipc = 88

    	Cat5k inband ipc

    .. data:: ios_linktype_nlsp_multicast = 89

    	NLSP multicast hello/update

    .. data:: ios_linktype_tag = 90

    	Tag switched packet

    .. data:: ios_linktype_mtag = 91

    	Multicast TAG (MTAG)

    .. data:: ios_linktype_alps = 92

    	Airline Protocol Support

    .. data:: ios_linktype_drip = 93

    	Cisco DRIP

    .. data:: ios_linktype_voice = 94

    	Voice over ATM

    .. data:: ios_linktype_fr_atm = 95

    	FR-ATM network interworking

    .. data:: ios_linktype_fcp = 96

    	layer3 switching on earl2

    .. data:: ios_linktype_voice_no_rt = 97

    	Non real time voice

    .. data:: ios_linktype_vlan_br_spanning = 98

    	VLAN Bridge spanning tree BPDU

    .. data:: ios_linktype_dot1q = 99

    	IEEE 802.1Q

    .. data:: ios_linktype_cisco_ipc = 100

    	cisco ipc msg.

    .. data:: ios_linktype_vsi = 101

    	Cisco VSI Protocol

    .. data:: ios_linktype_isdn_manual_call = 102

    	for manual ISDN call

    .. data:: ios_linktype_comp_non_tcp = 103

    	IPHC compression

    .. data:: ios_linktype_comp_tcp_nodelta = 104

    	IPHC compression

    .. data:: ios_linktype_fr_atm_srv = 105

    	FR-ATM service interworking

    .. data:: ios_linktype_fr_eek = 106

    	FR end-to-end keepalive

    .. data:: ios_linktype_ehsa = 107

    	Test type for EHSA

    .. data:: ios_linktype_mscp = 108

    	Multicast Shortcut PDU

    .. data:: ios_linktype_scp = 109

    	Cat6k - linecard control

    .. data:: ios_linktype_pppoe_discovery = 110

    	PPP over Ethernet Discovery

    .. data:: ios_linktype_pppoe_session = 111

    	PPP over Ethernet Session

    .. data:: ios_linktype_l2rly = 112

    	GPRS l2rly

    .. data:: ios_linktype_gtp = 113

    	GPRS GTP

    .. data:: ios_linktype_comp_rtp_16 = 114

    	Compressed RTP-UDP-IP 16 bit CID

    .. data:: ios_linktype_comp_udp_16 = 115

    	Compressed RTP-UDP-IP 16 bit CID

    .. data:: ios_linktype_atm_switch = 116

    	ATM PDU switching

    .. data:: ios_linktype_pagp = 117

    	Port Aggregation Protocol

    .. data:: ios_linktype_sstp = 118

    	Shared Spanning Tree BPDU

    .. data:: ios_linktype_rlq_req = 119

    	STP Root Link Query Request

    .. data:: ios_linktype_rlq_resp = 120

    	STP Root Link Query Response

    .. data:: ios_linktype_dyntrk = 121

    	Dynamic Trunk Protocol (DTP) PDU

    .. data:: ios_linktype_mls_ip = 122

    	layer3 switching internal flush

    .. data:: ios_linktype_dyntrk_encap = 123

    	DTP PDUs sent w/ SW ISL encap

    .. data:: ios_linktype_udld = 124

    	UniDirectional Link Protocol

    .. data:: ios_linktype_srp = 125

    	Spatial Reuse Protocol (SRP)

    .. data:: ios_linktype_rgmp = 126

    	Router-port Group Management Protocol (RGMP)

    .. data:: ios_linktype_mistp = 127

    	Multi Instance Spanning Tree

    .. data:: ios_linktype_compressed_fr = 128

    	Compressed Frame Relay

    .. data:: ios_linktype_vito_scp = 129

    	Vito SCP protocol

    .. data:: ios_linktype_const_ftep = 130

    	Constellation Forwarding Table Edit Protocol

    .. data:: ios_linktype_vlan_switch = 131

    	VLAN PDU switching

    .. data:: ios_linktype_atom = 132

    	ATOM (Process) switching

    .. data:: ios_linktype_raw = 133

    	Raw switching

    .. data:: ios_linktype_oscp = 134

    	Optical Supervisory Channel Protocol

    .. data:: ios_linktype_diag = 135

    	For Diag lpback via Ethernet chip

    .. data:: ios_linktype_stack_disc = 136

    	STP DUF STACK discovery

    .. data:: ios_linktype_fast_trans = 137

    	STP DUF Fast Transition

    .. data:: ios_linktype_dot1x = 138

    	802.1X Port Access Entity Type

    .. data:: ios_linktype_fr_frag = 139

    	FR fragmentation

    .. data:: ios_linktype_slow_proto = 140

    	802.3AD Slow Protocol

    .. data:: ios_linktype_eompls = 141

    	sync damage please name me

    .. data:: ios_linktype_ieee_dot1q = 142

    	sync damage please name me

    .. data:: ios_linktype_voice_nrt = 143

    	sync damage please name me

    .. data:: ios_linktype_uti_raw = 144

    	sync damage please name me

    .. data:: ios_linktype_hdlc_hapi = 145

    	ACE IPsec accelerator control

    .. data:: ios_linktype_cwan_ipsec = 146

    	IPSec acceleration for CWAN

    .. data:: ios_linktype_sstp_spanning = 147

    	Shared Spanning Tree BPDU

    .. data:: ios_linktype_fr_saa = 148

    	FR SAA round trip measurement

    .. data:: ios_linktype_froe = 149

    	Frame Relay over Ethernet

    .. data:: ios_linktype_vpdn = 150

    	Forwarded VPDN packets

    .. data:: ios_linktype_slm_saa = 151

    	SAA SLM Link Type

    .. data:: ios_linktype_rf_kpa = 152

    	Redundancy Facility keepalives

    .. data:: ios_linktype_rbcp = 153

    	Router blade control protocol

    .. data:: ios_linktype_p2ipc = 154

    	P2IPC LinkType

    .. data:: ios_linktype_p2ipc_mpls = 155

    	P2IPC LinkType for MPLS controller

    .. data:: ios_linktype_xconnect = 156

    	Xconnect (Process switching)

    .. data:: ios_linktype_slm_fr_saa = 157

    	FR SLM Link Type

    .. data:: ios_linktype_cdma_rp = 158

    	CDMA RP

    .. data:: ios_linktype_pw_ip_deprecated = 159

    	Deprecated

    	do not reuse due to potential ISSU conflict

    .. data:: ios_linktype_vj_uncomp_tcp = 160

    	VJ Uncompressed TCP/IP

    .. data:: ios_linktype_vj_comp_tcp = 161

    	VJ Compressed TCP/IP

    .. data:: ios_linktype_online_diags = 162

    	Online Diags

    .. data:: ios_linktype_vrf_ipsec = 163

    	VRF Aware Ipsec Crypto

    .. data:: ios_linktype_broadcom = 164

    	Link Broadcom

    .. data:: ios_linktype_http = 165

    	HyperText Transfer Protocol (HTTP)

    .. data:: ios_linktype_lfp = 166

    	Link Fault Propagation

    .. data:: ios_linktype_drprip = 167

    	Dual RPR Interconnect Protocol

    .. data:: ios_linktype_ether_cfm = 168

    	Ethernet Connectivity Fault Management

    	(Version D1)

    .. data:: ios_linktype_ether_oam = 169

    	Ethernet OAM (802.3ah) 

    .. data:: ios_linktype_mmu = 170

    	Mac Move Update

    .. data:: ios_linktype_vslp = 171

    	Virtual Switch Link Protocol

    .. data:: ios_linktype_ether_lmi = 172

    	Ethernet Local Management Interface

    .. data:: ios_linktype_lldp = 173

    	Link Layer Discovery Protocol(IEEE 802.1AB)

    .. data:: ios_linktype_gvrp = 174

    	GARP VLAN Registration Protocol (802.1Q GVRP)

    .. data:: ios_linktype_gmrp = 175

    	GARP Multicast Registration Protocol (802.1Q GMRP)

    .. data:: ios_linktype_ancp = 176

    	Access Node Control Protocol

    .. data:: ios_linktype_rep = 177

    	Resilient Ethernet Protocol

    .. data:: ios_linktype_rep_hfl = 178

    	Resilient Ethernet Protocol Hardware Flood Layer

    .. data:: ios_linktype_ipe = 179

    	IPe Bootstrap

    .. data:: ios_linktype_mvrp = 180

    	Multiple VLAN Registration Protocol

    	MVRP (802.1ak)

    .. data:: ios_linktype_vsda = 181

    	Virtual Switch Dual Active Protocol

    .. data:: ios_linktype_ecfm = 182

    	Ethernet Connectivity Fault Management

    	(IEEE Version)

    .. data:: ios_linktype_dot1ah = 183

    	Ethernet Mac tunneling Protocol

    	(802.1ah I-TAG Version)

    .. data:: ios_linktype_sdp = 184

    	Satellite Discovery And Control protocol

    .. data:: ios_linktype_cdpfwd = 185

    	CDP Forwarding (CDPFWD)

    .. data:: ios_linktype_t101 = 186

    	IEC 60870-5 101 Async Link

    .. data:: ios_linktype_rsvp = 187

    	RSVP Protocol 

    .. data:: ios_linktype_isisl2_otv_all_l1_is = 188

    	ISIS L2 OTV - All Level 1 ISes

    .. data:: ios_linktype_isisl2_otv_all_l2_is = 189

    	ISIS L2 OTV - All Level 2 ISes

    .. data:: ios_linktype_g8032 = 190

    	G.8032

    .. data:: ios_linktype_sdac = 191

    	Satellite Discovery And Control protocol

    .. data:: ios_linktype_ptppd = 192

    	PTP Peer Delay protocol

    .. data:: ios_linktype_rawtcp = 193

    	RAWTCP

    .. data:: ios_linktype_an_ch = 194

    	Autonomic Networking

    .. data:: ios_linktype_fex_sdp = 195

    	FEX SDP/SRP Satellite Discovey Protocol

    	Satellite Registration Protocols

    .. data:: ios_linktype_esmc = 196

    	Ethernet Synchronous Messaging Channel (ESCM)

    .. data:: ios_linktype_cisp = 197

    	Client Information Signaling Protocol (CISP)

    .. data:: ios_linktype_async = 198

    	punt/inject path Async Packet

    .. data:: ios_linktype_msrp = 199

    	Multiple Stream Reservation Protocol

    .. data:: ios_linktype_macsec_post_exp = 200

    	Online Diags

    .. data:: ios_linktype_macsec_sectag = 201

    	Online Diags

    """

    ios_linktype_illegal = Enum.YLeaf(0, "ios-linktype-illegal")

    ios_linktype_arp = Enum.YLeaf(1, "ios-linktype-arp")

    ios_linktype_rarp = Enum.YLeaf(2, "ios-linktype-rarp")

    ios_linktype_xarp = Enum.YLeaf(3, "ios-linktype-xarp")

    ios_linktype_probe = Enum.YLeaf(4, "ios-linktype-probe")

    ios_linktype_loop = Enum.YLeaf(5, "ios-linktype-loop")

    ios_linktype_address = Enum.YLeaf(6, "ios-linktype-address")

    ios_linktype_ip = Enum.YLeaf(7, "ios-linktype-ip")

    ios_linktype_pup = Enum.YLeaf(8, "ios-linktype-pup")

    ios_linktype_9_unused = Enum.YLeaf(9, "ios-linktype-9-unused")

    ios_linktype_xns = Enum.YLeaf(10, "ios-linktype-xns")

    ios_linktype_novell = Enum.YLeaf(11, "ios-linktype-novell")

    ios_linktype_apollo = Enum.YLeaf(12, "ios-linktype-apollo")

    ios_linktype_vines = Enum.YLeaf(13, "ios-linktype-vines")

    ios_linktype_pad = Enum.YLeaf(14, "ios-linktype-pad")

    ios_linktype_x25 = Enum.YLeaf(15, "ios-linktype-x25")

    ios_linktype_appletalk = Enum.YLeaf(16, "ios-linktype-appletalk")

    ios_linktype_aarp = Enum.YLeaf(17, "ios-linktype-aarp")

    ios_linktype_dec_spanning = Enum.YLeaf(18, "ios-linktype-dec-spanning")

    ios_linktype_ieee_spanning = Enum.YLeaf(19, "ios-linktype-ieee-spanning")

    ios_linktype_nbf = Enum.YLeaf(20, "ios-linktype-nbf")

    ios_linktype_21_unused = Enum.YLeaf(21, "ios-linktype-21-unused")

    ios_linktype_decnet = Enum.YLeaf(22, "ios-linktype-decnet")

    ios_linktype_decnet_router_l1 = Enum.YLeaf(23, "ios-linktype-decnet-router-l1")

    ios_linktype_decnet_node = Enum.YLeaf(24, "ios-linktype-decnet-node")

    ios_linktype_clns = Enum.YLeaf(25, "ios-linktype-clns")

    ios_linktype_clns_all_es = Enum.YLeaf(26, "ios-linktype-clns-all-es")

    ios_linktype_clns_all_is = Enum.YLeaf(27, "ios-linktype-clns-all-is")

    ios_linktype_clns_bcast = Enum.YLeaf(28, "ios-linktype-clns-bcast")

    ios_linktype_xot = Enum.YLeaf(29, "ios-linktype-xot")

    ios_linktype_ppp = Enum.YLeaf(30, "ios-linktype-ppp")

    ios_linktype_lat = Enum.YLeaf(31, "ios-linktype-lat")

    ios_linktype_vines_echo = Enum.YLeaf(32, "ios-linktype-vines-echo")

    ios_linktype_vines_loop = Enum.YLeaf(33, "ios-linktype-vines-loop")

    ios_linktype_atalk_short = Enum.YLeaf(34, "ios-linktype-atalk-short")

    ios_linktype_mop_boot = Enum.YLeaf(35, "ios-linktype-mop-boot")

    ios_linktype_mop_console = Enum.YLeaf(36, "ios-linktype-mop-console")

    ios_linktype_rsrb = Enum.YLeaf(37, "ios-linktype-rsrb")

    ios_linktype_bridge = Enum.YLeaf(38, "ios-linktype-bridge")

    ios_linktype_stun = Enum.YLeaf(39, "ios-linktype-stun")

    ios_linktype_fr_arp = Enum.YLeaf(40, "ios-linktype-fr-arp")

    ios_linktype_smds_arp = Enum.YLeaf(41, "ios-linktype-smds-arp")

    ios_linktype_mac = Enum.YLeaf(42, "ios-linktype-mac")

    ios_linktype_ibmnm = Enum.YLeaf(43, "ios-linktype-ibmnm")

    ios_linktype_uarp = Enum.YLeaf(44, "ios-linktype-uarp")

    ios_linktype_ultra_hello = Enum.YLeaf(45, "ios-linktype-ultra-hello")

    ios_linktype_x25service = Enum.YLeaf(46, "ios-linktype-x25service")

    ios_linktype_uncompressed_tcp = Enum.YLeaf(47, "ios-linktype-uncompressed-tcp")

    ios_linktype_compressed_tcp = Enum.YLeaf(48, "ios-linktype-compressed-tcp")

    ios_linktype_llc2 = Enum.YLeaf(49, "ios-linktype-llc2")

    ios_linktype_cmns = Enum.YLeaf(50, "ios-linktype-cmns")

    ios_linktype_isis_all_l1_is = Enum.YLeaf(51, "ios-linktype-isis-all-l1-is")

    ios_linktype_isis_all_l2_is = Enum.YLeaf(52, "ios-linktype-isis-all-l2-is")

    ios_linktype_fr_switch = Enum.YLeaf(53, "ios-linktype-fr-switch")

    ios_linktype_decnet_prime_router = Enum.YLeaf(54, "ios-linktype-decnet-prime-router")

    ios_linktype_srb = Enum.YLeaf(55, "ios-linktype-srb")

    ios_linktype_qllc = Enum.YLeaf(56, "ios-linktype-qllc")

    ios_linktype_x25_multi_enc = Enum.YLeaf(57, "ios-linktype-x25-multi-enc")

    ios_linktype_lex = Enum.YLeaf(58, "ios-linktype-lex")

    ios_linktype_lex_rcmd = Enum.YLeaf(59, "ios-linktype-lex-rcmd")

    ios_linktype_decnet_router_l2 = Enum.YLeaf(60, "ios-linktype-decnet-router-l2")

    ios_linktype_cls = Enum.YLeaf(61, "ios-linktype-cls")

    ios_linktype_snapshot = Enum.YLeaf(62, "ios-linktype-snapshot")

    ios_linktype_dlsw = Enum.YLeaf(63, "ios-linktype-dlsw")

    ios_linktype_sde = Enum.YLeaf(64, "ios-linktype-sde")

    ios_linktype_cdp = Enum.YLeaf(65, "ios-linktype-cdp")

    ios_linktype_ppp_compression = Enum.YLeaf(66, "ios-linktype-ppp-compression")

    ios_linktype_nmp = Enum.YLeaf(67, "ios-linktype-nmp")

    ios_linktype_bstun = Enum.YLeaf(68, "ios-linktype-bstun")

    ios_linktype_ipc = Enum.YLeaf(69, "ios-linktype-ipc")

    ios_linktype_love = Enum.YLeaf(70, "ios-linktype-love")

    ios_linktype_cfgack = Enum.YLeaf(71, "ios-linktype-cfgack")

    ios_linktype_appn_anr = Enum.YLeaf(72, "ios-linktype-appn-anr")

    ios_linktype_multilink = Enum.YLeaf(73, "ios-linktype-multilink")

    ios_linktype_nhrp = Enum.YLeaf(74, "ios-linktype-nhrp")

    ios_linktype_mac_exp = Enum.YLeaf(75, "ios-linktype-mac-exp")

    ios_linktype_cgmp = Enum.YLeaf(76, "ios-linktype-cgmp")

    ios_linktype_vtp = Enum.YLeaf(77, "ios-linktype-vtp")

    ios_linktype_cpp = Enum.YLeaf(78, "ios-linktype-cpp")

    ios_linktype_ipv6 = Enum.YLeaf(79, "ios-linktype-ipv6")

    ios_linktype_atm = Enum.YLeaf(80, "ios-linktype-atm")

    ios_linktype_isl = Enum.YLeaf(81, "ios-linktype-isl")

    ios_linktype_bap = Enum.YLeaf(82, "ios-linktype-bap")

    ios_linktype_compressed_rtp = Enum.YLeaf(83, "ios-linktype-compressed-rtp")

    ios_linktype_compressed_udp = Enum.YLeaf(84, "ios-linktype-compressed-udp")

    ios_linktype_uncompressed_udp = Enum.YLeaf(85, "ios-linktype-uncompressed-udp")

    ios_linktype_context_status = Enum.YLeaf(86, "ios-linktype-context-status")

    ios_linktype_fr_switch_serial = Enum.YLeaf(87, "ios-linktype-fr-switch-serial")

    ios_linktype_c5_ibipc = Enum.YLeaf(88, "ios-linktype-c5-ibipc")

    ios_linktype_nlsp_multicast = Enum.YLeaf(89, "ios-linktype-nlsp-multicast")

    ios_linktype_tag = Enum.YLeaf(90, "ios-linktype-tag")

    ios_linktype_mtag = Enum.YLeaf(91, "ios-linktype-mtag")

    ios_linktype_alps = Enum.YLeaf(92, "ios-linktype-alps")

    ios_linktype_drip = Enum.YLeaf(93, "ios-linktype-drip")

    ios_linktype_voice = Enum.YLeaf(94, "ios-linktype-voice")

    ios_linktype_fr_atm = Enum.YLeaf(95, "ios-linktype-fr-atm")

    ios_linktype_fcp = Enum.YLeaf(96, "ios-linktype-fcp")

    ios_linktype_voice_no_rt = Enum.YLeaf(97, "ios-linktype-voice-no-rt")

    ios_linktype_vlan_br_spanning = Enum.YLeaf(98, "ios-linktype-vlan-br-spanning")

    ios_linktype_dot1q = Enum.YLeaf(99, "ios-linktype-dot1q")

    ios_linktype_cisco_ipc = Enum.YLeaf(100, "ios-linktype-cisco-ipc")

    ios_linktype_vsi = Enum.YLeaf(101, "ios-linktype-vsi")

    ios_linktype_isdn_manual_call = Enum.YLeaf(102, "ios-linktype-isdn-manual-call")

    ios_linktype_comp_non_tcp = Enum.YLeaf(103, "ios-linktype-comp-non-tcp")

    ios_linktype_comp_tcp_nodelta = Enum.YLeaf(104, "ios-linktype-comp-tcp-nodelta")

    ios_linktype_fr_atm_srv = Enum.YLeaf(105, "ios-linktype-fr-atm-srv")

    ios_linktype_fr_eek = Enum.YLeaf(106, "ios-linktype-fr-eek")

    ios_linktype_ehsa = Enum.YLeaf(107, "ios-linktype-ehsa")

    ios_linktype_mscp = Enum.YLeaf(108, "ios-linktype-mscp")

    ios_linktype_scp = Enum.YLeaf(109, "ios-linktype-scp")

    ios_linktype_pppoe_discovery = Enum.YLeaf(110, "ios-linktype-pppoe-discovery")

    ios_linktype_pppoe_session = Enum.YLeaf(111, "ios-linktype-pppoe-session")

    ios_linktype_l2rly = Enum.YLeaf(112, "ios-linktype-l2rly")

    ios_linktype_gtp = Enum.YLeaf(113, "ios-linktype-gtp")

    ios_linktype_comp_rtp_16 = Enum.YLeaf(114, "ios-linktype-comp-rtp-16")

    ios_linktype_comp_udp_16 = Enum.YLeaf(115, "ios-linktype-comp-udp-16")

    ios_linktype_atm_switch = Enum.YLeaf(116, "ios-linktype-atm-switch")

    ios_linktype_pagp = Enum.YLeaf(117, "ios-linktype-pagp")

    ios_linktype_sstp = Enum.YLeaf(118, "ios-linktype-sstp")

    ios_linktype_rlq_req = Enum.YLeaf(119, "ios-linktype-rlq-req")

    ios_linktype_rlq_resp = Enum.YLeaf(120, "ios-linktype-rlq-resp")

    ios_linktype_dyntrk = Enum.YLeaf(121, "ios-linktype-dyntrk")

    ios_linktype_mls_ip = Enum.YLeaf(122, "ios-linktype-mls-ip")

    ios_linktype_dyntrk_encap = Enum.YLeaf(123, "ios-linktype-dyntrk-encap")

    ios_linktype_udld = Enum.YLeaf(124, "ios-linktype-udld")

    ios_linktype_srp = Enum.YLeaf(125, "ios-linktype-srp")

    ios_linktype_rgmp = Enum.YLeaf(126, "ios-linktype-rgmp")

    ios_linktype_mistp = Enum.YLeaf(127, "ios-linktype-mistp")

    ios_linktype_compressed_fr = Enum.YLeaf(128, "ios-linktype-compressed-fr")

    ios_linktype_vito_scp = Enum.YLeaf(129, "ios-linktype-vito-scp")

    ios_linktype_const_ftep = Enum.YLeaf(130, "ios-linktype-const-ftep")

    ios_linktype_vlan_switch = Enum.YLeaf(131, "ios-linktype-vlan-switch")

    ios_linktype_atom = Enum.YLeaf(132, "ios-linktype-atom")

    ios_linktype_raw = Enum.YLeaf(133, "ios-linktype-raw")

    ios_linktype_oscp = Enum.YLeaf(134, "ios-linktype-oscp")

    ios_linktype_diag = Enum.YLeaf(135, "ios-linktype-diag")

    ios_linktype_stack_disc = Enum.YLeaf(136, "ios-linktype-stack-disc")

    ios_linktype_fast_trans = Enum.YLeaf(137, "ios-linktype-fast-trans")

    ios_linktype_dot1x = Enum.YLeaf(138, "ios-linktype-dot1x")

    ios_linktype_fr_frag = Enum.YLeaf(139, "ios-linktype-fr-frag")

    ios_linktype_slow_proto = Enum.YLeaf(140, "ios-linktype-slow-proto")

    ios_linktype_eompls = Enum.YLeaf(141, "ios-linktype-eompls")

    ios_linktype_ieee_dot1q = Enum.YLeaf(142, "ios-linktype-ieee-dot1q")

    ios_linktype_voice_nrt = Enum.YLeaf(143, "ios-linktype-voice-nrt")

    ios_linktype_uti_raw = Enum.YLeaf(144, "ios-linktype-uti-raw")

    ios_linktype_hdlc_hapi = Enum.YLeaf(145, "ios-linktype-hdlc-hapi")

    ios_linktype_cwan_ipsec = Enum.YLeaf(146, "ios-linktype-cwan-ipsec")

    ios_linktype_sstp_spanning = Enum.YLeaf(147, "ios-linktype-sstp-spanning")

    ios_linktype_fr_saa = Enum.YLeaf(148, "ios-linktype-fr-saa")

    ios_linktype_froe = Enum.YLeaf(149, "ios-linktype-froe")

    ios_linktype_vpdn = Enum.YLeaf(150, "ios-linktype-vpdn")

    ios_linktype_slm_saa = Enum.YLeaf(151, "ios-linktype-slm-saa")

    ios_linktype_rf_kpa = Enum.YLeaf(152, "ios-linktype-rf-kpa")

    ios_linktype_rbcp = Enum.YLeaf(153, "ios-linktype-rbcp")

    ios_linktype_p2ipc = Enum.YLeaf(154, "ios-linktype-p2ipc")

    ios_linktype_p2ipc_mpls = Enum.YLeaf(155, "ios-linktype-p2ipc-mpls")

    ios_linktype_xconnect = Enum.YLeaf(156, "ios-linktype-xconnect")

    ios_linktype_slm_fr_saa = Enum.YLeaf(157, "ios-linktype-slm-fr-saa")

    ios_linktype_cdma_rp = Enum.YLeaf(158, "ios-linktype-cdma-rp")

    ios_linktype_pw_ip_deprecated = Enum.YLeaf(159, "ios-linktype-pw-ip-deprecated")

    ios_linktype_vj_uncomp_tcp = Enum.YLeaf(160, "ios-linktype-vj-uncomp-tcp")

    ios_linktype_vj_comp_tcp = Enum.YLeaf(161, "ios-linktype-vj-comp-tcp")

    ios_linktype_online_diags = Enum.YLeaf(162, "ios-linktype-online-diags")

    ios_linktype_vrf_ipsec = Enum.YLeaf(163, "ios-linktype-vrf-ipsec")

    ios_linktype_broadcom = Enum.YLeaf(164, "ios-linktype-broadcom")

    ios_linktype_http = Enum.YLeaf(165, "ios-linktype-http")

    ios_linktype_lfp = Enum.YLeaf(166, "ios-linktype-lfp")

    ios_linktype_drprip = Enum.YLeaf(167, "ios-linktype-drprip")

    ios_linktype_ether_cfm = Enum.YLeaf(168, "ios-linktype-ether-cfm")

    ios_linktype_ether_oam = Enum.YLeaf(169, "ios-linktype-ether-oam")

    ios_linktype_mmu = Enum.YLeaf(170, "ios-linktype-mmu")

    ios_linktype_vslp = Enum.YLeaf(171, "ios-linktype-vslp")

    ios_linktype_ether_lmi = Enum.YLeaf(172, "ios-linktype-ether-lmi")

    ios_linktype_lldp = Enum.YLeaf(173, "ios-linktype-lldp")

    ios_linktype_gvrp = Enum.YLeaf(174, "ios-linktype-gvrp")

    ios_linktype_gmrp = Enum.YLeaf(175, "ios-linktype-gmrp")

    ios_linktype_ancp = Enum.YLeaf(176, "ios-linktype-ancp")

    ios_linktype_rep = Enum.YLeaf(177, "ios-linktype-rep")

    ios_linktype_rep_hfl = Enum.YLeaf(178, "ios-linktype-rep-hfl")

    ios_linktype_ipe = Enum.YLeaf(179, "ios-linktype-ipe")

    ios_linktype_mvrp = Enum.YLeaf(180, "ios-linktype-mvrp")

    ios_linktype_vsda = Enum.YLeaf(181, "ios-linktype-vsda")

    ios_linktype_ecfm = Enum.YLeaf(182, "ios-linktype-ecfm")

    ios_linktype_dot1ah = Enum.YLeaf(183, "ios-linktype-dot1ah")

    ios_linktype_sdp = Enum.YLeaf(184, "ios-linktype-sdp")

    ios_linktype_cdpfwd = Enum.YLeaf(185, "ios-linktype-cdpfwd")

    ios_linktype_t101 = Enum.YLeaf(186, "ios-linktype-t101")

    ios_linktype_rsvp = Enum.YLeaf(187, "ios-linktype-rsvp")

    ios_linktype_isisl2_otv_all_l1_is = Enum.YLeaf(188, "ios-linktype-isisl2-otv-all-l1-is")

    ios_linktype_isisl2_otv_all_l2_is = Enum.YLeaf(189, "ios-linktype-isisl2-otv-all-l2-is")

    ios_linktype_g8032 = Enum.YLeaf(190, "ios-linktype-g8032")

    ios_linktype_sdac = Enum.YLeaf(191, "ios-linktype-sdac")

    ios_linktype_ptppd = Enum.YLeaf(192, "ios-linktype-ptppd")

    ios_linktype_rawtcp = Enum.YLeaf(193, "ios-linktype-rawtcp")

    ios_linktype_an_ch = Enum.YLeaf(194, "ios-linktype-an-ch")

    ios_linktype_fex_sdp = Enum.YLeaf(195, "ios-linktype-fex-sdp")

    ios_linktype_esmc = Enum.YLeaf(196, "ios-linktype-esmc")

    ios_linktype_cisp = Enum.YLeaf(197, "ios-linktype-cisp")

    ios_linktype_async = Enum.YLeaf(198, "ios-linktype-async")

    ios_linktype_msrp = Enum.YLeaf(199, "ios-linktype-msrp")

    ios_linktype_macsec_post_exp = Enum.YLeaf(200, "ios-linktype-macsec-post-exp")

    ios_linktype_macsec_sectag = Enum.YLeaf(201, "ios-linktype-macsec-sectag")


class IosSnpaType(Enum):
    """
    IosSnpaType (Enum Class)

    SNPA Type

    .. data:: ios_snpa_type_illegal = 0

    	illegal address

    .. data:: ios_snpa_type_ieee48 = 1

    	48bit IEEE 802.X address

    .. data:: ios_snpa_type_ieee16 = 2

    	16bit IEEE 802.X address

    .. data:: ios_snpa_type_xerox = 3

    	Xerox 3MB experimental ether

    .. data:: ios_snpa_type_x121 = 4

    	CCITT X.121 address

    .. data:: ios_snpa_type_cisco_hdlc = 5

    	cisco HDLC framing

    .. data:: ios_snpa_type_cisco_mlapb = 6

    	cisco multi-LAPB framing

    .. data:: ios_snpa_type_lapb = 7

    	ISO/CCITT LAPB framing

    .. data:: ios_snpa_type_smds48 = 8

    	SMDS w/ 48 bit addresses

    .. data:: ios_snpa_type_cisco_msdlc = 9

    	cisco multi-SDLC framing

    .. data:: ios_snpa_type_fr10 = 10

    	Frame Relay with 10-bit DLCI

    .. data:: ios_snpa_type_ultra = 11

    	CCCI defined Ultranet

    .. data:: ios_snpa_type_cisco_tunnel = 12

    	cisco tunnel and EON encoding

    .. data:: ios_snpa_type_cisco_ctunnel = 13

    	CLNP tunnel

    .. data:: ios_snpa_type_rrr_tunnel = 14

    	rrr tunnel

    .. data:: ios_snpa_type_ppp = 15

    	PPP framing

    .. data:: ios_snpa_type_smds64 = 16

    	SMDS 64-bit addressing

    .. data:: ios_snpa_type_atmvc = 17

    	AIP VC no.

    .. data:: ios_snpa_type_atm_bundle = 18

    	ATM PVC bundle

    .. data:: ios_snpa_type_atm_svc_bundle = 19

    	ATM SVC bundle

    .. data:: ios_snpa_type_atmnsap = 20

    	ATM NSAP address

    .. data:: ios_snpa_type_atm_e164 = 21

    	ATM E164 address

    .. data:: ios_snpa_type_atm_userspecified = 22

    	ATM User Specified address

    .. data:: ios_snpa_type_sdlc = 23

    	SDLC address

    .. data:: ios_snpa_type_x25pvc = 24

    	X.25 Lci fpr PVC's

    .. data:: ios_snpa_type_lapd = 25

    	LAPD framing

    .. data:: ios_snpa_type_masked_atmnsap = 26

    	masked ATM NSAP address

    .. data:: ios_snpa_type_atmesi = 27

    	ATM ESI address

    .. data:: ios_snpa_type_slip = 28

    	SLIP Framing

    .. data:: ios_snpa_type_routedesc = 29

    	route descriptor for TR LANE

    .. data:: ios_snpa_type_srp_outer = 30

    	48bit SRP address on outer ring

    .. data:: ios_snpa_type_srp_inner = 31

    	48bit SRP address on inner ring

    """

    ios_snpa_type_illegal = Enum.YLeaf(0, "ios-snpa-type-illegal")

    ios_snpa_type_ieee48 = Enum.YLeaf(1, "ios-snpa-type-ieee48")

    ios_snpa_type_ieee16 = Enum.YLeaf(2, "ios-snpa-type-ieee16")

    ios_snpa_type_xerox = Enum.YLeaf(3, "ios-snpa-type-xerox")

    ios_snpa_type_x121 = Enum.YLeaf(4, "ios-snpa-type-x121")

    ios_snpa_type_cisco_hdlc = Enum.YLeaf(5, "ios-snpa-type-cisco-hdlc")

    ios_snpa_type_cisco_mlapb = Enum.YLeaf(6, "ios-snpa-type-cisco-mlapb")

    ios_snpa_type_lapb = Enum.YLeaf(7, "ios-snpa-type-lapb")

    ios_snpa_type_smds48 = Enum.YLeaf(8, "ios-snpa-type-smds48")

    ios_snpa_type_cisco_msdlc = Enum.YLeaf(9, "ios-snpa-type-cisco-msdlc")

    ios_snpa_type_fr10 = Enum.YLeaf(10, "ios-snpa-type-fr10")

    ios_snpa_type_ultra = Enum.YLeaf(11, "ios-snpa-type-ultra")

    ios_snpa_type_cisco_tunnel = Enum.YLeaf(12, "ios-snpa-type-cisco-tunnel")

    ios_snpa_type_cisco_ctunnel = Enum.YLeaf(13, "ios-snpa-type-cisco-ctunnel")

    ios_snpa_type_rrr_tunnel = Enum.YLeaf(14, "ios-snpa-type-rrr-tunnel")

    ios_snpa_type_ppp = Enum.YLeaf(15, "ios-snpa-type-ppp")

    ios_snpa_type_smds64 = Enum.YLeaf(16, "ios-snpa-type-smds64")

    ios_snpa_type_atmvc = Enum.YLeaf(17, "ios-snpa-type-atmvc")

    ios_snpa_type_atm_bundle = Enum.YLeaf(18, "ios-snpa-type-atm-bundle")

    ios_snpa_type_atm_svc_bundle = Enum.YLeaf(19, "ios-snpa-type-atm-svc-bundle")

    ios_snpa_type_atmnsap = Enum.YLeaf(20, "ios-snpa-type-atmnsap")

    ios_snpa_type_atm_e164 = Enum.YLeaf(21, "ios-snpa-type-atm-e164")

    ios_snpa_type_atm_userspecified = Enum.YLeaf(22, "ios-snpa-type-atm-userspecified")

    ios_snpa_type_sdlc = Enum.YLeaf(23, "ios-snpa-type-sdlc")

    ios_snpa_type_x25pvc = Enum.YLeaf(24, "ios-snpa-type-x25pvc")

    ios_snpa_type_lapd = Enum.YLeaf(25, "ios-snpa-type-lapd")

    ios_snpa_type_masked_atmnsap = Enum.YLeaf(26, "ios-snpa-type-masked-atmnsap")

    ios_snpa_type_atmesi = Enum.YLeaf(27, "ios-snpa-type-atmesi")

    ios_snpa_type_slip = Enum.YLeaf(28, "ios-snpa-type-slip")

    ios_snpa_type_routedesc = Enum.YLeaf(29, "ios-snpa-type-routedesc")

    ios_snpa_type_srp_outer = Enum.YLeaf(30, "ios-snpa-type-srp-outer")

    ios_snpa_type_srp_inner = Enum.YLeaf(31, "ios-snpa-type-srp-inner")



