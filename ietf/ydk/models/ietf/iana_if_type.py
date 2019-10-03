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
import sys
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.ietf.ietf_interfaces import InterfaceType



class IanaInterfaceType(InterfaceType):
    """
    This identity is used as a base for all interface types
    defined in the 'ifType definitions' registry.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:iana-interface-type"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IanaInterfaceType, self).__init__(ns, pref, tag)



class VoiceFXO(IanaInterfaceType):
    """
    Voice Foreign Exchange Office.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceFXO"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceFXO, self).__init__(ns, pref, tag)



class AtmVciEndPt(IanaInterfaceType):
    """
    ATM VCI End Point.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:atmVciEndPt"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AtmVciEndPt, self).__init__(ns, pref, tag)



class PropBWAp2Mp(IanaInterfaceType):
    """
    PropBroadbandWirelessAccesspt2Multipt (use of this value
    for IEEE 802.16 WMAN interfaces as per IEEE Std 802.16f
    is deprecated, and ieee80216WMAN(237) should be used
    instead).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:propBWAp2Mp"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PropBWAp2Mp, self).__init__(ns, pref, tag)



class PropDocsWirelessDownstream(IanaInterfaceType):
    """
    Cisco proprietary Downstream.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:propDocsWirelessDownstream"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PropDocsWirelessDownstream, self).__init__(ns, pref, tag)



class V11(IanaInterfaceType):
    """
    CCITT V.11/X.21.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:v11"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(V11, self).__init__(ns, pref, tag)



class SoftwareLoopback(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:softwareLoopback"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SoftwareLoopback, self).__init__(ns, pref, tag)



class Hdlc(IanaInterfaceType):
    """
    HDLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:hdlc"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Hdlc, self).__init__(ns, pref, tag)



class VoiceFGDOS(IanaInterfaceType):
    """
    Voice FGD Operator Services.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceFGDOS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceFGDOS, self).__init__(ns, pref, tag)



class FastEtherFX(IanaInterfaceType):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:fastEtherFX"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FastEtherFX, self).__init__(ns, pref, tag)



class DvbTdm(IanaInterfaceType):
    """
    DVB Satellite TDM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:dvbTdm"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DvbTdm, self).__init__(ns, pref, tag)



class Nfas(IanaInterfaceType):
    """
    Non\-Facility Associated Signaling.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:nfas"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Nfas, self).__init__(ns, pref, tag)



class IfPwType(IanaInterfaceType):
    """
    Pseudowire interface type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ifPwType"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IfPwType, self).__init__(ns, pref, tag)



class L2vlan(IanaInterfaceType):
    """
    Layer 2 Virtual LAN using 802.1Q.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:l2vlan"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L2vlan, self).__init__(ns, pref, tag)



class Adsl2plus(IanaInterfaceType):
    """
    Asymmetric Digital Subscriber Loop Version 2 \-
    Version 2 Plus and all variants.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:adsl2plus"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Adsl2plus, self).__init__(ns, pref, tag)



class Ieee802154(IanaInterfaceType):
    """
    IEEE 802.15.4 WPAN interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ieee802154"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ieee802154, self).__init__(ns, pref, tag)



class VoiceFXS(IanaInterfaceType):
    """
    Voice Foreign Exchange Station.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceFXS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceFXS, self).__init__(ns, pref, tag)



class DvbRcsMacLayer(IanaInterfaceType):
    """
    DVB\-RCS MAC Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:dvbRcsMacLayer"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DvbRcsMacLayer, self).__init__(ns, pref, tag)



class Idsl(IanaInterfaceType):
    """
    Digital Subscriber Loop over ISDN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:idsl"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Idsl, self).__init__(ns, pref, tag)



class Infiniband(IanaInterfaceType):
    """
    Infiniband.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:infiniband"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Infiniband, self).__init__(ns, pref, tag)



class DdnX25(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ddnX25"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DdnX25, self).__init__(ns, pref, tag)



class WwanPP2(IanaInterfaceType):
    """
    3GPP2 WWAN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:wwanPP2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(WwanPP2, self).__init__(ns, pref, tag)



class DocsCableUpstream(IanaInterfaceType):
    """
    CATV Upstream interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:docsCableUpstream"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DocsCableUpstream, self).__init__(ns, pref, tag)



class Ethernet3Mbit(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ethernet3Mbit"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ethernet3Mbit, self).__init__(ns, pref, tag)



class DigitalPowerline(IanaInterfaceType):
    """
    IP over Power Lines.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:digitalPowerline"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DigitalPowerline, self).__init__(ns, pref, tag)



class H323Proxy(IanaInterfaceType):
    """
    H323 Voice and Video Proxy.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:h323Proxy"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(H323Proxy, self).__init__(ns, pref, tag)



class Gtp(IanaInterfaceType):
    """
    GTP (GPRS Tunneling Protocol).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:gtp"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Gtp, self).__init__(ns, pref, tag)



class IpOverAtm(IanaInterfaceType):
    """
    IBM ipOverAtm.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ipOverAtm"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IpOverAtm, self).__init__(ns, pref, tag)



class AluEpon(IanaInterfaceType):
    """
    Ethernet Passive Optical Networks (E\-PON).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:aluEpon"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AluEpon, self).__init__(ns, pref, tag)



class Imt(IanaInterfaceType):
    """
    Inter\-Machine Trunks.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:imt"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Imt, self).__init__(ns, pref, tag)



class IpSwitch(IanaInterfaceType):
    """
    IP Switching Objects.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ipSwitch"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IpSwitch, self).__init__(ns, pref, tag)



class Msdsl(IanaInterfaceType):
    """
    Multi\-rate Symmetric DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:msdsl"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Msdsl, self).__init__(ns, pref, tag)



class DvbRccMacLayer(IanaInterfaceType):
    """
    DVB\-RCC MAC Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:dvbRccMacLayer"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DvbRccMacLayer, self).__init__(ns, pref, tag)



class SmdsDxi(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:smdsDxi"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SmdsDxi, self).__init__(ns, pref, tag)



class VoiceOverAtm(IanaInterfaceType):
    """
    Voice over ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceOverAtm"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceOverAtm, self).__init__(ns, pref, tag)



class Arap(IanaInterfaceType):
    """
    Appletalk Remote Access Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:arap"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Arap, self).__init__(ns, pref, tag)



class FastEther(IanaInterfaceType):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:fastEther"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FastEther, self).__init__(ns, pref, tag)



class Mpc(IanaInterfaceType):
    """
    IBM multi\-protocol channel support.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:mpc"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Mpc, self).__init__(ns, pref, tag)



class Linegroup(IanaInterfaceType):
    """
    Interface common to multiple lines.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:linegroup"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Linegroup, self).__init__(ns, pref, tag)



class Hippi(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:hippi"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Hippi, self).__init__(ns, pref, tag)



class Rpr(IanaInterfaceType):
    """
    Resilient Packet Ring Interface Type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:rpr"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Rpr, self).__init__(ns, pref, tag)



class Ds1FDL(IanaInterfaceType):
    """
    Facility Data Link (4Kbps) on a DS1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ds1FDL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ds1FDL, self).__init__(ns, pref, tag)



class SonetVT(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:sonetVT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SonetVT, self).__init__(ns, pref, tag)



class VoiceEncap(IanaInterfaceType):
    """
    Voice encapsulation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceEncap"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceEncap, self).__init__(ns, pref, tag)



class Ss7SigLink(IanaInterfaceType):
    """
    SS7 Signaling Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ss7SigLink"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ss7SigLink, self).__init__(ns, pref, tag)



class Arcnet(IanaInterfaceType):
    """
    ARCnet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:arcnet"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Arcnet, self).__init__(ns, pref, tag)



class ActelisMetaLOOP(IanaInterfaceType):
    """
    Acteleis proprietary MetaLOOP High Speed Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:actelisMetaLOOP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ActelisMetaLOOP, self).__init__(ns, pref, tag)



class Qllc(IanaInterfaceType):
    """
    SNA QLLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:qllc"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Qllc, self).__init__(ns, pref, tag)



class Rfc877x25(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:rfc877x25"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Rfc877x25, self).__init__(ns, pref, tag)



class MpegTransport(IanaInterfaceType):
    """
    MPEG transport interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:mpegTransport"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MpegTransport, self).__init__(ns, pref, tag)



class X25mlp(IanaInterfaceType):
    """
    Multi\-Link Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:x25mlp"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(X25mlp, self).__init__(ns, pref, tag)



class VirtualTg(IanaInterfaceType):
    """
    Virtual Trunk Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:virtualTg"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VirtualTg, self).__init__(ns, pref, tag)



class HostPad(IanaInterfaceType):
    """
    CCITT\-ITU X.29 PAD Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:hostPad"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(HostPad, self).__init__(ns, pref, tag)



class StarLan(IanaInterfaceType):
    """
    Deprecated via RFC 3635.
    Use ethernetCsmacd(6) instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:starLan"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(StarLan, self).__init__(ns, pref, tag)



class Iso88025Dtr(IanaInterfaceType):
    """
    ISO 802.5r DTR.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:iso88025Dtr"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Iso88025Dtr, self).__init__(ns, pref, tag)



class Ibm370parChan(IanaInterfaceType):
    """
    IBM System 360/370 OEMI Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ibm370parChan"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ibm370parChan, self).__init__(ns, pref, tag)



class Adsl2(IanaInterfaceType):
    """
    Asymmetric Digital Subscriber Loop Version 2
    (DEPRECATED/OBSOLETED \- please use adsl2plus(238)
    instead).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:adsl2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Adsl2, self).__init__(ns, pref, tag)



class OtnOtu(IanaInterfaceType):
    """
    OTN Optical channel Transport Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:otnOtu"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OtnOtu, self).__init__(ns, pref, tag)



class PropWirelessP2P(IanaInterfaceType):
    """
    Prop. P2P wireless interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:propWirelessP2P"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PropWirelessP2P, self).__init__(ns, pref, tag)



class Interleave(IanaInterfaceType):
    """
    Interleave channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:interleave"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Interleave, self).__init__(ns, pref, tag)



class Isup(IanaInterfaceType):
    """
    ISUP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:isup"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Isup, self).__init__(ns, pref, tag)



class Regular1822(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:regular1822"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Regular1822, self).__init__(ns, pref, tag)



class Gr303RDT(IanaInterfaceType):
    """
    Remote Digital Terminal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:gr303RDT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Gr303RDT, self).__init__(ns, pref, tag)



class PropDocsWirelessMaclayer(IanaInterfaceType):
    """
    Cisco proprietary Maclayer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:propDocsWirelessMaclayer"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PropDocsWirelessMaclayer, self).__init__(ns, pref, tag)



class Async(IanaInterfaceType):
    """
    Asynchronous Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:async"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Async, self).__init__(ns, pref, tag)



class RadioMAC(IanaInterfaceType):
    """
    MAC layer over radio links.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:radioMAC"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(RadioMAC, self).__init__(ns, pref, tag)



class OpticalChannelGroup(IanaInterfaceType):
    """
    Optical Channel Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:opticalChannelGroup"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OpticalChannelGroup, self).__init__(ns, pref, tag)



class SixToFour(IanaInterfaceType):
    """
    6to4 interface (DEPRECATED).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:sixToFour"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SixToFour, self).__init__(ns, pref, tag)



class PropDocsWirelessUpstream(IanaInterfaceType):
    """
    Cisco proprietary Upstream.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:propDocsWirelessUpstream"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PropDocsWirelessUpstream, self).__init__(ns, pref, tag)



class Q2931(IanaInterfaceType):
    """
    Q.2931.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:q2931"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Q2931, self).__init__(ns, pref, tag)



class Fddi(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:fddi"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Fddi, self).__init__(ns, pref, tag)



class PropCnls(IanaInterfaceType):
    """
    Proprietary Connectionless Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:propCnls"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PropCnls, self).__init__(ns, pref, tag)



class Aal2(IanaInterfaceType):
    """
    ATM adaptation layer 2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:aal2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Aal2, self).__init__(ns, pref, tag)



class DvbAsiOut(IanaInterfaceType):
    """
    DVB\-ASI Output.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:dvbAsiOut"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DvbAsiOut, self).__init__(ns, pref, tag)



class AluELP(IanaInterfaceType):
    """
    Alcatel\-Lucent Ethernet Link Protection.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:aluELP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AluELP, self).__init__(ns, pref, tag)



class CiscoISLvlan(IanaInterfaceType):
    """
    Layer 2 Virtual LAN using Cisco ISL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ciscoISLvlan"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CiscoISLvlan, self).__init__(ns, pref, tag)



class DocsCableUpstreamRfPort(IanaInterfaceType):
    """
    DOCSIS CATV Upstream RF Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:docsCableUpstreamRfPort"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DocsCableUpstreamRfPort, self).__init__(ns, pref, tag)



class Aal5(IanaInterfaceType):
    """
    AAL5 over ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:aal5"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Aal5, self).__init__(ns, pref, tag)



class FrDlciEndPt(IanaInterfaceType):
    """
    Frame Relay DLCI End Point.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:frDlciEndPt"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FrDlciEndPt, self).__init__(ns, pref, tag)



class HippiInterface(IanaInterfaceType):
    """
    HIPPI interfaces.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:hippiInterface"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(HippiInterface, self).__init__(ns, pref, tag)



class L3ipvlan(IanaInterfaceType):
    """
    Layer 3 Virtual LAN using IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:l3ipvlan"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L3ipvlan, self).__init__(ns, pref, tag)



class Miox25(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:miox25"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Miox25, self).__init__(ns, pref, tag)



class Hssi(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:hssi"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Hssi, self).__init__(ns, pref, tag)



class AtmVirtual(IanaInterfaceType):
    """
    ATM Virtual Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:atmVirtual"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AtmVirtual, self).__init__(ns, pref, tag)



class AluGponOnu(IanaInterfaceType):
    """
    GPON Optical Network Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:aluGponOnu"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AluGponOnu, self).__init__(ns, pref, tag)



class Rfc1483(IanaInterfaceType):
    """
    Multiprotocol over ATM AAL5.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:rfc1483"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Rfc1483, self).__init__(ns, pref, tag)



class Cnr(IanaInterfaceType):
    """
    Combat Net Radio.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:cnr"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Cnr, self).__init__(ns, pref, tag)



class SipSig(IanaInterfaceType):
    """
    SIP Signaling.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:sipSig"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SipSig, self).__init__(ns, pref, tag)



class Myrinet(IanaInterfaceType):
    """
    Myricom Myrinet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:myrinet"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Myrinet, self).__init__(ns, pref, tag)



class Dlsw(IanaInterfaceType):
    """
    Data Link Switching.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:dlsw"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Dlsw, self).__init__(ns, pref, tag)



class GigabitEthernet(IanaInterfaceType):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:gigabitEthernet"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(GigabitEthernet, self).__init__(ns, pref, tag)



class X25ple(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:x25ple"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(X25ple, self).__init__(ns, pref, tag)



class Lmp(IanaInterfaceType):
    """
    Link Management Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:lmp"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Lmp, self).__init__(ns, pref, tag)



class OpticalTransport(IanaInterfaceType):
    """
    Optical Transport.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:opticalTransport"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OpticalTransport, self).__init__(ns, pref, tag)



class Sdlc(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:sdlc"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Sdlc, self).__init__(ns, pref, tag)



class VoiceEM(IanaInterfaceType):
    """
    Voice recEive and transMit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceEM"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceEM, self).__init__(ns, pref, tag)



class X86Laps(IanaInterfaceType):
    """
    LAPS based on ITU\-T X.86/Y.1323.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:x86Laps"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(X86Laps, self).__init__(ns, pref, tag)



class G9982(IanaInterfaceType):
    """
    G.998.2 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:g9982"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(G9982, self).__init__(ns, pref, tag)



class Iso88022llc(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:iso88022llc"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Iso88022llc, self).__init__(ns, pref, tag)



class DvbAsiIn(IanaInterfaceType):
    """
    DVB\-ASI Input.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:dvbAsiIn"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DvbAsiIn, self).__init__(ns, pref, tag)



class Bgppolicyaccounting(IanaInterfaceType):
    """
    BGP Policy Accounting.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:bgppolicyaccounting"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Bgppolicyaccounting, self).__init__(ns, pref, tag)



class AluEponOnu(IanaInterfaceType):
    """
    EPON Optical Network Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:aluEponOnu"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AluEponOnu, self).__init__(ns, pref, tag)



class MfSigLink(IanaInterfaceType):
    """
    Multi\-frequency signaling link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:mfSigLink"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MfSigLink, self).__init__(ns, pref, tag)



class Dcn(IanaInterfaceType):
    """
    Data Communications Network.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:dcn"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Dcn, self).__init__(ns, pref, tag)



class AtmDxi(IanaInterfaceType):
    """
    ATM DXI.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:atmDxi"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AtmDxi, self).__init__(ns, pref, tag)



class VoiceOverFrameRelay(IanaInterfaceType):
    """
    Voice Over Frame Relay.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceOverFrameRelay"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceOverFrameRelay, self).__init__(ns, pref, tag)



class Gfp(IanaInterfaceType):
    """
    Generic Framing Procedure (GFP).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:gfp"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Gfp, self).__init__(ns, pref, tag)



class SonetOverheadChannel(IanaInterfaceType):
    """
    SONET Overhead Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:sonetOverheadChannel"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SonetOverheadChannel, self).__init__(ns, pref, tag)



class VmwareVirtualNic(IanaInterfaceType):
    """
    VMware Virtual Network Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:vmwareVirtualNic"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VmwareVirtualNic, self).__init__(ns, pref, tag)



class FcipLink(IanaInterfaceType):
    """
    FCIP Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:fcipLink"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FcipLink, self).__init__(ns, pref, tag)



class IpOverClaw(IanaInterfaceType):
    """
    IBM Common Link Access to Workstn.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ipOverClaw"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IpOverClaw, self).__init__(ns, pref, tag)



class Coffee(IanaInterfaceType):
    """
    Coffee pot.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:coffee"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Coffee, self).__init__(ns, pref, tag)



class Radsl(IanaInterfaceType):
    """
    Rate\-Adapt. Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:radsl"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Radsl, self).__init__(ns, pref, tag)



class Vdsl2(IanaInterfaceType):
    """
    Very high speed digital subscriber line Version 2
    (as per ITU\-T Recommendation G.993.2).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:vdsl2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Vdsl2, self).__init__(ns, pref, tag)



class Rs232(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:rs232"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Rs232, self).__init__(ns, pref, tag)



class E1(IanaInterfaceType):
    """
    Obsolete; see DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:e1"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(E1, self).__init__(ns, pref, tag)



class ReachDSL(IanaInterfaceType):
    """
    Long Reach DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:reachDSL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ReachDSL, self).__init__(ns, pref, tag)



class VoiceOverCable(IanaInterfaceType):
    """
    Voice Over Cable Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceOverCable"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceOverCable, self).__init__(ns, pref, tag)



class Tr008(IanaInterfaceType):
    """
    TR008.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:tr008"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Tr008, self).__init__(ns, pref, tag)



class VoiceOverIp(IanaInterfaceType):
    """
    Voice over IP encapsulation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceOverIp"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceOverIp, self).__init__(ns, pref, tag)



class Atm(IanaInterfaceType):
    """
    ATM cells.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:atm"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Atm, self).__init__(ns, pref, tag)



class Ds3(IanaInterfaceType):
    """
    DS3\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ds3"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ds3, self).__init__(ns, pref, tag)



class Ds0(IanaInterfaceType):
    """
    Digital Signal Level 0.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ds0"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ds0, self).__init__(ns, pref, tag)



class Ds1(IanaInterfaceType):
    """
    DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ds1"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ds1, self).__init__(ns, pref, tag)



class Srp(IanaInterfaceType):
    """
    Spatial Reuse Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:srp"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Srp, self).__init__(ns, pref, tag)



class DocsCableDownstream(IanaInterfaceType):
    """
    CATV Downstream interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:docsCableDownstream"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DocsCableDownstream, self).__init__(ns, pref, tag)



class DvbRcsTdma(IanaInterfaceType):
    """
    DVB\-RCS TDMA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:dvbRcsTdma"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DvbRcsTdma, self).__init__(ns, pref, tag)



class G9983(IanaInterfaceType):
    """
    G.998.3 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:g9983"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(G9983, self).__init__(ns, pref, tag)



class Plc(IanaInterfaceType):
    """
    Power Line Communications.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:plc"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Plc, self).__init__(ns, pref, tag)



class FrameRelayMPI(IanaInterfaceType):
    """
    Multiproto Interconnect over FR.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:frameRelayMPI"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FrameRelayMPI, self).__init__(ns, pref, tag)



class Mvl(IanaInterfaceType):
    """
    Multiple Virtual Lines DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:mvl"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Mvl, self).__init__(ns, pref, tag)



class PropMultiplexor(IanaInterfaceType):
    """
    Proprietary multiplexing.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:propMultiplexor"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PropMultiplexor, self).__init__(ns, pref, tag)



class VoiceDID(IanaInterfaceType):
    """
    Voice Direct Inward Dialing.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceDID"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceDID, self).__init__(ns, pref, tag)



class CompositeLink(IanaInterfaceType):
    """
    Avici Composite Link Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:compositeLink"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CompositeLink, self).__init__(ns, pref, tag)



class Proteon10Mbit(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:proteon10Mbit"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Proteon10Mbit, self).__init__(ns, pref, tag)



class Atmbond(IanaInterfaceType):
    """
    atmbond.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:atmbond"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Atmbond, self).__init__(ns, pref, tag)



class Frf16MfrBundle(IanaInterfaceType):
    """
    FRF.16 Multilink Frame Relay.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:frf16MfrBundle"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Frf16MfrBundle, self).__init__(ns, pref, tag)



class CctEmul(IanaInterfaceType):
    """
    ATM Emulated circuit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:cctEmul"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CctEmul, self).__init__(ns, pref, tag)



class MplsTunnel(IanaInterfaceType):
    """
    MPLS Tunnel Virtual Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:mplsTunnel"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MplsTunnel, self).__init__(ns, pref, tag)



class Gpon(IanaInterfaceType):
    """
    Gigabit\-capable passive optical networks (G\-PON) as per
    ITU\-T G.948.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:gpon"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Gpon, self).__init__(ns, pref, tag)



class Vdsl(IanaInterfaceType):
    """
    Very H\-Speed Digital Subscrib. Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:vdsl"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Vdsl, self).__init__(ns, pref, tag)



class Pos(IanaInterfaceType):
    """
    Packet over SONET/SDH Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:pos"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Pos, self).__init__(ns, pref, tag)



class Ieee8023adLag(IanaInterfaceType):
    """
    IEEE 802.3ad Link Aggregate.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ieee8023adLag"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ieee8023adLag, self).__init__(ns, pref, tag)



class DocsCableMaclayer(IanaInterfaceType):
    """
    CATV Mac Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:docsCableMaclayer"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DocsCableMaclayer, self).__init__(ns, pref, tag)



class DocsCableMCmtsDownstream(IanaInterfaceType):
    """
    CATV Modular CMTS Downstream Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:docsCableMCmtsDownstream"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DocsCableMCmtsDownstream, self).__init__(ns, pref, tag)



class Ppp(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ppp"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ppp, self).__init__(ns, pref, tag)



class FrameRelay(IanaInterfaceType):
    """
    DTE only.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:frameRelay"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FrameRelay, self).__init__(ns, pref, tag)



class Eplrs(IanaInterfaceType):
    """
    Ext Pos Loc Report Sys.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:eplrs"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Eplrs, self).__init__(ns, pref, tag)



class VmwareNicTeam(IanaInterfaceType):
    """
    VMware NIC Team.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:vmwareNicTeam"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VmwareNicTeam, self).__init__(ns, pref, tag)



class CableDownstreamRfPort(IanaInterfaceType):
    """
    CATV downstream RF Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:cableDownstreamRfPort"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CableDownstreamRfPort, self).__init__(ns, pref, tag)



class MacSecUncontrolledIF(IanaInterfaceType):
    """
    MACSecUncontrolled.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:macSecUncontrolledIF"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MacSecUncontrolledIF, self).__init__(ns, pref, tag)



class Iso88023Csmacd(IanaInterfaceType):
    """
    Deprecated via RFC 3635.
    Use ethernetCsmacd(6) instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:iso88023Csmacd"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Iso88023Csmacd, self).__init__(ns, pref, tag)



class Usb(IanaInterfaceType):
    """
    USB Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:usb"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Usb, self).__init__(ns, pref, tag)



class AtmFuni(IanaInterfaceType):
    """
    ATM FUNI.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:atmFuni"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AtmFuni, self).__init__(ns, pref, tag)



class TeLink(IanaInterfaceType):
    """
    TE Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:teLink"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TeLink, self).__init__(ns, pref, tag)



class Pon622(IanaInterfaceType):
    """
    FSAN 622Mb Symetrical PON interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:pon622"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Pon622, self).__init__(ns, pref, tag)



class Econet(IanaInterfaceType):
    """
    Acorn Econet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:econet"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Econet, self).__init__(ns, pref, tag)



class Tdlc(IanaInterfaceType):
    """
    IBM twinaxial data link control.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:tdlc"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Tdlc, self).__init__(ns, pref, tag)



class Ds0Bundle(IanaInterfaceType):
    """
    Group of ds0s on the same ds1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ds0Bundle"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ds0Bundle, self).__init__(ns, pref, tag)



class Fast(IanaInterfaceType):
    """
    Fast channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:fast"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Fast, self).__init__(ns, pref, tag)



class Ieee1394(IanaInterfaceType):
    """
    IEEE1394 High Performance Serial Bus.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ieee1394"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ieee1394, self).__init__(ns, pref, tag)



class CblVectaStar(IanaInterfaceType):
    """
    Cambridge Broadband Networks Limited VectaStar.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:cblVectaStar"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CblVectaStar, self).__init__(ns, pref, tag)



class Rsrb(IanaInterfaceType):
    """
    Remote Source Route Bridging.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:rsrb"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Rsrb, self).__init__(ns, pref, tag)



class FrameRelayInterconnect(IanaInterfaceType):
    """
    Obsolete; use either
    frameRelay(32) or frameRelayService(44).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:frameRelayInterconnect"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FrameRelayInterconnect, self).__init__(ns, pref, tag)



class Isdns(IanaInterfaceType):
    """
    ISDN S/T interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:isdns"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Isdns, self).__init__(ns, pref, tag)



class PppMultilinkBundle(IanaInterfaceType):
    """
    PPP Multilink Bundle.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:pppMultilinkBundle"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PppMultilinkBundle, self).__init__(ns, pref, tag)



class Aflane8025(IanaInterfaceType):
    """
    ATM Emulated LAN for 802.5.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:aflane8025"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Aflane8025, self).__init__(ns, pref, tag)



class Lapb(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:lapb"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Lapb, self).__init__(ns, pref, tag)



class Aflane8023(IanaInterfaceType):
    """
    ATM Emulated LAN for 802.3.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:aflane8023"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Aflane8023, self).__init__(ns, pref, tag)



class Lapd(IanaInterfaceType):
    """
    Link Access Protocol D.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:lapd"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Lapd, self).__init__(ns, pref, tag)



class Isdnu(IanaInterfaceType):
    """
    ISDN U interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:isdnu"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Isdnu, self).__init__(ns, pref, tag)



class Lapf(IanaInterfaceType):
    """
    LAP F.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:lapf"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Lapf, self).__init__(ns, pref, tag)



class CapwapWtpVirtualRadio(IanaInterfaceType):
    """
    WTP Virtual Radio Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:capwapWtpVirtualRadio"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CapwapWtpVirtualRadio, self).__init__(ns, pref, tag)



class IfVfiType(IanaInterfaceType):
    """
    VPLS Forwarding Instance Interface Type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ifVfiType"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IfVfiType, self).__init__(ns, pref, tag)



class X25huntGroup(IanaInterfaceType):
    """
    X25 Hunt Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:x25huntGroup"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(X25huntGroup, self).__init__(ns, pref, tag)



class Para(IanaInterfaceType):
    """
    Parallel\-port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:para"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Para, self).__init__(ns, pref, tag)



class MacSecControlledIF(IanaInterfaceType):
    """
    MACSecControlled.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:macSecControlledIF"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MacSecControlledIF, self).__init__(ns, pref, tag)



class Iso88024TokenBus(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:iso88024TokenBus"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Iso88024TokenBus, self).__init__(ns, pref, tag)



class LocalTalk(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:localTalk"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LocalTalk, self).__init__(ns, pref, tag)



class Hyperchannel(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:hyperchannel"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Hyperchannel, self).__init__(ns, pref, tag)



class MediaMailOverIp(IanaInterfaceType):
    """
    Multimedia Mail over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:mediaMailOverIp"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MediaMailOverIp, self).__init__(ns, pref, tag)



class IfGsn(IanaInterfaceType):
    """
    HIPPI\-6400.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:if-gsn"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IfGsn, self).__init__(ns, pref, tag)



class CapwapDot11Profile(IanaInterfaceType):
    """
    WLAN Profile Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:capwapDot11Profile"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CapwapDot11Profile, self).__init__(ns, pref, tag)



class L3ipxvlan(IanaInterfaceType):
    """
    Layer 3 Virtual LAN using IPX.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:l3ipxvlan"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L3ipxvlan, self).__init__(ns, pref, tag)



class AtmSubInterface(IanaInterfaceType):
    """
    ATM Sub Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:atmSubInterface"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AtmSubInterface, self).__init__(ns, pref, tag)



class PrimaryISDN(IanaInterfaceType):
    """
    No longer used.  See also RFC 2127.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:primaryISDN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PrimaryISDN, self).__init__(ns, pref, tag)



class Proteon80Mbit(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:proteon80Mbit"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Proteon80Mbit, self).__init__(ns, pref, tag)



class Iso88026Man(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:iso88026Man"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Iso88026Man, self).__init__(ns, pref, tag)



class DigitalWrapperOverheadChannel(IanaInterfaceType):
    """
    Digital Wrapper.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:digitalWrapperOverheadChannel"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DigitalWrapperOverheadChannel, self).__init__(ns, pref, tag)



class DocsCableUpstreamChannel(IanaInterfaceType):
    """
    CATV Upstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:docsCableUpstreamChannel"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DocsCableUpstreamChannel, self).__init__(ns, pref, tag)



class OpticalChannel(IanaInterfaceType):
    """
    Optical Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:opticalChannel"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OpticalChannel, self).__init__(ns, pref, tag)



class EthernetCsmacd(IanaInterfaceType):
    """
    For all Ethernet\-like interfaces, regardless of speed,
    as per RFC 3635.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ethernetCsmacd"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(EthernetCsmacd, self).__init__(ns, pref, tag)



class Bits(IanaInterfaceType):
    """
    bitsport.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:bits"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Bits, self).__init__(ns, pref, tag)



class Tunnel(IanaInterfaceType):
    """
    Encapsulation interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:tunnel"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Tunnel, self).__init__(ns, pref, tag)



class Hdsl2(IanaInterfaceType):
    """
    High Bit\-Rate DSL \- 2nd generation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:hdsl2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Hdsl2, self).__init__(ns, pref, tag)



class FrameRelayService(IanaInterfaceType):
    """
    FRNETSERV\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:frameRelayService"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FrameRelayService, self).__init__(ns, pref, tag)



class Mpls(IanaInterfaceType):
    """
    MPLS.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:mpls"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Mpls, self).__init__(ns, pref, tag)



class Ieee80211(IanaInterfaceType):
    """
    Radio spread spectrum.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ieee80211"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ieee80211, self).__init__(ns, pref, tag)



class Ieee80212(IanaInterfaceType):
    """
    100BaseVG.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ieee80212"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ieee80212, self).__init__(ns, pref, tag)



class MocaVersion1(IanaInterfaceType):
    """
    MultiMedia over Coax Alliance (MoCA) Interface
    as documented in information provided privately to IANA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:mocaVersion1"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MocaVersion1, self).__init__(ns, pref, tag)



class Sonet(IanaInterfaceType):
    """
    SONET or SDH.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:sonet"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Sonet, self).__init__(ns, pref, tag)



class Escon(IanaInterfaceType):
    """
    IBM Enterprise Systems Connection.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:escon"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Escon, self).__init__(ns, pref, tag)



class AluEponLogicalLink(IanaInterfaceType):
    """
    The emulation of a point\-to\-point link over the EPON
    layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:aluEponLogicalLink"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AluEponLogicalLink, self).__init__(ns, pref, tag)



class G703at2mb(IanaInterfaceType):
    """
    Obsolete; see DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:g703at2mb"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(G703at2mb, self).__init__(ns, pref, tag)



class Ultra(IanaInterfaceType):
    """
    Ultra Technologies.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ultra"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ultra, self).__init__(ns, pref, tag)



class DvbRccDownstream(IanaInterfaceType):
    """
    DVB\-RCC Downstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:dvbRccDownstream"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DvbRccDownstream, self).__init__(ns, pref, tag)



class SipTg(IanaInterfaceType):
    """
    SIP Trunk Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:sipTg"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SipTg, self).__init__(ns, pref, tag)



class SmdsIcip(IanaInterfaceType):
    """
    SMDS InterCarrier Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:smdsIcip"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SmdsIcip, self).__init__(ns, pref, tag)



class Bridge(IanaInterfaceType):
    """
    Transparent bridge interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:bridge"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Bridge, self).__init__(ns, pref, tag)



class AtmLogical(IanaInterfaceType):
    """
    ATM Logical Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:atmLogical"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AtmLogical, self).__init__(ns, pref, tag)



class PropPointToPointSerial(IanaInterfaceType):
    """
    Proprietary serial.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:propPointToPointSerial"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PropPointToPointSerial, self).__init__(ns, pref, tag)



class V35(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:v35"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(V35, self).__init__(ns, pref, tag)



class V36(IanaInterfaceType):
    """
    CCITT V.36.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:v36"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(V36, self).__init__(ns, pref, tag)



class V37(IanaInterfaceType):
    """
    V.37.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:v37"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(V37, self).__init__(ns, pref, tag)



class Ip(IanaInterfaceType):
    """
    IP (for APPN HPR in IP networks).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ip"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ip, self).__init__(ns, pref, tag)



class Gr303IDT(IanaInterfaceType):
    """
    Integrated Digital Terminal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:gr303IDT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Gr303IDT, self).__init__(ns, pref, tag)



class BasicISDN(IanaInterfaceType):
    """
    No longer used.  See also RFC 2127.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:basicISDN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(BasicISDN, self).__init__(ns, pref, tag)



class G703at64k(IanaInterfaceType):
    """
    CCITT G703 at 64Kbps.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:g703at64k"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(G703at64k, self).__init__(ns, pref, tag)



class ArcnetPlus(IanaInterfaceType):
    """
    ARCnet Plus.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:arcnetPlus"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ArcnetPlus, self).__init__(ns, pref, tag)



class Pip(IanaInterfaceType):
    """
    Provider Instance Port on a bridge per IEEE 802.1ah PBB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:pip"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Pip, self).__init__(ns, pref, tag)



class Dtm(IanaInterfaceType):
    """
    Dynamic synchronous Transfer Mode.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:dtm"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Dtm, self).__init__(ns, pref, tag)



class Slip(IanaInterfaceType):
    """
    Generic SLIP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:slip"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Slip, self).__init__(ns, pref, tag)



class Hiperlan2(IanaInterfaceType):
    """
    HIPERLAN Type 2 Radio Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:hiperlan2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Hiperlan2, self).__init__(ns, pref, tag)



class Adsl(IanaInterfaceType):
    """
    Asymmetric Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:adsl"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Adsl, self).__init__(ns, pref, tag)



class Ieee80216WMAN(IanaInterfaceType):
    """
    IEEE 802.16 WMAN interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ieee80216WMAN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ieee80216WMAN, self).__init__(ns, pref, tag)



class AtmIma(IanaInterfaceType):
    """
    ATM IMA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:atmIma"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AtmIma, self).__init__(ns, pref, tag)



class Isdn(IanaInterfaceType):
    """
    ISDN and X.25.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:isdn"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Isdn, self).__init__(ns, pref, tag)



class CapwapDot11Bss(IanaInterfaceType):
    """
    WLAN BSS Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:capwapDot11Bss"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CapwapDot11Bss, self).__init__(ns, pref, tag)



class Sip(IanaInterfaceType):
    """
    SMDS, coffee.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:sip"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Sip, self).__init__(ns, pref, tag)



class PdnEtherLoop2(IanaInterfaceType):
    """
    Paradyne EtherLoop 2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:pdnEtherLoop2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PdnEtherLoop2, self).__init__(ns, pref, tag)



class VoiceEBS(IanaInterfaceType):
    """
    Voice P\-phone EBS physical interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceEBS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceEBS, self).__init__(ns, pref, tag)



class IpForward(IanaInterfaceType):
    """
    IP Forwarding Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ipForward"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IpForward, self).__init__(ns, pref, tag)



class Iso88025CRFPInt(IanaInterfaceType):
    """
    ISO 802.5 CRFP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:iso88025CRFPInt"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Iso88025CRFPInt, self).__init__(ns, pref, tag)



class PropVirtual(IanaInterfaceType):
    """
    Proprietary virtual/internal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:propVirtual"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PropVirtual, self).__init__(ns, pref, tag)



class WwanPP(IanaInterfaceType):
    """
    3GPP WWAN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:wwanPP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(WwanPP, self).__init__(ns, pref, tag)



class Other(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:other"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Other, self).__init__(ns, pref, tag)



class Pon155(IanaInterfaceType):
    """
    FSAN 155Mb Symetrical PON interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:pon155"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Pon155, self).__init__(ns, pref, tag)



class Qam(IanaInterfaceType):
    """
    RF Qam Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:qam"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Qam, self).__init__(ns, pref, tag)



class OtnOdu(IanaInterfaceType):
    """
    OTN Optical Data Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:otnOdu"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OtnOdu, self).__init__(ns, pref, tag)



class Iso88025Fiber(IanaInterfaceType):
    """
    ISO 802.5j Fiber Token Ring.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:iso88025Fiber"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Iso88025Fiber, self).__init__(ns, pref, tag)



class Channel(IanaInterfaceType):
    """
    Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:channel"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Channel, self).__init__(ns, pref, tag)



class VoiceEMFGD(IanaInterfaceType):
    """
    Voice E&M Feature Group D.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceEMFGD"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceEMFGD, self).__init__(ns, pref, tag)



class AluGponPhysicalUni(IanaInterfaceType):
    """
    GPON physical User to Network interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:aluGponPhysicalUni"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AluGponPhysicalUni, self).__init__(ns, pref, tag)



class A12MppSwitch(IanaInterfaceType):
    """
    Avalon Parallel Processor.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:a12MppSwitch"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(A12MppSwitch, self).__init__(ns, pref, tag)



class Ilan(IanaInterfaceType):
    """
    Internal LAN on a bridge per IEEE 802.1ap.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ilan"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ilan, self).__init__(ns, pref, tag)



class PdnEtherLoop1(IanaInterfaceType):
    """
    Paradyne EtherLoop 1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:pdnEtherLoop1"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PdnEtherLoop1, self).__init__(ns, pref, tag)



class X213(IanaInterfaceType):
    """
    CCITT\-ITU X213.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:x213"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(X213, self).__init__(ns, pref, tag)



class SonetPath(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:sonetPath"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SonetPath, self).__init__(ns, pref, tag)



class VoiceFGDEANA(IanaInterfaceType):
    """
    Voice FGD Exchange Access North American.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:voiceFGDEANA"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VoiceFGDEANA, self).__init__(ns, pref, tag)



class Iso88025TokenRing(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:iso88025TokenRing"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Iso88025TokenRing, self).__init__(ns, pref, tag)



class PropAtm(IanaInterfaceType):
    """
    Proprietary ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:propAtm"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PropAtm, self).__init__(ns, pref, tag)



class AluEponPhysicalUni(IanaInterfaceType):
    """
    EPON physical User to Network interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:aluEponPhysicalUni"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AluEponPhysicalUni, self).__init__(ns, pref, tag)



class StackToStack(IanaInterfaceType):
    """
    IBM stackToStack.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:stackToStack"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(StackToStack, self).__init__(ns, pref, tag)



class FrForward(IanaInterfaceType):
    """
    Frame Forward Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:frForward"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FrForward, self).__init__(ns, pref, tag)



class Homepna(IanaInterfaceType):
    """
    HomePNA ITU\-T G.989.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:homepna"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Homepna, self).__init__(ns, pref, tag)



class Sdsl(IanaInterfaceType):
    """
    Symmetric Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:sdsl"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Sdsl, self).__init__(ns, pref, tag)



class VirtualIpAddress(IanaInterfaceType):
    """
    IBM VIPA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:virtualIpAddress"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VirtualIpAddress, self).__init__(ns, pref, tag)



class Bsc(IanaInterfaceType):
    """
    Bisynchronous Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:bsc"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Bsc, self).__init__(ns, pref, tag)



class AtmRadio(IanaInterfaceType):
    """
    ATM over radio links.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:atmRadio"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AtmRadio, self).__init__(ns, pref, tag)



class AviciOpticalEther(IanaInterfaceType):
    """
    Avici Optical Ethernet Aggregate.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:aviciOpticalEther"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AviciOpticalEther, self).__init__(ns, pref, tag)



class G9981(IanaInterfaceType):
    """
    G.998.1 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:g9981"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(G9981, self).__init__(ns, pref, tag)



class FibreChannel(IanaInterfaceType):
    """
    Fibre Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:fibreChannel"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FibreChannel, self).__init__(ns, pref, tag)



class Shdsl(IanaInterfaceType):
    """
    Multirate HDSL2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:shdsl"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Shdsl, self).__init__(ns, pref, tag)



class Eon(IanaInterfaceType):
    """
    CLNP over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:eon"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Eon, self).__init__(ns, pref, tag)



class H323Gatekeeper(IanaInterfaceType):
    """
    H323 Gatekeeper.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:h323Gatekeeper"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(H323Gatekeeper, self).__init__(ns, pref, tag)



class Hdh1822(IanaInterfaceType):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:hdh1822"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Hdh1822, self).__init__(ns, pref, tag)



class DvbRccUpstream(IanaInterfaceType):
    """
    DVB\-RCC Upstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:dvbRccUpstream"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DvbRccUpstream, self).__init__(ns, pref, tag)



class Nsip(IanaInterfaceType):
    """
    XNS over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:nsip"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Nsip, self).__init__(ns, pref, tag)



class TranspHdlc(IanaInterfaceType):
    """
    Transp HDLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:transpHdlc"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TranspHdlc, self).__init__(ns, pref, tag)



class TermPad(IanaInterfaceType):
    """
    CCITT\-ITU X.3 PAD Facility.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:termPad"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TermPad, self).__init__(ns, pref, tag)



class IpOverCdlc(IanaInterfaceType):
    """
    IBM ipOverCdlc.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ipOverCdlc"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IpOverCdlc, self).__init__(ns, pref, tag)



class Ces(IanaInterfaceType):
    """
    Circuit Emulation Service.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:ces"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ces, self).__init__(ns, pref, tag)



class Modem(IanaInterfaceType):
    """
    Generic modem.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:iana-if-type", pref="iana-if-type", tag="iana-if-type:modem"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Modem, self).__init__(ns, pref, tag)



