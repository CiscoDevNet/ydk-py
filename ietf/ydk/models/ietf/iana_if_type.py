""" iana_if_type 

This YANG module defines YANG identities for IANA\-registered
interface types.

This YANG module is maintained by IANA and reflects the
'ifType definitions' registry.

The latest revision of this YANG module can be obtained from
the IANA web site.

Requests for new values should be made to IANA via
email (iana@iana.org).

Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

The initial version of this YANG module is part of RFC 7224;
see the RFC itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IanaInterfaceType(Identity):
    """
    This identity is used as a base for all interface types
    defined in the 'ifType definitions' registry.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(IanaInterfaceType, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iana-interface-type")


class VoiceFXO(Identity):
    """
    Voice Foreign Exchange Office.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceFXO, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceFXO")


class AtmVciEndPt(Identity):
    """
    ATM VCI End Point.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AtmVciEndPt, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmVciEndPt")


class PropBWAp2Mp(Identity):
    """
    PropBroadbandWirelessAccesspt2Multipt (use of this value
    for IEEE 802.16 WMAN interfaces as per IEEE Std 802.16f
    is deprecated, and ieee80216WMAN(237) should be used
    instead).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PropBWAp2Mp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propBWAp2Mp")


class PropDocsWirelessDownstream(Identity):
    """
    Cisco proprietary Downstream.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PropDocsWirelessDownstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propDocsWirelessDownstream")


class V11(Identity):
    """
    CCITT V.11/X.21.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(V11, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:v11")


class SoftwareLoopback(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(SoftwareLoopback, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:softwareLoopback")


class Hdlc(Identity):
    """
    HDLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hdlc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hdlc")


class VoiceFGDOS(Identity):
    """
    Voice FGD Operator Services.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceFGDOS, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceFGDOS")


class FastEtherFX(Identity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(FastEtherFX, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:fastEtherFX")


class DvbTdm(Identity):
    """
    DVB Satellite TDM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DvbTdm, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbTdm")


class Nfas(Identity):
    """
    Non\-Facility Associated Signaling.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Nfas, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:nfas")


class IfPwType(Identity):
    """
    Pseudowire interface type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(IfPwType, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ifPwType")


class L2vlan(Identity):
    """
    Layer 2 Virtual LAN using 802.1Q.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(L2vlan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:l2vlan")


class Adsl2plus(Identity):
    """
    Asymmetric Digital Subscriber Loop Version 2 \-
    Version 2 Plus and all variants.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Adsl2plus, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:adsl2plus")


class Ieee802154(Identity):
    """
    IEEE 802.15.4 WPAN interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ieee802154, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ieee802154")


class VoiceFXS(Identity):
    """
    Voice Foreign Exchange Station.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceFXS, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceFXS")


class DvbRcsMacLayer(Identity):
    """
    DVB\-RCS MAC Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DvbRcsMacLayer, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbRcsMacLayer")


class Idsl(Identity):
    """
    Digital Subscriber Loop over ISDN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Idsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:idsl")


class Infiniband(Identity):
    """
    Infiniband.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Infiniband, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:infiniband")


class DdnX25(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DdnX25, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ddnX25")


class WwanPP2(Identity):
    """
    3GPP2 WWAN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(WwanPP2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:wwanPP2")


class DocsCableUpstream(Identity):
    """
    CATV Upstream interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DocsCableUpstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:docsCableUpstream")


class Ethernet3Mbit(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ethernet3Mbit, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ethernet3Mbit")


class DigitalPowerline(Identity):
    """
    IP over Power Lines.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DigitalPowerline, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:digitalPowerline")


class H323Proxy(Identity):
    """
    H323 Voice and Video Proxy.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(H323Proxy, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:h323Proxy")


class Gtp(Identity):
    """
    GTP (GPRS Tunneling Protocol).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Gtp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:gtp")


class IpOverAtm(Identity):
    """
    IBM ipOverAtm.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(IpOverAtm, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ipOverAtm")


class AluEpon(Identity):
    """
    Ethernet Passive Optical Networks (E\-PON).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AluEpon, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluEpon")


class Imt(Identity):
    """
    Inter\-Machine Trunks.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Imt, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:imt")


class IpSwitch(Identity):
    """
    IP Switching Objects.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(IpSwitch, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ipSwitch")


class Msdsl(Identity):
    """
    Multi\-rate Symmetric DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Msdsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:msdsl")


class DvbRccMacLayer(Identity):
    """
    DVB\-RCC MAC Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DvbRccMacLayer, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbRccMacLayer")


class SmdsDxi(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(SmdsDxi, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:smdsDxi")


class VoiceOverAtm(Identity):
    """
    Voice over ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceOverAtm, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceOverAtm")


class Arap(Identity):
    """
    Appletalk Remote Access Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Arap, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:arap")


class FastEther(Identity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(FastEther, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:fastEther")


class Mpc(Identity):
    """
    IBM multi\-protocol channel support.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Mpc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mpc")


class Linegroup(Identity):
    """
    Interface common to multiple lines.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Linegroup, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:linegroup")


class Hippi(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hippi, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hippi")


class Rpr(Identity):
    """
    Resilient Packet Ring Interface Type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Rpr, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:rpr")


class Ds1FDL(Identity):
    """
    Facility Data Link (4Kbps) on a DS1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ds1FDL, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ds1FDL")


class SonetVT(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(SonetVT, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sonetVT")


class VoiceEncap(Identity):
    """
    Voice encapsulation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceEncap, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceEncap")


class Ss7SigLink(Identity):
    """
    SS7 Signaling Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ss7SigLink, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ss7SigLink")


class Arcnet(Identity):
    """
    ARCnet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Arcnet, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:arcnet")


class ActelisMetaLOOP(Identity):
    """
    Acteleis proprietary MetaLOOP High Speed Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(ActelisMetaLOOP, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:actelisMetaLOOP")


class Qllc(Identity):
    """
    SNA QLLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Qllc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:qllc")


class Rfc877x25(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Rfc877x25, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:rfc877x25")


class MpegTransport(Identity):
    """
    MPEG transport interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(MpegTransport, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mpegTransport")


class X25mlp(Identity):
    """
    Multi\-Link Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(X25mlp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:x25mlp")


class VirtualTg(Identity):
    """
    Virtual Trunk Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VirtualTg, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:virtualTg")


class HostPad(Identity):
    """
    CCITT\-ITU X.29 PAD Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(HostPad, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hostPad")


class StarLan(Identity):
    """
    Deprecated via RFC 3635.
    Use ethernetCsmacd(6) instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(StarLan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:starLan")


class Iso88025Dtr(Identity):
    """
    ISO 802.5r DTR.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88025Dtr, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88025Dtr")


class Ibm370parChan(Identity):
    """
    IBM System 360/370 OEMI Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ibm370parChan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ibm370parChan")


class Adsl2(Identity):
    """
    Asymmetric Digital Subscriber Loop Version 2
    (DEPRECATED/OBSOLETED \- please use adsl2plus(238)
    instead).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Adsl2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:adsl2")


class OtnOtu(Identity):
    """
    OTN Optical channel Transport Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(OtnOtu, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:otnOtu")


class PropWirelessP2P(Identity):
    """
    Prop. P2P wireless interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PropWirelessP2P, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propWirelessP2P")


class Interleave(Identity):
    """
    Interleave channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Interleave, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:interleave")


class Isup(Identity):
    """
    ISUP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Isup, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:isup")


class Regular1822(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Regular1822, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:regular1822")


class Gr303RDT(Identity):
    """
    Remote Digital Terminal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Gr303RDT, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:gr303RDT")


class PropDocsWirelessMaclayer(Identity):
    """
    Cisco proprietary Maclayer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PropDocsWirelessMaclayer, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propDocsWirelessMaclayer")


class Async(Identity):
    """
    Asynchronous Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Async, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:async")


class RadioMAC(Identity):
    """
    MAC layer over radio links.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(RadioMAC, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:radioMAC")


class OpticalChannelGroup(Identity):
    """
    Optical Channel Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(OpticalChannelGroup, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:opticalChannelGroup")


class SixToFour(Identity):
    """
    6to4 interface (DEPRECATED).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(SixToFour, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sixToFour")


class PropDocsWirelessUpstream(Identity):
    """
    Cisco proprietary Upstream.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PropDocsWirelessUpstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propDocsWirelessUpstream")


class Q2931(Identity):
    """
    Q.2931.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Q2931, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:q2931")


class Fddi(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Fddi, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:fddi")


class PropCnls(Identity):
    """
    Proprietary Connectionless Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PropCnls, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propCnls")


class Aal2(Identity):
    """
    ATM adaptation layer 2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Aal2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aal2")


class DvbAsiOut(Identity):
    """
    DVB\-ASI Output.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DvbAsiOut, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbAsiOut")


class AluELP(Identity):
    """
    Alcatel\-Lucent Ethernet Link Protection.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AluELP, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluELP")


class CiscoISLvlan(Identity):
    """
    Layer 2 Virtual LAN using Cisco ISL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(CiscoISLvlan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ciscoISLvlan")


class DocsCableUpstreamRfPort(Identity):
    """
    DOCSIS CATV Upstream RF Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DocsCableUpstreamRfPort, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:docsCableUpstreamRfPort")


class Aal5(Identity):
    """
    AAL5 over ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Aal5, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aal5")


class FrDlciEndPt(Identity):
    """
    Frame Relay DLCI End Point.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(FrDlciEndPt, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frDlciEndPt")


class HippiInterface(Identity):
    """
    HIPPI interfaces.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(HippiInterface, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hippiInterface")


class L3ipvlan(Identity):
    """
    Layer 3 Virtual LAN using IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(L3ipvlan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:l3ipvlan")


class Miox25(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Miox25, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:miox25")


class Hssi(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hssi, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hssi")


class AtmVirtual(Identity):
    """
    ATM Virtual Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AtmVirtual, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmVirtual")


class AluGponOnu(Identity):
    """
    GPON Optical Network Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AluGponOnu, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluGponOnu")


class Rfc1483(Identity):
    """
    Multiprotocol over ATM AAL5.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Rfc1483, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:rfc1483")


class Cnr(Identity):
    """
    Combat Net Radio.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Cnr, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:cnr")


class SipSig(Identity):
    """
    SIP Signaling.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(SipSig, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sipSig")


class Myrinet(Identity):
    """
    Myricom Myrinet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Myrinet, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:myrinet")


class Dlsw(Identity):
    """
    Data Link Switching.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dlsw, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dlsw")


class GigabitEthernet(Identity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(GigabitEthernet, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:gigabitEthernet")


class X25ple(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(X25ple, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:x25ple")


class Lmp(Identity):
    """
    Link Management Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Lmp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:lmp")


class OpticalTransport(Identity):
    """
    Optical Transport.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(OpticalTransport, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:opticalTransport")


class Sdlc(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sdlc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sdlc")


class VoiceEM(Identity):
    """
    Voice recEive and transMit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceEM, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceEM")


class X86Laps(Identity):
    """
    LAPS based on ITU\-T X.86/Y.1323.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(X86Laps, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:x86Laps")


class G9982(Identity):
    """
    G.998.2 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(G9982, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:g9982")


class Iso88022llc(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88022llc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88022llc")


class DvbAsiIn(Identity):
    """
    DVB\-ASI Input.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DvbAsiIn, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbAsiIn")


class Bgppolicyaccounting(Identity):
    """
    BGP Policy Accounting.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Bgppolicyaccounting, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:bgppolicyaccounting")


class AluEponOnu(Identity):
    """
    EPON Optical Network Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AluEponOnu, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluEponOnu")


class MfSigLink(Identity):
    """
    Multi\-frequency signaling link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(MfSigLink, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mfSigLink")


class Dcn(Identity):
    """
    Data Communications Network.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dcn, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dcn")


class AtmDxi(Identity):
    """
    ATM DXI.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AtmDxi, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmDxi")


class VoiceOverFrameRelay(Identity):
    """
    Voice Over Frame Relay.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceOverFrameRelay, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceOverFrameRelay")


class Gfp(Identity):
    """
    Generic Framing Procedure (GFP).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Gfp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:gfp")


class SonetOverheadChannel(Identity):
    """
    SONET Overhead Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(SonetOverheadChannel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sonetOverheadChannel")


class VmwareVirtualNic(Identity):
    """
    VMware Virtual Network Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VmwareVirtualNic, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:vmwareVirtualNic")


class FcipLink(Identity):
    """
    FCIP Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(FcipLink, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:fcipLink")


class IpOverClaw(Identity):
    """
    IBM Common Link Access to Workstn.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(IpOverClaw, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ipOverClaw")


class Coffee(Identity):
    """
    Coffee pot.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Coffee, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:coffee")


class Radsl(Identity):
    """
    Rate\-Adapt. Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Radsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:radsl")


class Vdsl2(Identity):
    """
    Very high speed digital subscriber line Version 2
    (as per ITU\-T Recommendation G.993.2).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Vdsl2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:vdsl2")


class Rs232(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Rs232, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:rs232")


class E1(Identity):
    """
    Obsolete; see DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(E1, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:e1")


class ReachDSL(Identity):
    """
    Long Reach DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(ReachDSL, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:reachDSL")


class VoiceOverCable(Identity):
    """
    Voice Over Cable Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceOverCable, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceOverCable")


class Tr008(Identity):
    """
    TR008.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Tr008, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:tr008")


class VoiceOverIp(Identity):
    """
    Voice over IP encapsulation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceOverIp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceOverIp")


class Atm(Identity):
    """
    ATM cells.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Atm, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atm")


class Ds3(Identity):
    """
    DS3\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ds3, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ds3")


class Ds0(Identity):
    """
    Digital Signal Level 0.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ds0, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ds0")


class Ds1(Identity):
    """
    DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ds1, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ds1")


class Srp(Identity):
    """
    Spatial Reuse Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Srp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:srp")


class DocsCableDownstream(Identity):
    """
    CATV Downstream interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DocsCableDownstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:docsCableDownstream")


class DvbRcsTdma(Identity):
    """
    DVB\-RCS TDMA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DvbRcsTdma, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbRcsTdma")


class G9983(Identity):
    """
    G.998.3 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(G9983, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:g9983")


class Plc(Identity):
    """
    Power Line Communications.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Plc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:plc")


class FrameRelayMPI(Identity):
    """
    Multiproto Interconnect over FR.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(FrameRelayMPI, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frameRelayMPI")


class Mvl(Identity):
    """
    Multiple Virtual Lines DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Mvl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mvl")


class PropMultiplexor(Identity):
    """
    Proprietary multiplexing.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PropMultiplexor, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propMultiplexor")


class VoiceDID(Identity):
    """
    Voice Direct Inward Dialing.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceDID, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceDID")


class CompositeLink(Identity):
    """
    Avici Composite Link Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(CompositeLink, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:compositeLink")


class Proteon10Mbit(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Proteon10Mbit, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:proteon10Mbit")


class Atmbond(Identity):
    """
    atmbond.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Atmbond, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmbond")


class Frf16MfrBundle(Identity):
    """
    FRF.16 Multilink Frame Relay.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Frf16MfrBundle, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frf16MfrBundle")


class CctEmul(Identity):
    """
    ATM Emulated circuit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(CctEmul, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:cctEmul")


class MplsTunnel(Identity):
    """
    MPLS Tunnel Virtual Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(MplsTunnel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mplsTunnel")


class Gpon(Identity):
    """
    Gigabit\-capable passive optical networks (G\-PON) as per
    ITU\-T G.948.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Gpon, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:gpon")


class Vdsl(Identity):
    """
    Very H\-Speed Digital Subscrib. Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Vdsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:vdsl")


class Pos(Identity):
    """
    Packet over SONET/SDH Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Pos, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pos")


class Ieee8023adLag(Identity):
    """
    IEEE 802.3ad Link Aggregate.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ieee8023adLag, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ieee8023adLag")


class DocsCableMaclayer(Identity):
    """
    CATV Mac Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DocsCableMaclayer, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:docsCableMaclayer")


class DocsCableMCmtsDownstream(Identity):
    """
    CATV Modular CMTS Downstream Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DocsCableMCmtsDownstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:docsCableMCmtsDownstream")


class Ppp(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ppp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ppp")


class FrameRelay(Identity):
    """
    DTE only.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(FrameRelay, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frameRelay")


class Eplrs(Identity):
    """
    Ext Pos Loc Report Sys.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Eplrs, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:eplrs")


class VmwareNicTeam(Identity):
    """
    VMware NIC Team.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VmwareNicTeam, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:vmwareNicTeam")


class CableDownstreamRfPort(Identity):
    """
    CATV downstream RF Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(CableDownstreamRfPort, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:cableDownstreamRfPort")


class MacSecUncontrolledIF(Identity):
    """
    MACSecUncontrolled.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(MacSecUncontrolledIF, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:macSecUncontrolledIF")


class Iso88023Csmacd(Identity):
    """
    Deprecated via RFC 3635.
    Use ethernetCsmacd(6) instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88023Csmacd, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88023Csmacd")


class Usb(Identity):
    """
    USB Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Usb, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:usb")


class AtmFuni(Identity):
    """
    ATM FUNI.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AtmFuni, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmFuni")


class TeLink(Identity):
    """
    TE Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(TeLink, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:teLink")


class Pon622(Identity):
    """
    FSAN 622Mb Symetrical PON interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Pon622, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pon622")


class Econet(Identity):
    """
    Acorn Econet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Econet, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:econet")


class Tdlc(Identity):
    """
    IBM twinaxial data link control.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Tdlc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:tdlc")


class Ds0Bundle(Identity):
    """
    Group of ds0s on the same ds1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ds0Bundle, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ds0Bundle")


class Fast(Identity):
    """
    Fast channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Fast, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:fast")


class Ieee1394(Identity):
    """
    IEEE1394 High Performance Serial Bus.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ieee1394, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ieee1394")


class CblVectaStar(Identity):
    """
    Cambridge Broadband Networks Limited VectaStar.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(CblVectaStar, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:cblVectaStar")


class Rsrb(Identity):
    """
    Remote Source Route Bridging.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Rsrb, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:rsrb")


class FrameRelayInterconnect(Identity):
    """
    Obsolete; use either
    frameRelay(32) or frameRelayService(44).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(FrameRelayInterconnect, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frameRelayInterconnect")


class Isdns(Identity):
    """
    ISDN S/T interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Isdns, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:isdns")


class PppMultilinkBundle(Identity):
    """
    PPP Multilink Bundle.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PppMultilinkBundle, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pppMultilinkBundle")


class Aflane8025(Identity):
    """
    ATM Emulated LAN for 802.5.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Aflane8025, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aflane8025")


class Lapb(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Lapb, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:lapb")


class Aflane8023(Identity):
    """
    ATM Emulated LAN for 802.3.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Aflane8023, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aflane8023")


class Lapd(Identity):
    """
    Link Access Protocol D.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Lapd, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:lapd")


class Isdnu(Identity):
    """
    ISDN U interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Isdnu, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:isdnu")


class Lapf(Identity):
    """
    LAP F.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Lapf, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:lapf")


class CapwapWtpVirtualRadio(Identity):
    """
    WTP Virtual Radio Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(CapwapWtpVirtualRadio, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:capwapWtpVirtualRadio")


class IfVfiType(Identity):
    """
    VPLS Forwarding Instance Interface Type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(IfVfiType, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ifVfiType")


class X25huntGroup(Identity):
    """
    X25 Hunt Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(X25huntGroup, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:x25huntGroup")


class Para(Identity):
    """
    Parallel\-port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Para, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:para")


class MacSecControlledIF(Identity):
    """
    MACSecControlled.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(MacSecControlledIF, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:macSecControlledIF")


class Iso88024TokenBus(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88024TokenBus, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88024TokenBus")


class LocalTalk(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(LocalTalk, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:localTalk")


class Hyperchannel(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hyperchannel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hyperchannel")


class MediaMailOverIp(Identity):
    """
    Multimedia Mail over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(MediaMailOverIp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mediaMailOverIp")


class IfGsn(Identity):
    """
    HIPPI\-6400.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(IfGsn, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:if-gsn")


class CapwapDot11Profile(Identity):
    """
    WLAN Profile Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(CapwapDot11Profile, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:capwapDot11Profile")


class L3ipxvlan(Identity):
    """
    Layer 3 Virtual LAN using IPX.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(L3ipxvlan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:l3ipxvlan")


class AtmSubInterface(Identity):
    """
    ATM Sub Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AtmSubInterface, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmSubInterface")


class PrimaryISDN(Identity):
    """
    No longer used.  See also RFC 2127.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PrimaryISDN, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:primaryISDN")


class Proteon80Mbit(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Proteon80Mbit, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:proteon80Mbit")


class Iso88026Man(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88026Man, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88026Man")


class DigitalWrapperOverheadChannel(Identity):
    """
    Digital Wrapper.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DigitalWrapperOverheadChannel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:digitalWrapperOverheadChannel")


class DocsCableUpstreamChannel(Identity):
    """
    CATV Upstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DocsCableUpstreamChannel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:docsCableUpstreamChannel")


class OpticalChannel(Identity):
    """
    Optical Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(OpticalChannel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:opticalChannel")


class EthernetCsmacd(Identity):
    """
    For all Ethernet\-like interfaces, regardless of speed,
    as per RFC 3635.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(EthernetCsmacd, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ethernetCsmacd")


class Bits(Identity):
    """
    bitsport.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Bits, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:bits")


class Tunnel(Identity):
    """
    Encapsulation interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Tunnel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:tunnel")


class Hdsl2(Identity):
    """
    High Bit\-Rate DSL \- 2nd generation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hdsl2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hdsl2")


class FrameRelayService(Identity):
    """
    FRNETSERV\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(FrameRelayService, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frameRelayService")


class Mpls(Identity):
    """
    MPLS.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Mpls, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mpls")


class Ieee80211(Identity):
    """
    Radio spread spectrum.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ieee80211, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ieee80211")


class Ieee80212(Identity):
    """
    100BaseVG.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ieee80212, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ieee80212")


class MocaVersion1(Identity):
    """
    MultiMedia over Coax Alliance (MoCA) Interface
    as documented in information provided privately to IANA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(MocaVersion1, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mocaVersion1")


class Sonet(Identity):
    """
    SONET or SDH.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sonet, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sonet")


class Escon(Identity):
    """
    IBM Enterprise Systems Connection.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Escon, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:escon")


class AluEponLogicalLink(Identity):
    """
    The emulation of a point\-to\-point link over the EPON
    layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AluEponLogicalLink, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluEponLogicalLink")


class G703at2mb(Identity):
    """
    Obsolete; see DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(G703at2mb, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:g703at2mb")


class Ultra(Identity):
    """
    Ultra Technologies.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ultra, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ultra")


class DvbRccDownstream(Identity):
    """
    DVB\-RCC Downstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DvbRccDownstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbRccDownstream")


class SipTg(Identity):
    """
    SIP Trunk Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(SipTg, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sipTg")


class SmdsIcip(Identity):
    """
    SMDS InterCarrier Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(SmdsIcip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:smdsIcip")


class Bridge(Identity):
    """
    Transparent bridge interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Bridge, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:bridge")


class AtmLogical(Identity):
    """
    ATM Logical Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AtmLogical, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmLogical")


class PropPointToPointSerial(Identity):
    """
    Proprietary serial.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PropPointToPointSerial, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propPointToPointSerial")


class V35(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(V35, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:v35")


class V36(Identity):
    """
    CCITT V.36.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(V36, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:v36")


class V37(Identity):
    """
    V.37.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(V37, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:v37")


class Ip(Identity):
    """
    IP (for APPN HPR in IP networks).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ip")


class Gr303IDT(Identity):
    """
    Integrated Digital Terminal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Gr303IDT, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:gr303IDT")


class BasicISDN(Identity):
    """
    No longer used.  See also RFC 2127.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(BasicISDN, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:basicISDN")


class G703at64k(Identity):
    """
    CCITT G703 at 64Kbps.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(G703at64k, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:g703at64k")


class ArcnetPlus(Identity):
    """
    ARCnet Plus.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(ArcnetPlus, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:arcnetPlus")


class Pip(Identity):
    """
    Provider Instance Port on a bridge per IEEE 802.1ah PBB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Pip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pip")


class Dtm(Identity):
    """
    Dynamic synchronous Transfer Mode.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dtm, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dtm")


class Slip(Identity):
    """
    Generic SLIP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Slip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:slip")


class Hiperlan2(Identity):
    """
    HIPERLAN Type 2 Radio Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hiperlan2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hiperlan2")


class Adsl(Identity):
    """
    Asymmetric Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Adsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:adsl")


class Ieee80216WMAN(Identity):
    """
    IEEE 802.16 WMAN interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ieee80216WMAN, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ieee80216WMAN")


class AtmIma(Identity):
    """
    ATM IMA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AtmIma, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmIma")


class Isdn(Identity):
    """
    ISDN and X.25.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Isdn, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:isdn")


class CapwapDot11Bss(Identity):
    """
    WLAN BSS Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(CapwapDot11Bss, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:capwapDot11Bss")


class Sip(Identity):
    """
    SMDS, coffee.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sip")


class PdnEtherLoop2(Identity):
    """
    Paradyne EtherLoop 2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PdnEtherLoop2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pdnEtherLoop2")


class VoiceEBS(Identity):
    """
    Voice P\-phone EBS physical interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceEBS, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceEBS")


class IpForward(Identity):
    """
    IP Forwarding Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(IpForward, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ipForward")


class Iso88025CRFPInt(Identity):
    """
    ISO 802.5 CRFP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88025CRFPInt, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88025CRFPInt")


class PropVirtual(Identity):
    """
    Proprietary virtual/internal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PropVirtual, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propVirtual")


class WwanPP(Identity):
    """
    3GPP WWAN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(WwanPP, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:wwanPP")


class Other(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Other, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:other")


class Pon155(Identity):
    """
    FSAN 155Mb Symetrical PON interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Pon155, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pon155")


class Qam(Identity):
    """
    RF Qam Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Qam, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:qam")


class OtnOdu(Identity):
    """
    OTN Optical Data Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(OtnOdu, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:otnOdu")


class Iso88025Fiber(Identity):
    """
    ISO 802.5j Fiber Token Ring.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88025Fiber, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88025Fiber")


class Channel(Identity):
    """
    Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Channel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:channel")


class VoiceEMFGD(Identity):
    """
    Voice E&M Feature Group D.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceEMFGD, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceEMFGD")


class AluGponPhysicalUni(Identity):
    """
    GPON physical User to Network interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AluGponPhysicalUni, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluGponPhysicalUni")


class A12MppSwitch(Identity):
    """
    Avalon Parallel Processor.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(A12MppSwitch, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:a12MppSwitch")


class Ilan(Identity):
    """
    Internal LAN on a bridge per IEEE 802.1ap.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ilan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ilan")


class PdnEtherLoop1(Identity):
    """
    Paradyne EtherLoop 1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PdnEtherLoop1, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pdnEtherLoop1")


class X213(Identity):
    """
    CCITT\-ITU X213.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(X213, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:x213")


class SonetPath(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(SonetPath, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sonetPath")


class VoiceFGDEANA(Identity):
    """
    Voice FGD Exchange Access North American.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VoiceFGDEANA, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceFGDEANA")


class Iso88025TokenRing(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88025TokenRing, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88025TokenRing")


class PropAtm(Identity):
    """
    Proprietary ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(PropAtm, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propAtm")


class AluEponPhysicalUni(Identity):
    """
    EPON physical User to Network interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AluEponPhysicalUni, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluEponPhysicalUni")


class StackToStack(Identity):
    """
    IBM stackToStack.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(StackToStack, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:stackToStack")


class FrForward(Identity):
    """
    Frame Forward Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(FrForward, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frForward")


class Homepna(Identity):
    """
    HomePNA ITU\-T G.989.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Homepna, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:homepna")


class Sdsl(Identity):
    """
    Symmetric Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sdsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sdsl")


class VirtualIpAddress(Identity):
    """
    IBM VIPA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(VirtualIpAddress, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:virtualIpAddress")


class Bsc(Identity):
    """
    Bisynchronous Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Bsc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:bsc")


class AtmRadio(Identity):
    """
    ATM over radio links.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AtmRadio, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmRadio")


class AviciOpticalEther(Identity):
    """
    Avici Optical Ethernet Aggregate.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(AviciOpticalEther, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aviciOpticalEther")


class G9981(Identity):
    """
    G.998.1 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(G9981, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:g9981")


class FibreChannel(Identity):
    """
    Fibre Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(FibreChannel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:fibreChannel")


class Shdsl(Identity):
    """
    Multirate HDSL2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Shdsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:shdsl")


class Eon(Identity):
    """
    CLNP over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Eon, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:eon")


class H323Gatekeeper(Identity):
    """
    H323 Gatekeeper.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(H323Gatekeeper, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:h323Gatekeeper")


class Hdh1822(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hdh1822, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hdh1822")


class DvbRccUpstream(Identity):
    """
    DVB\-RCC Upstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(DvbRccUpstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbRccUpstream")


class Nsip(Identity):
    """
    XNS over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Nsip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:nsip")


class TranspHdlc(Identity):
    """
    Transp HDLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(TranspHdlc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:transpHdlc")


class TermPad(Identity):
    """
    CCITT\-ITU X.3 PAD Facility.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(TermPad, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:termPad")


class IpOverCdlc(Identity):
    """
    IBM ipOverCdlc.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(IpOverCdlc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ipOverCdlc")


class Ces(Identity):
    """
    Circuit Emulation Service.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ces, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ces")


class Modem(Identity):
    """
    Generic modem.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Modem, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:modem")


