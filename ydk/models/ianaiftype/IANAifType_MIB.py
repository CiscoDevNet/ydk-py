""" IANAifType_MIB 

This MIB module defines the IANAifType Textual
Convention, and thus the enumerated values of
the ifType object defined in MIB\-II's ifTable.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class IANAifType_Enum(Enum):
    """
    IANAifType_Enum

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

    """

    OTHER = 1

    REGULAR1822 = 2

    HDH1822 = 3

    DDNX25 = 4

    RFC877X25 = 5

    ETHERNETCSMACD = 6

    ISO88023CSMACD = 7

    ISO88024TOKENBUS = 8

    ISO88025TOKENRING = 9

    ISO88026MAN = 10

    STARLAN = 11

    PROTEON10MBIT = 12

    PROTEON80MBIT = 13

    HYPERCHANNEL = 14

    FDDI = 15

    LAPB = 16

    SDLC = 17

    DS1 = 18

    E1 = 19

    BASICISDN = 20

    PRIMARYISDN = 21

    PROPPOINTTOPOINTSERIAL = 22

    PPP = 23

    SOFTWARELOOPBACK = 24

    EON = 25

    ETHERNET3MBIT = 26

    NSIP = 27

    SLIP = 28

    ULTRA = 29

    DS3 = 30

    SIP = 31

    FRAMERELAY = 32

    RS232 = 33

    PARA = 34

    ARCNET = 35

    ARCNETPLUS = 36

    ATM = 37

    MIOX25 = 38

    SONET = 39

    X25PLE = 40

    ISO88022LLC = 41

    LOCALTALK = 42

    SMDSDXI = 43

    FRAMERELAYSERVICE = 44

    V35 = 45

    HSSI = 46

    HIPPI = 47

    MODEM = 48

    AAL5 = 49

    SONETPATH = 50

    SONETVT = 51

    SMDSICIP = 52

    PROPVIRTUAL = 53

    PROPMULTIPLEXOR = 54

    IEEE80212 = 55

    FIBRECHANNEL = 56

    HIPPIINTERFACE = 57

    FRAMERELAYINTERCONNECT = 58

    AFLANE8023 = 59

    AFLANE8025 = 60

    CCTEMUL = 61

    FASTETHER = 62

    ISDN = 63

    V11 = 64

    V36 = 65

    G703AT64K = 66

    G703AT2MB = 67

    QLLC = 68

    FASTETHERFX = 69

    CHANNEL = 70

    IEEE80211 = 71

    IBM370PARCHAN = 72

    ESCON = 73

    DLSW = 74

    ISDNS = 75

    ISDNU = 76

    LAPD = 77

    IPSWITCH = 78

    RSRB = 79

    ATMLOGICAL = 80

    DS0 = 81

    DS0BUNDLE = 82

    BSC = 83

    ASYNC = 84

    CNR = 85

    ISO88025DTR = 86

    EPLRS = 87

    ARAP = 88

    PROPCNLS = 89

    HOSTPAD = 90

    TERMPAD = 91

    FRAMERELAYMPI = 92

    X213 = 93

    ADSL = 94

    RADSL = 95

    SDSL = 96

    VDSL = 97

    ISO88025CRFPINT = 98

    MYRINET = 99

    VOICEEM = 100

    VOICEFXO = 101

    VOICEFXS = 102

    VOICEENCAP = 103

    VOICEOVERIP = 104

    ATMDXI = 105

    ATMFUNI = 106

    ATMIMA = 107

    PPPMULTILINKBUNDLE = 108

    IPOVERCDLC = 109

    IPOVERCLAW = 110

    STACKTOSTACK = 111

    VIRTUALIPADDRESS = 112

    MPC = 113

    IPOVERATM = 114

    ISO88025FIBER = 115

    TDLC = 116

    GIGABITETHERNET = 117

    HDLC = 118

    LAPF = 119

    V37 = 120

    X25MLP = 121

    X25HUNTGROUP = 122

    TRASNPHDLC = 123

    INTERLEAVE = 124

    FAST = 125

    IP = 126

    DOCSCABLEMACLAYER = 127

    DOCSCABLEDOWNSTREAM = 128

    DOCSCABLEUPSTREAM = 129

    A12MPPSWITCH = 130

    TUNNEL = 131

    COFFEE = 132

    CES = 133

    ATMSUBINTERFACE = 134

    L2VLAN = 135

    L3IPVLAN = 136

    L3IPXVLAN = 137

    DIGITALPOWERLINE = 138

    MEDIAMAILOVERIP = 139

    DTM = 140

    DCN = 141

    IPFORWARD = 142

    MSDSL = 143

    IEEE1394 = 144

    IF_GSN = 145

    DVBRCCMACLAYER = 146

    DVBRCCDOWNSTREAM = 147

    DVBRCCUPSTREAM = 148

    ATMVIRTUAL = 149

    MPLSTUNNEL = 150

    SRP = 151

    VOICEOVERATM = 152

    VOICEOVERFRAMERELAY = 153

    IDSL = 154

    COMPOSITELINK = 155

    SS7SIGLINK = 156

    PROPWIRELESSP2P = 157

    FRFORWARD = 158

    RFC1483 = 159

    USB = 160

    IEEE8023ADLAG = 161

    BGPPOLICYACCOUNTING = 162

    FRF16MFRBUNDLE = 163

    H323GATEKEEPER = 164

    H323PROXY = 165

    MPLS = 166

    MFSIGLINK = 167

    HDSL2 = 168

    SHDSL = 169

    DS1FDL = 170

    POS = 171

    DVBASIIN = 172

    DVBASIOUT = 173

    PLC = 174

    NFAS = 175

    TR008 = 176

    GR303RDT = 177

    GR303IDT = 178

    ISUP = 179

    PROPDOCSWIRELESSMACLAYER = 180

    PROPDOCSWIRELESSDOWNSTREAM = 181

    PROPDOCSWIRELESSUPSTREAM = 182

    HIPERLAN2 = 183

    PROPBWAP2MP = 184

    SONETOVERHEADCHANNEL = 185

    DIGITALWRAPPEROVERHEADCHANNEL = 186

    AAL2 = 187

    RADIOMAC = 188

    ATMRADIO = 189

    IMT = 190

    MVL = 191

    REACHDSL = 192

    FRDLCIENDPT = 193

    ATMVCIENDPT = 194

    OPTICALCHANNEL = 195

    OPTICALTRANSPORT = 196

    PROPATM = 197

    VOICEOVERCABLE = 198

    INFINIBAND = 199

    TELINK = 200

    Q2931 = 201

    VIRTUALTG = 202

    SIPTG = 203

    SIPSIG = 204

    DOCSCABLEUPSTREAMCHANNEL = 205

    ECONET = 206

    PON155 = 207

    PON622 = 208

    BRIDGE = 209

    LINEGROUP = 210

    VOICEEMFGD = 211

    VOICEFGDEANA = 212

    VOICEDID = 213

    MPEGTRANSPORT = 214

    SIXTOFOUR = 215

    GTP = 216

    PDNETHERLOOP1 = 217

    PDNETHERLOOP2 = 218

    OPTICALCHANNELGROUP = 219

    HOMEPNA = 220

    GFP = 221

    CISCOISLVLAN = 222

    ACTELISMETALOOP = 223

    FCIPLINK = 224

    RPR = 225

    QAM = 226

    LMP = 227

    CBLVECTASTAR = 228

    DOCSCABLEMCMTSDOWNSTREAM = 229

    ADSL2 = 230

    MACSECCONTROLLEDIF = 231

    MACSECUNCONTROLLEDIF = 232

    AVICIOPTICALETHER = 233

    ATMBOND = 234


    @staticmethod
    def _meta_info():
        from ydk.models.ianaiftype._meta import _IANAifType_MIB as meta
        return meta._meta_table['IANAifType_Enum']


class IANAtunnelType_Enum(Enum):
    """
    IANAtunnelType_Enum

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

    """

    OTHER = 1

    DIRECT = 2

    GRE = 3

    MINIMAL = 4

    L2TP = 5

    PPTP = 6

    L2F = 7

    UDP = 8

    ATMP = 9

    MSDP = 10

    SIXTOFOUR = 11

    SIXOVERFOUR = 12

    ISATAP = 13

    TEREDO = 14


    @staticmethod
    def _meta_info():
        from ydk.models.ianaiftype._meta import _IANAifType_MIB as meta
        return meta._meta_table['IANAtunnelType_Enum']



