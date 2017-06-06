""" IANAifType_MIB 

This MIB module defines the IANAifType Textual
Convention, and thus the enumerated values of
the ifType object defined in MIB\-II's ifTable.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IanaiftypeEnum(Enum):
    """
    IanaiftypeEnum

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

    other = 1

    regular1822 = 2

    hdh1822 = 3

    ddnX25 = 4

    rfc877x25 = 5

    ethernetCsmacd = 6

    iso88023Csmacd = 7

    iso88024TokenBus = 8

    iso88025TokenRing = 9

    iso88026Man = 10

    starLan = 11

    proteon10Mbit = 12

    proteon80Mbit = 13

    hyperchannel = 14

    fddi = 15

    lapb = 16

    sdlc = 17

    ds1 = 18

    e1 = 19

    basicISDN = 20

    primaryISDN = 21

    propPointToPointSerial = 22

    ppp = 23

    softwareLoopback = 24

    eon = 25

    ethernet3Mbit = 26

    nsip = 27

    slip = 28

    ultra = 29

    ds3 = 30

    sip = 31

    frameRelay = 32

    rs232 = 33

    para = 34

    arcnet = 35

    arcnetPlus = 36

    atm = 37

    miox25 = 38

    sonet = 39

    x25ple = 40

    iso88022llc = 41

    localTalk = 42

    smdsDxi = 43

    frameRelayService = 44

    v35 = 45

    hssi = 46

    hippi = 47

    modem = 48

    aal5 = 49

    sonetPath = 50

    sonetVT = 51

    smdsIcip = 52

    propVirtual = 53

    propMultiplexor = 54

    ieee80212 = 55

    fibreChannel = 56

    hippiInterface = 57

    frameRelayInterconnect = 58

    aflane8023 = 59

    aflane8025 = 60

    cctEmul = 61

    fastEther = 62

    isdn = 63

    v11 = 64

    v36 = 65

    g703at64k = 66

    g703at2mb = 67

    qllc = 68

    fastEtherFX = 69

    channel = 70

    ieee80211 = 71

    ibm370parChan = 72

    escon = 73

    dlsw = 74

    isdns = 75

    isdnu = 76

    lapd = 77

    ipSwitch = 78

    rsrb = 79

    atmLogical = 80

    ds0 = 81

    ds0Bundle = 82

    bsc = 83

    async = 84

    cnr = 85

    iso88025Dtr = 86

    eplrs = 87

    arap = 88

    propCnls = 89

    hostPad = 90

    termPad = 91

    frameRelayMPI = 92

    x213 = 93

    adsl = 94

    radsl = 95

    sdsl = 96

    vdsl = 97

    iso88025CRFPInt = 98

    myrinet = 99

    voiceEM = 100

    voiceFXO = 101

    voiceFXS = 102

    voiceEncap = 103

    voiceOverIp = 104

    atmDxi = 105

    atmFuni = 106

    atmIma = 107

    pppMultilinkBundle = 108

    ipOverCdlc = 109

    ipOverClaw = 110

    stackToStack = 111

    virtualIpAddress = 112

    mpc = 113

    ipOverAtm = 114

    iso88025Fiber = 115

    tdlc = 116

    gigabitEthernet = 117

    hdlc = 118

    lapf = 119

    v37 = 120

    x25mlp = 121

    x25huntGroup = 122

    trasnpHdlc = 123

    interleave = 124

    fast = 125

    ip = 126

    docsCableMaclayer = 127

    docsCableDownstream = 128

    docsCableUpstream = 129

    a12MppSwitch = 130

    tunnel = 131

    coffee = 132

    ces = 133

    atmSubInterface = 134

    l2vlan = 135

    l3ipvlan = 136

    l3ipxvlan = 137

    digitalPowerline = 138

    mediaMailOverIp = 139

    dtm = 140

    dcn = 141

    ipForward = 142

    msdsl = 143

    ieee1394 = 144

    if_gsn = 145

    dvbRccMacLayer = 146

    dvbRccDownstream = 147

    dvbRccUpstream = 148

    atmVirtual = 149

    mplsTunnel = 150

    srp = 151

    voiceOverAtm = 152

    voiceOverFrameRelay = 153

    idsl = 154

    compositeLink = 155

    ss7SigLink = 156

    propWirelessP2P = 157

    frForward = 158

    rfc1483 = 159

    usb = 160

    ieee8023adLag = 161

    bgppolicyaccounting = 162

    frf16MfrBundle = 163

    h323Gatekeeper = 164

    h323Proxy = 165

    mpls = 166

    mfSigLink = 167

    hdsl2 = 168

    shdsl = 169

    ds1FDL = 170

    pos = 171

    dvbAsiIn = 172

    dvbAsiOut = 173

    plc = 174

    nfas = 175

    tr008 = 176

    gr303RDT = 177

    gr303IDT = 178

    isup = 179

    propDocsWirelessMaclayer = 180

    propDocsWirelessDownstream = 181

    propDocsWirelessUpstream = 182

    hiperlan2 = 183

    propBWAp2Mp = 184

    sonetOverheadChannel = 185

    digitalWrapperOverheadChannel = 186

    aal2 = 187

    radioMAC = 188

    atmRadio = 189

    imt = 190

    mvl = 191

    reachDSL = 192

    frDlciEndPt = 193

    atmVciEndPt = 194

    opticalChannel = 195

    opticalTransport = 196

    propAtm = 197

    voiceOverCable = 198

    infiniband = 199

    teLink = 200

    q2931 = 201

    virtualTg = 202

    sipTg = 203

    sipSig = 204

    docsCableUpstreamChannel = 205

    econet = 206

    pon155 = 207

    pon622 = 208

    bridge = 209

    linegroup = 210

    voiceEMFGD = 211

    voiceFGDEANA = 212

    voiceDID = 213

    mpegTransport = 214

    sixToFour = 215

    gtp = 216

    pdnEtherLoop1 = 217

    pdnEtherLoop2 = 218

    opticalChannelGroup = 219

    homepna = 220

    gfp = 221

    ciscoISLvlan = 222

    actelisMetaLOOP = 223

    fcipLink = 224

    rpr = 225

    qam = 226

    lmp = 227

    cblVectaStar = 228

    docsCableMCmtsDownstream = 229

    adsl2 = 230

    macSecControlledIF = 231

    macSecUncontrolledIF = 232

    aviciOpticalEther = 233

    atmbond = 234

    voiceFGDOS = 235

    mocaVersion1 = 236

    ieee80216WMAN = 237

    adsl2plus = 238

    dvbRcsMacLayer = 239

    dvbTdm = 240

    dvbRcsTdma = 241

    x86Laps = 242

    wwanPP = 243

    wwanPP2 = 244

    voiceEBS = 245

    ifPwType = 246

    ilan = 247

    pip = 248

    aluELP = 249

    gpon = 250

    vdsl2 = 251

    capwapDot11Profile = 252

    capwapDot11Bss = 253

    capwapWtpVirtualRadio = 254

    bits = 255

    docsCableUpstreamRfPort = 256

    cableDownstreamRfPort = 257

    vmwareVirtualNic = 258

    ieee802154 = 259

    otnOdu = 260

    otnOtu = 261

    ifVfiType = 262

    g9981 = 263

    g9982 = 264

    g9983 = 265

    aluEpon = 266

    aluEponOnu = 267

    aluEponPhysicalUni = 268

    aluEponLogicalLink = 269

    aluGponOnu = 270

    aluGponPhysicalUni = 271

    vmwareNicTeam = 272

    docsOfdmDownstream = 277

    docsOfdmaUpstream = 278

    gfast = 279

    sdci = 280

    xboxWireless = 281

    fastdsl = 282

    docsCableScte55d1FwdOob = 283

    docsCableScte55d1RetOob = 284

    docsCableScte55d2DsOob = 285

    docsCableScte55d2UsOob = 286

    docsCableNdf = 287

    docsCableNdr = 288


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IANAifType_MIB as meta
        return meta._meta_table['IanaiftypeEnum']


class IanatunneltypeEnum(Enum):
    """
    IanatunneltypeEnum

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

    other = 1

    direct = 2

    gre = 3

    minimal = 4

    l2tp = 5

    pptp = 6

    l2f = 7

    udp = 8

    atmp = 9

    msdp = 10

    sixToFour = 11

    sixOverFour = 12

    isatap = 13

    teredo = 14


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IANAifType_MIB as meta
        return meta._meta_table['IanatunneltypeEnum']



