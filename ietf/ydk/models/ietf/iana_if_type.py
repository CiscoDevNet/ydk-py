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
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
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


class A12Mppswitch(Identity):
    """
    Avalon Parallel Processor.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(A12Mppswitch, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:a12MppSwitch")


class Aal2(Identity):
    """
    ATM adaptation layer 2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Aal2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aal2")


class Aal5(Identity):
    """
    AAL5 over ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Aal5, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aal5")


class Actelismetaloop(Identity):
    """
    Acteleis proprietary MetaLOOP High Speed Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Actelismetaloop, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:actelisMetaLOOP")


class Adsl(Identity):
    """
    Asymmetric Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Adsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:adsl")


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


class Adsl2Plus(Identity):
    """
    Asymmetric Digital Subscriber Loop Version 2 \-
    Version 2 Plus and all variants.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Adsl2Plus, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:adsl2plus")


class Aflane8023(Identity):
    """
    ATM Emulated LAN for 802.3.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Aflane8023, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aflane8023")


class Aflane8025(Identity):
    """
    ATM Emulated LAN for 802.5.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Aflane8025, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aflane8025")


class Aluelp(Identity):
    """
    Alcatel\-Lucent Ethernet Link Protection.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Aluelp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluELP")


class Aluepon(Identity):
    """
    Ethernet Passive Optical Networks (E\-PON).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Aluepon, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluEpon")


class Alueponlogicallink(Identity):
    """
    The emulation of a point\-to\-point link over the EPON
    layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Alueponlogicallink, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluEponLogicalLink")


class Aluepononu(Identity):
    """
    EPON Optical Network Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Aluepononu, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluEponOnu")


class Alueponphysicaluni(Identity):
    """
    EPON physical User to Network interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Alueponphysicaluni, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluEponPhysicalUni")


class Alugpononu(Identity):
    """
    GPON Optical Network Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Alugpononu, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluGponOnu")


class Alugponphysicaluni(Identity):
    """
    GPON physical User to Network interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Alugponphysicaluni, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aluGponPhysicalUni")


class Arap(Identity):
    """
    Appletalk Remote Access Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Arap, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:arap")


class Arcnet(Identity):
    """
    ARCnet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Arcnet, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:arcnet")


class Arcnetplus(Identity):
    """
    ARCnet Plus.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Arcnetplus, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:arcnetPlus")


class Async(Identity):
    """
    Asynchronous Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Async, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:async")


class Atm(Identity):
    """
    ATM cells.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Atm, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atm")


class Atmbond(Identity):
    """
    atmbond.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Atmbond, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmbond")


class Atmdxi(Identity):
    """
    ATM DXI.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Atmdxi, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmDxi")


class Atmfuni(Identity):
    """
    ATM FUNI.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Atmfuni, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmFuni")


class Atmima(Identity):
    """
    ATM IMA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Atmima, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmIma")


class Atmlogical(Identity):
    """
    ATM Logical Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Atmlogical, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmLogical")


class Atmradio(Identity):
    """
    ATM over radio links.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Atmradio, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmRadio")


class Atmsubinterface(Identity):
    """
    ATM Sub Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Atmsubinterface, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmSubInterface")


class Atmvciendpt(Identity):
    """
    ATM VCI End Point.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Atmvciendpt, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmVciEndPt")


class Atmvirtual(Identity):
    """
    ATM Virtual Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Atmvirtual, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:atmVirtual")


class Aviciopticalether(Identity):
    """
    Avici Optical Ethernet Aggregate.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Aviciopticalether, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:aviciOpticalEther")


class Basicisdn(Identity):
    """
    No longer used.  See also RFC 2127.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Basicisdn, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:basicISDN")


class Bgppolicyaccounting(Identity):
    """
    BGP Policy Accounting.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Bgppolicyaccounting, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:bgppolicyaccounting")


class Bits(Identity):
    """
    bitsport.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Bits, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:bits")


class Bridge(Identity):
    """
    Transparent bridge interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Bridge, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:bridge")


class Bsc(Identity):
    """
    Bisynchronous Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Bsc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:bsc")


class Cabledownstreamrfport(Identity):
    """
    CATV downstream RF Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Cabledownstreamrfport, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:cableDownstreamRfPort")


class Capwapdot11Bss(Identity):
    """
    WLAN BSS Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Capwapdot11Bss, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:capwapDot11Bss")


class Capwapdot11Profile(Identity):
    """
    WLAN Profile Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Capwapdot11Profile, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:capwapDot11Profile")


class Capwapwtpvirtualradio(Identity):
    """
    WTP Virtual Radio Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Capwapwtpvirtualradio, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:capwapWtpVirtualRadio")


class Cblvectastar(Identity):
    """
    Cambridge Broadband Networks Limited VectaStar.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Cblvectastar, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:cblVectaStar")


class Cctemul(Identity):
    """
    ATM Emulated circuit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Cctemul, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:cctEmul")


class Ces(Identity):
    """
    Circuit Emulation Service.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ces, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ces")


class Channel(Identity):
    """
    Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Channel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:channel")


class Ciscoislvlan(Identity):
    """
    Layer 2 Virtual LAN using Cisco ISL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ciscoislvlan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ciscoISLvlan")


class Cnr(Identity):
    """
    Combat Net Radio.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Cnr, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:cnr")


class Coffee(Identity):
    """
    Coffee pot.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Coffee, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:coffee")


class Compositelink(Identity):
    """
    Avici Composite Link Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Compositelink, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:compositeLink")


class Dcn(Identity):
    """
    Data Communications Network.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dcn, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dcn")


class Ddnx25(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ddnx25, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ddnX25")


class Digitalpowerline(Identity):
    """
    IP over Power Lines.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Digitalpowerline, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:digitalPowerline")


class Digitalwrapperoverheadchannel(Identity):
    """
    Digital Wrapper.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Digitalwrapperoverheadchannel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:digitalWrapperOverheadChannel")


class Dlsw(Identity):
    """
    Data Link Switching.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dlsw, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dlsw")


class Docscabledownstream(Identity):
    """
    CATV Downstream interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Docscabledownstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:docsCableDownstream")


class Docscablemaclayer(Identity):
    """
    CATV Mac Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Docscablemaclayer, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:docsCableMaclayer")


class Docscablemcmtsdownstream(Identity):
    """
    CATV Modular CMTS Downstream Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Docscablemcmtsdownstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:docsCableMCmtsDownstream")


class Docscableupstream(Identity):
    """
    CATV Upstream interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Docscableupstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:docsCableUpstream")


class Docscableupstreamchannel(Identity):
    """
    CATV Upstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Docscableupstreamchannel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:docsCableUpstreamChannel")


class Docscableupstreamrfport(Identity):
    """
    DOCSIS CATV Upstream RF Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Docscableupstreamrfport, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:docsCableUpstreamRfPort")


class Ds0(Identity):
    """
    Digital Signal Level 0.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ds0, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ds0")


class Ds0Bundle(Identity):
    """
    Group of ds0s on the same ds1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ds0Bundle, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ds0Bundle")


class Ds1(Identity):
    """
    DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ds1, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ds1")


class Ds1Fdl(Identity):
    """
    Facility Data Link (4Kbps) on a DS1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ds1Fdl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ds1FDL")


class Ds3(Identity):
    """
    DS3\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ds3, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ds3")


class Dtm(Identity):
    """
    Dynamic synchronous Transfer Mode.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dtm, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dtm")


class Dvbasiin(Identity):
    """
    DVB\-ASI Input.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dvbasiin, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbAsiIn")


class Dvbasiout(Identity):
    """
    DVB\-ASI Output.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dvbasiout, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbAsiOut")


class Dvbrccdownstream(Identity):
    """
    DVB\-RCC Downstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dvbrccdownstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbRccDownstream")


class Dvbrccmaclayer(Identity):
    """
    DVB\-RCC MAC Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dvbrccmaclayer, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbRccMacLayer")


class Dvbrccupstream(Identity):
    """
    DVB\-RCC Upstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dvbrccupstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbRccUpstream")


class Dvbrcsmaclayer(Identity):
    """
    DVB\-RCS MAC Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dvbrcsmaclayer, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbRcsMacLayer")


class Dvbrcstdma(Identity):
    """
    DVB\-RCS TDMA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dvbrcstdma, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbRcsTdma")


class Dvbtdm(Identity):
    """
    DVB Satellite TDM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Dvbtdm, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:dvbTdm")


class E1(Identity):
    """
    Obsolete; see DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(E1, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:e1")


class Econet(Identity):
    """
    Acorn Econet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Econet, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:econet")


class Eon(Identity):
    """
    CLNP over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Eon, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:eon")


class Eplrs(Identity):
    """
    Ext Pos Loc Report Sys.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Eplrs, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:eplrs")


class Escon(Identity):
    """
    IBM Enterprise Systems Connection.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Escon, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:escon")


class Ethernet3Mbit(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ethernet3Mbit, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ethernet3Mbit")


class Ethernetcsmacd(Identity):
    """
    For all Ethernet\-like interfaces, regardless of speed,
    as per RFC 3635.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ethernetcsmacd, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ethernetCsmacd")


class Fast(Identity):
    """
    Fast channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Fast, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:fast")


class Fastether(Identity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Fastether, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:fastEther")


class Fastetherfx(Identity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Fastetherfx, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:fastEtherFX")


class Fciplink(Identity):
    """
    FCIP Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Fciplink, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:fcipLink")


class Fddi(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Fddi, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:fddi")


class Fibrechannel(Identity):
    """
    Fibre Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Fibrechannel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:fibreChannel")


class Framerelay(Identity):
    """
    DTE only.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Framerelay, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frameRelay")


class Framerelayinterconnect(Identity):
    """
    Obsolete; use either
    frameRelay(32) or frameRelayService(44).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Framerelayinterconnect, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frameRelayInterconnect")


class Framerelaympi(Identity):
    """
    Multiproto Interconnect over FR.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Framerelaympi, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frameRelayMPI")


class Framerelayservice(Identity):
    """
    FRNETSERV\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Framerelayservice, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frameRelayService")


class Frdlciendpt(Identity):
    """
    Frame Relay DLCI End Point.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Frdlciendpt, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frDlciEndPt")


class Frf16Mfrbundle(Identity):
    """
    FRF.16 Multilink Frame Relay.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Frf16Mfrbundle, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frf16MfrBundle")


class Frforward(Identity):
    """
    Frame Forward Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Frforward, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:frForward")


class G703At2Mb(Identity):
    """
    Obsolete; see DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(G703At2Mb, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:g703at2mb")


class G703At64K(Identity):
    """
    CCITT G703 at 64Kbps.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(G703At64K, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:g703at64k")


class G9981(Identity):
    """
    G.998.1 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(G9981, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:g9981")


class G9982(Identity):
    """
    G.998.2 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(G9982, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:g9982")


class G9983(Identity):
    """
    G.998.3 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(G9983, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:g9983")


class Gfp(Identity):
    """
    Generic Framing Procedure (GFP).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Gfp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:gfp")


class Gigabitethernet(Identity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Gigabitethernet, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:gigabitEthernet")


class Gpon(Identity):
    """
    Gigabit\-capable passive optical networks (G\-PON) as per
    ITU\-T G.948.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Gpon, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:gpon")


class Gr303Idt(Identity):
    """
    Integrated Digital Terminal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Gr303Idt, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:gr303IDT")


class Gr303Rdt(Identity):
    """
    Remote Digital Terminal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Gr303Rdt, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:gr303RDT")


class Gtp(Identity):
    """
    GTP (GPRS Tunneling Protocol).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Gtp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:gtp")


class H323Gatekeeper(Identity):
    """
    H323 Gatekeeper.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(H323Gatekeeper, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:h323Gatekeeper")


class H323Proxy(Identity):
    """
    H323 Voice and Video Proxy.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(H323Proxy, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:h323Proxy")


class Hdh1822(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hdh1822, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hdh1822")


class Hdlc(Identity):
    """
    HDLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hdlc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hdlc")


class Hdsl2(Identity):
    """
    High Bit\-Rate DSL \- 2nd generation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hdsl2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hdsl2")


class Hiperlan2(Identity):
    """
    HIPERLAN Type 2 Radio Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hiperlan2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hiperlan2")


class Hippi(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hippi, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hippi")


class Hippiinterface(Identity):
    """
    HIPPI interfaces.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hippiinterface, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hippiInterface")


class Homepna(Identity):
    """
    HomePNA ITU\-T G.989.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Homepna, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:homepna")


class Hostpad(Identity):
    """
    CCITT\-ITU X.29 PAD Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hostpad, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hostPad")


class Hssi(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hssi, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hssi")


class Hyperchannel(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Hyperchannel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:hyperchannel")


class Ibm370Parchan(Identity):
    """
    IBM System 360/370 OEMI Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ibm370Parchan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ibm370parChan")


class Idsl(Identity):
    """
    Digital Subscriber Loop over ISDN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Idsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:idsl")


class Ieee1394(Identity):
    """
    IEEE1394 High Performance Serial Bus.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ieee1394, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ieee1394")


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


class Ieee802154(Identity):
    """
    IEEE 802.15.4 WPAN interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ieee802154, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ieee802154")


class Ieee80216Wman(Identity):
    """
    IEEE 802.16 WMAN interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ieee80216Wman, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ieee80216WMAN")


class Ieee8023Adlag(Identity):
    """
    IEEE 802.3ad Link Aggregate.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ieee8023Adlag, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ieee8023adLag")


class IfGsn(Identity):
    """
    HIPPI\-6400.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(IfGsn, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:if-gsn")


class Ifpwtype(Identity):
    """
    Pseudowire interface type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ifpwtype, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ifPwType")


class Ifvfitype(Identity):
    """
    VPLS Forwarding Instance Interface Type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ifvfitype, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ifVfiType")


class Ilan(Identity):
    """
    Internal LAN on a bridge per IEEE 802.1ap.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ilan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ilan")


class Imt(Identity):
    """
    Inter\-Machine Trunks.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Imt, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:imt")


class Infiniband(Identity):
    """
    Infiniband.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Infiniband, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:infiniband")


class Interleave(Identity):
    """
    Interleave channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Interleave, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:interleave")


class Ip(Identity):
    """
    IP (for APPN HPR in IP networks).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ip")


class Ipforward(Identity):
    """
    IP Forwarding Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ipforward, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ipForward")


class Ipoveratm(Identity):
    """
    IBM ipOverAtm.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ipoveratm, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ipOverAtm")


class Ipovercdlc(Identity):
    """
    IBM ipOverCdlc.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ipovercdlc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ipOverCdlc")


class Ipoverclaw(Identity):
    """
    IBM Common Link Access to Workstn.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ipoverclaw, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ipOverClaw")


class Ipswitch(Identity):
    """
    IP Switching Objects.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ipswitch, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ipSwitch")


class Isdn(Identity):
    """
    ISDN and X.25.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Isdn, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:isdn")


class Isdns(Identity):
    """
    ISDN S/T interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Isdns, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:isdns")


class Isdnu(Identity):
    """
    ISDN U interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Isdnu, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:isdnu")


class Iso88022Llc(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88022Llc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88022llc")


class Iso88023Csmacd(Identity):
    """
    Deprecated via RFC 3635.
    Use ethernetCsmacd(6) instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88023Csmacd, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88023Csmacd")


class Iso88024Tokenbus(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88024Tokenbus, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88024TokenBus")


class Iso88025Crfpint(Identity):
    """
    ISO 802.5 CRFP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88025Crfpint, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88025CRFPInt")


class Iso88025Dtr(Identity):
    """
    ISO 802.5r DTR.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88025Dtr, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88025Dtr")


class Iso88025Fiber(Identity):
    """
    ISO 802.5j Fiber Token Ring.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88025Fiber, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88025Fiber")


class Iso88025Tokenring(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88025Tokenring, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88025TokenRing")


class Iso88026Man(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Iso88026Man, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:iso88026Man")


class Isup(Identity):
    """
    ISUP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Isup, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:isup")


class L2Vlan(Identity):
    """
    Layer 2 Virtual LAN using 802.1Q.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(L2Vlan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:l2vlan")


class L3Ipvlan(Identity):
    """
    Layer 3 Virtual LAN using IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(L3Ipvlan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:l3ipvlan")


class L3Ipxvlan(Identity):
    """
    Layer 3 Virtual LAN using IPX.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(L3Ipxvlan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:l3ipxvlan")


class Lapb(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Lapb, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:lapb")


class Lapd(Identity):
    """
    Link Access Protocol D.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Lapd, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:lapd")


class Lapf(Identity):
    """
    LAP F.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Lapf, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:lapf")


class Linegroup(Identity):
    """
    Interface common to multiple lines.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Linegroup, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:linegroup")


class Lmp(Identity):
    """
    Link Management Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Lmp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:lmp")


class Localtalk(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Localtalk, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:localTalk")


class Macseccontrolledif(Identity):
    """
    MACSecControlled.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Macseccontrolledif, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:macSecControlledIF")


class Macsecuncontrolledif(Identity):
    """
    MACSecUncontrolled.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Macsecuncontrolledif, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:macSecUncontrolledIF")


class Mediamailoverip(Identity):
    """
    Multimedia Mail over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Mediamailoverip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mediaMailOverIp")


class Mfsiglink(Identity):
    """
    Multi\-frequency signaling link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Mfsiglink, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mfSigLink")


class Miox25(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Miox25, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:miox25")


class Mocaversion1(Identity):
    """
    MultiMedia over Coax Alliance (MoCA) Interface
    as documented in information provided privately to IANA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Mocaversion1, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mocaVersion1")


class Modem(Identity):
    """
    Generic modem.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Modem, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:modem")


class Mpc(Identity):
    """
    IBM multi\-protocol channel support.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Mpc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mpc")


class Mpegtransport(Identity):
    """
    MPEG transport interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Mpegtransport, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mpegTransport")


class Mpls(Identity):
    """
    MPLS.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Mpls, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mpls")


class Mplstunnel(Identity):
    """
    MPLS Tunnel Virtual Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Mplstunnel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mplsTunnel")


class Msdsl(Identity):
    """
    Multi\-rate Symmetric DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Msdsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:msdsl")


class Mvl(Identity):
    """
    Multiple Virtual Lines DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Mvl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:mvl")


class Myrinet(Identity):
    """
    Myricom Myrinet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Myrinet, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:myrinet")


class Nfas(Identity):
    """
    Non\-Facility Associated Signaling.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Nfas, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:nfas")


class Nsip(Identity):
    """
    XNS over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Nsip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:nsip")


class Opticalchannel(Identity):
    """
    Optical Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Opticalchannel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:opticalChannel")


class Opticalchannelgroup(Identity):
    """
    Optical Channel Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Opticalchannelgroup, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:opticalChannelGroup")


class Opticaltransport(Identity):
    """
    Optical Transport.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Opticaltransport, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:opticalTransport")


class Other(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Other, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:other")


class Otnodu(Identity):
    """
    OTN Optical Data Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Otnodu, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:otnOdu")


class Otnotu(Identity):
    """
    OTN Optical channel Transport Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Otnotu, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:otnOtu")


class Para(Identity):
    """
    Parallel\-port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Para, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:para")


class Pdnetherloop1(Identity):
    """
    Paradyne EtherLoop 1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Pdnetherloop1, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pdnEtherLoop1")


class Pdnetherloop2(Identity):
    """
    Paradyne EtherLoop 2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Pdnetherloop2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pdnEtherLoop2")


class Pip(Identity):
    """
    Provider Instance Port on a bridge per IEEE 802.1ah PBB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Pip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pip")


class Plc(Identity):
    """
    Power Line Communications.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Plc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:plc")


class Pon155(Identity):
    """
    FSAN 155Mb Symetrical PON interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Pon155, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pon155")


class Pon622(Identity):
    """
    FSAN 622Mb Symetrical PON interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Pon622, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pon622")


class Pos(Identity):
    """
    Packet over SONET/SDH Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Pos, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pos")


class Ppp(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ppp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ppp")


class Pppmultilinkbundle(Identity):
    """
    PPP Multilink Bundle.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Pppmultilinkbundle, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:pppMultilinkBundle")


class Primaryisdn(Identity):
    """
    No longer used.  See also RFC 2127.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Primaryisdn, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:primaryISDN")


class Propatm(Identity):
    """
    Proprietary ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Propatm, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propAtm")


class Propbwap2Mp(Identity):
    """
    PropBroadbandWirelessAccesspt2Multipt (use of this value
    for IEEE 802.16 WMAN interfaces as per IEEE Std 802.16f
    is deprecated, and ieee80216WMAN(237) should be used
    instead).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Propbwap2Mp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propBWAp2Mp")


class Propcnls(Identity):
    """
    Proprietary Connectionless Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Propcnls, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propCnls")


class Propdocswirelessdownstream(Identity):
    """
    Cisco proprietary Downstream.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Propdocswirelessdownstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propDocsWirelessDownstream")


class Propdocswirelessmaclayer(Identity):
    """
    Cisco proprietary Maclayer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Propdocswirelessmaclayer, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propDocsWirelessMaclayer")


class Propdocswirelessupstream(Identity):
    """
    Cisco proprietary Upstream.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Propdocswirelessupstream, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propDocsWirelessUpstream")


class Propmultiplexor(Identity):
    """
    Proprietary multiplexing.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Propmultiplexor, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propMultiplexor")


class Proppointtopointserial(Identity):
    """
    Proprietary serial.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Proppointtopointserial, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propPointToPointSerial")


class Propvirtual(Identity):
    """
    Proprietary virtual/internal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Propvirtual, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propVirtual")


class Propwirelessp2P(Identity):
    """
    Prop. P2P wireless interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Propwirelessp2P, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:propWirelessP2P")


class Proteon10Mbit(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Proteon10Mbit, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:proteon10Mbit")


class Proteon80Mbit(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Proteon80Mbit, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:proteon80Mbit")


class Q2931(Identity):
    """
    Q.2931.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Q2931, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:q2931")


class Qam(Identity):
    """
    RF Qam Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Qam, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:qam")


class Qllc(Identity):
    """
    SNA QLLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Qllc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:qllc")


class Radiomac(Identity):
    """
    MAC layer over radio links.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Radiomac, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:radioMAC")


class Radsl(Identity):
    """
    Rate\-Adapt. Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Radsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:radsl")


class Reachdsl(Identity):
    """
    Long Reach DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Reachdsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:reachDSL")


class Regular1822(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Regular1822, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:regular1822")


class Rfc1483(Identity):
    """
    Multiprotocol over ATM AAL5.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Rfc1483, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:rfc1483")


class Rfc877X25(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Rfc877X25, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:rfc877x25")


class Rpr(Identity):
    """
    Resilient Packet Ring Interface Type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Rpr, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:rpr")


class Rs232(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Rs232, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:rs232")


class Rsrb(Identity):
    """
    Remote Source Route Bridging.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Rsrb, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:rsrb")


class Sdlc(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sdlc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sdlc")


class Sdsl(Identity):
    """
    Symmetric Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sdsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sdsl")


class Shdsl(Identity):
    """
    Multirate HDSL2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Shdsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:shdsl")


class Sip(Identity):
    """
    SMDS, coffee.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sip")


class Sipsig(Identity):
    """
    SIP Signaling.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sipsig, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sipSig")


class Siptg(Identity):
    """
    SIP Trunk Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Siptg, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sipTg")


class Sixtofour(Identity):
    """
    6to4 interface (DEPRECATED).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sixtofour, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sixToFour")


class Slip(Identity):
    """
    Generic SLIP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Slip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:slip")


class Smdsdxi(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Smdsdxi, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:smdsDxi")


class Smdsicip(Identity):
    """
    SMDS InterCarrier Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Smdsicip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:smdsIcip")


class Softwareloopback(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Softwareloopback, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:softwareLoopback")


class Sonet(Identity):
    """
    SONET or SDH.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sonet, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sonet")


class Sonetoverheadchannel(Identity):
    """
    SONET Overhead Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sonetoverheadchannel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sonetOverheadChannel")


class Sonetpath(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sonetpath, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sonetPath")


class Sonetvt(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Sonetvt, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:sonetVT")


class Srp(Identity):
    """
    Spatial Reuse Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Srp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:srp")


class Ss7Siglink(Identity):
    """
    SS7 Signaling Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ss7Siglink, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ss7SigLink")


class Stacktostack(Identity):
    """
    IBM stackToStack.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Stacktostack, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:stackToStack")


class Starlan(Identity):
    """
    Deprecated via RFC 3635.
    Use ethernetCsmacd(6) instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Starlan, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:starLan")


class Tdlc(Identity):
    """
    IBM twinaxial data link control.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Tdlc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:tdlc")


class Telink(Identity):
    """
    TE Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Telink, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:teLink")


class Termpad(Identity):
    """
    CCITT\-ITU X.3 PAD Facility.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Termpad, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:termPad")


class Tr008(Identity):
    """
    TR008.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Tr008, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:tr008")


class Transphdlc(Identity):
    """
    Transp HDLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Transphdlc, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:transpHdlc")


class Tunnel(Identity):
    """
    Encapsulation interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Tunnel, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:tunnel")


class Ultra(Identity):
    """
    Ultra Technologies.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Ultra, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:ultra")


class Usb(Identity):
    """
    USB Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Usb, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:usb")


class V11(Identity):
    """
    CCITT V.11/X.21.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(V11, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:v11")


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


class Vdsl(Identity):
    """
    Very H\-Speed Digital Subscrib. Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Vdsl, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:vdsl")


class Vdsl2(Identity):
    """
    Very high speed digital subscriber line Version 2
    (as per ITU\-T Recommendation G.993.2).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Vdsl2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:vdsl2")


class Virtualipaddress(Identity):
    """
    IBM VIPA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Virtualipaddress, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:virtualIpAddress")


class Virtualtg(Identity):
    """
    Virtual Trunk Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Virtualtg, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:virtualTg")


class Vmwarenicteam(Identity):
    """
    VMware NIC Team.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Vmwarenicteam, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:vmwareNicTeam")


class Vmwarevirtualnic(Identity):
    """
    VMware Virtual Network Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Vmwarevirtualnic, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:vmwareVirtualNic")


class Voicedid(Identity):
    """
    Voice Direct Inward Dialing.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voicedid, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceDID")


class Voiceebs(Identity):
    """
    Voice P\-phone EBS physical interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voiceebs, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceEBS")


class Voiceem(Identity):
    """
    Voice recEive and transMit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voiceem, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceEM")


class Voiceemfgd(Identity):
    """
    Voice E&M Feature Group D.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voiceemfgd, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceEMFGD")


class Voiceencap(Identity):
    """
    Voice encapsulation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voiceencap, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceEncap")


class Voicefgdeana(Identity):
    """
    Voice FGD Exchange Access North American.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voicefgdeana, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceFGDEANA")


class Voicefgdos(Identity):
    """
    Voice FGD Operator Services.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voicefgdos, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceFGDOS")


class Voicefxo(Identity):
    """
    Voice Foreign Exchange Office.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voicefxo, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceFXO")


class Voicefxs(Identity):
    """
    Voice Foreign Exchange Station.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voicefxs, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceFXS")


class Voiceoveratm(Identity):
    """
    Voice over ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voiceoveratm, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceOverAtm")


class Voiceovercable(Identity):
    """
    Voice Over Cable Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voiceovercable, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceOverCable")


class Voiceoverframerelay(Identity):
    """
    Voice Over Frame Relay.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voiceoverframerelay, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceOverFrameRelay")


class Voiceoverip(Identity):
    """
    Voice over IP encapsulation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Voiceoverip, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:voiceOverIp")


class Wwanpp(Identity):
    """
    3GPP WWAN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Wwanpp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:wwanPP")


class Wwanpp2(Identity):
    """
    3GPP2 WWAN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(Wwanpp2, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:wwanPP2")


class X213(Identity):
    """
    CCITT\-ITU X213.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(X213, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:x213")


class X25Huntgroup(Identity):
    """
    X25 Hunt Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(X25Huntgroup, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:x25huntGroup")


class X25Mlp(Identity):
    """
    Multi\-Link Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(X25Mlp, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:x25mlp")


class X25Ple(Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(X25Ple, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:x25ple")


class X86Laps(Identity):
    """
    LAPS based on ITU\-T X.86/Y.1323.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        super(X86Laps, self).__init__("urn:ietf:params:xml:ns:yang:iana-if-type", "iana-if-type", "iana-if-type:x86Laps")


