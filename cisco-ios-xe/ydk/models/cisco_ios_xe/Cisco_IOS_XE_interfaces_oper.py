""" Cisco_IOS_XE_interfaces_oper 

This module contains a collection of YANG definitions for
monitoring the interfaces in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EtherDuplex(Enum):
    """
    EtherDuplex (Enum Class)

    The duplex setting of the interface

    .. data:: full_duplex = 0

    .. data:: half_duplex = 1

    .. data:: auto_duplex = 2

    .. data:: unknown_duplex = 3

    """

    full_duplex = Enum.YLeaf(0, "full-duplex")

    half_duplex = Enum.YLeaf(1, "half-duplex")

    auto_duplex = Enum.YLeaf(2, "auto-duplex")

    unknown_duplex = Enum.YLeaf(3, "unknown-duplex")


class EtherSpeed(Enum):
    """
    EtherSpeed (Enum Class)

    The speed setting of the interface

    .. data:: speed_10mb = 0

    .. data:: speed_100mb = 1

    .. data:: speed_1gb = 2

    .. data:: speed_10bg = 3

    .. data:: speed_25gb = 4

    .. data:: speed_40gb = 5

    .. data:: speed_50gb = 6

    .. data:: speed_100bg = 7

    .. data:: speed_unknown = 8

    """

    speed_10mb = Enum.YLeaf(0, "speed-10mb")

    speed_100mb = Enum.YLeaf(1, "speed-100mb")

    speed_1gb = Enum.YLeaf(2, "speed-1gb")

    speed_10bg = Enum.YLeaf(3, "speed-10bg")

    speed_25gb = Enum.YLeaf(4, "speed-25gb")

    speed_40gb = Enum.YLeaf(5, "speed-40gb")

    speed_50gb = Enum.YLeaf(6, "speed-50gb")

    speed_100bg = Enum.YLeaf(7, "speed-100bg")

    speed_unknown = Enum.YLeaf(8, "speed-unknown")


class IetfIntfType(Enum):
    """
    IetfIntfType (Enum Class)

    IANAifType

    This data type is used as the syntax of the ifType

    object in the (updated) definition of MIB\-II's ifTable

    .. data:: iana_iftype_other = 1

    .. data:: iana_iftype_regular1822 = 2

    .. data:: iana_iftype_hdh1822 = 3

    .. data:: iana_iftype_ddnx25 = 4

    .. data:: iana_iftype_rfc877x25 = 5

    .. data:: iana_iftype_ethernet_csmacd = 6

    .. data:: iana_iftype_iso88023_csmacd = 7

    .. data:: iana_iftype_iso88024_tokenbus = 8

    .. data:: iana_iftype_iso88025_tokenring = 9

    .. data:: iana_iftype_iso88026_man = 10

    .. data:: iana_iftype_starlan = 11

    .. data:: iana_iftype_proteon10mbit = 12

    .. data:: iana_iftype_proteon80mbit = 13

    .. data:: iana_iftype_hyperchannel = 14

    .. data:: iana_iftype_fddi = 15

    .. data:: iana_iftype_lapb = 16

    .. data:: iana_iftype_sdlc = 17

    .. data:: iana_iftype_ds1 = 18

    .. data:: iana_iftype_e1 = 19

    .. data:: iana_iftype_basicisdn = 20

    .. data:: iana_iftype_primaryisdn = 21

    .. data:: iana_iftype_prop_p2p_serial = 22

    .. data:: iana_iftype_ppp = 23

    .. data:: iana_iftype_sw_loopback = 24

    .. data:: iana_iftype_eon = 25

    .. data:: iana_iftype_ethernet3mbit = 26

    .. data:: iana_iftype_nsip = 27

    .. data:: iana_iftype_slip = 28

    .. data:: iana_iftype_ultra = 29

    .. data:: iana_iftype_ds3 = 30

    .. data:: iana_iftype_sip = 31

    .. data:: iana_iftype_framerelay = 32

    .. data:: iana_iftype_rs232 = 33

    .. data:: iana_iftype_para = 34

    .. data:: iana_iftype_arcnet = 35

    .. data:: iana_iftype_arcnetplus = 36

    .. data:: iana_iftype_atm = 37

    .. data:: iana_iftype_miox25 = 38

    .. data:: iana_iftype_sonet = 39

    .. data:: iana_iftype_x25ple = 40

    .. data:: iana_iftype_iso88022_llc = 41

    .. data:: iana_iftype_localtalk = 42

    .. data:: iana_iftype_smdsdxi = 43

    .. data:: iana_iftype_framerelay_service = 44

    .. data:: iana_iftype_v35 = 45

    .. data:: iana_iftype_hssi = 46

    .. data:: iana_iftype_hippi = 47

    .. data:: iana_iftype_modem = 48

    .. data:: iana_iftype_aal5 = 49

    .. data:: iana_iftype_sonetpath = 50

    .. data:: iana_iftype_sonetvt = 51

    .. data:: iana_iftype_smdsicip = 52

    .. data:: iana_iftype_propvirtual = 53

    .. data:: iana_iftype_propmultiplexor = 54

    .. data:: iana_iftype_ieee80212 = 55

    .. data:: iana_iftype_fiberchannel = 56

    .. data:: iana_iftype_hippi_interface = 57

    .. data:: iana_iftype_framerelay_interconnect = 58

    .. data:: iana_iftype_aflane8023 = 59

    .. data:: iana_iftype_aflane8025 = 60

    .. data:: iana_iftype_cctemul = 61

    .. data:: iana_iftype_fastether = 62

    .. data:: iana_iftype_isdn = 63

    .. data:: iana_iftype_v11 = 64

    .. data:: iana_iftype_v36 = 65

    .. data:: iana_iftype_g703at64k = 66

    .. data:: iana_iftype_g703at2mb = 67

    .. data:: iana_iftype_qllc = 68

    .. data:: iana_iftype_fastetherfx = 69

    .. data:: iana_iftype_channel = 70

    .. data:: iana_iftype_ieee80211 = 71

    .. data:: iana_iftype_ibm370parchan = 72

    .. data:: iana_iftype_escon = 73

    .. data:: iana_iftype_dlsw = 74

    .. data:: iana_iftype_isdns = 75

    .. data:: iana_iftype_isdnu = 76

    .. data:: iana_iftype_lapd = 77

    .. data:: iana_iftype_ipswitch = 78

    .. data:: iana_iftype_rsrb = 79

    .. data:: iana_iftype_atmlogical = 80

    .. data:: iana_iftype_ds0 = 81

    .. data:: iana_iftype_ds0bundle = 82

    .. data:: iana_iftype_bsc = 83

    .. data:: iana_iftype_async = 84

    .. data:: iana_iftype_cnr = 85

    .. data:: iana_iftype_iso88025_dtr = 86

    .. data:: iana_iftype_eplrs = 87

    .. data:: iana_iftype_arap = 88

    .. data:: iana_iftype_propcnls = 89

    .. data:: iana_iftype_hostpad = 90

    .. data:: iana_iftype_termpad = 91

    .. data:: iana_iftype_framerelay_mpi = 92

    .. data:: iana_iftype_x213 = 93

    .. data:: iana_iftype_adsl = 94

    .. data:: iana_iftype_radsl = 95

    .. data:: iana_iftype_sdsl = 96

    .. data:: iana_iftype_vdsl = 97

    .. data:: iana_iftype_iso88025_crfpint = 98

    .. data:: iana_iftype_myrinet = 99

    .. data:: iana_iftype_voiceem = 100

    .. data:: iana_iftype_voicefxo = 101

    .. data:: iana_iftype_voicefxs = 102

    .. data:: iana_iftype_voiceencap = 103

    .. data:: iana_iftype_voip = 104

    .. data:: iana_iftype_atmdxi = 105

    .. data:: iana_iftype_atmfuni = 106

    .. data:: iana_iftype_atmima = 107

    .. data:: iana_iftype_ppp_multilinkbundle = 108

    .. data:: iana_iftype_ipovercdlc = 109

    .. data:: iana_iftype_ipoverclaw = 110

    .. data:: iana_iftype_stack2stack = 111

    .. data:: iana_iftype_virtualipaddress = 112

    .. data:: iana_iftype_mpc = 113

    .. data:: iana_iftype_ipoveratm = 114

    .. data:: iana_iftype_iso88025_fiber = 115

    .. data:: iana_iftype_tdlc = 116

    .. data:: iana_iftype_gige = 117

    .. data:: iana_iftype_hdlc = 118

    .. data:: iana_iftype_lapf = 119

    .. data:: iana_iftype_v37 = 120

    .. data:: iana_iftype_x25mlp = 121

    .. data:: iana_iftype_x25huntgroup = 122

    .. data:: iana_iftype_transphdlc = 123

    .. data:: iana_iftype_interleave = 124

    .. data:: iana_iftype_fast = 125

    .. data:: iana_iftype_ip = 126

    .. data:: iana_iftype_docs_cable_maclayer = 127

    .. data:: iana_iftype_docs_cable_downstream = 128

    .. data:: iana_iftype_docs_cable_upstream = 129

    .. data:: iana_iftype_a12mppswitch = 130

    .. data:: iana_iftype_tunnel = 131

    .. data:: iana_iftype_coffee = 132

    .. data:: iana_iftype_ces = 133

    .. data:: iana_iftype_atmsubinterface = 134

    .. data:: iana_iftype_l2vlan = 135

    .. data:: iana_iftype_l3ipvlan = 136

    .. data:: iana_iftype_l3ipxvlan = 137

    .. data:: iana_iftype_digital_powerline = 138

    .. data:: iana_iftype_media_mailoverip = 139

    .. data:: iana_iftype_dtm = 140

    .. data:: iana_iftype_dcn = 141

    .. data:: iana_iftype_ipforward = 142

    .. data:: iana_iftype_msdsl = 143

    .. data:: iana_iftype_ieee1394 = 144

    .. data:: iana_iftype_gsn = 145

    .. data:: iana_iftype_dvbrcc_maclayer = 146

    .. data:: iana_iftype_dvbrcc_downstream = 147

    .. data:: iana_iftype_dvbrcc_upstream = 148

    .. data:: iana_iftype_atmvirtual = 149

    .. data:: iana_iftype_mplstunnel = 150

    .. data:: iana_iftype_srp = 151

    .. data:: iana_iftype_voiceoveratm = 152

    .. data:: iana_iftype_voiceoverframerelay = 153

    .. data:: iana_iftype_idsl = 154

    .. data:: iana_iftype_compositelink = 155

    .. data:: iana_iftype_ss7siglink = 156

    .. data:: iana_iftype_propwireless_p2p = 157

    .. data:: iana_iftype_frforward = 158

    .. data:: iana_iftype_rfc1483 = 159

    .. data:: iana_iftype_usb = 160

    .. data:: iana_iftype_ieee8023_adlag = 161

    .. data:: iana_iftype_bgppolicy_accounting = 162

    .. data:: iana_iftype_frf16mfrbundle = 163

    .. data:: iana_iftype_h323gatekeeper = 164

    .. data:: iana_iftype_h323proxy = 165

    .. data:: iana_iftype_mpls = 166

    .. data:: iana_iftype_mfsiglink = 167

    .. data:: iana_iftype_hdsl2 = 168

    .. data:: iana_iftype_shdsl = 169

    .. data:: iana_iftype_ds1fdl = 170

    .. data:: iana_iftype_pos = 171

    .. data:: iana_iftype_dvbasiin = 172

    .. data:: iana_iftype_dvbasiout = 173

    .. data:: iana_iftype_plc = 174

    .. data:: iana_iftype_nfas = 175

    .. data:: iana_iftype_tr008 = 176

    .. data:: iana_iftype_gr303rdt = 177

    .. data:: iana_iftype_gr303idt = 178

    .. data:: iana_iftype_isup = 179

    .. data:: iana_iftype_prop_docs_wireless_maclayer = 180

    .. data:: iana_iftype_prop_docs_wireless_downstream = 181

    .. data:: iana_iftype_prop_docs_wireless_upstream = 182

    .. data:: iana_iftype_hiperlan2 = 183

    .. data:: iana_iftype_prop_bwap2mp = 184

    .. data:: iana_iftype_sonetoverheadchannel = 185

    .. data:: iana_iftype_digital_wrapperoverheadchannel = 186

    .. data:: iana_iftype_aal2 = 187

    .. data:: iana_iftype_radiomac = 188

    .. data:: iana_iftype_atmradio = 189

    .. data:: iana_iftype_imt = 190

    .. data:: iana_iftype_mvl = 191

    .. data:: iana_iftype_reachhdsl = 192

    .. data:: iana_iftype_frdlciendpt = 193

    .. data:: iana_iftype_atmvciendpt = 194

    .. data:: iana_iftype_opticalchannel = 195

    .. data:: iana_iftype_opticaltransport = 196

    .. data:: iana_iftype_propatm = 197

    .. data:: iana_iftype_voiceovercable = 198

    .. data:: iana_iftype_infiniband = 199

    .. data:: iana_iftype_telink = 200

    .. data:: iana_iftype_q2931 = 201

    .. data:: iana_iftype_virtualatg = 202

    .. data:: iana_iftype_siptg = 203

    .. data:: iana_iftype_sipsig = 204

    .. data:: iana_iftype_docs_cable_upstreamchannel = 205

    .. data:: iana_iftype_econet = 206

    .. data:: iana_iftype_pon155 = 207

    .. data:: iana_iftype_pon622 = 208

    .. data:: iana_iftype_bridge_if = 209

    .. data:: iana_iftype_linegroup = 210

    .. data:: iana_iftype_voiceemfgd = 211

    .. data:: iana_iftype_voiceefgdeana = 212

    .. data:: iana_iftype_voicedid = 213

    .. data:: iana_iftype_mpegtransport = 214

    .. data:: iana_iftype_sixtofour = 215

    .. data:: iana_iftype_gtp = 216

    .. data:: iana_iftype_pdnetherloop1 = 217

    .. data:: iana_iftype_pdnetherloop2 = 218

    .. data:: iana_iftype_opticalchannel_group = 219

    .. data:: iana_iftype_homepna = 220

    .. data:: iana_iftype_gfp = 221

    .. data:: iana_iftype_ciscoislvlan = 222

    .. data:: iana_iftype_actelismetaloop = 223

    .. data:: iana_iftype_fciplink = 224

    .. data:: iana_iftype_rpr = 225

    .. data:: iana_iftype_qam = 226

    .. data:: iana_iftype_lmp = 227

    .. data:: iana_iftype_cblvectastar = 228

    .. data:: iana_iftype_docs_cable_mcmts_downtream = 229

    .. data:: iana_iftype_adsl2 = 230

    .. data:: iana_iftype_macseccontrolledif = 231

    .. data:: iana_iftype_macsecuncontrolledif = 232

    .. data:: iana_iftype_aviciopticalether = 233

    .. data:: iana_iftype_atmbond = 234

    .. data:: iana_iftype_voicefgdos = 235

    .. data:: iana_iftype_mocaversion1 = 236

    .. data:: iana_iftype_ieee80216_wman = 237

    .. data:: iana_iftype_adsl2plus = 238

    .. data:: iana_iftype_dvbrcsmaclayer = 239

    .. data:: iana_iftype_dvbtdm = 240

    .. data:: iana_iftype_dvbrcstdma = 241

    .. data:: iana_iftype_x86laps = 242

    .. data:: iana_iftype_wwanpp = 243

    .. data:: iana_iftype_wwanpp2 = 244

    .. data:: iana_iftype_voiceebs = 245

    .. data:: iana_iftype_ifpwtype = 246

    .. data:: iana_iftype_ilan = 247

    .. data:: iana_iftype_pip = 248

    .. data:: iana_iftype_aluelp = 249

    .. data:: iana_iftype_gpon = 250

    .. data:: iana_iftype_vdsl2 = 251

    .. data:: iana_iftype_capwapdot11_profile = 252

    .. data:: iana_iftype_capwapdot11_bss = 253

    .. data:: iana_iftype_capwapwtp_virtualradio = 254

    .. data:: iana_iftype_bits = 255

    .. data:: iana_iftype_docs_cable_upstreamrfport = 256

    .. data:: iana_iftype_cable_downstreamrfport = 257

    .. data:: iana_iftype_vmware_virtualnic = 258

    .. data:: iana_iftype_ieee802154 = 259

    .. data:: iana_iftype_otnodu = 260

    .. data:: iana_iftype_otnotu = 261

    .. data:: iana_iftype_ifvfitype = 262

    .. data:: iana_iftype_g9981 = 263

    .. data:: iana_iftype_g9982 = 264

    .. data:: iana_iftype_g9983 = 265

    .. data:: iana_iftype_aluepon = 266

    .. data:: iana_iftype_aluepon_onu = 267

    .. data:: iana_iftype_aluepon_physicaluni = 268

    .. data:: iana_iftype_aluepon_logicalink = 269

    .. data:: iana_iftype_alugpon_onu = 270

    .. data:: iana_iftype_alugpon_physicaluni = 271

    .. data:: iana_iftype_vmwarenicteam = 272

    .. data:: iana_iftype_docs_ofdm_downstream = 277

    .. data:: iana_iftype_docs_ofdma_upstream = 278

    .. data:: iana_iftype_gfast = 279

    .. data:: iana_iftype_sdci = 280

    .. data:: iana_iftype_xbox_wireless = 281

    .. data:: iana_iftype_fastdsl = 282

    """

    iana_iftype_other = Enum.YLeaf(1, "iana-iftype-other")

    iana_iftype_regular1822 = Enum.YLeaf(2, "iana-iftype-regular1822")

    iana_iftype_hdh1822 = Enum.YLeaf(3, "iana-iftype-hdh1822")

    iana_iftype_ddnx25 = Enum.YLeaf(4, "iana-iftype-ddnx25")

    iana_iftype_rfc877x25 = Enum.YLeaf(5, "iana-iftype-rfc877x25")

    iana_iftype_ethernet_csmacd = Enum.YLeaf(6, "iana-iftype-ethernet-csmacd")

    iana_iftype_iso88023_csmacd = Enum.YLeaf(7, "iana-iftype-iso88023-csmacd")

    iana_iftype_iso88024_tokenbus = Enum.YLeaf(8, "iana-iftype-iso88024-tokenbus")

    iana_iftype_iso88025_tokenring = Enum.YLeaf(9, "iana-iftype-iso88025-tokenring")

    iana_iftype_iso88026_man = Enum.YLeaf(10, "iana-iftype-iso88026-man")

    iana_iftype_starlan = Enum.YLeaf(11, "iana-iftype-starlan")

    iana_iftype_proteon10mbit = Enum.YLeaf(12, "iana-iftype-proteon10mbit")

    iana_iftype_proteon80mbit = Enum.YLeaf(13, "iana-iftype-proteon80mbit")

    iana_iftype_hyperchannel = Enum.YLeaf(14, "iana-iftype-hyperchannel")

    iana_iftype_fddi = Enum.YLeaf(15, "iana-iftype-fddi")

    iana_iftype_lapb = Enum.YLeaf(16, "iana-iftype-lapb")

    iana_iftype_sdlc = Enum.YLeaf(17, "iana-iftype-sdlc")

    iana_iftype_ds1 = Enum.YLeaf(18, "iana-iftype-ds1")

    iana_iftype_e1 = Enum.YLeaf(19, "iana-iftype-e1")

    iana_iftype_basicisdn = Enum.YLeaf(20, "iana-iftype-basicisdn")

    iana_iftype_primaryisdn = Enum.YLeaf(21, "iana-iftype-primaryisdn")

    iana_iftype_prop_p2p_serial = Enum.YLeaf(22, "iana-iftype-prop-p2p-serial")

    iana_iftype_ppp = Enum.YLeaf(23, "iana-iftype-ppp")

    iana_iftype_sw_loopback = Enum.YLeaf(24, "iana-iftype-sw-loopback")

    iana_iftype_eon = Enum.YLeaf(25, "iana-iftype-eon")

    iana_iftype_ethernet3mbit = Enum.YLeaf(26, "iana-iftype-ethernet3mbit")

    iana_iftype_nsip = Enum.YLeaf(27, "iana-iftype-nsip")

    iana_iftype_slip = Enum.YLeaf(28, "iana-iftype-slip")

    iana_iftype_ultra = Enum.YLeaf(29, "iana-iftype-ultra")

    iana_iftype_ds3 = Enum.YLeaf(30, "iana-iftype-ds3")

    iana_iftype_sip = Enum.YLeaf(31, "iana-iftype-sip")

    iana_iftype_framerelay = Enum.YLeaf(32, "iana-iftype-framerelay")

    iana_iftype_rs232 = Enum.YLeaf(33, "iana-iftype-rs232")

    iana_iftype_para = Enum.YLeaf(34, "iana-iftype-para")

    iana_iftype_arcnet = Enum.YLeaf(35, "iana-iftype-arcnet")

    iana_iftype_arcnetplus = Enum.YLeaf(36, "iana-iftype-arcnetplus")

    iana_iftype_atm = Enum.YLeaf(37, "iana-iftype-atm")

    iana_iftype_miox25 = Enum.YLeaf(38, "iana-iftype-miox25")

    iana_iftype_sonet = Enum.YLeaf(39, "iana-iftype-sonet")

    iana_iftype_x25ple = Enum.YLeaf(40, "iana-iftype-x25ple")

    iana_iftype_iso88022_llc = Enum.YLeaf(41, "iana-iftype-iso88022-llc")

    iana_iftype_localtalk = Enum.YLeaf(42, "iana-iftype-localtalk")

    iana_iftype_smdsdxi = Enum.YLeaf(43, "iana-iftype-smdsdxi")

    iana_iftype_framerelay_service = Enum.YLeaf(44, "iana-iftype-framerelay-service")

    iana_iftype_v35 = Enum.YLeaf(45, "iana-iftype-v35")

    iana_iftype_hssi = Enum.YLeaf(46, "iana-iftype-hssi")

    iana_iftype_hippi = Enum.YLeaf(47, "iana-iftype-hippi")

    iana_iftype_modem = Enum.YLeaf(48, "iana-iftype-modem")

    iana_iftype_aal5 = Enum.YLeaf(49, "iana-iftype-aal5")

    iana_iftype_sonetpath = Enum.YLeaf(50, "iana-iftype-sonetpath")

    iana_iftype_sonetvt = Enum.YLeaf(51, "iana-iftype-sonetvt")

    iana_iftype_smdsicip = Enum.YLeaf(52, "iana-iftype-smdsicip")

    iana_iftype_propvirtual = Enum.YLeaf(53, "iana-iftype-propvirtual")

    iana_iftype_propmultiplexor = Enum.YLeaf(54, "iana-iftype-propmultiplexor")

    iana_iftype_ieee80212 = Enum.YLeaf(55, "iana-iftype-ieee80212")

    iana_iftype_fiberchannel = Enum.YLeaf(56, "iana-iftype-fiberchannel")

    iana_iftype_hippi_interface = Enum.YLeaf(57, "iana-iftype-hippi-interface")

    iana_iftype_framerelay_interconnect = Enum.YLeaf(58, "iana-iftype-framerelay-interconnect")

    iana_iftype_aflane8023 = Enum.YLeaf(59, "iana-iftype-aflane8023")

    iana_iftype_aflane8025 = Enum.YLeaf(60, "iana-iftype-aflane8025")

    iana_iftype_cctemul = Enum.YLeaf(61, "iana-iftype-cctemul")

    iana_iftype_fastether = Enum.YLeaf(62, "iana-iftype-fastether")

    iana_iftype_isdn = Enum.YLeaf(63, "iana-iftype-isdn")

    iana_iftype_v11 = Enum.YLeaf(64, "iana-iftype-v11")

    iana_iftype_v36 = Enum.YLeaf(65, "iana-iftype-v36")

    iana_iftype_g703at64k = Enum.YLeaf(66, "iana-iftype-g703at64k")

    iana_iftype_g703at2mb = Enum.YLeaf(67, "iana-iftype-g703at2mb")

    iana_iftype_qllc = Enum.YLeaf(68, "iana-iftype-qllc")

    iana_iftype_fastetherfx = Enum.YLeaf(69, "iana-iftype-fastetherfx")

    iana_iftype_channel = Enum.YLeaf(70, "iana-iftype-channel")

    iana_iftype_ieee80211 = Enum.YLeaf(71, "iana-iftype-ieee80211")

    iana_iftype_ibm370parchan = Enum.YLeaf(72, "iana-iftype-ibm370parchan")

    iana_iftype_escon = Enum.YLeaf(73, "iana-iftype-escon")

    iana_iftype_dlsw = Enum.YLeaf(74, "iana-iftype-dlsw")

    iana_iftype_isdns = Enum.YLeaf(75, "iana-iftype-isdns")

    iana_iftype_isdnu = Enum.YLeaf(76, "iana-iftype-isdnu")

    iana_iftype_lapd = Enum.YLeaf(77, "iana-iftype-lapd")

    iana_iftype_ipswitch = Enum.YLeaf(78, "iana-iftype-ipswitch")

    iana_iftype_rsrb = Enum.YLeaf(79, "iana-iftype-rsrb")

    iana_iftype_atmlogical = Enum.YLeaf(80, "iana-iftype-atmlogical")

    iana_iftype_ds0 = Enum.YLeaf(81, "iana-iftype-ds0")

    iana_iftype_ds0bundle = Enum.YLeaf(82, "iana-iftype-ds0bundle")

    iana_iftype_bsc = Enum.YLeaf(83, "iana-iftype-bsc")

    iana_iftype_async = Enum.YLeaf(84, "iana-iftype-async")

    iana_iftype_cnr = Enum.YLeaf(85, "iana-iftype-cnr")

    iana_iftype_iso88025_dtr = Enum.YLeaf(86, "iana-iftype-iso88025-dtr")

    iana_iftype_eplrs = Enum.YLeaf(87, "iana-iftype-eplrs")

    iana_iftype_arap = Enum.YLeaf(88, "iana-iftype-arap")

    iana_iftype_propcnls = Enum.YLeaf(89, "iana-iftype-propcnls")

    iana_iftype_hostpad = Enum.YLeaf(90, "iana-iftype-hostpad")

    iana_iftype_termpad = Enum.YLeaf(91, "iana-iftype-termpad")

    iana_iftype_framerelay_mpi = Enum.YLeaf(92, "iana-iftype-framerelay-mpi")

    iana_iftype_x213 = Enum.YLeaf(93, "iana-iftype-x213")

    iana_iftype_adsl = Enum.YLeaf(94, "iana-iftype-adsl")

    iana_iftype_radsl = Enum.YLeaf(95, "iana-iftype-radsl")

    iana_iftype_sdsl = Enum.YLeaf(96, "iana-iftype-sdsl")

    iana_iftype_vdsl = Enum.YLeaf(97, "iana-iftype-vdsl")

    iana_iftype_iso88025_crfpint = Enum.YLeaf(98, "iana-iftype-iso88025-crfpint")

    iana_iftype_myrinet = Enum.YLeaf(99, "iana-iftype-myrinet")

    iana_iftype_voiceem = Enum.YLeaf(100, "iana-iftype-voiceem")

    iana_iftype_voicefxo = Enum.YLeaf(101, "iana-iftype-voicefxo")

    iana_iftype_voicefxs = Enum.YLeaf(102, "iana-iftype-voicefxs")

    iana_iftype_voiceencap = Enum.YLeaf(103, "iana-iftype-voiceencap")

    iana_iftype_voip = Enum.YLeaf(104, "iana-iftype-voip")

    iana_iftype_atmdxi = Enum.YLeaf(105, "iana-iftype-atmdxi")

    iana_iftype_atmfuni = Enum.YLeaf(106, "iana-iftype-atmfuni")

    iana_iftype_atmima = Enum.YLeaf(107, "iana-iftype-atmima")

    iana_iftype_ppp_multilinkbundle = Enum.YLeaf(108, "iana-iftype-ppp-multilinkbundle")

    iana_iftype_ipovercdlc = Enum.YLeaf(109, "iana-iftype-ipovercdlc")

    iana_iftype_ipoverclaw = Enum.YLeaf(110, "iana-iftype-ipoverclaw")

    iana_iftype_stack2stack = Enum.YLeaf(111, "iana-iftype-stack2stack")

    iana_iftype_virtualipaddress = Enum.YLeaf(112, "iana-iftype-virtualipaddress")

    iana_iftype_mpc = Enum.YLeaf(113, "iana-iftype-mpc")

    iana_iftype_ipoveratm = Enum.YLeaf(114, "iana-iftype-ipoveratm")

    iana_iftype_iso88025_fiber = Enum.YLeaf(115, "iana-iftype-iso88025-fiber")

    iana_iftype_tdlc = Enum.YLeaf(116, "iana-iftype-tdlc")

    iana_iftype_gige = Enum.YLeaf(117, "iana-iftype-gige")

    iana_iftype_hdlc = Enum.YLeaf(118, "iana-iftype-hdlc")

    iana_iftype_lapf = Enum.YLeaf(119, "iana-iftype-lapf")

    iana_iftype_v37 = Enum.YLeaf(120, "iana-iftype-v37")

    iana_iftype_x25mlp = Enum.YLeaf(121, "iana-iftype-x25mlp")

    iana_iftype_x25huntgroup = Enum.YLeaf(122, "iana-iftype-x25huntgroup")

    iana_iftype_transphdlc = Enum.YLeaf(123, "iana-iftype-transphdlc")

    iana_iftype_interleave = Enum.YLeaf(124, "iana-iftype-interleave")

    iana_iftype_fast = Enum.YLeaf(125, "iana-iftype-fast")

    iana_iftype_ip = Enum.YLeaf(126, "iana-iftype-ip")

    iana_iftype_docs_cable_maclayer = Enum.YLeaf(127, "iana-iftype-docs-cable-maclayer")

    iana_iftype_docs_cable_downstream = Enum.YLeaf(128, "iana-iftype-docs-cable-downstream")

    iana_iftype_docs_cable_upstream = Enum.YLeaf(129, "iana-iftype-docs-cable-upstream")

    iana_iftype_a12mppswitch = Enum.YLeaf(130, "iana-iftype-a12mppswitch")

    iana_iftype_tunnel = Enum.YLeaf(131, "iana-iftype-tunnel")

    iana_iftype_coffee = Enum.YLeaf(132, "iana-iftype-coffee")

    iana_iftype_ces = Enum.YLeaf(133, "iana-iftype-ces")

    iana_iftype_atmsubinterface = Enum.YLeaf(134, "iana-iftype-atmsubinterface")

    iana_iftype_l2vlan = Enum.YLeaf(135, "iana-iftype-l2vlan")

    iana_iftype_l3ipvlan = Enum.YLeaf(136, "iana-iftype-l3ipvlan")

    iana_iftype_l3ipxvlan = Enum.YLeaf(137, "iana-iftype-l3ipxvlan")

    iana_iftype_digital_powerline = Enum.YLeaf(138, "iana-iftype-digital-powerline")

    iana_iftype_media_mailoverip = Enum.YLeaf(139, "iana-iftype-media-mailoverip")

    iana_iftype_dtm = Enum.YLeaf(140, "iana-iftype-dtm")

    iana_iftype_dcn = Enum.YLeaf(141, "iana-iftype-dcn")

    iana_iftype_ipforward = Enum.YLeaf(142, "iana-iftype-ipforward")

    iana_iftype_msdsl = Enum.YLeaf(143, "iana-iftype-msdsl")

    iana_iftype_ieee1394 = Enum.YLeaf(144, "iana-iftype-ieee1394")

    iana_iftype_gsn = Enum.YLeaf(145, "iana-iftype-gsn")

    iana_iftype_dvbrcc_maclayer = Enum.YLeaf(146, "iana-iftype-dvbrcc-maclayer")

    iana_iftype_dvbrcc_downstream = Enum.YLeaf(147, "iana-iftype-dvbrcc-downstream")

    iana_iftype_dvbrcc_upstream = Enum.YLeaf(148, "iana-iftype-dvbrcc-upstream")

    iana_iftype_atmvirtual = Enum.YLeaf(149, "iana-iftype-atmvirtual")

    iana_iftype_mplstunnel = Enum.YLeaf(150, "iana-iftype-mplstunnel")

    iana_iftype_srp = Enum.YLeaf(151, "iana-iftype-srp")

    iana_iftype_voiceoveratm = Enum.YLeaf(152, "iana-iftype-voiceoveratm")

    iana_iftype_voiceoverframerelay = Enum.YLeaf(153, "iana-iftype-voiceoverframerelay")

    iana_iftype_idsl = Enum.YLeaf(154, "iana-iftype-idsl")

    iana_iftype_compositelink = Enum.YLeaf(155, "iana-iftype-compositelink")

    iana_iftype_ss7siglink = Enum.YLeaf(156, "iana-iftype-ss7siglink")

    iana_iftype_propwireless_p2p = Enum.YLeaf(157, "iana-iftype-propwireless-p2p")

    iana_iftype_frforward = Enum.YLeaf(158, "iana-iftype-frforward")

    iana_iftype_rfc1483 = Enum.YLeaf(159, "iana-iftype-rfc1483")

    iana_iftype_usb = Enum.YLeaf(160, "iana-iftype-usb")

    iana_iftype_ieee8023_adlag = Enum.YLeaf(161, "iana-iftype-ieee8023-adlag")

    iana_iftype_bgppolicy_accounting = Enum.YLeaf(162, "iana-iftype-bgppolicy-accounting")

    iana_iftype_frf16mfrbundle = Enum.YLeaf(163, "iana-iftype-frf16mfrbundle")

    iana_iftype_h323gatekeeper = Enum.YLeaf(164, "iana-iftype-h323gatekeeper")

    iana_iftype_h323proxy = Enum.YLeaf(165, "iana-iftype-h323proxy")

    iana_iftype_mpls = Enum.YLeaf(166, "iana-iftype-mpls")

    iana_iftype_mfsiglink = Enum.YLeaf(167, "iana-iftype-mfsiglink")

    iana_iftype_hdsl2 = Enum.YLeaf(168, "iana-iftype-hdsl2")

    iana_iftype_shdsl = Enum.YLeaf(169, "iana-iftype-shdsl")

    iana_iftype_ds1fdl = Enum.YLeaf(170, "iana-iftype-ds1fdl")

    iana_iftype_pos = Enum.YLeaf(171, "iana-iftype-pos")

    iana_iftype_dvbasiin = Enum.YLeaf(172, "iana-iftype-dvbasiin")

    iana_iftype_dvbasiout = Enum.YLeaf(173, "iana-iftype-dvbasiout")

    iana_iftype_plc = Enum.YLeaf(174, "iana-iftype-plc")

    iana_iftype_nfas = Enum.YLeaf(175, "iana-iftype-nfas")

    iana_iftype_tr008 = Enum.YLeaf(176, "iana-iftype-tr008")

    iana_iftype_gr303rdt = Enum.YLeaf(177, "iana-iftype-gr303rdt")

    iana_iftype_gr303idt = Enum.YLeaf(178, "iana-iftype-gr303idt")

    iana_iftype_isup = Enum.YLeaf(179, "iana-iftype-isup")

    iana_iftype_prop_docs_wireless_maclayer = Enum.YLeaf(180, "iana-iftype-prop-docs-wireless-maclayer")

    iana_iftype_prop_docs_wireless_downstream = Enum.YLeaf(181, "iana-iftype-prop-docs-wireless-downstream")

    iana_iftype_prop_docs_wireless_upstream = Enum.YLeaf(182, "iana-iftype-prop-docs-wireless-upstream")

    iana_iftype_hiperlan2 = Enum.YLeaf(183, "iana-iftype-hiperlan2")

    iana_iftype_prop_bwap2mp = Enum.YLeaf(184, "iana-iftype-prop-bwap2mp")

    iana_iftype_sonetoverheadchannel = Enum.YLeaf(185, "iana-iftype-sonetoverheadchannel")

    iana_iftype_digital_wrapperoverheadchannel = Enum.YLeaf(186, "iana-iftype-digital-wrapperoverheadchannel")

    iana_iftype_aal2 = Enum.YLeaf(187, "iana-iftype-aal2")

    iana_iftype_radiomac = Enum.YLeaf(188, "iana-iftype-radiomac")

    iana_iftype_atmradio = Enum.YLeaf(189, "iana-iftype-atmradio")

    iana_iftype_imt = Enum.YLeaf(190, "iana-iftype-imt")

    iana_iftype_mvl = Enum.YLeaf(191, "iana-iftype-mvl")

    iana_iftype_reachhdsl = Enum.YLeaf(192, "iana-iftype-reachhdsl")

    iana_iftype_frdlciendpt = Enum.YLeaf(193, "iana-iftype-frdlciendpt")

    iana_iftype_atmvciendpt = Enum.YLeaf(194, "iana-iftype-atmvciendpt")

    iana_iftype_opticalchannel = Enum.YLeaf(195, "iana-iftype-opticalchannel")

    iana_iftype_opticaltransport = Enum.YLeaf(196, "iana-iftype-opticaltransport")

    iana_iftype_propatm = Enum.YLeaf(197, "iana-iftype-propatm")

    iana_iftype_voiceovercable = Enum.YLeaf(198, "iana-iftype-voiceovercable")

    iana_iftype_infiniband = Enum.YLeaf(199, "iana-iftype-infiniband")

    iana_iftype_telink = Enum.YLeaf(200, "iana-iftype-telink")

    iana_iftype_q2931 = Enum.YLeaf(201, "iana-iftype-q2931")

    iana_iftype_virtualatg = Enum.YLeaf(202, "iana-iftype-virtualatg")

    iana_iftype_siptg = Enum.YLeaf(203, "iana-iftype-siptg")

    iana_iftype_sipsig = Enum.YLeaf(204, "iana-iftype-sipsig")

    iana_iftype_docs_cable_upstreamchannel = Enum.YLeaf(205, "iana-iftype-docs-cable-upstreamchannel")

    iana_iftype_econet = Enum.YLeaf(206, "iana-iftype-econet")

    iana_iftype_pon155 = Enum.YLeaf(207, "iana-iftype-pon155")

    iana_iftype_pon622 = Enum.YLeaf(208, "iana-iftype-pon622")

    iana_iftype_bridge_if = Enum.YLeaf(209, "iana-iftype-bridge-if")

    iana_iftype_linegroup = Enum.YLeaf(210, "iana-iftype-linegroup")

    iana_iftype_voiceemfgd = Enum.YLeaf(211, "iana-iftype-voiceemfgd")

    iana_iftype_voiceefgdeana = Enum.YLeaf(212, "iana-iftype-voiceefgdeana")

    iana_iftype_voicedid = Enum.YLeaf(213, "iana-iftype-voicedid")

    iana_iftype_mpegtransport = Enum.YLeaf(214, "iana-iftype-mpegtransport")

    iana_iftype_sixtofour = Enum.YLeaf(215, "iana-iftype-sixtofour")

    iana_iftype_gtp = Enum.YLeaf(216, "iana-iftype-gtp")

    iana_iftype_pdnetherloop1 = Enum.YLeaf(217, "iana-iftype-pdnetherloop1")

    iana_iftype_pdnetherloop2 = Enum.YLeaf(218, "iana-iftype-pdnetherloop2")

    iana_iftype_opticalchannel_group = Enum.YLeaf(219, "iana-iftype-opticalchannel-group")

    iana_iftype_homepna = Enum.YLeaf(220, "iana-iftype-homepna")

    iana_iftype_gfp = Enum.YLeaf(221, "iana-iftype-gfp")

    iana_iftype_ciscoislvlan = Enum.YLeaf(222, "iana-iftype-ciscoislvlan")

    iana_iftype_actelismetaloop = Enum.YLeaf(223, "iana-iftype-actelismetaloop")

    iana_iftype_fciplink = Enum.YLeaf(224, "iana-iftype-fciplink")

    iana_iftype_rpr = Enum.YLeaf(225, "iana-iftype-rpr")

    iana_iftype_qam = Enum.YLeaf(226, "iana-iftype-qam")

    iana_iftype_lmp = Enum.YLeaf(227, "iana-iftype-lmp")

    iana_iftype_cblvectastar = Enum.YLeaf(228, "iana-iftype-cblvectastar")

    iana_iftype_docs_cable_mcmts_downtream = Enum.YLeaf(229, "iana-iftype-docs-cable-mcmts-downtream")

    iana_iftype_adsl2 = Enum.YLeaf(230, "iana-iftype-adsl2")

    iana_iftype_macseccontrolledif = Enum.YLeaf(231, "iana-iftype-macseccontrolledif")

    iana_iftype_macsecuncontrolledif = Enum.YLeaf(232, "iana-iftype-macsecuncontrolledif")

    iana_iftype_aviciopticalether = Enum.YLeaf(233, "iana-iftype-aviciopticalether")

    iana_iftype_atmbond = Enum.YLeaf(234, "iana-iftype-atmbond")

    iana_iftype_voicefgdos = Enum.YLeaf(235, "iana-iftype-voicefgdos")

    iana_iftype_mocaversion1 = Enum.YLeaf(236, "iana-iftype-mocaversion1")

    iana_iftype_ieee80216_wman = Enum.YLeaf(237, "iana-iftype-ieee80216-wman")

    iana_iftype_adsl2plus = Enum.YLeaf(238, "iana-iftype-adsl2plus")

    iana_iftype_dvbrcsmaclayer = Enum.YLeaf(239, "iana-iftype-dvbrcsmaclayer")

    iana_iftype_dvbtdm = Enum.YLeaf(240, "iana-iftype-dvbtdm")

    iana_iftype_dvbrcstdma = Enum.YLeaf(241, "iana-iftype-dvbrcstdma")

    iana_iftype_x86laps = Enum.YLeaf(242, "iana-iftype-x86laps")

    iana_iftype_wwanpp = Enum.YLeaf(243, "iana-iftype-wwanpp")

    iana_iftype_wwanpp2 = Enum.YLeaf(244, "iana-iftype-wwanpp2")

    iana_iftype_voiceebs = Enum.YLeaf(245, "iana-iftype-voiceebs")

    iana_iftype_ifpwtype = Enum.YLeaf(246, "iana-iftype-ifpwtype")

    iana_iftype_ilan = Enum.YLeaf(247, "iana-iftype-ilan")

    iana_iftype_pip = Enum.YLeaf(248, "iana-iftype-pip")

    iana_iftype_aluelp = Enum.YLeaf(249, "iana-iftype-aluelp")

    iana_iftype_gpon = Enum.YLeaf(250, "iana-iftype-gpon")

    iana_iftype_vdsl2 = Enum.YLeaf(251, "iana-iftype-vdsl2")

    iana_iftype_capwapdot11_profile = Enum.YLeaf(252, "iana-iftype-capwapdot11-profile")

    iana_iftype_capwapdot11_bss = Enum.YLeaf(253, "iana-iftype-capwapdot11-bss")

    iana_iftype_capwapwtp_virtualradio = Enum.YLeaf(254, "iana-iftype-capwapwtp-virtualradio")

    iana_iftype_bits = Enum.YLeaf(255, "iana-iftype-bits")

    iana_iftype_docs_cable_upstreamrfport = Enum.YLeaf(256, "iana-iftype-docs-cable-upstreamrfport")

    iana_iftype_cable_downstreamrfport = Enum.YLeaf(257, "iana-iftype-cable-downstreamrfport")

    iana_iftype_vmware_virtualnic = Enum.YLeaf(258, "iana-iftype-vmware-virtualnic")

    iana_iftype_ieee802154 = Enum.YLeaf(259, "iana-iftype-ieee802154")

    iana_iftype_otnodu = Enum.YLeaf(260, "iana-iftype-otnodu")

    iana_iftype_otnotu = Enum.YLeaf(261, "iana-iftype-otnotu")

    iana_iftype_ifvfitype = Enum.YLeaf(262, "iana-iftype-ifvfitype")

    iana_iftype_g9981 = Enum.YLeaf(263, "iana-iftype-g9981")

    iana_iftype_g9982 = Enum.YLeaf(264, "iana-iftype-g9982")

    iana_iftype_g9983 = Enum.YLeaf(265, "iana-iftype-g9983")

    iana_iftype_aluepon = Enum.YLeaf(266, "iana-iftype-aluepon")

    iana_iftype_aluepon_onu = Enum.YLeaf(267, "iana-iftype-aluepon-onu")

    iana_iftype_aluepon_physicaluni = Enum.YLeaf(268, "iana-iftype-aluepon-physicaluni")

    iana_iftype_aluepon_logicalink = Enum.YLeaf(269, "iana-iftype-aluepon-logicalink")

    iana_iftype_alugpon_onu = Enum.YLeaf(270, "iana-iftype-alugpon-onu")

    iana_iftype_alugpon_physicaluni = Enum.YLeaf(271, "iana-iftype-alugpon-physicaluni")

    iana_iftype_vmwarenicteam = Enum.YLeaf(272, "iana-iftype-vmwarenicteam")

    iana_iftype_docs_ofdm_downstream = Enum.YLeaf(277, "iana-iftype-docs-ofdm-downstream")

    iana_iftype_docs_ofdma_upstream = Enum.YLeaf(278, "iana-iftype-docs-ofdma-upstream")

    iana_iftype_gfast = Enum.YLeaf(279, "iana-iftype-gfast")

    iana_iftype_sdci = Enum.YLeaf(280, "iana-iftype-sdci")

    iana_iftype_xbox_wireless = Enum.YLeaf(281, "iana-iftype-xbox-wireless")

    iana_iftype_fastdsl = Enum.YLeaf(282, "iana-iftype-fastdsl")


class IntfState(Enum):
    """
    IntfState (Enum Class)

    The desired state of the interface.

    This leaf has the same read semantics as ifAdminStatus.

    Reference\:

    RFC 2863\: The Interfaces Group MIB \- ifAdminStatus

    .. data:: if_state_unknown = 0

    .. data:: if_state_up = 1

    .. data:: if_state_down = 2

    .. data:: if_state_test = 3

    """

    if_state_unknown = Enum.YLeaf(0, "if-state-unknown")

    if_state_up = Enum.YLeaf(1, "if-state-up")

    if_state_down = Enum.YLeaf(2, "if-state-down")

    if_state_test = Enum.YLeaf(3, "if-state-test")


class OperState(Enum):
    """
    OperState (Enum Class)

    The current operational state of the interface.

    This leaf has the same semantics as ifOperStatus.

    Reference\:

    RFC 2863\: The Interfaces Group MIB \- ifOperStatus

    .. data:: if_oper_state_invalid = 0

    .. data:: if_oper_state_ready = 1

    .. data:: if_oper_state_no_pass = 2

    .. data:: if_oper_state_test = 3

    .. data:: if_oper_state_unknown = 4

    .. data:: if_oper_state_dormant = 5

    .. data:: if_oper_state_not_present = 6

    .. data:: if_oper_state_lower_layer_down = 7

    """

    if_oper_state_invalid = Enum.YLeaf(0, "if-oper-state-invalid")

    if_oper_state_ready = Enum.YLeaf(1, "if-oper-state-ready")

    if_oper_state_no_pass = Enum.YLeaf(2, "if-oper-state-no-pass")

    if_oper_state_test = Enum.YLeaf(3, "if-oper-state-test")

    if_oper_state_unknown = Enum.YLeaf(4, "if-oper-state-unknown")

    if_oper_state_dormant = Enum.YLeaf(5, "if-oper-state-dormant")

    if_oper_state_not_present = Enum.YLeaf(6, "if-oper-state-not-present")

    if_oper_state_lower_layer_down = Enum.YLeaf(7, "if-oper-state-lower-layer-down")


class QosDirection(Enum):
    """
    QosDirection (Enum Class)

    QoS direction indication

    .. data:: qos_inbound = 0

    	Direction of traffic coming into the network entry

    .. data:: qos_outbound = 1

    	Direction of traffic going out of the network entry

    """

    qos_inbound = Enum.YLeaf(0, "qos-inbound")

    qos_outbound = Enum.YLeaf(1, "qos-outbound")


class QosMatchType(Enum):
    """
    QosMatchType (Enum Class)

    QOS match type

    .. data:: qos_match_dscp = 0

    .. data:: qos_match_src_ip = 1

    .. data:: qos_match_dst_ip = 2

    .. data:: qos_match_src_port = 3

    .. data:: qos_match_dst_port = 4

    .. data:: qos_match_proto = 5

    """

    qos_match_dscp = Enum.YLeaf(0, "qos-match-dscp")

    qos_match_src_ip = Enum.YLeaf(1, "qos-match-src-ip")

    qos_match_dst_ip = Enum.YLeaf(2, "qos-match-dst-ip")

    qos_match_src_port = Enum.YLeaf(3, "qos-match-src-port")

    qos_match_dst_port = Enum.YLeaf(4, "qos-match-dst-port")

    qos_match_proto = Enum.YLeaf(5, "qos-match-proto")


class SerialCrc(Enum):
    """
    SerialCrc (Enum Class)

    The Cyclic Redundancy Code type

    .. data:: serial_crc32 = 0

    	32-bit Cyclic Redundancy Code

    .. data:: serial_crc16 = 1

    	16 bit Cyclic Redundancy Code

    """

    serial_crc32 = Enum.YLeaf(0, "serial-crc32")

    serial_crc16 = Enum.YLeaf(1, "serial-crc16")


class SubrateSpeed(Enum):
    """
    SubrateSpeed (Enum Class)

    The subrate on a serial interface

    .. data:: dsx1_subrate_56kbps = 0

    	56 kilobits per second subrate

    .. data:: dsx1_subrate_64kbps = 1

    	64 kilobits per second subrate

    """

    dsx1_subrate_56kbps = Enum.YLeaf(0, "dsx1-subrate-56kbps")

    dsx1_subrate_64kbps = Enum.YLeaf(1, "dsx1-subrate-64kbps")


class T1E1LoopbackMode(Enum):
    """
    T1E1LoopbackMode (Enum Class)

    Loopback mode type

    .. data:: t1e1_no_loopback = 0

    	No loopback mode

    .. data:: t1e1_cli_local_loopback = 1

    	Command line interface enforced local loopback

    .. data:: t1e1_line_cli_local_loopback = 2

    	Command line interface enforced line local loopback

    .. data:: t1e1_payload_cli_local_loopback = 3

    	Command line interface enforced payload local loopback

    .. data:: t1e1_local_line_loopback = 4

    	Local line loopback

    .. data:: t1e1_local_payload_loopback = 5

    	Local payload loopback

    .. data:: t1e1_local_ansi_fdl_remote_loopback = 6

    	Line ANSI FDL remote loopback

    .. data:: t1e1_line_att_fdl_remote_loopback = 7

    	Line ATT FDL remote loopback

    .. data:: t1e1_payload_ansi_fdl_remote_loopback = 8

    	Payload ANSI FDL remote loopback

    .. data:: t1e1_payload_att_fdl_remote_loopback = 9

    	Payload ATT FDL remote loopback

    .. data:: t1e1_line_iboc_remote_loopback = 10

    	Line IBOC remote loopback

    .. data:: t1e1_line_ansi_fdl_local_loopback = 11

    	Line ANSI FDL local loopback

    .. data:: t1e1_line_att_fdl_local_loopback = 12

    	Line ATT FDL local loopback

    .. data:: t1e1_payload_ansi_fdl_local_loopback = 13

    	Payload ANSI FDL local loopback

    .. data:: t1e1_payload_att_fdl_local_loopback = 14

    	Payload ATT FDL local loopback

    .. data:: t1e1_line_iboc_local_loopback = 15

    	Line IBOC local loopback

    """

    t1e1_no_loopback = Enum.YLeaf(0, "t1e1-no-loopback")

    t1e1_cli_local_loopback = Enum.YLeaf(1, "t1e1-cli-local-loopback")

    t1e1_line_cli_local_loopback = Enum.YLeaf(2, "t1e1-line-cli-local-loopback")

    t1e1_payload_cli_local_loopback = Enum.YLeaf(3, "t1e1-payload-cli-local-loopback")

    t1e1_local_line_loopback = Enum.YLeaf(4, "t1e1-local-line-loopback")

    t1e1_local_payload_loopback = Enum.YLeaf(5, "t1e1-local-payload-loopback")

    t1e1_local_ansi_fdl_remote_loopback = Enum.YLeaf(6, "t1e1-local-ansi-fdl-remote-loopback")

    t1e1_line_att_fdl_remote_loopback = Enum.YLeaf(7, "t1e1-line-att-fdl-remote-loopback")

    t1e1_payload_ansi_fdl_remote_loopback = Enum.YLeaf(8, "t1e1-payload-ansi-fdl-remote-loopback")

    t1e1_payload_att_fdl_remote_loopback = Enum.YLeaf(9, "t1e1-payload-att-fdl-remote-loopback")

    t1e1_line_iboc_remote_loopback = Enum.YLeaf(10, "t1e1-line-iboc-remote-loopback")

    t1e1_line_ansi_fdl_local_loopback = Enum.YLeaf(11, "t1e1-line-ansi-fdl-local-loopback")

    t1e1_line_att_fdl_local_loopback = Enum.YLeaf(12, "t1e1-line-att-fdl-local-loopback")

    t1e1_payload_ansi_fdl_local_loopback = Enum.YLeaf(13, "t1e1-payload-ansi-fdl-local-loopback")

    t1e1_payload_att_fdl_local_loopback = Enum.YLeaf(14, "t1e1-payload-att-fdl-local-loopback")

    t1e1_line_iboc_local_loopback = Enum.YLeaf(15, "t1e1-line-iboc-local-loopback")


class ThreshUnit(Enum):
    """
    ThreshUnit (Enum Class)

    Units of threshold

    .. data:: thresh_units_default = 0

    .. data:: thresh_units_bytes = 1

    .. data:: thresh_units_sec = 2

    .. data:: thresh_units_packets = 3

    .. data:: thresh_units_cells = 4

    .. data:: thresh_units_percent = 5

    """

    thresh_units_default = Enum.YLeaf(0, "thresh-units-default")

    thresh_units_bytes = Enum.YLeaf(1, "thresh-units-bytes")

    thresh_units_sec = Enum.YLeaf(2, "thresh-units-sec")

    thresh_units_packets = Enum.YLeaf(3, "thresh-units-packets")

    thresh_units_cells = Enum.YLeaf(4, "thresh-units-cells")

    thresh_units_percent = Enum.YLeaf(5, "thresh-units-percent")



class Interfaces(Entity):
    """
    Operational state of interfaces
    
    .. attribute:: interface
    
    	List of interfaces
    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface>`
    
    

    """

    _prefix = 'interfaces-ios-xe-oper'
    _revision = '2017-10-10'

    def __init__(self):
        super(Interfaces, self).__init__()
        self._top_entity = None

        self.yang_name = "interfaces"
        self.yang_parent_name = "Cisco-IOS-XE-interfaces-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("interface", ("interface", Interfaces.Interface))])
        self._leafs = OrderedDict()

        self.interface = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-interfaces-oper:interfaces"

    def __setattr__(self, name, value):
        self._perform_setattr(Interfaces, [], name, value)


    class Interface(Entity):
        """
        List of interfaces
        
        .. attribute:: name  (key)
        
        	The name of the interface. A server implementation MAY map this leaf to the ifName MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifName.  The definition of such a mechanism is outside the scope of this document
        	**type**\: str
        
        .. attribute:: interface_type
        
        	When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface. If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case
        	**type**\:  :py:class:`IetfIntfType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.IetfIntfType>`
        
        .. attribute:: admin_status
        
        	The desired state of the interface. This leaf has the same read semantics as ifAdminStatus
        	**type**\:  :py:class:`IntfState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.IntfState>`
        
        .. attribute:: oper_status
        
        	The current operational state of the interface. This leaf has the same semantics as ifOperStatus
        	**type**\:  :py:class:`OperState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.OperState>`
        
        .. attribute:: last_change
        
        	The time the interface entered its current operational state. If the current state was entered prior to the last re\-initialization of the local network management subsystem, then this node is not present
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: if_index
        
        	The ifIndex value for the ifEntry represented by this interface
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: phys_address
        
        	The interface's address at its protocol sub\-layer.  For example, for an 802.x interface, this object normally contains a Media Access Control (MAC) address.  The interface's media\-specific modules must define the bit and byte ordering and the format of the value of this object.  For interfaces that do not have such an address (e.g., a serial line), this node is not present
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: higher_layer_if
        
        	A list of references to interfaces layered on top of this interface
        	**type**\: list of str
        
        .. attribute:: lower_layer_if
        
        	A list of references to interfaces layered underneath this interface
        	**type**\: list of str
        
        .. attribute:: speed
        
        	An estimate of the interface's current bandwidth in bits per second.  For interfaces that do not vary in bandwidth or for those where no accurate estimation can be made, this node should contain the nominal bandwidth. For interfaces that have no concept of bandwidth, this node is not present
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: statistics
        
        	A collection of interface\-related statistics objects
        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.Statistics>`
        
        .. attribute:: diffserv_info
        
        	diffserv related details
        	**type**\: list of  		 :py:class:`DiffservInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo>`
        
        .. attribute:: vrf
        
        	VRF to which this interface belongs to. If the  interface is not in a VRF then it is 'Global'
        	**type**\: str
        
        .. attribute:: ipv4
        
        	IPv4 address configured on interface
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: ipv4_subnet_mask
        
        	IPv4 Subnet Mask
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: description
        
        	Interface description
        	**type**\: str
        
        .. attribute:: mtu
        
        	Maximum transmission unit
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: input_security_acl
        
        	Input Security ACL
        	**type**\: str
        
        .. attribute:: output_security_acl
        
        	Output Security ACL
        	**type**\: str
        
        .. attribute:: v4_protocol_stats
        
        	IPv4 traffic statistics for this interface
        	**type**\:  :py:class:`V4ProtocolStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.V4ProtocolStats>`
        
        .. attribute:: v6_protocol_stats
        
        	IPv6 traffic statistics for this interface
        	**type**\:  :py:class:`V6ProtocolStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.V6ProtocolStats>`
        
        .. attribute:: bia_address
        
        	The burnt\-in mac address that was associated with this interface from manufacturing. This is only relevant for interfaces that have the concept of burnt in ethernet  addresses, otherwise it is zero
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: ether_state
        
        	The Ethernet state information
        	**type**\:  :py:class:`EtherState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.EtherState>`
        
        .. attribute:: ether_stats
        
        	The Ethernet statistics
        	**type**\:  :py:class:`EtherStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.EtherStats>`
        
        .. attribute:: serial_state
        
        	The T1E1 serial state information
        	**type**\:  :py:class:`SerialState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.SerialState>`
        
        .. attribute:: serial_stats
        
        	The T1E1 statistics
        	**type**\:  :py:class:`SerialStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.SerialStats>`
        
        .. attribute:: intf_class_unspecified
        
        	No specific interface class information
        	**type**\: bool
        
        

        """

        _prefix = 'interfaces-ios-xe-oper'
        _revision = '2017-10-10'

        def __init__(self):
            super(Interfaces.Interface, self).__init__()

            self.yang_name = "interface"
            self.yang_parent_name = "interfaces"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_container_classes = OrderedDict([("statistics", ("statistics", Interfaces.Interface.Statistics)), ("v4-protocol-stats", ("v4_protocol_stats", Interfaces.Interface.V4ProtocolStats)), ("v6-protocol-stats", ("v6_protocol_stats", Interfaces.Interface.V6ProtocolStats)), ("ether-state", ("ether_state", Interfaces.Interface.EtherState)), ("ether-stats", ("ether_stats", Interfaces.Interface.EtherStats)), ("serial-state", ("serial_state", Interfaces.Interface.SerialState)), ("serial-stats", ("serial_stats", Interfaces.Interface.SerialStats))])
            self._child_list_classes = OrderedDict([("diffserv-info", ("diffserv_info", Interfaces.Interface.DiffservInfo))])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
                ('interface_type', YLeaf(YType.enumeration, 'interface-type')),
                ('admin_status', YLeaf(YType.enumeration, 'admin-status')),
                ('oper_status', YLeaf(YType.enumeration, 'oper-status')),
                ('last_change', YLeaf(YType.str, 'last-change')),
                ('if_index', YLeaf(YType.int32, 'if-index')),
                ('phys_address', YLeaf(YType.str, 'phys-address')),
                ('higher_layer_if', YLeafList(YType.str, 'higher-layer-if')),
                ('lower_layer_if', YLeafList(YType.str, 'lower-layer-if')),
                ('speed', YLeaf(YType.uint64, 'speed')),
                ('vrf', YLeaf(YType.str, 'vrf')),
                ('ipv4', YLeaf(YType.str, 'ipv4')),
                ('ipv4_subnet_mask', YLeaf(YType.str, 'ipv4-subnet-mask')),
                ('description', YLeaf(YType.str, 'description')),
                ('mtu', YLeaf(YType.uint32, 'mtu')),
                ('input_security_acl', YLeaf(YType.str, 'input-security-acl')),
                ('output_security_acl', YLeaf(YType.str, 'output-security-acl')),
                ('bia_address', YLeaf(YType.str, 'bia-address')),
                ('intf_class_unspecified', YLeaf(YType.boolean, 'intf-class-unspecified')),
            ])
            self.name = None
            self.interface_type = None
            self.admin_status = None
            self.oper_status = None
            self.last_change = None
            self.if_index = None
            self.phys_address = None
            self.higher_layer_if = []
            self.lower_layer_if = []
            self.speed = None
            self.vrf = None
            self.ipv4 = None
            self.ipv4_subnet_mask = None
            self.description = None
            self.mtu = None
            self.input_security_acl = None
            self.output_security_acl = None
            self.bia_address = None
            self.intf_class_unspecified = None

            self.statistics = Interfaces.Interface.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._children_yang_names.add("statistics")

            self.v4_protocol_stats = Interfaces.Interface.V4ProtocolStats()
            self.v4_protocol_stats.parent = self
            self._children_name_map["v4_protocol_stats"] = "v4-protocol-stats"
            self._children_yang_names.add("v4-protocol-stats")

            self.v6_protocol_stats = Interfaces.Interface.V6ProtocolStats()
            self.v6_protocol_stats.parent = self
            self._children_name_map["v6_protocol_stats"] = "v6-protocol-stats"
            self._children_yang_names.add("v6-protocol-stats")

            self.ether_state = Interfaces.Interface.EtherState()
            self.ether_state.parent = self
            self._children_name_map["ether_state"] = "ether-state"
            self._children_yang_names.add("ether-state")

            self.ether_stats = Interfaces.Interface.EtherStats()
            self.ether_stats.parent = self
            self._children_name_map["ether_stats"] = "ether-stats"
            self._children_yang_names.add("ether-stats")

            self.serial_state = Interfaces.Interface.SerialState()
            self.serial_state.parent = self
            self._children_name_map["serial_state"] = "serial-state"
            self._children_yang_names.add("serial-state")

            self.serial_stats = Interfaces.Interface.SerialStats()
            self.serial_stats.parent = self
            self._children_name_map["serial_stats"] = "serial-stats"
            self._children_yang_names.add("serial-stats")

            self.diffserv_info = YList(self)
            self._segment_path = lambda: "interface" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-interfaces-oper:interfaces/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Interfaces.Interface, ['name', 'interface_type', 'admin_status', 'oper_status', 'last_change', 'if_index', 'phys_address', 'higher_layer_if', 'lower_layer_if', 'speed', 'vrf', 'ipv4', 'ipv4_subnet_mask', 'description', 'mtu', 'input_security_acl', 'output_security_acl', 'bia_address', 'intf_class_unspecified'], name, value)


        class Statistics(Entity):
            """
            A collection of interface\-related statistics objects
            
            .. attribute:: discontinuity_time
            
            	The time on the most recent occasion at which any one or more of this interface's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this node contains the time the local management subsystem re\-initialized itself
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: in_octets
            
            	The total number of octets received on the interface, including framing characters. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discontinuity\-time
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_unicast_pkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were not addressed to a multicast or broadcast address at this sub\-layer. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: new_name
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a broadcast address at this sub\-layer. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_multicast_pkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a multicast address at this sub\-layer.  For a MAC\-layer protocol, this includes both Group and Functional addresses. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_discards
            
            	The number of inbound packets that were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: in_errors
            
            	For packet\-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol.  For character\- oriented or fixed\-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher\-layer protocol. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: in_unknown_protos
            
            	For packet\-oriented interfaces, the number of packets received via the interface that were discarded because of an unknown or unsupported protocol.  For character\-oriented or fixed\-length interfaces that support protocol multiplexing, the number of transmission units received via the interface that were discarded because of an unknown or unsupported protocol. For any interface that does not support protocol multiplexing, this counter is not present. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_octets
            
            	The total number of octets transmitted out of the interface, including framing characters. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_unicast_pkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and that were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_broadcast_pkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_multicast_pkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC\-layer protocol, this includes both Group and Functional addresses. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_discards
            
            	The number of outbound packets that were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_errors
            
            	For packet\-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character\-oriented or fixed\-length interfaces, the number of outbound transmission units that could not be transmitted because of errors. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rx_pps
            
            	The receive packet per second rate on this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: rx_kbps
            
            	The receive kilobits per second rate on this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: tx_pps
            
            	The transmit packet per second rate on this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: tx_kbps
            
            	The transmit kilobits per second rate on this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: num_flaps
            
            	The number of times the interface state transitioned between up and down
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_crc_errors
            
            	Number of receive error events due to FCS/CRC check failure
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'interfaces-ios-xe-oper'
            _revision = '2017-10-10'

            def __init__(self):
                super(Interfaces.Interface.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('discontinuity_time', YLeaf(YType.str, 'discontinuity-time')),
                    ('in_octets', YLeaf(YType.uint64, 'in-octets')),
                    ('in_unicast_pkts', YLeaf(YType.uint64, 'in-unicast-pkts')),
                    ('new_name', YLeaf(YType.uint64, 'new-name')),
                    ('in_multicast_pkts', YLeaf(YType.uint64, 'in-multicast-pkts')),
                    ('in_discards', YLeaf(YType.uint32, 'in-discards')),
                    ('in_errors', YLeaf(YType.uint32, 'in-errors')),
                    ('in_unknown_protos', YLeaf(YType.uint32, 'in-unknown-protos')),
                    ('out_octets', YLeaf(YType.uint32, 'out-octets')),
                    ('out_unicast_pkts', YLeaf(YType.uint64, 'out-unicast-pkts')),
                    ('out_broadcast_pkts', YLeaf(YType.uint64, 'out-broadcast-pkts')),
                    ('out_multicast_pkts', YLeaf(YType.uint64, 'out-multicast-pkts')),
                    ('out_discards', YLeaf(YType.uint64, 'out-discards')),
                    ('out_errors', YLeaf(YType.uint64, 'out-errors')),
                    ('rx_pps', YLeaf(YType.uint64, 'rx-pps')),
                    ('rx_kbps', YLeaf(YType.uint64, 'rx-kbps')),
                    ('tx_pps', YLeaf(YType.uint64, 'tx-pps')),
                    ('tx_kbps', YLeaf(YType.uint64, 'tx-kbps')),
                    ('num_flaps', YLeaf(YType.uint64, 'num-flaps')),
                    ('in_crc_errors', YLeaf(YType.uint64, 'in-crc-errors')),
                ])
                self.discontinuity_time = None
                self.in_octets = None
                self.in_unicast_pkts = None
                self.new_name = None
                self.in_multicast_pkts = None
                self.in_discards = None
                self.in_errors = None
                self.in_unknown_protos = None
                self.out_octets = None
                self.out_unicast_pkts = None
                self.out_broadcast_pkts = None
                self.out_multicast_pkts = None
                self.out_discards = None
                self.out_errors = None
                self.rx_pps = None
                self.rx_kbps = None
                self.tx_pps = None
                self.tx_kbps = None
                self.num_flaps = None
                self.in_crc_errors = None
                self._segment_path = lambda: "statistics"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.Statistics, ['discontinuity_time', 'in_octets', 'in_unicast_pkts', 'new_name', 'in_multicast_pkts', 'in_discards', 'in_errors', 'in_unknown_protos', 'out_octets', 'out_unicast_pkts', 'out_broadcast_pkts', 'out_multicast_pkts', 'out_discards', 'out_errors', 'rx_pps', 'rx_kbps', 'tx_pps', 'tx_kbps', 'num_flaps', 'in_crc_errors'], name, value)


        class DiffservInfo(Entity):
            """
            diffserv related details
            
            .. attribute:: direction  (key)
            
            	Direction fo the traffic flow either inbound or outbound
            	**type**\:  :py:class:`QosDirection <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.QosDirection>`
            
            .. attribute:: policy_name  (key)
            
            	Policy entry name
            	**type**\: str
            
            .. attribute:: diffserv_target_classifier_stats
            
            	Statistics for each Classifier Entry in a Policy
            	**type**\: list of  		 :py:class:`DiffservTargetClassifierStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats>`
            
            .. attribute:: priority_oper_list
            
            	Statistics for aggregrate priority per policy instance
            	**type**\: list of  		 :py:class:`PriorityOperList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.PriorityOperList>`
            
            

            """

            _prefix = 'interfaces-ios-xe-oper'
            _revision = '2017-10-10'

            def __init__(self):
                super(Interfaces.Interface.DiffservInfo, self).__init__()

                self.yang_name = "diffserv-info"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['direction','policy_name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("diffserv-target-classifier-stats", ("diffserv_target_classifier_stats", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats)), ("priority-oper-list", ("priority_oper_list", Interfaces.Interface.DiffservInfo.PriorityOperList))])
                self._leafs = OrderedDict([
                    ('direction', YLeaf(YType.enumeration, 'direction')),
                    ('policy_name', YLeaf(YType.str, 'policy-name')),
                ])
                self.direction = None
                self.policy_name = None

                self.diffserv_target_classifier_stats = YList(self)
                self.priority_oper_list = YList(self)
                self._segment_path = lambda: "diffserv-info" + "[direction='" + str(self.direction) + "']" + "[policy-name='" + str(self.policy_name) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.DiffservInfo, ['direction', 'policy_name'], name, value)


            class DiffservTargetClassifierStats(Entity):
                """
                Statistics for each Classifier Entry in a Policy
                
                .. attribute:: classifier_entry_name  (key)
                
                	Classifier Entry Name
                	**type**\: str
                
                .. attribute:: parent_path  (key)
                
                	Path of the Classifier Entry in a hierarchial policy
                	**type**\: str
                
                .. attribute:: classifier_entry_stats
                
                	Classifier Counters
                	**type**\:  :py:class:`ClassifierEntryStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.ClassifierEntryStats>`
                
                .. attribute:: meter_stats
                
                	Meter statistics
                	**type**\: list of  		 :py:class:`MeterStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MeterStats>`
                
                .. attribute:: queuing_stats
                
                	Queuing Counters
                	**type**\:  :py:class:`QueuingStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats>`
                
                .. attribute:: subclass_list
                
                	List of statistics for random\-detect based on subclass type and value pair Technically these are a field in the queuing statistics \-> wred statisitcs, but GREEN EI does not allow that nesting structure
                	**type**\: list of  		 :py:class:`SubclassList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList>`
                
                .. attribute:: marking_stats
                
                	Statistics for marking actions
                	**type**\:  :py:class:`MarkingStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats>`
                
                

                """

                _prefix = 'interfaces-ios-xe-oper'
                _revision = '2017-10-10'

                def __init__(self):
                    super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats, self).__init__()

                    self.yang_name = "diffserv-target-classifier-stats"
                    self.yang_parent_name = "diffserv-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['classifier_entry_name','parent_path']
                    self._child_container_classes = OrderedDict([("classifier-entry-stats", ("classifier_entry_stats", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.ClassifierEntryStats)), ("queuing-stats", ("queuing_stats", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats)), ("marking-stats", ("marking_stats", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats))])
                    self._child_list_classes = OrderedDict([("meter-stats", ("meter_stats", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MeterStats)), ("subclass-list", ("subclass_list", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList))])
                    self._leafs = OrderedDict([
                        ('classifier_entry_name', YLeaf(YType.str, 'classifier-entry-name')),
                        ('parent_path', YLeaf(YType.str, 'parent-path')),
                    ])
                    self.classifier_entry_name = None
                    self.parent_path = None

                    self.classifier_entry_stats = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.ClassifierEntryStats()
                    self.classifier_entry_stats.parent = self
                    self._children_name_map["classifier_entry_stats"] = "classifier-entry-stats"
                    self._children_yang_names.add("classifier-entry-stats")

                    self.queuing_stats = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats()
                    self.queuing_stats.parent = self
                    self._children_name_map["queuing_stats"] = "queuing-stats"
                    self._children_yang_names.add("queuing-stats")

                    self.marking_stats = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats()
                    self.marking_stats.parent = self
                    self._children_name_map["marking_stats"] = "marking-stats"
                    self._children_yang_names.add("marking-stats")

                    self.meter_stats = YList(self)
                    self.subclass_list = YList(self)
                    self._segment_path = lambda: "diffserv-target-classifier-stats" + "[classifier-entry-name='" + str(self.classifier_entry_name) + "']" + "[parent-path='" + str(self.parent_path) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats, ['classifier_entry_name', 'parent_path'], name, value)


                class ClassifierEntryStats(Entity):
                    """
                    Classifier Counters
                    
                    .. attribute:: classified_pkts
                    
                    	Number of total packets which filtered to the classifier\-entry
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: classified_bytes
                    
                    	Number of total bytes which filtered to the classifier\-entry
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: classified_rate
                    
                    	Rate of average data flow through the classifier\-entry
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'interfaces-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.ClassifierEntryStats, self).__init__()

                        self.yang_name = "classifier-entry-stats"
                        self.yang_parent_name = "diffserv-target-classifier-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('classified_pkts', YLeaf(YType.uint64, 'classified-pkts')),
                            ('classified_bytes', YLeaf(YType.uint64, 'classified-bytes')),
                            ('classified_rate', YLeaf(YType.uint64, 'classified-rate')),
                        ])
                        self.classified_pkts = None
                        self.classified_bytes = None
                        self.classified_rate = None
                        self._segment_path = lambda: "classifier-entry-stats"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.ClassifierEntryStats, ['classified_pkts', 'classified_bytes', 'classified_rate'], name, value)


                class MeterStats(Entity):
                    """
                    Meter statistics
                    
                    .. attribute:: meter_id  (key)
                    
                    	Meter Identifier
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: meter_succeed_pkts
                    
                    	Number of packets which succeed the meter
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_succeed_bytes
                    
                    	Bytes of packets which succeed the meter
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_failed_pkts
                    
                    	Number of packets which failed the meter
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_failed_bytes
                    
                    	Bytes of packets which failed the meter
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'interfaces-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MeterStats, self).__init__()

                        self.yang_name = "meter-stats"
                        self.yang_parent_name = "diffserv-target-classifier-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['meter_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('meter_id', YLeaf(YType.uint16, 'meter-id')),
                            ('meter_succeed_pkts', YLeaf(YType.uint64, 'meter-succeed-pkts')),
                            ('meter_succeed_bytes', YLeaf(YType.uint64, 'meter-succeed-bytes')),
                            ('meter_failed_pkts', YLeaf(YType.uint64, 'meter-failed-pkts')),
                            ('meter_failed_bytes', YLeaf(YType.uint64, 'meter-failed-bytes')),
                        ])
                        self.meter_id = None
                        self.meter_succeed_pkts = None
                        self.meter_succeed_bytes = None
                        self.meter_failed_pkts = None
                        self.meter_failed_bytes = None
                        self._segment_path = lambda: "meter-stats" + "[meter-id='" + str(self.meter_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MeterStats, ['meter_id', 'meter_succeed_pkts', 'meter_succeed_bytes', 'meter_failed_pkts', 'meter_failed_bytes'], name, value)


                class QueuingStats(Entity):
                    """
                    Queuing Counters
                    
                    .. attribute:: output_pkts
                    
                    	Number of packets transmitted from queue
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_bytes
                    
                    	Number of bytes transmitted from queue
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: queue_size_pkts
                    
                    	Number of packets currently buffered 
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: queue_size_bytes
                    
                    	Number of bytes currently buffered
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drop_pkts
                    
                    	Total number of packets dropped
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drop_bytes
                    
                    	Total number of bytes dropped
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: wred_stats
                    
                    	WRED Counters
                    	**type**\:  :py:class:`WredStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats.WredStats>`
                    
                    .. attribute:: cac_stats
                    
                    	CAC statistics
                    	**type**\:  :py:class:`CacStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats.CacStats>`
                    
                    

                    """

                    _prefix = 'interfaces-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats, self).__init__()

                        self.yang_name = "queuing-stats"
                        self.yang_parent_name = "diffserv-target-classifier-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("wred-stats", ("wred_stats", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats.WredStats)), ("cac-stats", ("cac_stats", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats.CacStats))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('output_pkts', YLeaf(YType.uint64, 'output-pkts')),
                            ('output_bytes', YLeaf(YType.uint64, 'output-bytes')),
                            ('queue_size_pkts', YLeaf(YType.uint64, 'queue-size-pkts')),
                            ('queue_size_bytes', YLeaf(YType.uint64, 'queue-size-bytes')),
                            ('drop_pkts', YLeaf(YType.uint64, 'drop-pkts')),
                            ('drop_bytes', YLeaf(YType.uint64, 'drop-bytes')),
                        ])
                        self.output_pkts = None
                        self.output_bytes = None
                        self.queue_size_pkts = None
                        self.queue_size_bytes = None
                        self.drop_pkts = None
                        self.drop_bytes = None

                        self.wred_stats = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats.WredStats()
                        self.wred_stats.parent = self
                        self._children_name_map["wred_stats"] = "wred-stats"
                        self._children_yang_names.add("wred-stats")

                        self.cac_stats = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats.CacStats()
                        self.cac_stats.parent = self
                        self._children_name_map["cac_stats"] = "cac-stats"
                        self._children_yang_names.add("cac-stats")
                        self._segment_path = lambda: "queuing-stats"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats, ['output_pkts', 'output_bytes', 'queue_size_pkts', 'queue_size_bytes', 'drop_pkts', 'drop_bytes'], name, value)


                    class WredStats(Entity):
                        """
                        WRED Counters
                        
                        .. attribute:: early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: mean_queue_depth
                        
                        	Current mean queue depth
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: transmitted_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: transmitted_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: tail_drop_pkts
                        
                        	Total number of packets dropped
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: tail_drop_bytes
                        
                        	Total number of bytes dropped
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: drop_pkts_flow
                        
                        	Total number of packets dropped
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: drop_pkts_no_buffer
                        
                        	Number of packets dropped due to buffers being unavailable system\-wide or at the associated interface. This is a sub\-set of drop\-pkts
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: queue_peak_size_pkts
                        
                        	Queue max que depth Packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: queue_peak_size_bytes
                        
                        	Queue max que depth Bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: bandwidth_exceed_drops
                        
                        	Priority stats. Bandwidth exceed drops
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats.WredStats, self).__init__()

                            self.yang_name = "wred-stats"
                            self.yang_parent_name = "queuing-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('early_drop_pkts', YLeaf(YType.uint64, 'early-drop-pkts')),
                                ('early_drop_bytes', YLeaf(YType.uint64, 'early-drop-bytes')),
                                ('mean_queue_depth', YLeaf(YType.uint16, 'mean-queue-depth')),
                                ('transmitted_pkts', YLeaf(YType.uint64, 'transmitted-pkts')),
                                ('transmitted_bytes', YLeaf(YType.uint64, 'transmitted-bytes')),
                                ('tail_drop_pkts', YLeaf(YType.uint64, 'tail-drop-pkts')),
                                ('tail_drop_bytes', YLeaf(YType.uint64, 'tail-drop-bytes')),
                                ('drop_pkts_flow', YLeaf(YType.uint64, 'drop-pkts-flow')),
                                ('drop_pkts_no_buffer', YLeaf(YType.uint64, 'drop-pkts-no-buffer')),
                                ('queue_peak_size_pkts', YLeaf(YType.uint64, 'queue-peak-size-pkts')),
                                ('queue_peak_size_bytes', YLeaf(YType.uint64, 'queue-peak-size-bytes')),
                                ('bandwidth_exceed_drops', YLeaf(YType.uint64, 'bandwidth-exceed-drops')),
                            ])
                            self.early_drop_pkts = None
                            self.early_drop_bytes = None
                            self.mean_queue_depth = None
                            self.transmitted_pkts = None
                            self.transmitted_bytes = None
                            self.tail_drop_pkts = None
                            self.tail_drop_bytes = None
                            self.drop_pkts_flow = None
                            self.drop_pkts_no_buffer = None
                            self.queue_peak_size_pkts = None
                            self.queue_peak_size_bytes = None
                            self.bandwidth_exceed_drops = None
                            self._segment_path = lambda: "wred-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats.WredStats, ['early_drop_pkts', 'early_drop_bytes', 'mean_queue_depth', 'transmitted_pkts', 'transmitted_bytes', 'tail_drop_pkts', 'tail_drop_bytes', 'drop_pkts_flow', 'drop_pkts_no_buffer', 'queue_peak_size_pkts', 'queue_peak_size_bytes', 'bandwidth_exceed_drops'], name, value)


                    class CacStats(Entity):
                        """
                        CAC statistics
                        
                        .. attribute:: num_admitted_flows
                        
                        	Number of admitted flows
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: num_non_admitted_flows
                        
                        	Number of non\-admitted flows
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats.CacStats, self).__init__()

                            self.yang_name = "cac-stats"
                            self.yang_parent_name = "queuing-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('num_admitted_flows', YLeaf(YType.uint32, 'num-admitted-flows')),
                                ('num_non_admitted_flows', YLeaf(YType.uint32, 'num-non-admitted-flows')),
                            ])
                            self.num_admitted_flows = None
                            self.num_non_admitted_flows = None
                            self._segment_path = lambda: "cac-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.QueuingStats.CacStats, ['num_admitted_flows', 'num_non_admitted_flows'], name, value)


                class SubclassList(Entity):
                    """
                    List of statistics for random\-detect
                    based on subclass type and value pair
                    Technically these are a field in the queuing
                    statistics \-> wred statisitcs, but GREEN EI
                    does not allow that nesting structure
                    
                    .. attribute:: match_type  (key)
                    
                    	Subclass match type
                    	**type**\:  :py:class:`QosMatchType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.QosMatchType>`
                    
                    .. attribute:: cos_counters
                    
                    	Counters for sub\-class matching a range of Class\-of\-Service (COS) value (and, optionally, additional COS range
                    	**type**\: list of  		 :py:class:`CosCounters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.CosCounters>`
                    
                    .. attribute:: cos_default
                    
                    	statistics for cos default
                    	**type**\:  :py:class:`CosDefault <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.CosDefault>`
                    
                    .. attribute:: dscp_counters
                    
                    	List for statistics based on dscp value range
                    	**type**\: list of  		 :py:class:`DscpCounters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DscpCounters>`
                    
                    .. attribute:: dscp_default
                    
                    	Statistics for dscp default
                    	**type**\:  :py:class:`DscpDefault <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DscpDefault>`
                    
                    .. attribute:: discard_class_counters
                    
                    	Composed multiple discard class ranges
                    	**type**\: list of  		 :py:class:`DiscardClassCounters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DiscardClassCounters>`
                    
                    .. attribute:: disc_class_default
                    
                    	Statistics for discard class default
                    	**type**\:  :py:class:`DiscClassDefault <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DiscClassDefault>`
                    
                    .. attribute:: precedence_counters
                    
                    	List for statistics based on precedence value range
                    	**type**\: list of  		 :py:class:`PrecedenceCounters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.PrecedenceCounters>`
                    
                    .. attribute:: prec_default
                    
                    	Precedence default
                    	**type**\:  :py:class:`PrecDefault <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.PrecDefault>`
                    
                    .. attribute:: mpls_exp_counters
                    
                    	List for statistics based on mpls exp value range
                    	**type**\: list of  		 :py:class:`MplsExpCounters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.MplsExpCounters>`
                    
                    .. attribute:: mpls_exp_default
                    
                    	Statistics for mpls\-exp default
                    	**type**\:  :py:class:`MplsExpDefault <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.MplsExpDefault>`
                    
                    .. attribute:: dei_counters
                    
                    	Composed by multiple dei ranges
                    	**type**\: list of  		 :py:class:`DeiCounters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DeiCounters>`
                    
                    .. attribute:: dei_counts_default
                    
                    	Statistics for dei default
                    	**type**\:  :py:class:`DeiCountsDefault <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DeiCountsDefault>`
                    
                    .. attribute:: clp_counters
                    
                    	Statistics for each value range for a specifc subclass type
                    	**type**\: list of  		 :py:class:`ClpCounters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.ClpCounters>`
                    
                    .. attribute:: clp_default
                    
                    	Statistic for atm clp default
                    	**type**\:  :py:class:`ClpDefault <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.ClpDefault>`
                    
                    

                    """

                    _prefix = 'interfaces-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList, self).__init__()

                        self.yang_name = "subclass-list"
                        self.yang_parent_name = "diffserv-target-classifier-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['match_type']
                        self._child_container_classes = OrderedDict([("cos-default", ("cos_default", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.CosDefault)), ("dscp-default", ("dscp_default", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DscpDefault)), ("disc-class-default", ("disc_class_default", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DiscClassDefault)), ("prec-default", ("prec_default", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.PrecDefault)), ("mpls-exp-default", ("mpls_exp_default", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.MplsExpDefault)), ("dei-counts-default", ("dei_counts_default", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DeiCountsDefault)), ("clp-default", ("clp_default", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.ClpDefault))])
                        self._child_list_classes = OrderedDict([("cos-counters", ("cos_counters", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.CosCounters)), ("dscp-counters", ("dscp_counters", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DscpCounters)), ("discard-class-counters", ("discard_class_counters", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DiscardClassCounters)), ("precedence-counters", ("precedence_counters", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.PrecedenceCounters)), ("mpls-exp-counters", ("mpls_exp_counters", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.MplsExpCounters)), ("dei-counters", ("dei_counters", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DeiCounters)), ("clp-counters", ("clp_counters", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.ClpCounters))])
                        self._leafs = OrderedDict([
                            ('match_type', YLeaf(YType.enumeration, 'match-type')),
                        ])
                        self.match_type = None

                        self.cos_default = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.CosDefault()
                        self.cos_default.parent = self
                        self._children_name_map["cos_default"] = "cos-default"
                        self._children_yang_names.add("cos-default")

                        self.dscp_default = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DscpDefault()
                        self.dscp_default.parent = self
                        self._children_name_map["dscp_default"] = "dscp-default"
                        self._children_yang_names.add("dscp-default")

                        self.disc_class_default = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DiscClassDefault()
                        self.disc_class_default.parent = self
                        self._children_name_map["disc_class_default"] = "disc-class-default"
                        self._children_yang_names.add("disc-class-default")

                        self.prec_default = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.PrecDefault()
                        self.prec_default.parent = self
                        self._children_name_map["prec_default"] = "prec-default"
                        self._children_yang_names.add("prec-default")

                        self.mpls_exp_default = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.MplsExpDefault()
                        self.mpls_exp_default.parent = self
                        self._children_name_map["mpls_exp_default"] = "mpls-exp-default"
                        self._children_yang_names.add("mpls-exp-default")

                        self.dei_counts_default = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DeiCountsDefault()
                        self.dei_counts_default.parent = self
                        self._children_name_map["dei_counts_default"] = "dei-counts-default"
                        self._children_yang_names.add("dei-counts-default")

                        self.clp_default = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.ClpDefault()
                        self.clp_default.parent = self
                        self._children_name_map["clp_default"] = "clp-default"
                        self._children_yang_names.add("clp-default")

                        self.cos_counters = YList(self)
                        self.dscp_counters = YList(self)
                        self.discard_class_counters = YList(self)
                        self.precedence_counters = YList(self)
                        self.mpls_exp_counters = YList(self)
                        self.dei_counters = YList(self)
                        self.clp_counters = YList(self)
                        self._segment_path = lambda: "subclass-list" + "[match-type='" + str(self.match_type) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList, ['match_type'], name, value)


                    class CosCounters(Entity):
                        """
                        Counters for sub\-class matching a range of
                        Class\-of\-Service (COS) value (and, optionally, additional COS range
                        
                        .. attribute:: cos_min  (key)
                        
                        	Min COS value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cos_max  (key)
                        
                        	Max COS value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.CosCounters, self).__init__()

                            self.yang_name = "cos-counters"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['cos_min','cos_max']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('cos_min', YLeaf(YType.uint32, 'cos-min')),
                                ('cos_max', YLeaf(YType.uint32, 'cos-max')),
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.cos_min = None
                            self.cos_max = None
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "cos-counters" + "[cos-min='" + str(self.cos_min) + "']" + "[cos-max='" + str(self.cos_max) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.CosCounters, ['cos_min', 'cos_max', 'wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class CosDefault(Entity):
                        """
                        statistics for cos default
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.CosDefault, self).__init__()

                            self.yang_name = "cos-default"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "cos-default"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.CosDefault, ['wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class DscpCounters(Entity):
                        """
                        List for statistics based on dscp value range
                        
                        .. attribute:: dscp_min  (key)
                        
                        	Minimum of dscp range
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dscp_max  (key)
                        
                        	Maximum of dscp range
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DscpCounters, self).__init__()

                            self.yang_name = "dscp-counters"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['dscp_min','dscp_max']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('dscp_min', YLeaf(YType.uint32, 'dscp-min')),
                                ('dscp_max', YLeaf(YType.uint32, 'dscp-max')),
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.dscp_min = None
                            self.dscp_max = None
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "dscp-counters" + "[dscp-min='" + str(self.dscp_min) + "']" + "[dscp-max='" + str(self.dscp_max) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DscpCounters, ['dscp_min', 'dscp_max', 'wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class DscpDefault(Entity):
                        """
                        Statistics for dscp default
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DscpDefault, self).__init__()

                            self.yang_name = "dscp-default"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "dscp-default"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DscpDefault, ['wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class DiscardClassCounters(Entity):
                        """
                        Composed multiple discard class ranges
                        
                        .. attribute:: disc_class_min  (key)
                        
                        	Minimum value for discard class in the range
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: disc_class_max  (key)
                        
                        	Maximum value for discard class in the range
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DiscardClassCounters, self).__init__()

                            self.yang_name = "discard-class-counters"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['disc_class_min','disc_class_max']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('disc_class_min', YLeaf(YType.uint32, 'disc-class-min')),
                                ('disc_class_max', YLeaf(YType.uint32, 'disc-class-max')),
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.disc_class_min = None
                            self.disc_class_max = None
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "discard-class-counters" + "[disc-class-min='" + str(self.disc_class_min) + "']" + "[disc-class-max='" + str(self.disc_class_max) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DiscardClassCounters, ['disc_class_min', 'disc_class_max', 'wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class DiscClassDefault(Entity):
                        """
                        Statistics for discard class default
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DiscClassDefault, self).__init__()

                            self.yang_name = "disc-class-default"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "disc-class-default"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DiscClassDefault, ['wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class PrecedenceCounters(Entity):
                        """
                        List for statistics based on precedence value range
                        
                        .. attribute:: prec_min  (key)
                        
                        	Precedence min
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prec_max  (key)
                        
                        	Precedence max
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.PrecedenceCounters, self).__init__()

                            self.yang_name = "precedence-counters"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['prec_min','prec_max']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prec_min', YLeaf(YType.uint32, 'prec-min')),
                                ('prec_max', YLeaf(YType.uint32, 'prec-max')),
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.prec_min = None
                            self.prec_max = None
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "precedence-counters" + "[prec-min='" + str(self.prec_min) + "']" + "[prec-max='" + str(self.prec_max) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.PrecedenceCounters, ['prec_min', 'prec_max', 'wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class PrecDefault(Entity):
                        """
                        Precedence default
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.PrecDefault, self).__init__()

                            self.yang_name = "prec-default"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "prec-default"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.PrecDefault, ['wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class MplsExpCounters(Entity):
                        """
                        List for statistics based on mpls exp value range
                        
                        .. attribute:: exp_min  (key)
                        
                        	The minimum EXP field value to be used as match criteria. Any number from 0 to 7
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: exp_max  (key)
                        
                        	The maximum EXP field value to be used as match criteria. Any number from 0 to 7
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.MplsExpCounters, self).__init__()

                            self.yang_name = "mpls-exp-counters"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['exp_min','exp_max']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('exp_min', YLeaf(YType.uint32, 'exp-min')),
                                ('exp_max', YLeaf(YType.uint32, 'exp-max')),
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.exp_min = None
                            self.exp_max = None
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "mpls-exp-counters" + "[exp-min='" + str(self.exp_min) + "']" + "[exp-max='" + str(self.exp_max) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.MplsExpCounters, ['exp_min', 'exp_max', 'wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class MplsExpDefault(Entity):
                        """
                        Statistics for mpls\-exp default
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.MplsExpDefault, self).__init__()

                            self.yang_name = "mpls-exp-default"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "mpls-exp-default"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.MplsExpDefault, ['wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class DeiCounters(Entity):
                        """
                        Composed by multiple dei ranges
                        
                        .. attribute:: dei_min  (key)
                        
                        	Dei min
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dei_max  (key)
                        
                        	Dei max
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DeiCounters, self).__init__()

                            self.yang_name = "dei-counters"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['dei_min','dei_max']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('dei_min', YLeaf(YType.uint32, 'dei-min')),
                                ('dei_max', YLeaf(YType.uint32, 'dei-max')),
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.dei_min = None
                            self.dei_max = None
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "dei-counters" + "[dei-min='" + str(self.dei_min) + "']" + "[dei-max='" + str(self.dei_max) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DeiCounters, ['dei_min', 'dei_max', 'wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class DeiCountsDefault(Entity):
                        """
                        Statistics for dei default
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DeiCountsDefault, self).__init__()

                            self.yang_name = "dei-counts-default"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "dei-counts-default"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.DeiCountsDefault, ['wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class ClpCounters(Entity):
                        """
                        Statistics for each value range for a specifc subclass type
                        
                        .. attribute:: clp_val  (key)
                        
                        	Composed by multiple atm clp values
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.ClpCounters, self).__init__()

                            self.yang_name = "clp-counters"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['clp_val']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('clp_val', YLeaf(YType.uint32, 'clp-val')),
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.clp_val = None
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "clp-counters" + "[clp-val='" + str(self.clp_val) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.ClpCounters, ['clp_val', 'wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                    class ClpDefault(Entity):
                        """
                        Statistic for atm clp default
                        
                        .. attribute:: wred_tx_pkts
                        
                        	Transmitted packtes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tx_bytes
                        
                        	Transmitted bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_pkts
                        
                        	Tail drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_tail_drop_bytes
                        
                        	Tail drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_pkts
                        
                        	Early drop packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: wred_early_drop_bytes
                        
                        	Early drop bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.ClpDefault, self).__init__()

                            self.yang_name = "clp-default"
                            self.yang_parent_name = "subclass-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('wred_tx_pkts', YLeaf(YType.uint64, 'wred-tx-pkts')),
                                ('wred_tx_bytes', YLeaf(YType.uint64, 'wred-tx-bytes')),
                                ('wred_tail_drop_pkts', YLeaf(YType.uint64, 'wred-tail-drop-pkts')),
                                ('wred_tail_drop_bytes', YLeaf(YType.uint64, 'wred-tail-drop-bytes')),
                                ('wred_early_drop_pkts', YLeaf(YType.uint64, 'wred-early-drop-pkts')),
                                ('wred_early_drop_bytes', YLeaf(YType.uint64, 'wred-early-drop-bytes')),
                            ])
                            self.wred_tx_pkts = None
                            self.wred_tx_bytes = None
                            self.wred_tail_drop_pkts = None
                            self.wred_tail_drop_bytes = None
                            self.wred_early_drop_pkts = None
                            self.wred_early_drop_bytes = None
                            self._segment_path = lambda: "clp-default"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.SubclassList.ClpDefault, ['wred_tx_pkts', 'wred_tx_bytes', 'wred_tail_drop_pkts', 'wred_tail_drop_bytes', 'wred_early_drop_pkts', 'wred_early_drop_bytes'], name, value)


                class MarkingStats(Entity):
                    """
                    Statistics for marking actions
                    
                    .. attribute:: marking_dscp_stats_val
                    
                    	Statistics for set dscp
                    	**type**\:  :py:class:`MarkingDscpStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDscpStatsVal>`
                    
                    .. attribute:: marking_dscp_tunnel_stats_val
                    
                    	Statistics for set dscp tunnel
                    	**type**\:  :py:class:`MarkingDscpTunnelStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDscpTunnelStatsVal>`
                    
                    .. attribute:: marking_cos_stats_val
                    
                    	Statistics for set cos
                    	**type**\:  :py:class:`MarkingCosStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingCosStatsVal>`
                    
                    .. attribute:: marking_cos_inner_stats_val
                    
                    	Statistics for set cos\-inner
                    	**type**\:  :py:class:`MarkingCosInnerStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingCosInnerStatsVal>`
                    
                    .. attribute:: marking_discard_class_stats_val
                    
                    	Statistics for set discard\-class
                    	**type**\:  :py:class:`MarkingDiscardClassStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDiscardClassStatsVal>`
                    
                    .. attribute:: marking_qos_grp_stats_val
                    
                    	Statistics for set qos\-group
                    	**type**\:  :py:class:`MarkingQosGrpStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingQosGrpStatsVal>`
                    
                    .. attribute:: marking_prec_stats_val
                    
                    	Statistics for set precedence
                    	**type**\:  :py:class:`MarkingPrecStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingPrecStatsVal>`
                    
                    .. attribute:: marking_prec_tunnel_stats_val
                    
                    	Statistics for set precedence tunnel
                    	**type**\:  :py:class:`MarkingPrecTunnelStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingPrecTunnelStatsVal>`
                    
                    .. attribute:: marking_mpls_exp_imp_stats_val
                    
                    	Statistics for set mpls exp imposition
                    	**type**\:  :py:class:`MarkingMplsExpImpStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingMplsExpImpStatsVal>`
                    
                    .. attribute:: marking_mpls_exp_top_stats_val
                    
                    	Statistics for set mpls exp topmost
                    	**type**\:  :py:class:`MarkingMplsExpTopStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingMplsExpTopStatsVal>`
                    
                    .. attribute:: marking_fr_de_stats_val
                    
                    	Statistics for set fr\-de
                    	**type**\:  :py:class:`MarkingFrDeStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingFrDeStatsVal>`
                    
                    .. attribute:: marking_fr_fecn_becn_stats_val
                    
                    	Statistics for set fr\-fecn\-becn
                    	**type**\:  :py:class:`MarkingFrFecnBecnStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingFrFecnBecnStatsVal>`
                    
                    .. attribute:: marking_atm_clp_stats_val
                    
                    	Statistics for set atm\-clp
                    	**type**\:  :py:class:`MarkingAtmClpStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingAtmClpStatsVal>`
                    
                    .. attribute:: marking_vlan_inner_stats_val
                    
                    	Statistics for set vlan\-inner
                    	**type**\:  :py:class:`MarkingVlanInnerStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingVlanInnerStatsVal>`
                    
                    .. attribute:: marking_dei_stats_val
                    
                    	Statistics for set dei
                    	**type**\:  :py:class:`MarkingDeiStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDeiStatsVal>`
                    
                    .. attribute:: marking_dei_imp_stats_val
                    
                    	Statistics for set dei\-imposition
                    	**type**\:  :py:class:`MarkingDeiImpStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDeiImpStatsVal>`
                    
                    .. attribute:: marking_srp_priority_stats_val
                    
                    	Statistics for set srp\-priority
                    	**type**\:  :py:class:`MarkingSrpPriorityStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingSrpPriorityStatsVal>`
                    
                    .. attribute:: marking_wlan_user_priority_stats_val
                    
                    	Statistics for set wlan\-user\-priority
                    	**type**\:  :py:class:`MarkingWlanUserPriorityStatsVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingWlanUserPriorityStatsVal>`
                    
                    

                    """

                    _prefix = 'interfaces-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats, self).__init__()

                        self.yang_name = "marking-stats"
                        self.yang_parent_name = "diffserv-target-classifier-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("marking-dscp-stats-val", ("marking_dscp_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDscpStatsVal)), ("marking-dscp-tunnel-stats-val", ("marking_dscp_tunnel_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDscpTunnelStatsVal)), ("marking-cos-stats-val", ("marking_cos_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingCosStatsVal)), ("marking-cos-inner-stats-val", ("marking_cos_inner_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingCosInnerStatsVal)), ("marking-discard-class-stats-val", ("marking_discard_class_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDiscardClassStatsVal)), ("marking-qos-grp-stats-val", ("marking_qos_grp_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingQosGrpStatsVal)), ("marking-prec-stats-val", ("marking_prec_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingPrecStatsVal)), ("marking-prec-tunnel-stats-val", ("marking_prec_tunnel_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingPrecTunnelStatsVal)), ("marking-mpls-exp-imp-stats-val", ("marking_mpls_exp_imp_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingMplsExpImpStatsVal)), ("marking-mpls-exp-top-stats-val", ("marking_mpls_exp_top_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingMplsExpTopStatsVal)), ("marking-fr-de-stats-val", ("marking_fr_de_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingFrDeStatsVal)), ("marking-fr-fecn-becn-stats-val", ("marking_fr_fecn_becn_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingFrFecnBecnStatsVal)), ("marking-atm-clp-stats-val", ("marking_atm_clp_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingAtmClpStatsVal)), ("marking-vlan-inner-stats-val", ("marking_vlan_inner_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingVlanInnerStatsVal)), ("marking-dei-stats-val", ("marking_dei_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDeiStatsVal)), ("marking-dei-imp-stats-val", ("marking_dei_imp_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDeiImpStatsVal)), ("marking-srp-priority-stats-val", ("marking_srp_priority_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingSrpPriorityStatsVal)), ("marking-wlan-user-priority-stats-val", ("marking_wlan_user_priority_stats_val", Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingWlanUserPriorityStatsVal))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.marking_dscp_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDscpStatsVal()
                        self.marking_dscp_stats_val.parent = self
                        self._children_name_map["marking_dscp_stats_val"] = "marking-dscp-stats-val"
                        self._children_yang_names.add("marking-dscp-stats-val")

                        self.marking_dscp_tunnel_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDscpTunnelStatsVal()
                        self.marking_dscp_tunnel_stats_val.parent = self
                        self._children_name_map["marking_dscp_tunnel_stats_val"] = "marking-dscp-tunnel-stats-val"
                        self._children_yang_names.add("marking-dscp-tunnel-stats-val")

                        self.marking_cos_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingCosStatsVal()
                        self.marking_cos_stats_val.parent = self
                        self._children_name_map["marking_cos_stats_val"] = "marking-cos-stats-val"
                        self._children_yang_names.add("marking-cos-stats-val")

                        self.marking_cos_inner_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingCosInnerStatsVal()
                        self.marking_cos_inner_stats_val.parent = self
                        self._children_name_map["marking_cos_inner_stats_val"] = "marking-cos-inner-stats-val"
                        self._children_yang_names.add("marking-cos-inner-stats-val")

                        self.marking_discard_class_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDiscardClassStatsVal()
                        self.marking_discard_class_stats_val.parent = self
                        self._children_name_map["marking_discard_class_stats_val"] = "marking-discard-class-stats-val"
                        self._children_yang_names.add("marking-discard-class-stats-val")

                        self.marking_qos_grp_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingQosGrpStatsVal()
                        self.marking_qos_grp_stats_val.parent = self
                        self._children_name_map["marking_qos_grp_stats_val"] = "marking-qos-grp-stats-val"
                        self._children_yang_names.add("marking-qos-grp-stats-val")

                        self.marking_prec_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingPrecStatsVal()
                        self.marking_prec_stats_val.parent = self
                        self._children_name_map["marking_prec_stats_val"] = "marking-prec-stats-val"
                        self._children_yang_names.add("marking-prec-stats-val")

                        self.marking_prec_tunnel_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingPrecTunnelStatsVal()
                        self.marking_prec_tunnel_stats_val.parent = self
                        self._children_name_map["marking_prec_tunnel_stats_val"] = "marking-prec-tunnel-stats-val"
                        self._children_yang_names.add("marking-prec-tunnel-stats-val")

                        self.marking_mpls_exp_imp_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingMplsExpImpStatsVal()
                        self.marking_mpls_exp_imp_stats_val.parent = self
                        self._children_name_map["marking_mpls_exp_imp_stats_val"] = "marking-mpls-exp-imp-stats-val"
                        self._children_yang_names.add("marking-mpls-exp-imp-stats-val")

                        self.marking_mpls_exp_top_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingMplsExpTopStatsVal()
                        self.marking_mpls_exp_top_stats_val.parent = self
                        self._children_name_map["marking_mpls_exp_top_stats_val"] = "marking-mpls-exp-top-stats-val"
                        self._children_yang_names.add("marking-mpls-exp-top-stats-val")

                        self.marking_fr_de_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingFrDeStatsVal()
                        self.marking_fr_de_stats_val.parent = self
                        self._children_name_map["marking_fr_de_stats_val"] = "marking-fr-de-stats-val"
                        self._children_yang_names.add("marking-fr-de-stats-val")

                        self.marking_fr_fecn_becn_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingFrFecnBecnStatsVal()
                        self.marking_fr_fecn_becn_stats_val.parent = self
                        self._children_name_map["marking_fr_fecn_becn_stats_val"] = "marking-fr-fecn-becn-stats-val"
                        self._children_yang_names.add("marking-fr-fecn-becn-stats-val")

                        self.marking_atm_clp_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingAtmClpStatsVal()
                        self.marking_atm_clp_stats_val.parent = self
                        self._children_name_map["marking_atm_clp_stats_val"] = "marking-atm-clp-stats-val"
                        self._children_yang_names.add("marking-atm-clp-stats-val")

                        self.marking_vlan_inner_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingVlanInnerStatsVal()
                        self.marking_vlan_inner_stats_val.parent = self
                        self._children_name_map["marking_vlan_inner_stats_val"] = "marking-vlan-inner-stats-val"
                        self._children_yang_names.add("marking-vlan-inner-stats-val")

                        self.marking_dei_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDeiStatsVal()
                        self.marking_dei_stats_val.parent = self
                        self._children_name_map["marking_dei_stats_val"] = "marking-dei-stats-val"
                        self._children_yang_names.add("marking-dei-stats-val")

                        self.marking_dei_imp_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDeiImpStatsVal()
                        self.marking_dei_imp_stats_val.parent = self
                        self._children_name_map["marking_dei_imp_stats_val"] = "marking-dei-imp-stats-val"
                        self._children_yang_names.add("marking-dei-imp-stats-val")

                        self.marking_srp_priority_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingSrpPriorityStatsVal()
                        self.marking_srp_priority_stats_val.parent = self
                        self._children_name_map["marking_srp_priority_stats_val"] = "marking-srp-priority-stats-val"
                        self._children_yang_names.add("marking-srp-priority-stats-val")

                        self.marking_wlan_user_priority_stats_val = Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingWlanUserPriorityStatsVal()
                        self.marking_wlan_user_priority_stats_val.parent = self
                        self._children_name_map["marking_wlan_user_priority_stats_val"] = "marking-wlan-user-priority-stats-val"
                        self._children_yang_names.add("marking-wlan-user-priority-stats-val")
                        self._segment_path = lambda: "marking-stats"


                    class MarkingDscpStatsVal(Entity):
                        """
                        Statistics for set dscp
                        
                        .. attribute:: dscp
                        
                        	dscp marking
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDscpStatsVal, self).__init__()

                            self.yang_name = "marking-dscp-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('dscp', YLeaf(YType.uint32, 'dscp')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.dscp = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-dscp-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDscpStatsVal, ['dscp', 'marked_pkts'], name, value)


                    class MarkingDscpTunnelStatsVal(Entity):
                        """
                        Statistics for set dscp tunnel
                        
                        .. attribute:: dscp_val
                        
                        	dscp value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDscpTunnelStatsVal, self).__init__()

                            self.yang_name = "marking-dscp-tunnel-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('dscp_val', YLeaf(YType.uint32, 'dscp-val')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.dscp_val = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-dscp-tunnel-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDscpTunnelStatsVal, ['dscp_val', 'marked_pkts'], name, value)


                    class MarkingCosStatsVal(Entity):
                        """
                        Statistics for set cos
                        
                        .. attribute:: cos_val
                        
                        	cos value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingCosStatsVal, self).__init__()

                            self.yang_name = "marking-cos-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('cos_val', YLeaf(YType.uint32, 'cos-val')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.cos_val = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-cos-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingCosStatsVal, ['cos_val', 'marked_pkts'], name, value)


                    class MarkingCosInnerStatsVal(Entity):
                        """
                        Statistics for set cos\-inner
                        
                        .. attribute:: cos_inner_val
                        
                        	cos inner value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingCosInnerStatsVal, self).__init__()

                            self.yang_name = "marking-cos-inner-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('cos_inner_val', YLeaf(YType.uint32, 'cos-inner-val')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.cos_inner_val = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-cos-inner-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingCosInnerStatsVal, ['cos_inner_val', 'marked_pkts'], name, value)


                    class MarkingDiscardClassStatsVal(Entity):
                        """
                        Statistics for set discard\-class
                        
                        .. attribute:: disc_class_val
                        
                        	discard\-class value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDiscardClassStatsVal, self).__init__()

                            self.yang_name = "marking-discard-class-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('disc_class_val', YLeaf(YType.uint32, 'disc-class-val')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.disc_class_val = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-discard-class-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDiscardClassStatsVal, ['disc_class_val', 'marked_pkts'], name, value)


                    class MarkingQosGrpStatsVal(Entity):
                        """
                        Statistics for set qos\-group
                        
                        .. attribute:: qos_grp_val
                        
                        	qos group value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingQosGrpStatsVal, self).__init__()

                            self.yang_name = "marking-qos-grp-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('qos_grp_val', YLeaf(YType.uint32, 'qos-grp-val')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.qos_grp_val = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-qos-grp-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingQosGrpStatsVal, ['qos_grp_val', 'marked_pkts'], name, value)


                    class MarkingPrecStatsVal(Entity):
                        """
                        Statistics for set precedence
                        
                        .. attribute:: prec_val
                        
                        	precedence value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingPrecStatsVal, self).__init__()

                            self.yang_name = "marking-prec-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prec_val', YLeaf(YType.uint32, 'prec-val')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.prec_val = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-prec-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingPrecStatsVal, ['prec_val', 'marked_pkts'], name, value)


                    class MarkingPrecTunnelStatsVal(Entity):
                        """
                        Statistics for set precedence tunnel
                        
                        .. attribute:: prec_val
                        
                        	precedence value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingPrecTunnelStatsVal, self).__init__()

                            self.yang_name = "marking-prec-tunnel-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prec_val', YLeaf(YType.uint32, 'prec-val')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.prec_val = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-prec-tunnel-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingPrecTunnelStatsVal, ['prec_val', 'marked_pkts'], name, value)


                    class MarkingMplsExpImpStatsVal(Entity):
                        """
                        Statistics for set mpls exp imposition
                        
                        .. attribute:: mpls_exp_imp_val
                        
                        	mpls exp value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingMplsExpImpStatsVal, self).__init__()

                            self.yang_name = "marking-mpls-exp-imp-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mpls_exp_imp_val', YLeaf(YType.uint32, 'mpls-exp-imp-val')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.mpls_exp_imp_val = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-mpls-exp-imp-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingMplsExpImpStatsVal, ['mpls_exp_imp_val', 'marked_pkts'], name, value)


                    class MarkingMplsExpTopStatsVal(Entity):
                        """
                        Statistics for set mpls exp topmost
                        
                        .. attribute:: mpls_exp_top_val
                        
                        	mpls exp value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingMplsExpTopStatsVal, self).__init__()

                            self.yang_name = "marking-mpls-exp-top-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mpls_exp_top_val', YLeaf(YType.uint32, 'mpls-exp-top-val')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.mpls_exp_top_val = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-mpls-exp-top-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingMplsExpTopStatsVal, ['mpls_exp_top_val', 'marked_pkts'], name, value)


                    class MarkingFrDeStatsVal(Entity):
                        """
                        Statistics for set fr\-de
                        
                        .. attribute:: fr_de
                        
                        	fr de set or not
                        	**type**\: bool
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingFrDeStatsVal, self).__init__()

                            self.yang_name = "marking-fr-de-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('fr_de', YLeaf(YType.boolean, 'fr-de')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.fr_de = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-fr-de-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingFrDeStatsVal, ['fr_de', 'marked_pkts'], name, value)


                    class MarkingFrFecnBecnStatsVal(Entity):
                        """
                        Statistics for set fr\-fecn\-becn
                        
                        .. attribute:: fecn_becn_val
                        
                        	fecn becn value. qos\:percent\-value\-1to100
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingFrFecnBecnStatsVal, self).__init__()

                            self.yang_name = "marking-fr-fecn-becn-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('fecn_becn_val', YLeaf(YType.uint32, 'fecn-becn-val')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.fecn_becn_val = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-fr-fecn-becn-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingFrFecnBecnStatsVal, ['fecn_becn_val', 'marked_pkts'], name, value)


                    class MarkingAtmClpStatsVal(Entity):
                        """
                        Statistics for set atm\-clp
                        
                        .. attribute:: atm_clp_val
                        
                        	atm clp value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingAtmClpStatsVal, self).__init__()

                            self.yang_name = "marking-atm-clp-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('atm_clp_val', YLeaf(YType.uint8, 'atm-clp-val')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.atm_clp_val = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-atm-clp-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingAtmClpStatsVal, ['atm_clp_val', 'marked_pkts'], name, value)


                    class MarkingVlanInnerStatsVal(Entity):
                        """
                        Statistics for set vlan\-inner
                        
                        .. attribute:: vlan_inner_val
                        
                        	vlan value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingVlanInnerStatsVal, self).__init__()

                            self.yang_name = "marking-vlan-inner-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vlan_inner_val', YLeaf(YType.uint32, 'vlan-inner-val')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.vlan_inner_val = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-vlan-inner-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingVlanInnerStatsVal, ['vlan_inner_val', 'marked_pkts'], name, value)


                    class MarkingDeiStatsVal(Entity):
                        """
                        Statistics for set dei
                        
                        .. attribute:: dei_imp_value
                        
                        	dei value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDeiStatsVal, self).__init__()

                            self.yang_name = "marking-dei-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('dei_imp_value', YLeaf(YType.uint32, 'dei-imp-value')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.dei_imp_value = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-dei-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDeiStatsVal, ['dei_imp_value', 'marked_pkts'], name, value)


                    class MarkingDeiImpStatsVal(Entity):
                        """
                        Statistics for set dei\-imposition
                        
                        .. attribute:: dei_imp_value
                        
                        	dei value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDeiImpStatsVal, self).__init__()

                            self.yang_name = "marking-dei-imp-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('dei_imp_value', YLeaf(YType.uint32, 'dei-imp-value')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.dei_imp_value = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-dei-imp-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingDeiImpStatsVal, ['dei_imp_value', 'marked_pkts'], name, value)


                    class MarkingSrpPriorityStatsVal(Entity):
                        """
                        Statistics for set srp\-priority
                        
                        .. attribute:: srp_priority_value
                        
                        	srp priority value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingSrpPriorityStatsVal, self).__init__()

                            self.yang_name = "marking-srp-priority-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('srp_priority_value', YLeaf(YType.uint8, 'srp-priority-value')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.srp_priority_value = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-srp-priority-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingSrpPriorityStatsVal, ['srp_priority_value', 'marked_pkts'], name, value)


                    class MarkingWlanUserPriorityStatsVal(Entity):
                        """
                        Statistics for set wlan\-user\-priority
                        
                        .. attribute:: wlan_user_priority_value
                        
                        	wlan user priority value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: marked_pkts
                        
                        	Number of packets been marked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'interfaces-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingWlanUserPriorityStatsVal, self).__init__()

                            self.yang_name = "marking-wlan-user-priority-stats-val"
                            self.yang_parent_name = "marking-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('wlan_user_priority_value', YLeaf(YType.uint8, 'wlan-user-priority-value')),
                                ('marked_pkts', YLeaf(YType.uint64, 'marked-pkts')),
                            ])
                            self.wlan_user_priority_value = None
                            self.marked_pkts = None
                            self._segment_path = lambda: "marking-wlan-user-priority-stats-val"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.DiffservInfo.DiffservTargetClassifierStats.MarkingStats.MarkingWlanUserPriorityStatsVal, ['wlan_user_priority_value', 'marked_pkts'], name, value)


            class PriorityOperList(Entity):
                """
                Statistics for aggregrate priority per policy instance
                
                .. attribute:: priority_level  (key)
                
                	Priority Level, 0 means no priority level set
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: agg_priority_stats
                
                	Counters in aggregate priority
                	**type**\:  :py:class:`AggPriorityStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.PriorityOperList.AggPriorityStats>`
                
                .. attribute:: qlimit_default_thresh
                
                	qlimit default threshold
                	**type**\:  :py:class:`QlimitDefaultThresh <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDefaultThresh>`
                
                .. attribute:: qlimit_cos_thresh_list
                
                	cos\-based queue limit data
                	**type**\: list of  		 :py:class:`QlimitCosThreshList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitCosThreshList>`
                
                .. attribute:: qlimit_disc_class_thresh_list
                
                	discard\-class\-based queue limit data
                	**type**\: list of  		 :py:class:`QlimitDiscClassThreshList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDiscClassThreshList>`
                
                .. attribute:: qlimit_qos_grp_thresh_list
                
                	qos\-group\-based queue limit data
                	**type**\: list of  		 :py:class:`QlimitQosGrpThreshList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitQosGrpThreshList>`
                
                .. attribute:: qlimit_mpls_exp_thresh_list
                
                	mpls\-exp\-based queue limit data
                	**type**\: list of  		 :py:class:`QlimitMplsExpThreshList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitMplsExpThreshList>`
                
                .. attribute:: qlimit_dscp_thresh_list
                
                	queue limit per dscp range
                	**type**\: list of  		 :py:class:`QlimitDscpThreshList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDscpThreshList>`
                
                

                """

                _prefix = 'interfaces-ios-xe-oper'
                _revision = '2017-10-10'

                def __init__(self):
                    super(Interfaces.Interface.DiffservInfo.PriorityOperList, self).__init__()

                    self.yang_name = "priority-oper-list"
                    self.yang_parent_name = "diffserv-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['priority_level']
                    self._child_container_classes = OrderedDict([("agg-priority-stats", ("agg_priority_stats", Interfaces.Interface.DiffservInfo.PriorityOperList.AggPriorityStats)), ("qlimit-default-thresh", ("qlimit_default_thresh", Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDefaultThresh))])
                    self._child_list_classes = OrderedDict([("qlimit-cos-thresh-list", ("qlimit_cos_thresh_list", Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitCosThreshList)), ("qlimit-disc-class-thresh-list", ("qlimit_disc_class_thresh_list", Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDiscClassThreshList)), ("qlimit-qos-grp-thresh-list", ("qlimit_qos_grp_thresh_list", Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitQosGrpThreshList)), ("qlimit-mpls-exp-thresh-list", ("qlimit_mpls_exp_thresh_list", Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitMplsExpThreshList)), ("qlimit-dscp-thresh-list", ("qlimit_dscp_thresh_list", Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDscpThreshList))])
                    self._leafs = OrderedDict([
                        ('priority_level', YLeaf(YType.uint16, 'priority-level')),
                    ])
                    self.priority_level = None

                    self.agg_priority_stats = Interfaces.Interface.DiffservInfo.PriorityOperList.AggPriorityStats()
                    self.agg_priority_stats.parent = self
                    self._children_name_map["agg_priority_stats"] = "agg-priority-stats"
                    self._children_yang_names.add("agg-priority-stats")

                    self.qlimit_default_thresh = Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDefaultThresh()
                    self.qlimit_default_thresh.parent = self
                    self._children_name_map["qlimit_default_thresh"] = "qlimit-default-thresh"
                    self._children_yang_names.add("qlimit-default-thresh")

                    self.qlimit_cos_thresh_list = YList(self)
                    self.qlimit_disc_class_thresh_list = YList(self)
                    self.qlimit_qos_grp_thresh_list = YList(self)
                    self.qlimit_mpls_exp_thresh_list = YList(self)
                    self.qlimit_dscp_thresh_list = YList(self)
                    self._segment_path = lambda: "priority-oper-list" + "[priority-level='" + str(self.priority_level) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.DiffservInfo.PriorityOperList, ['priority_level'], name, value)


                class AggPriorityStats(Entity):
                    """
                    Counters in aggregate priority
                    
                    .. attribute:: output_pkts
                    
                    	Number of packets transmitted from queue
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_bytes
                    
                    	Number of bytes transmitted from queue
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: queue_size_pkts
                    
                    	Number of packets currently buffered
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: queue_size_bytes
                    
                    	Number of bytes currently buffered
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drop_pkts
                    
                    	Total number of packets dropped
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drop_bytes
                    
                    	Total number of bytes dropped
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drop_pkts_flow
                    
                    	Number of packets that were dropped by flow\-based fair\-queuing (fair\-queue). This is a sub\-set of drop\-pkts
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drop_pkts_no_buffer
                    
                    	Number of packets dropped due to buffers being unavailable system\-wide or at the associated interface. This is a sub\-set of drop\-pkts
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'interfaces-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(Interfaces.Interface.DiffservInfo.PriorityOperList.AggPriorityStats, self).__init__()

                        self.yang_name = "agg-priority-stats"
                        self.yang_parent_name = "priority-oper-list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('output_pkts', YLeaf(YType.uint64, 'output-pkts')),
                            ('output_bytes', YLeaf(YType.uint64, 'output-bytes')),
                            ('queue_size_pkts', YLeaf(YType.uint64, 'queue-size-pkts')),
                            ('queue_size_bytes', YLeaf(YType.uint64, 'queue-size-bytes')),
                            ('drop_pkts', YLeaf(YType.uint64, 'drop-pkts')),
                            ('drop_bytes', YLeaf(YType.uint64, 'drop-bytes')),
                            ('drop_pkts_flow', YLeaf(YType.uint64, 'drop-pkts-flow')),
                            ('drop_pkts_no_buffer', YLeaf(YType.uint64, 'drop-pkts-no-buffer')),
                        ])
                        self.output_pkts = None
                        self.output_bytes = None
                        self.queue_size_pkts = None
                        self.queue_size_bytes = None
                        self.drop_pkts = None
                        self.drop_bytes = None
                        self.drop_pkts_flow = None
                        self.drop_pkts_no_buffer = None
                        self._segment_path = lambda: "agg-priority-stats"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.DiffservInfo.PriorityOperList.AggPriorityStats, ['output_pkts', 'output_bytes', 'queue_size_pkts', 'queue_size_bytes', 'drop_pkts', 'drop_bytes', 'drop_pkts_flow', 'drop_pkts_no_buffer'], name, value)


                class QlimitDefaultThresh(Entity):
                    """
                    qlimit default threshold
                    
                    .. attribute:: bytes
                    
                    	Threshold bytes
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: thresh_size_metric
                    
                    	Threshold size unit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unit_val
                    
                    	Threshold size basic units
                    	**type**\:  :py:class:`ThreshUnit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.ThreshUnit>`
                    
                    .. attribute:: threshold_interval
                    
                    	Threshold interval
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: thresh_interval_metric
                    
                    	Threshold units metric
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interval_unit_val
                    
                    	Threshold intveral basic units
                    	**type**\:  :py:class:`ThreshUnit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.ThreshUnit>`
                    
                    

                    """

                    _prefix = 'interfaces-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDefaultThresh, self).__init__()

                        self.yang_name = "qlimit-default-thresh"
                        self.yang_parent_name = "priority-oper-list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('bytes', YLeaf(YType.uint64, 'bytes')),
                            ('thresh_size_metric', YLeaf(YType.uint32, 'thresh-size-metric')),
                            ('unit_val', YLeaf(YType.enumeration, 'unit-val')),
                            ('threshold_interval', YLeaf(YType.uint64, 'threshold-interval')),
                            ('thresh_interval_metric', YLeaf(YType.uint32, 'thresh-interval-metric')),
                            ('interval_unit_val', YLeaf(YType.enumeration, 'interval-unit-val')),
                        ])
                        self.bytes = None
                        self.thresh_size_metric = None
                        self.unit_val = None
                        self.threshold_interval = None
                        self.thresh_interval_metric = None
                        self.interval_unit_val = None
                        self._segment_path = lambda: "qlimit-default-thresh"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDefaultThresh, ['bytes', 'thresh_size_metric', 'unit_val', 'threshold_interval', 'thresh_interval_metric', 'interval_unit_val'], name, value)


                class QlimitCosThreshList(Entity):
                    """
                    cos\-based queue limit data
                    
                    .. attribute:: cos_min  (key)
                    
                    	Min COS value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cos_max  (key)
                    
                    	Max COS value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes
                    
                    	Threshold bytes
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: thresh_size_metric
                    
                    	Threshold size unit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unit_val
                    
                    	Threshold size basic units
                    	**type**\:  :py:class:`ThreshUnit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.ThreshUnit>`
                    
                    .. attribute:: threshold_interval
                    
                    	Threshold interval
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: thresh_interval_metric
                    
                    	Threshold units metric
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interval_unit_val
                    
                    	Threshold intveral basic units
                    	**type**\:  :py:class:`ThreshUnit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.ThreshUnit>`
                    
                    

                    """

                    _prefix = 'interfaces-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitCosThreshList, self).__init__()

                        self.yang_name = "qlimit-cos-thresh-list"
                        self.yang_parent_name = "priority-oper-list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['cos_min','cos_max']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('cos_min', YLeaf(YType.uint32, 'cos-min')),
                            ('cos_max', YLeaf(YType.uint32, 'cos-max')),
                            ('bytes', YLeaf(YType.uint64, 'bytes')),
                            ('thresh_size_metric', YLeaf(YType.uint32, 'thresh-size-metric')),
                            ('unit_val', YLeaf(YType.enumeration, 'unit-val')),
                            ('threshold_interval', YLeaf(YType.uint64, 'threshold-interval')),
                            ('thresh_interval_metric', YLeaf(YType.uint32, 'thresh-interval-metric')),
                            ('interval_unit_val', YLeaf(YType.enumeration, 'interval-unit-val')),
                        ])
                        self.cos_min = None
                        self.cos_max = None
                        self.bytes = None
                        self.thresh_size_metric = None
                        self.unit_val = None
                        self.threshold_interval = None
                        self.thresh_interval_metric = None
                        self.interval_unit_val = None
                        self._segment_path = lambda: "qlimit-cos-thresh-list" + "[cos-min='" + str(self.cos_min) + "']" + "[cos-max='" + str(self.cos_max) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitCosThreshList, ['cos_min', 'cos_max', 'bytes', 'thresh_size_metric', 'unit_val', 'threshold_interval', 'thresh_interval_metric', 'interval_unit_val'], name, value)


                class QlimitDiscClassThreshList(Entity):
                    """
                    discard\-class\-based queue limit data
                    
                    .. attribute:: disc_class_min  (key)
                    
                    	Minimum value for discard class in the range
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: disc_class_max  (key)
                    
                    	Maximum value for discard class in the range
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes
                    
                    	Threshold bytes
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: thresh_size_metric
                    
                    	Threshold size unit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unit_val
                    
                    	Threshold size basic units
                    	**type**\:  :py:class:`ThreshUnit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.ThreshUnit>`
                    
                    .. attribute:: threshold_interval
                    
                    	Threshold interval
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: thresh_interval_metric
                    
                    	Threshold units metric
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interval_unit_val
                    
                    	Threshold intveral basic units
                    	**type**\:  :py:class:`ThreshUnit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.ThreshUnit>`
                    
                    

                    """

                    _prefix = 'interfaces-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDiscClassThreshList, self).__init__()

                        self.yang_name = "qlimit-disc-class-thresh-list"
                        self.yang_parent_name = "priority-oper-list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['disc_class_min','disc_class_max']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('disc_class_min', YLeaf(YType.uint32, 'disc-class-min')),
                            ('disc_class_max', YLeaf(YType.uint32, 'disc-class-max')),
                            ('bytes', YLeaf(YType.uint64, 'bytes')),
                            ('thresh_size_metric', YLeaf(YType.uint32, 'thresh-size-metric')),
                            ('unit_val', YLeaf(YType.enumeration, 'unit-val')),
                            ('threshold_interval', YLeaf(YType.uint64, 'threshold-interval')),
                            ('thresh_interval_metric', YLeaf(YType.uint32, 'thresh-interval-metric')),
                            ('interval_unit_val', YLeaf(YType.enumeration, 'interval-unit-val')),
                        ])
                        self.disc_class_min = None
                        self.disc_class_max = None
                        self.bytes = None
                        self.thresh_size_metric = None
                        self.unit_val = None
                        self.threshold_interval = None
                        self.thresh_interval_metric = None
                        self.interval_unit_val = None
                        self._segment_path = lambda: "qlimit-disc-class-thresh-list" + "[disc-class-min='" + str(self.disc_class_min) + "']" + "[disc-class-max='" + str(self.disc_class_max) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDiscClassThreshList, ['disc_class_min', 'disc_class_max', 'bytes', 'thresh_size_metric', 'unit_val', 'threshold_interval', 'thresh_interval_metric', 'interval_unit_val'], name, value)


                class QlimitQosGrpThreshList(Entity):
                    """
                    qos\-group\-based queue limit data
                    
                    .. attribute:: qos_group_min  (key)
                    
                    	Specifies the minimum value range from 0 to used to identify a QoS group value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: qos_group_max  (key)
                    
                    	Specifies the maximum value range from 0 to used to identify a QoS group value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes
                    
                    	Threshold bytes
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: thresh_size_metric
                    
                    	Threshold size unit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unit_val
                    
                    	Threshold size basic units
                    	**type**\:  :py:class:`ThreshUnit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.ThreshUnit>`
                    
                    .. attribute:: threshold_interval
                    
                    	Threshold interval
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: thresh_interval_metric
                    
                    	Threshold units metric
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interval_unit_val
                    
                    	Threshold intveral basic units
                    	**type**\:  :py:class:`ThreshUnit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.ThreshUnit>`
                    
                    

                    """

                    _prefix = 'interfaces-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitQosGrpThreshList, self).__init__()

                        self.yang_name = "qlimit-qos-grp-thresh-list"
                        self.yang_parent_name = "priority-oper-list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['qos_group_min','qos_group_max']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('qos_group_min', YLeaf(YType.uint32, 'qos-group-min')),
                            ('qos_group_max', YLeaf(YType.uint32, 'qos-group-max')),
                            ('bytes', YLeaf(YType.uint64, 'bytes')),
                            ('thresh_size_metric', YLeaf(YType.uint32, 'thresh-size-metric')),
                            ('unit_val', YLeaf(YType.enumeration, 'unit-val')),
                            ('threshold_interval', YLeaf(YType.uint64, 'threshold-interval')),
                            ('thresh_interval_metric', YLeaf(YType.uint32, 'thresh-interval-metric')),
                            ('interval_unit_val', YLeaf(YType.enumeration, 'interval-unit-val')),
                        ])
                        self.qos_group_min = None
                        self.qos_group_max = None
                        self.bytes = None
                        self.thresh_size_metric = None
                        self.unit_val = None
                        self.threshold_interval = None
                        self.thresh_interval_metric = None
                        self.interval_unit_val = None
                        self._segment_path = lambda: "qlimit-qos-grp-thresh-list" + "[qos-group-min='" + str(self.qos_group_min) + "']" + "[qos-group-max='" + str(self.qos_group_max) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitQosGrpThreshList, ['qos_group_min', 'qos_group_max', 'bytes', 'thresh_size_metric', 'unit_val', 'threshold_interval', 'thresh_interval_metric', 'interval_unit_val'], name, value)


                class QlimitMplsExpThreshList(Entity):
                    """
                    mpls\-exp\-based queue limit data
                    
                    .. attribute:: exp_min  (key)
                    
                    	The minimum EXP field value to be used as match criteria. Any number from 0 to 7
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: exp_max  (key)
                    
                    	The maximum EXP field value to be used as match criteria. Any number from 0 to 7
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes
                    
                    	Threshold bytes
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: thresh_size_metric
                    
                    	Threshold size unit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unit_val
                    
                    	Threshold size basic units
                    	**type**\:  :py:class:`ThreshUnit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.ThreshUnit>`
                    
                    .. attribute:: threshold_interval
                    
                    	Threshold interval
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: thresh_interval_metric
                    
                    	Threshold units metric
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interval_unit_val
                    
                    	Threshold intveral basic units
                    	**type**\:  :py:class:`ThreshUnit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.ThreshUnit>`
                    
                    

                    """

                    _prefix = 'interfaces-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitMplsExpThreshList, self).__init__()

                        self.yang_name = "qlimit-mpls-exp-thresh-list"
                        self.yang_parent_name = "priority-oper-list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['exp_min','exp_max']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('exp_min', YLeaf(YType.uint32, 'exp-min')),
                            ('exp_max', YLeaf(YType.uint32, 'exp-max')),
                            ('bytes', YLeaf(YType.uint64, 'bytes')),
                            ('thresh_size_metric', YLeaf(YType.uint32, 'thresh-size-metric')),
                            ('unit_val', YLeaf(YType.enumeration, 'unit-val')),
                            ('threshold_interval', YLeaf(YType.uint64, 'threshold-interval')),
                            ('thresh_interval_metric', YLeaf(YType.uint32, 'thresh-interval-metric')),
                            ('interval_unit_val', YLeaf(YType.enumeration, 'interval-unit-val')),
                        ])
                        self.exp_min = None
                        self.exp_max = None
                        self.bytes = None
                        self.thresh_size_metric = None
                        self.unit_val = None
                        self.threshold_interval = None
                        self.thresh_interval_metric = None
                        self.interval_unit_val = None
                        self._segment_path = lambda: "qlimit-mpls-exp-thresh-list" + "[exp-min='" + str(self.exp_min) + "']" + "[exp-max='" + str(self.exp_max) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitMplsExpThreshList, ['exp_min', 'exp_max', 'bytes', 'thresh_size_metric', 'unit_val', 'threshold_interval', 'thresh_interval_metric', 'interval_unit_val'], name, value)


                class QlimitDscpThreshList(Entity):
                    """
                    queue limit per dscp range
                    
                    .. attribute:: dscp_min  (key)
                    
                    	Minimum of dscp range
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dscp_max  (key)
                    
                    	Maximum of dscp range
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes
                    
                    	Threshold bytes
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: thresh_size_metric
                    
                    	Threshold size unit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unit_val
                    
                    	Threshold size basic units
                    	**type**\:  :py:class:`ThreshUnit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.ThreshUnit>`
                    
                    .. attribute:: threshold_interval
                    
                    	Threshold interval
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: thresh_interval_metric
                    
                    	Threshold units metric
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interval_unit_val
                    
                    	Threshold intveral basic units
                    	**type**\:  :py:class:`ThreshUnit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.ThreshUnit>`
                    
                    

                    """

                    _prefix = 'interfaces-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDscpThreshList, self).__init__()

                        self.yang_name = "qlimit-dscp-thresh-list"
                        self.yang_parent_name = "priority-oper-list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['dscp_min','dscp_max']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('dscp_min', YLeaf(YType.uint32, 'dscp-min')),
                            ('dscp_max', YLeaf(YType.uint32, 'dscp-max')),
                            ('bytes', YLeaf(YType.uint64, 'bytes')),
                            ('thresh_size_metric', YLeaf(YType.uint32, 'thresh-size-metric')),
                            ('unit_val', YLeaf(YType.enumeration, 'unit-val')),
                            ('threshold_interval', YLeaf(YType.uint64, 'threshold-interval')),
                            ('thresh_interval_metric', YLeaf(YType.uint32, 'thresh-interval-metric')),
                            ('interval_unit_val', YLeaf(YType.enumeration, 'interval-unit-val')),
                        ])
                        self.dscp_min = None
                        self.dscp_max = None
                        self.bytes = None
                        self.thresh_size_metric = None
                        self.unit_val = None
                        self.threshold_interval = None
                        self.thresh_interval_metric = None
                        self.interval_unit_val = None
                        self._segment_path = lambda: "qlimit-dscp-thresh-list" + "[dscp-min='" + str(self.dscp_min) + "']" + "[dscp-max='" + str(self.dscp_max) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.DiffservInfo.PriorityOperList.QlimitDscpThreshList, ['dscp_min', 'dscp_max', 'bytes', 'thresh_size_metric', 'unit_val', 'threshold_interval', 'thresh_interval_metric', 'interval_unit_val'], name, value)


        class V4ProtocolStats(Entity):
            """
            IPv4 traffic statistics for this interface
            
            .. attribute:: in_pkts
            
            	The total number of packets received for the specified address family, including those received in error
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_octets
            
            	The total number of octets received in input packets for the specified address family, including those received in error
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_error_pkts
            
            	Number of packets discarded due to errors for the specified address family, including errors in the header, no route found to the destination, invalid address, unknown protocol, etc
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_forwarded_pkts
            
            	The number of input packets for which the device was not their final destination and for which the device attempted to find a route to forward them to that final destination
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_forwarded_octets
            
            	The number of octets received in input packets for the specified address family for which the device was not their final lodestination and for which the device attempted to find a route to forward them to that final destination
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_discarded_pkts
            
            	The number of input IP packets for the specified address family, for which no problems were encountered to prevent their continued processing, but were discarded (e.g., for lack of buffer space)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_pkts
            
            	The total number of IP packets for the specified address family that the device supplied to the lower layers for transmission.  This includes packets generated locally and those forwarded by the device
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_octets
            
            	The total number of octets in IP packets for the specified address family that the device supplied to the lower layers for transmission.  This includes packets generated locally and those forwarded by the device
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_error_pkts
            
            	Number of IP packets for the specified address family locally generated and discarded due to errors, including no route found to the IP destination
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_forwarded_pkts
            
            	The number of packets for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.text
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_forwarded_octets
            
            	The number of octets in packets for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_discarded_pkts
            
            	The number of output IP packets for the specified address family for which no problem was encountered to prevent their transmission to their destination, but were discarded (e.g., for lack of buffer space)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'interfaces-ios-xe-oper'
            _revision = '2017-10-10'

            def __init__(self):
                super(Interfaces.Interface.V4ProtocolStats, self).__init__()

                self.yang_name = "v4-protocol-stats"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('in_pkts', YLeaf(YType.uint64, 'in-pkts')),
                    ('in_octets', YLeaf(YType.uint64, 'in-octets')),
                    ('in_error_pkts', YLeaf(YType.uint64, 'in-error-pkts')),
                    ('in_forwarded_pkts', YLeaf(YType.uint64, 'in-forwarded-pkts')),
                    ('in_forwarded_octets', YLeaf(YType.uint64, 'in-forwarded-octets')),
                    ('in_discarded_pkts', YLeaf(YType.uint64, 'in-discarded-pkts')),
                    ('out_pkts', YLeaf(YType.uint64, 'out-pkts')),
                    ('out_octets', YLeaf(YType.uint64, 'out-octets')),
                    ('out_error_pkts', YLeaf(YType.uint64, 'out-error-pkts')),
                    ('out_forwarded_pkts', YLeaf(YType.uint64, 'out-forwarded-pkts')),
                    ('out_forwarded_octets', YLeaf(YType.uint64, 'out-forwarded-octets')),
                    ('out_discarded_pkts', YLeaf(YType.uint64, 'out-discarded-pkts')),
                ])
                self.in_pkts = None
                self.in_octets = None
                self.in_error_pkts = None
                self.in_forwarded_pkts = None
                self.in_forwarded_octets = None
                self.in_discarded_pkts = None
                self.out_pkts = None
                self.out_octets = None
                self.out_error_pkts = None
                self.out_forwarded_pkts = None
                self.out_forwarded_octets = None
                self.out_discarded_pkts = None
                self._segment_path = lambda: "v4-protocol-stats"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.V4ProtocolStats, ['in_pkts', 'in_octets', 'in_error_pkts', 'in_forwarded_pkts', 'in_forwarded_octets', 'in_discarded_pkts', 'out_pkts', 'out_octets', 'out_error_pkts', 'out_forwarded_pkts', 'out_forwarded_octets', 'out_discarded_pkts'], name, value)


        class V6ProtocolStats(Entity):
            """
            IPv6 traffic statistics for this interface
            
            .. attribute:: in_pkts
            
            	The total number of packets received for the specified address family, including those received in error
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_octets
            
            	The total number of octets received in input packets for the specified address family, including those received in error
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_error_pkts
            
            	Number of packets discarded due to errors for the specified address family, including errors in the header, no route found to the destination, invalid address, unknown protocol, etc
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_forwarded_pkts
            
            	The number of input packets for which the device was not their final destination and for which the device attempted to find a route to forward them to that final destination
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_forwarded_octets
            
            	The number of octets received in input packets for the specified address family for which the device was not their final lodestination and for which the device attempted to find a route to forward them to that final destination
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_discarded_pkts
            
            	The number of input IP packets for the specified address family, for which no problems were encountered to prevent their continued processing, but were discarded (e.g., for lack of buffer space)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_pkts
            
            	The total number of IP packets for the specified address family that the device supplied to the lower layers for transmission.  This includes packets generated locally and those forwarded by the device
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_octets
            
            	The total number of octets in IP packets for the specified address family that the device supplied to the lower layers for transmission.  This includes packets generated locally and those forwarded by the device
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_error_pkts
            
            	Number of IP packets for the specified address family locally generated and discarded due to errors, including no route found to the IP destination
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_forwarded_pkts
            
            	The number of packets for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.text
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_forwarded_octets
            
            	The number of octets in packets for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_discarded_pkts
            
            	The number of output IP packets for the specified address family for which no problem was encountered to prevent their transmission to their destination, but were discarded (e.g., for lack of buffer space)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'interfaces-ios-xe-oper'
            _revision = '2017-10-10'

            def __init__(self):
                super(Interfaces.Interface.V6ProtocolStats, self).__init__()

                self.yang_name = "v6-protocol-stats"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('in_pkts', YLeaf(YType.uint64, 'in-pkts')),
                    ('in_octets', YLeaf(YType.uint64, 'in-octets')),
                    ('in_error_pkts', YLeaf(YType.uint64, 'in-error-pkts')),
                    ('in_forwarded_pkts', YLeaf(YType.uint64, 'in-forwarded-pkts')),
                    ('in_forwarded_octets', YLeaf(YType.uint64, 'in-forwarded-octets')),
                    ('in_discarded_pkts', YLeaf(YType.uint64, 'in-discarded-pkts')),
                    ('out_pkts', YLeaf(YType.uint64, 'out-pkts')),
                    ('out_octets', YLeaf(YType.uint64, 'out-octets')),
                    ('out_error_pkts', YLeaf(YType.uint64, 'out-error-pkts')),
                    ('out_forwarded_pkts', YLeaf(YType.uint64, 'out-forwarded-pkts')),
                    ('out_forwarded_octets', YLeaf(YType.uint64, 'out-forwarded-octets')),
                    ('out_discarded_pkts', YLeaf(YType.uint64, 'out-discarded-pkts')),
                ])
                self.in_pkts = None
                self.in_octets = None
                self.in_error_pkts = None
                self.in_forwarded_pkts = None
                self.in_forwarded_octets = None
                self.in_discarded_pkts = None
                self.out_pkts = None
                self.out_octets = None
                self.out_error_pkts = None
                self.out_forwarded_pkts = None
                self.out_forwarded_octets = None
                self.out_discarded_pkts = None
                self._segment_path = lambda: "v6-protocol-stats"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.V6ProtocolStats, ['in_pkts', 'in_octets', 'in_error_pkts', 'in_forwarded_pkts', 'in_forwarded_octets', 'in_discarded_pkts', 'out_pkts', 'out_octets', 'out_error_pkts', 'out_forwarded_pkts', 'out_forwarded_octets', 'out_discarded_pkts'], name, value)


        class EtherState(Entity):
            """
            The Ethernet state information
            
            .. attribute:: negotiated_duplex_mode
            
            	When auto\-negotiate is set to TRUE, and the  interface has completed auto\-negotiation with the  remote peer, this value shows the duplex mode that  has been negotiated
            	**type**\:  :py:class:`EtherDuplex <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.EtherDuplex>`
            
            .. attribute:: negotiated_port_speed
            
            	When auto\-negotiate is set to TRUE, and  the interface has completed auto\-negotiation with  the remote peer, this value shows the interface  speed that has been negotiated
            	**type**\:  :py:class:`EtherSpeed <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.EtherSpeed>`
            
            .. attribute:: auto_negotiate
            
            	Set to TRUE to request the interface to  auto\-negotiate transmission parameters with its  peer interface. When set to FALSE, the transmission parameters are specified manually
            	**type**\: bool
            
            .. attribute:: enable_flow_control
            
            	Enable or disable flow control for this  interface. Ethernet flow control is a mechanism by  which a receiver may send PAUSE frames to a sender to stop transmission for a specified time.  This setting should override auto\-negotiated flow  control settings. If left unspecified, and  auto\-negotiate is TRUE, flow control mode is  negotiated with the peer interface
            	**type**\: bool
            
            

            """

            _prefix = 'interfaces-ios-xe-oper'
            _revision = '2017-10-10'

            def __init__(self):
                super(Interfaces.Interface.EtherState, self).__init__()

                self.yang_name = "ether-state"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('negotiated_duplex_mode', YLeaf(YType.enumeration, 'negotiated-duplex-mode')),
                    ('negotiated_port_speed', YLeaf(YType.enumeration, 'negotiated-port-speed')),
                    ('auto_negotiate', YLeaf(YType.boolean, 'auto-negotiate')),
                    ('enable_flow_control', YLeaf(YType.boolean, 'enable-flow-control')),
                ])
                self.negotiated_duplex_mode = None
                self.negotiated_port_speed = None
                self.auto_negotiate = None
                self.enable_flow_control = None
                self._segment_path = lambda: "ether-state"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.EtherState, ['negotiated_duplex_mode', 'negotiated_port_speed', 'auto_negotiate', 'enable_flow_control'], name, value)


        class EtherStats(Entity):
            """
            The Ethernet statistics
            
            .. attribute:: in_mac_control_frames
            
            	MAC layer control frames received on the interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_mac_pause_frames
            
            	MAC layer PAUSE frames received on the interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_oversize_frames
            
            	Number of oversize frames received on the interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_jabber_frames
            
            	Number of jabber frames received on the interface.  Jabber frames are typically defined as oversize frames which also have a bad CRC.  Implementations may use slightly different definitions of what constitutes a jabber frame.  Often indicative of a NIC hardware problem
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_fragment_frames
            
            	Number of fragment frames received on the interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_8021q_frames
            
            	Number of 802.1q tagged frames received on the interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_mac_control_frames
            
            	MAC layer control frames sent on the interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_mac_pause_frames
            
            	MAC layer PAUSE frames sent on the interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_8021q_frames
            
            	Number of 802.1q tagged frames sent on the interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'interfaces-ios-xe-oper'
            _revision = '2017-10-10'

            def __init__(self):
                super(Interfaces.Interface.EtherStats, self).__init__()

                self.yang_name = "ether-stats"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('in_mac_control_frames', YLeaf(YType.uint64, 'in-mac-control-frames')),
                    ('in_mac_pause_frames', YLeaf(YType.uint64, 'in-mac-pause-frames')),
                    ('in_oversize_frames', YLeaf(YType.uint64, 'in-oversize-frames')),
                    ('in_jabber_frames', YLeaf(YType.uint64, 'in-jabber-frames')),
                    ('in_fragment_frames', YLeaf(YType.uint64, 'in-fragment-frames')),
                    ('in_8021q_frames', YLeaf(YType.uint64, 'in-8021q-frames')),
                    ('out_mac_control_frames', YLeaf(YType.uint64, 'out-mac-control-frames')),
                    ('out_mac_pause_frames', YLeaf(YType.uint64, 'out-mac-pause-frames')),
                    ('out_8021q_frames', YLeaf(YType.uint64, 'out-8021q-frames')),
                ])
                self.in_mac_control_frames = None
                self.in_mac_pause_frames = None
                self.in_oversize_frames = None
                self.in_jabber_frames = None
                self.in_fragment_frames = None
                self.in_8021q_frames = None
                self.out_mac_control_frames = None
                self.out_mac_pause_frames = None
                self.out_8021q_frames = None
                self._segment_path = lambda: "ether-stats"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.EtherStats, ['in_mac_control_frames', 'in_mac_pause_frames', 'in_oversize_frames', 'in_jabber_frames', 'in_fragment_frames', 'in_8021q_frames', 'out_mac_control_frames', 'out_mac_pause_frames', 'out_8021q_frames'], name, value)


        class SerialState(Entity):
            """
            The T1E1 serial state information
            
            .. attribute:: crc_type
            
            	Cyclic Redundancy Code type configured on the interface
            	**type**\:  :py:class:`SerialCrc <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.SerialCrc>`
            
            .. attribute:: loopback
            
            	Loopback mode the interface is operating in
            	**type**\:  :py:class:`T1E1LoopbackMode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.T1E1LoopbackMode>`
            
            .. attribute:: keeplive
            
            	Keeplive interval in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: timeslot
            
            	Time slots bitmap occupied by this serial interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: subrate
            
            	Subrate operating per slot
            	**type**\:  :py:class:`SubrateSpeed <ydk.models.cisco_ios_xe.Cisco_IOS_XE_interfaces_oper.SubrateSpeed>`
            
            

            """

            _prefix = 'interfaces-ios-xe-oper'
            _revision = '2017-10-10'

            def __init__(self):
                super(Interfaces.Interface.SerialState, self).__init__()

                self.yang_name = "serial-state"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('crc_type', YLeaf(YType.enumeration, 'crc-type')),
                    ('loopback', YLeaf(YType.enumeration, 'loopback')),
                    ('keeplive', YLeaf(YType.uint32, 'keeplive')),
                    ('timeslot', YLeaf(YType.uint32, 'timeslot')),
                    ('subrate', YLeaf(YType.enumeration, 'subrate')),
                ])
                self.crc_type = None
                self.loopback = None
                self.keeplive = None
                self.timeslot = None
                self.subrate = None
                self._segment_path = lambda: "serial-state"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.SerialState, ['crc_type', 'loopback', 'keeplive', 'timeslot', 'subrate'], name, value)


        class SerialStats(Entity):
            """
            The T1E1 statistics
            
            .. attribute:: in_abort_clock_error
            
            	Number of receive abort packets due to clock slides
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'interfaces-ios-xe-oper'
            _revision = '2017-10-10'

            def __init__(self):
                super(Interfaces.Interface.SerialStats, self).__init__()

                self.yang_name = "serial-stats"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('in_abort_clock_error', YLeaf(YType.uint32, 'in-abort-clock-error')),
                ])
                self.in_abort_clock_error = None
                self._segment_path = lambda: "serial-stats"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.SerialStats, ['in_abort_clock_error'], name, value)

    def clone_ptr(self):
        self._top_entity = Interfaces()
        return self._top_entity

