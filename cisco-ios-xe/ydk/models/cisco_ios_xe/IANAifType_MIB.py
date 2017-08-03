""" IANAifType_MIB 

This MIB module defines the IANAifType Textual
Convention, and thus the enumerated values of
the ifType object defined in MIB\-II's ifTable.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ianaiftype(Enum):
    """
    Ianaiftype

    This data type is used as the syntax of the ifType

    object in the (updated) definition of MIB\-II's

    ifTable.

    The definition of this textual convention with the

    addition of newly assigned values is published

    periodically by the IANA, in either the Assigned

    Numbers RFC, or some derivative of it specific to

    Internet Network Management number assignments.  (The

    latest arrangements can be obtained by contacting the

    IANA.)

    Requests for new values should be made to IANA via

    email (iana@iana.org).

    The relationship between the assignment of ifType

    values and of OIDs to particular media\-specific MIBs

    is solely the purview of IANA and is subject to change

    without notice.  Quite often, a media\-specific MIB's

    OID\-subtree assignment within MIB\-II's 'transmission'

    subtree will be the same as its ifType value.

    However, in some circumstances this will not be the

    case, and implementors must not pre\-assume any

    specific relationship between ifType values and

    transmission subtree OIDs.

    .. data:: other = 1

    .. data:: regular1822 = 2

    .. data:: hdh1822 = 3

    .. data:: ddnX25 = 4

    .. data:: rfc877x25 = 5

    .. data:: ethernetCsmacd = 6

    .. data:: iso88023Csmacd = 7

    .. data:: iso88024TokenBus = 8

    .. data:: iso88025TokenRing = 9

    .. data:: iso88026Man = 10

    .. data:: starLan = 11

    .. data:: proteon10Mbit = 12

    .. data:: proteon80Mbit = 13

    .. data:: hyperchannel = 14

    .. data:: fddi = 15

    .. data:: lapb = 16

    .. data:: sdlc = 17

    .. data:: ds1 = 18

    .. data:: e1 = 19

    .. data:: basicISDN = 20

    .. data:: primaryISDN = 21

    .. data:: propPointToPointSerial = 22

    .. data:: ppp = 23

    .. data:: softwareLoopback = 24

    .. data:: eon = 25

    .. data:: ethernet3Mbit = 26

    .. data:: nsip = 27

    .. data:: slip = 28

    .. data:: ultra = 29

    .. data:: ds3 = 30

    .. data:: sip = 31

    .. data:: frameRelay = 32

    .. data:: rs232 = 33

    .. data:: para = 34

    .. data:: arcnet = 35

    .. data:: arcnetPlus = 36

    .. data:: atm = 37

    .. data:: miox25 = 38

    .. data:: sonet = 39

    .. data:: x25ple = 40

    .. data:: iso88022llc = 41

    .. data:: localTalk = 42

    .. data:: smdsDxi = 43

    .. data:: frameRelayService = 44

    .. data:: v35 = 45

    .. data:: hssi = 46

    .. data:: hippi = 47

    .. data:: modem = 48

    .. data:: aal5 = 49

    .. data:: sonetPath = 50

    .. data:: sonetVT = 51

    .. data:: smdsIcip = 52

    .. data:: propVirtual = 53

    .. data:: propMultiplexor = 54

    .. data:: ieee80212 = 55

    .. data:: fibreChannel = 56

    .. data:: hippiInterface = 57

    .. data:: frameRelayInterconnect = 58

    .. data:: aflane8023 = 59

    .. data:: aflane8025 = 60

    .. data:: cctEmul = 61

    .. data:: fastEther = 62

    .. data:: isdn = 63

    .. data:: v11 = 64

    .. data:: v36 = 65

    .. data:: g703at64k = 66

    .. data:: g703at2mb = 67

    .. data:: qllc = 68

    .. data:: fastEtherFX = 69

    .. data:: channel = 70

    .. data:: ieee80211 = 71

    .. data:: ibm370parChan = 72

    .. data:: escon = 73

    .. data:: dlsw = 74

    .. data:: isdns = 75

    .. data:: isdnu = 76

    .. data:: lapd = 77

    .. data:: ipSwitch = 78

    .. data:: rsrb = 79

    .. data:: atmLogical = 80

    .. data:: ds0 = 81

    .. data:: ds0Bundle = 82

    .. data:: bsc = 83

    .. data:: async = 84

    .. data:: cnr = 85

    .. data:: iso88025Dtr = 86

    .. data:: eplrs = 87

    .. data:: arap = 88

    .. data:: propCnls = 89

    .. data:: hostPad = 90

    .. data:: termPad = 91

    .. data:: frameRelayMPI = 92

    .. data:: x213 = 93

    .. data:: adsl = 94

    .. data:: radsl = 95

    .. data:: sdsl = 96

    .. data:: vdsl = 97

    .. data:: iso88025CRFPInt = 98

    .. data:: myrinet = 99

    .. data:: voiceEM = 100

    .. data:: voiceFXO = 101

    .. data:: voiceFXS = 102

    .. data:: voiceEncap = 103

    .. data:: voiceOverIp = 104

    .. data:: atmDxi = 105

    .. data:: atmFuni = 106

    .. data:: atmIma = 107

    .. data:: pppMultilinkBundle = 108

    .. data:: ipOverCdlc = 109

    .. data:: ipOverClaw = 110

    .. data:: stackToStack = 111

    .. data:: virtualIpAddress = 112

    .. data:: mpc = 113

    .. data:: ipOverAtm = 114

    .. data:: iso88025Fiber = 115

    .. data:: tdlc = 116

    .. data:: gigabitEthernet = 117

    .. data:: hdlc = 118

    .. data:: lapf = 119

    .. data:: v37 = 120

    .. data:: x25mlp = 121

    .. data:: x25huntGroup = 122

    .. data:: trasnpHdlc = 123

    .. data:: interleave = 124

    .. data:: fast = 125

    .. data:: ip = 126

    .. data:: docsCableMaclayer = 127

    .. data:: docsCableDownstream = 128

    .. data:: docsCableUpstream = 129

    .. data:: a12MppSwitch = 130

    .. data:: tunnel = 131

    .. data:: coffee = 132

    .. data:: ces = 133

    .. data:: atmSubInterface = 134

    .. data:: l2vlan = 135

    .. data:: l3ipvlan = 136

    .. data:: l3ipxvlan = 137

    .. data:: digitalPowerline = 138

    .. data:: mediaMailOverIp = 139

    .. data:: dtm = 140

    .. data:: dcn = 141

    .. data:: ipForward = 142

    .. data:: msdsl = 143

    .. data:: ieee1394 = 144

    .. data:: if_gsn = 145

    .. data:: dvbRccMacLayer = 146

    .. data:: dvbRccDownstream = 147

    .. data:: dvbRccUpstream = 148

    .. data:: atmVirtual = 149

    .. data:: mplsTunnel = 150

    .. data:: srp = 151

    .. data:: voiceOverAtm = 152

    .. data:: voiceOverFrameRelay = 153

    .. data:: idsl = 154

    .. data:: compositeLink = 155

    .. data:: ss7SigLink = 156

    .. data:: propWirelessP2P = 157

    .. data:: frForward = 158

    .. data:: rfc1483 = 159

    .. data:: usb = 160

    .. data:: ieee8023adLag = 161

    .. data:: bgppolicyaccounting = 162

    .. data:: frf16MfrBundle = 163

    .. data:: h323Gatekeeper = 164

    .. data:: h323Proxy = 165

    .. data:: mpls = 166

    .. data:: mfSigLink = 167

    .. data:: hdsl2 = 168

    .. data:: shdsl = 169

    .. data:: ds1FDL = 170

    .. data:: pos = 171

    .. data:: dvbAsiIn = 172

    .. data:: dvbAsiOut = 173

    .. data:: plc = 174

    .. data:: nfas = 175

    .. data:: tr008 = 176

    .. data:: gr303RDT = 177

    .. data:: gr303IDT = 178

    .. data:: isup = 179

    .. data:: propDocsWirelessMaclayer = 180

    .. data:: propDocsWirelessDownstream = 181

    .. data:: propDocsWirelessUpstream = 182

    .. data:: hiperlan2 = 183

    .. data:: propBWAp2Mp = 184

    .. data:: sonetOverheadChannel = 185

    .. data:: digitalWrapperOverheadChannel = 186

    .. data:: aal2 = 187

    .. data:: radioMAC = 188

    .. data:: atmRadio = 189

    .. data:: imt = 190

    .. data:: mvl = 191

    .. data:: reachDSL = 192

    .. data:: frDlciEndPt = 193

    .. data:: atmVciEndPt = 194

    .. data:: opticalChannel = 195

    .. data:: opticalTransport = 196

    .. data:: propAtm = 197

    .. data:: voiceOverCable = 198

    .. data:: infiniband = 199

    .. data:: teLink = 200

    .. data:: q2931 = 201

    .. data:: virtualTg = 202

    .. data:: sipTg = 203

    .. data:: sipSig = 204

    .. data:: docsCableUpstreamChannel = 205

    .. data:: econet = 206

    .. data:: pon155 = 207

    .. data:: pon622 = 208

    .. data:: bridge = 209

    .. data:: linegroup = 210

    .. data:: voiceEMFGD = 211

    .. data:: voiceFGDEANA = 212

    .. data:: voiceDID = 213

    .. data:: mpegTransport = 214

    .. data:: sixToFour = 215

    .. data:: gtp = 216

    .. data:: pdnEtherLoop1 = 217

    .. data:: pdnEtherLoop2 = 218

    .. data:: opticalChannelGroup = 219

    .. data:: homepna = 220

    .. data:: gfp = 221

    .. data:: ciscoISLvlan = 222

    .. data:: actelisMetaLOOP = 223

    .. data:: fcipLink = 224

    .. data:: rpr = 225

    .. data:: qam = 226

    .. data:: lmp = 227

    .. data:: cblVectaStar = 228

    .. data:: docsCableMCmtsDownstream = 229

    .. data:: adsl2 = 230

    .. data:: macSecControlledIF = 231

    .. data:: macSecUncontrolledIF = 232

    .. data:: aviciOpticalEther = 233

    .. data:: atmbond = 234

    .. data:: voiceFGDOS = 235

    .. data:: mocaVersion1 = 236

    .. data:: ieee80216WMAN = 237

    .. data:: adsl2plus = 238

    .. data:: dvbRcsMacLayer = 239

    .. data:: dvbTdm = 240

    .. data:: dvbRcsTdma = 241

    .. data:: x86Laps = 242

    .. data:: wwanPP = 243

    .. data:: wwanPP2 = 244

    .. data:: voiceEBS = 245

    .. data:: ifPwType = 246

    .. data:: ilan = 247

    .. data:: pip = 248

    .. data:: aluELP = 249

    .. data:: gpon = 250

    .. data:: vdsl2 = 251

    .. data:: capwapDot11Profile = 252

    .. data:: capwapDot11Bss = 253

    .. data:: capwapWtpVirtualRadio = 254

    .. data:: bits = 255

    .. data:: docsCableUpstreamRfPort = 256

    .. data:: cableDownstreamRfPort = 257

    .. data:: vmwareVirtualNic = 258

    .. data:: ieee802154 = 259

    .. data:: otnOdu = 260

    .. data:: otnOtu = 261

    .. data:: ifVfiType = 262

    .. data:: g9981 = 263

    .. data:: g9982 = 264

    .. data:: g9983 = 265

    .. data:: aluEpon = 266

    .. data:: aluEponOnu = 267

    .. data:: aluEponPhysicalUni = 268

    .. data:: aluEponLogicalLink = 269

    .. data:: aluGponOnu = 270

    .. data:: aluGponPhysicalUni = 271

    .. data:: vmwareNicTeam = 272

    .. data:: docsOfdmDownstream = 277

    .. data:: docsOfdmaUpstream = 278

    .. data:: gfast = 279

    .. data:: sdci = 280

    .. data:: xboxWireless = 281

    .. data:: fastdsl = 282

    .. data:: docsCableScte55d1FwdOob = 283

    .. data:: docsCableScte55d1RetOob = 284

    .. data:: docsCableScte55d2DsOob = 285

    .. data:: docsCableScte55d2UsOob = 286

    .. data:: docsCableNdf = 287

    .. data:: docsCableNdr = 288

    """

    other = Enum.YLeaf(1, "other")

    regular1822 = Enum.YLeaf(2, "regular1822")

    hdh1822 = Enum.YLeaf(3, "hdh1822")

    ddnX25 = Enum.YLeaf(4, "ddnX25")

    rfc877x25 = Enum.YLeaf(5, "rfc877x25")

    ethernetCsmacd = Enum.YLeaf(6, "ethernetCsmacd")

    iso88023Csmacd = Enum.YLeaf(7, "iso88023Csmacd")

    iso88024TokenBus = Enum.YLeaf(8, "iso88024TokenBus")

    iso88025TokenRing = Enum.YLeaf(9, "iso88025TokenRing")

    iso88026Man = Enum.YLeaf(10, "iso88026Man")

    starLan = Enum.YLeaf(11, "starLan")

    proteon10Mbit = Enum.YLeaf(12, "proteon10Mbit")

    proteon80Mbit = Enum.YLeaf(13, "proteon80Mbit")

    hyperchannel = Enum.YLeaf(14, "hyperchannel")

    fddi = Enum.YLeaf(15, "fddi")

    lapb = Enum.YLeaf(16, "lapb")

    sdlc = Enum.YLeaf(17, "sdlc")

    ds1 = Enum.YLeaf(18, "ds1")

    e1 = Enum.YLeaf(19, "e1")

    basicISDN = Enum.YLeaf(20, "basicISDN")

    primaryISDN = Enum.YLeaf(21, "primaryISDN")

    propPointToPointSerial = Enum.YLeaf(22, "propPointToPointSerial")

    ppp = Enum.YLeaf(23, "ppp")

    softwareLoopback = Enum.YLeaf(24, "softwareLoopback")

    eon = Enum.YLeaf(25, "eon")

    ethernet3Mbit = Enum.YLeaf(26, "ethernet3Mbit")

    nsip = Enum.YLeaf(27, "nsip")

    slip = Enum.YLeaf(28, "slip")

    ultra = Enum.YLeaf(29, "ultra")

    ds3 = Enum.YLeaf(30, "ds3")

    sip = Enum.YLeaf(31, "sip")

    frameRelay = Enum.YLeaf(32, "frameRelay")

    rs232 = Enum.YLeaf(33, "rs232")

    para = Enum.YLeaf(34, "para")

    arcnet = Enum.YLeaf(35, "arcnet")

    arcnetPlus = Enum.YLeaf(36, "arcnetPlus")

    atm = Enum.YLeaf(37, "atm")

    miox25 = Enum.YLeaf(38, "miox25")

    sonet = Enum.YLeaf(39, "sonet")

    x25ple = Enum.YLeaf(40, "x25ple")

    iso88022llc = Enum.YLeaf(41, "iso88022llc")

    localTalk = Enum.YLeaf(42, "localTalk")

    smdsDxi = Enum.YLeaf(43, "smdsDxi")

    frameRelayService = Enum.YLeaf(44, "frameRelayService")

    v35 = Enum.YLeaf(45, "v35")

    hssi = Enum.YLeaf(46, "hssi")

    hippi = Enum.YLeaf(47, "hippi")

    modem = Enum.YLeaf(48, "modem")

    aal5 = Enum.YLeaf(49, "aal5")

    sonetPath = Enum.YLeaf(50, "sonetPath")

    sonetVT = Enum.YLeaf(51, "sonetVT")

    smdsIcip = Enum.YLeaf(52, "smdsIcip")

    propVirtual = Enum.YLeaf(53, "propVirtual")

    propMultiplexor = Enum.YLeaf(54, "propMultiplexor")

    ieee80212 = Enum.YLeaf(55, "ieee80212")

    fibreChannel = Enum.YLeaf(56, "fibreChannel")

    hippiInterface = Enum.YLeaf(57, "hippiInterface")

    frameRelayInterconnect = Enum.YLeaf(58, "frameRelayInterconnect")

    aflane8023 = Enum.YLeaf(59, "aflane8023")

    aflane8025 = Enum.YLeaf(60, "aflane8025")

    cctEmul = Enum.YLeaf(61, "cctEmul")

    fastEther = Enum.YLeaf(62, "fastEther")

    isdn = Enum.YLeaf(63, "isdn")

    v11 = Enum.YLeaf(64, "v11")

    v36 = Enum.YLeaf(65, "v36")

    g703at64k = Enum.YLeaf(66, "g703at64k")

    g703at2mb = Enum.YLeaf(67, "g703at2mb")

    qllc = Enum.YLeaf(68, "qllc")

    fastEtherFX = Enum.YLeaf(69, "fastEtherFX")

    channel = Enum.YLeaf(70, "channel")

    ieee80211 = Enum.YLeaf(71, "ieee80211")

    ibm370parChan = Enum.YLeaf(72, "ibm370parChan")

    escon = Enum.YLeaf(73, "escon")

    dlsw = Enum.YLeaf(74, "dlsw")

    isdns = Enum.YLeaf(75, "isdns")

    isdnu = Enum.YLeaf(76, "isdnu")

    lapd = Enum.YLeaf(77, "lapd")

    ipSwitch = Enum.YLeaf(78, "ipSwitch")

    rsrb = Enum.YLeaf(79, "rsrb")

    atmLogical = Enum.YLeaf(80, "atmLogical")

    ds0 = Enum.YLeaf(81, "ds0")

    ds0Bundle = Enum.YLeaf(82, "ds0Bundle")

    bsc = Enum.YLeaf(83, "bsc")

    async = Enum.YLeaf(84, "async")

    cnr = Enum.YLeaf(85, "cnr")

    iso88025Dtr = Enum.YLeaf(86, "iso88025Dtr")

    eplrs = Enum.YLeaf(87, "eplrs")

    arap = Enum.YLeaf(88, "arap")

    propCnls = Enum.YLeaf(89, "propCnls")

    hostPad = Enum.YLeaf(90, "hostPad")

    termPad = Enum.YLeaf(91, "termPad")

    frameRelayMPI = Enum.YLeaf(92, "frameRelayMPI")

    x213 = Enum.YLeaf(93, "x213")

    adsl = Enum.YLeaf(94, "adsl")

    radsl = Enum.YLeaf(95, "radsl")

    sdsl = Enum.YLeaf(96, "sdsl")

    vdsl = Enum.YLeaf(97, "vdsl")

    iso88025CRFPInt = Enum.YLeaf(98, "iso88025CRFPInt")

    myrinet = Enum.YLeaf(99, "myrinet")

    voiceEM = Enum.YLeaf(100, "voiceEM")

    voiceFXO = Enum.YLeaf(101, "voiceFXO")

    voiceFXS = Enum.YLeaf(102, "voiceFXS")

    voiceEncap = Enum.YLeaf(103, "voiceEncap")

    voiceOverIp = Enum.YLeaf(104, "voiceOverIp")

    atmDxi = Enum.YLeaf(105, "atmDxi")

    atmFuni = Enum.YLeaf(106, "atmFuni")

    atmIma = Enum.YLeaf(107, "atmIma")

    pppMultilinkBundle = Enum.YLeaf(108, "pppMultilinkBundle")

    ipOverCdlc = Enum.YLeaf(109, "ipOverCdlc")

    ipOverClaw = Enum.YLeaf(110, "ipOverClaw")

    stackToStack = Enum.YLeaf(111, "stackToStack")

    virtualIpAddress = Enum.YLeaf(112, "virtualIpAddress")

    mpc = Enum.YLeaf(113, "mpc")

    ipOverAtm = Enum.YLeaf(114, "ipOverAtm")

    iso88025Fiber = Enum.YLeaf(115, "iso88025Fiber")

    tdlc = Enum.YLeaf(116, "tdlc")

    gigabitEthernet = Enum.YLeaf(117, "gigabitEthernet")

    hdlc = Enum.YLeaf(118, "hdlc")

    lapf = Enum.YLeaf(119, "lapf")

    v37 = Enum.YLeaf(120, "v37")

    x25mlp = Enum.YLeaf(121, "x25mlp")

    x25huntGroup = Enum.YLeaf(122, "x25huntGroup")

    trasnpHdlc = Enum.YLeaf(123, "trasnpHdlc")

    interleave = Enum.YLeaf(124, "interleave")

    fast = Enum.YLeaf(125, "fast")

    ip = Enum.YLeaf(126, "ip")

    docsCableMaclayer = Enum.YLeaf(127, "docsCableMaclayer")

    docsCableDownstream = Enum.YLeaf(128, "docsCableDownstream")

    docsCableUpstream = Enum.YLeaf(129, "docsCableUpstream")

    a12MppSwitch = Enum.YLeaf(130, "a12MppSwitch")

    tunnel = Enum.YLeaf(131, "tunnel")

    coffee = Enum.YLeaf(132, "coffee")

    ces = Enum.YLeaf(133, "ces")

    atmSubInterface = Enum.YLeaf(134, "atmSubInterface")

    l2vlan = Enum.YLeaf(135, "l2vlan")

    l3ipvlan = Enum.YLeaf(136, "l3ipvlan")

    l3ipxvlan = Enum.YLeaf(137, "l3ipxvlan")

    digitalPowerline = Enum.YLeaf(138, "digitalPowerline")

    mediaMailOverIp = Enum.YLeaf(139, "mediaMailOverIp")

    dtm = Enum.YLeaf(140, "dtm")

    dcn = Enum.YLeaf(141, "dcn")

    ipForward = Enum.YLeaf(142, "ipForward")

    msdsl = Enum.YLeaf(143, "msdsl")

    ieee1394 = Enum.YLeaf(144, "ieee1394")

    if_gsn = Enum.YLeaf(145, "if-gsn")

    dvbRccMacLayer = Enum.YLeaf(146, "dvbRccMacLayer")

    dvbRccDownstream = Enum.YLeaf(147, "dvbRccDownstream")

    dvbRccUpstream = Enum.YLeaf(148, "dvbRccUpstream")

    atmVirtual = Enum.YLeaf(149, "atmVirtual")

    mplsTunnel = Enum.YLeaf(150, "mplsTunnel")

    srp = Enum.YLeaf(151, "srp")

    voiceOverAtm = Enum.YLeaf(152, "voiceOverAtm")

    voiceOverFrameRelay = Enum.YLeaf(153, "voiceOverFrameRelay")

    idsl = Enum.YLeaf(154, "idsl")

    compositeLink = Enum.YLeaf(155, "compositeLink")

    ss7SigLink = Enum.YLeaf(156, "ss7SigLink")

    propWirelessP2P = Enum.YLeaf(157, "propWirelessP2P")

    frForward = Enum.YLeaf(158, "frForward")

    rfc1483 = Enum.YLeaf(159, "rfc1483")

    usb = Enum.YLeaf(160, "usb")

    ieee8023adLag = Enum.YLeaf(161, "ieee8023adLag")

    bgppolicyaccounting = Enum.YLeaf(162, "bgppolicyaccounting")

    frf16MfrBundle = Enum.YLeaf(163, "frf16MfrBundle")

    h323Gatekeeper = Enum.YLeaf(164, "h323Gatekeeper")

    h323Proxy = Enum.YLeaf(165, "h323Proxy")

    mpls = Enum.YLeaf(166, "mpls")

    mfSigLink = Enum.YLeaf(167, "mfSigLink")

    hdsl2 = Enum.YLeaf(168, "hdsl2")

    shdsl = Enum.YLeaf(169, "shdsl")

    ds1FDL = Enum.YLeaf(170, "ds1FDL")

    pos = Enum.YLeaf(171, "pos")

    dvbAsiIn = Enum.YLeaf(172, "dvbAsiIn")

    dvbAsiOut = Enum.YLeaf(173, "dvbAsiOut")

    plc = Enum.YLeaf(174, "plc")

    nfas = Enum.YLeaf(175, "nfas")

    tr008 = Enum.YLeaf(176, "tr008")

    gr303RDT = Enum.YLeaf(177, "gr303RDT")

    gr303IDT = Enum.YLeaf(178, "gr303IDT")

    isup = Enum.YLeaf(179, "isup")

    propDocsWirelessMaclayer = Enum.YLeaf(180, "propDocsWirelessMaclayer")

    propDocsWirelessDownstream = Enum.YLeaf(181, "propDocsWirelessDownstream")

    propDocsWirelessUpstream = Enum.YLeaf(182, "propDocsWirelessUpstream")

    hiperlan2 = Enum.YLeaf(183, "hiperlan2")

    propBWAp2Mp = Enum.YLeaf(184, "propBWAp2Mp")

    sonetOverheadChannel = Enum.YLeaf(185, "sonetOverheadChannel")

    digitalWrapperOverheadChannel = Enum.YLeaf(186, "digitalWrapperOverheadChannel")

    aal2 = Enum.YLeaf(187, "aal2")

    radioMAC = Enum.YLeaf(188, "radioMAC")

    atmRadio = Enum.YLeaf(189, "atmRadio")

    imt = Enum.YLeaf(190, "imt")

    mvl = Enum.YLeaf(191, "mvl")

    reachDSL = Enum.YLeaf(192, "reachDSL")

    frDlciEndPt = Enum.YLeaf(193, "frDlciEndPt")

    atmVciEndPt = Enum.YLeaf(194, "atmVciEndPt")

    opticalChannel = Enum.YLeaf(195, "opticalChannel")

    opticalTransport = Enum.YLeaf(196, "opticalTransport")

    propAtm = Enum.YLeaf(197, "propAtm")

    voiceOverCable = Enum.YLeaf(198, "voiceOverCable")

    infiniband = Enum.YLeaf(199, "infiniband")

    teLink = Enum.YLeaf(200, "teLink")

    q2931 = Enum.YLeaf(201, "q2931")

    virtualTg = Enum.YLeaf(202, "virtualTg")

    sipTg = Enum.YLeaf(203, "sipTg")

    sipSig = Enum.YLeaf(204, "sipSig")

    docsCableUpstreamChannel = Enum.YLeaf(205, "docsCableUpstreamChannel")

    econet = Enum.YLeaf(206, "econet")

    pon155 = Enum.YLeaf(207, "pon155")

    pon622 = Enum.YLeaf(208, "pon622")

    bridge = Enum.YLeaf(209, "bridge")

    linegroup = Enum.YLeaf(210, "linegroup")

    voiceEMFGD = Enum.YLeaf(211, "voiceEMFGD")

    voiceFGDEANA = Enum.YLeaf(212, "voiceFGDEANA")

    voiceDID = Enum.YLeaf(213, "voiceDID")

    mpegTransport = Enum.YLeaf(214, "mpegTransport")

    sixToFour = Enum.YLeaf(215, "sixToFour")

    gtp = Enum.YLeaf(216, "gtp")

    pdnEtherLoop1 = Enum.YLeaf(217, "pdnEtherLoop1")

    pdnEtherLoop2 = Enum.YLeaf(218, "pdnEtherLoop2")

    opticalChannelGroup = Enum.YLeaf(219, "opticalChannelGroup")

    homepna = Enum.YLeaf(220, "homepna")

    gfp = Enum.YLeaf(221, "gfp")

    ciscoISLvlan = Enum.YLeaf(222, "ciscoISLvlan")

    actelisMetaLOOP = Enum.YLeaf(223, "actelisMetaLOOP")

    fcipLink = Enum.YLeaf(224, "fcipLink")

    rpr = Enum.YLeaf(225, "rpr")

    qam = Enum.YLeaf(226, "qam")

    lmp = Enum.YLeaf(227, "lmp")

    cblVectaStar = Enum.YLeaf(228, "cblVectaStar")

    docsCableMCmtsDownstream = Enum.YLeaf(229, "docsCableMCmtsDownstream")

    adsl2 = Enum.YLeaf(230, "adsl2")

    macSecControlledIF = Enum.YLeaf(231, "macSecControlledIF")

    macSecUncontrolledIF = Enum.YLeaf(232, "macSecUncontrolledIF")

    aviciOpticalEther = Enum.YLeaf(233, "aviciOpticalEther")

    atmbond = Enum.YLeaf(234, "atmbond")

    voiceFGDOS = Enum.YLeaf(235, "voiceFGDOS")

    mocaVersion1 = Enum.YLeaf(236, "mocaVersion1")

    ieee80216WMAN = Enum.YLeaf(237, "ieee80216WMAN")

    adsl2plus = Enum.YLeaf(238, "adsl2plus")

    dvbRcsMacLayer = Enum.YLeaf(239, "dvbRcsMacLayer")

    dvbTdm = Enum.YLeaf(240, "dvbTdm")

    dvbRcsTdma = Enum.YLeaf(241, "dvbRcsTdma")

    x86Laps = Enum.YLeaf(242, "x86Laps")

    wwanPP = Enum.YLeaf(243, "wwanPP")

    wwanPP2 = Enum.YLeaf(244, "wwanPP2")

    voiceEBS = Enum.YLeaf(245, "voiceEBS")

    ifPwType = Enum.YLeaf(246, "ifPwType")

    ilan = Enum.YLeaf(247, "ilan")

    pip = Enum.YLeaf(248, "pip")

    aluELP = Enum.YLeaf(249, "aluELP")

    gpon = Enum.YLeaf(250, "gpon")

    vdsl2 = Enum.YLeaf(251, "vdsl2")

    capwapDot11Profile = Enum.YLeaf(252, "capwapDot11Profile")

    capwapDot11Bss = Enum.YLeaf(253, "capwapDot11Bss")

    capwapWtpVirtualRadio = Enum.YLeaf(254, "capwapWtpVirtualRadio")

    bits = Enum.YLeaf(255, "bits")

    docsCableUpstreamRfPort = Enum.YLeaf(256, "docsCableUpstreamRfPort")

    cableDownstreamRfPort = Enum.YLeaf(257, "cableDownstreamRfPort")

    vmwareVirtualNic = Enum.YLeaf(258, "vmwareVirtualNic")

    ieee802154 = Enum.YLeaf(259, "ieee802154")

    otnOdu = Enum.YLeaf(260, "otnOdu")

    otnOtu = Enum.YLeaf(261, "otnOtu")

    ifVfiType = Enum.YLeaf(262, "ifVfiType")

    g9981 = Enum.YLeaf(263, "g9981")

    g9982 = Enum.YLeaf(264, "g9982")

    g9983 = Enum.YLeaf(265, "g9983")

    aluEpon = Enum.YLeaf(266, "aluEpon")

    aluEponOnu = Enum.YLeaf(267, "aluEponOnu")

    aluEponPhysicalUni = Enum.YLeaf(268, "aluEponPhysicalUni")

    aluEponLogicalLink = Enum.YLeaf(269, "aluEponLogicalLink")

    aluGponOnu = Enum.YLeaf(270, "aluGponOnu")

    aluGponPhysicalUni = Enum.YLeaf(271, "aluGponPhysicalUni")

    vmwareNicTeam = Enum.YLeaf(272, "vmwareNicTeam")

    docsOfdmDownstream = Enum.YLeaf(277, "docsOfdmDownstream")

    docsOfdmaUpstream = Enum.YLeaf(278, "docsOfdmaUpstream")

    gfast = Enum.YLeaf(279, "gfast")

    sdci = Enum.YLeaf(280, "sdci")

    xboxWireless = Enum.YLeaf(281, "xboxWireless")

    fastdsl = Enum.YLeaf(282, "fastdsl")

    docsCableScte55d1FwdOob = Enum.YLeaf(283, "docsCableScte55d1FwdOob")

    docsCableScte55d1RetOob = Enum.YLeaf(284, "docsCableScte55d1RetOob")

    docsCableScte55d2DsOob = Enum.YLeaf(285, "docsCableScte55d2DsOob")

    docsCableScte55d2UsOob = Enum.YLeaf(286, "docsCableScte55d2UsOob")

    docsCableNdf = Enum.YLeaf(287, "docsCableNdf")

    docsCableNdr = Enum.YLeaf(288, "docsCableNdr")


class Ianatunneltype(Enum):
    """
    Ianatunneltype

    The encapsulation method used by a tunnel. The value

    direct indicates that a packet is encapsulated

    directly within a normal IP header, with no

    intermediate header, and unicast to the remote tunnel

    endpoint (e.g., an RFC 2003 IP\-in\-IP tunnel, or an RFC

    1933 IPv6\-in\-IPv4 tunnel). The value minimal indicates

    that a Minimal Forwarding Header (RFC 2004) is

    inserted between the outer header and the payload

    packet. The value UDP indicates that the payload

    packet is encapsulated within a normal UDP packet

    (e.g., RFC 1234).

    The values sixToFour, sixOverFour, and isatap

    indicates that an IPv6 packet is encapsulated directly

    within an IPv4 header, with no intermediate header,

    and unicast to the destination determined by the 6to4,

    6over4, or ISATAP protocol.

    The remaining protocol\-specific values indicate that a

    header of the protocol of that name is inserted

    between the outer header and the payload header.

    The assignment policy for IANAtunnelType values is

    identical to the policy for assigning IANAifType

    values.

    .. data:: other = 1

    .. data:: direct = 2

    .. data:: gre = 3

    .. data:: minimal = 4

    .. data:: l2tp = 5

    .. data:: pptp = 6

    .. data:: l2f = 7

    .. data:: udp = 8

    .. data:: atmp = 9

    .. data:: msdp = 10

    .. data:: sixToFour = 11

    .. data:: sixOverFour = 12

    .. data:: isatap = 13

    .. data:: teredo = 14

    """

    other = Enum.YLeaf(1, "other")

    direct = Enum.YLeaf(2, "direct")

    gre = Enum.YLeaf(3, "gre")

    minimal = Enum.YLeaf(4, "minimal")

    l2tp = Enum.YLeaf(5, "l2tp")

    pptp = Enum.YLeaf(6, "pptp")

    l2f = Enum.YLeaf(7, "l2f")

    udp = Enum.YLeaf(8, "udp")

    atmp = Enum.YLeaf(9, "atmp")

    msdp = Enum.YLeaf(10, "msdp")

    sixToFour = Enum.YLeaf(11, "sixToFour")

    sixOverFour = Enum.YLeaf(12, "sixOverFour")

    isatap = Enum.YLeaf(13, "isatap")

    teredo = Enum.YLeaf(14, "teredo")



