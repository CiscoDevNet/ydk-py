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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.ietf.ietf_interfaces import InterfaceType_Identity


class IanaInterfaceType_Identity(InterfaceType_Identity):
    """
    This identity is used as a base for all interface types
    defined in the 'ifType definitions' registry.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        InterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['IanaInterfaceType_Identity']['meta_info']


class A12Mppswitch_Identity(IanaInterfaceType_Identity):
    """
    Avalon Parallel Processor.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['A12Mppswitch_Identity']['meta_info']


class Aal2_Identity(IanaInterfaceType_Identity):
    """
    ATM adaptation layer 2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Aal2_Identity']['meta_info']


class Aal5_Identity(IanaInterfaceType_Identity):
    """
    AAL5 over ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Aal5_Identity']['meta_info']


class Actelismetaloop_Identity(IanaInterfaceType_Identity):
    """
    Acteleis proprietary MetaLOOP High Speed Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Actelismetaloop_Identity']['meta_info']


class Adsl2Plus_Identity(IanaInterfaceType_Identity):
    """
    Asymmetric Digital Subscriber Loop Version 2 \-
    Version 2 Plus and all variants.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Adsl2Plus_Identity']['meta_info']


class Adsl2_Identity(IanaInterfaceType_Identity):
    """
    Asymmetric Digital Subscriber Loop Version 2
    (DEPRECATED/OBSOLETED \- please use adsl2plus(238)
    instead).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Adsl2_Identity']['meta_info']


class Adsl_Identity(IanaInterfaceType_Identity):
    """
    Asymmetric Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Adsl_Identity']['meta_info']


class Aflane8023_Identity(IanaInterfaceType_Identity):
    """
    ATM Emulated LAN for 802.3.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Aflane8023_Identity']['meta_info']


class Aflane8025_Identity(IanaInterfaceType_Identity):
    """
    ATM Emulated LAN for 802.5.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Aflane8025_Identity']['meta_info']


class Aluelp_Identity(IanaInterfaceType_Identity):
    """
    Alcatel\-Lucent Ethernet Link Protection.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Aluelp_Identity']['meta_info']


class Aluepon_Identity(IanaInterfaceType_Identity):
    """
    Ethernet Passive Optical Networks (E\-PON).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Aluepon_Identity']['meta_info']


class Alueponlogicallink_Identity(IanaInterfaceType_Identity):
    """
    The emulation of a point\-to\-point link over the EPON
    layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Alueponlogicallink_Identity']['meta_info']


class Aluepononu_Identity(IanaInterfaceType_Identity):
    """
    EPON Optical Network Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Aluepononu_Identity']['meta_info']


class Alueponphysicaluni_Identity(IanaInterfaceType_Identity):
    """
    EPON physical User to Network interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Alueponphysicaluni_Identity']['meta_info']


class Alugpononu_Identity(IanaInterfaceType_Identity):
    """
    GPON Optical Network Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Alugpononu_Identity']['meta_info']


class Alugponphysicaluni_Identity(IanaInterfaceType_Identity):
    """
    GPON physical User to Network interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Alugponphysicaluni_Identity']['meta_info']


class Arap_Identity(IanaInterfaceType_Identity):
    """
    Appletalk Remote Access Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Arap_Identity']['meta_info']


class Arcnet_Identity(IanaInterfaceType_Identity):
    """
    ARCnet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Arcnet_Identity']['meta_info']


class Arcnetplus_Identity(IanaInterfaceType_Identity):
    """
    ARCnet Plus.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Arcnetplus_Identity']['meta_info']


class Async_Identity(IanaInterfaceType_Identity):
    """
    Asynchronous Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Async_Identity']['meta_info']


class Atm_Identity(IanaInterfaceType_Identity):
    """
    ATM cells.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Atm_Identity']['meta_info']


class Atmbond_Identity(IanaInterfaceType_Identity):
    """
    atmbond.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Atmbond_Identity']['meta_info']


class Atmdxi_Identity(IanaInterfaceType_Identity):
    """
    ATM DXI.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Atmdxi_Identity']['meta_info']


class Atmfuni_Identity(IanaInterfaceType_Identity):
    """
    ATM FUNI.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Atmfuni_Identity']['meta_info']


class Atmima_Identity(IanaInterfaceType_Identity):
    """
    ATM IMA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Atmima_Identity']['meta_info']


class Atmlogical_Identity(IanaInterfaceType_Identity):
    """
    ATM Logical Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Atmlogical_Identity']['meta_info']


class Atmradio_Identity(IanaInterfaceType_Identity):
    """
    ATM over radio links.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Atmradio_Identity']['meta_info']


class Atmsubinterface_Identity(IanaInterfaceType_Identity):
    """
    ATM Sub Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Atmsubinterface_Identity']['meta_info']


class Atmvciendpt_Identity(IanaInterfaceType_Identity):
    """
    ATM VCI End Point.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Atmvciendpt_Identity']['meta_info']


class Atmvirtual_Identity(IanaInterfaceType_Identity):
    """
    ATM Virtual Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Atmvirtual_Identity']['meta_info']


class Aviciopticalether_Identity(IanaInterfaceType_Identity):
    """
    Avici Optical Ethernet Aggregate.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Aviciopticalether_Identity']['meta_info']


class Basicisdn_Identity(IanaInterfaceType_Identity):
    """
    No longer used.  See also RFC 2127.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Basicisdn_Identity']['meta_info']


class Bgppolicyaccounting_Identity(IanaInterfaceType_Identity):
    """
    BGP Policy Accounting.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Bgppolicyaccounting_Identity']['meta_info']


class Bits_Identity(IanaInterfaceType_Identity):
    """
    bitsport.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Bits_Identity']['meta_info']


class Bridge_Identity(IanaInterfaceType_Identity):
    """
    Transparent bridge interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Bridge_Identity']['meta_info']


class Bsc_Identity(IanaInterfaceType_Identity):
    """
    Bisynchronous Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Bsc_Identity']['meta_info']


class Cabledownstreamrfport_Identity(IanaInterfaceType_Identity):
    """
    CATV downstream RF Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Cabledownstreamrfport_Identity']['meta_info']


class Capwapdot11Bss_Identity(IanaInterfaceType_Identity):
    """
    WLAN BSS Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Capwapdot11Bss_Identity']['meta_info']


class Capwapdot11Profile_Identity(IanaInterfaceType_Identity):
    """
    WLAN Profile Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Capwapdot11Profile_Identity']['meta_info']


class Capwapwtpvirtualradio_Identity(IanaInterfaceType_Identity):
    """
    WTP Virtual Radio Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Capwapwtpvirtualradio_Identity']['meta_info']


class Cblvectastar_Identity(IanaInterfaceType_Identity):
    """
    Cambridge Broadband Networks Limited VectaStar.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Cblvectastar_Identity']['meta_info']


class Cctemul_Identity(IanaInterfaceType_Identity):
    """
    ATM Emulated circuit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Cctemul_Identity']['meta_info']


class Ces_Identity(IanaInterfaceType_Identity):
    """
    Circuit Emulation Service.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ces_Identity']['meta_info']


class Channel_Identity(IanaInterfaceType_Identity):
    """
    Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Channel_Identity']['meta_info']


class Ciscoislvlan_Identity(IanaInterfaceType_Identity):
    """
    Layer 2 Virtual LAN using Cisco ISL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ciscoislvlan_Identity']['meta_info']


class Cnr_Identity(IanaInterfaceType_Identity):
    """
    Combat Net Radio.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Cnr_Identity']['meta_info']


class Coffee_Identity(IanaInterfaceType_Identity):
    """
    Coffee pot.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Coffee_Identity']['meta_info']


class Compositelink_Identity(IanaInterfaceType_Identity):
    """
    Avici Composite Link Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Compositelink_Identity']['meta_info']


class Dcn_Identity(IanaInterfaceType_Identity):
    """
    Data Communications Network.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dcn_Identity']['meta_info']


class Ddnx25_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ddnx25_Identity']['meta_info']


class Digitalpowerline_Identity(IanaInterfaceType_Identity):
    """
    IP over Power Lines.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Digitalpowerline_Identity']['meta_info']


class Digitalwrapperoverheadchannel_Identity(IanaInterfaceType_Identity):
    """
    Digital Wrapper.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Digitalwrapperoverheadchannel_Identity']['meta_info']


class Dlsw_Identity(IanaInterfaceType_Identity):
    """
    Data Link Switching.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dlsw_Identity']['meta_info']


class Docscabledownstream_Identity(IanaInterfaceType_Identity):
    """
    CATV Downstream interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Docscabledownstream_Identity']['meta_info']


class Docscablemaclayer_Identity(IanaInterfaceType_Identity):
    """
    CATV Mac Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Docscablemaclayer_Identity']['meta_info']


class Docscablemcmtsdownstream_Identity(IanaInterfaceType_Identity):
    """
    CATV Modular CMTS Downstream Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Docscablemcmtsdownstream_Identity']['meta_info']


class Docscableupstream_Identity(IanaInterfaceType_Identity):
    """
    CATV Upstream interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Docscableupstream_Identity']['meta_info']


class Docscableupstreamchannel_Identity(IanaInterfaceType_Identity):
    """
    CATV Upstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Docscableupstreamchannel_Identity']['meta_info']


class Docscableupstreamrfport_Identity(IanaInterfaceType_Identity):
    """
    DOCSIS CATV Upstream RF Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Docscableupstreamrfport_Identity']['meta_info']


class Ds0Bundle_Identity(IanaInterfaceType_Identity):
    """
    Group of ds0s on the same ds1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ds0Bundle_Identity']['meta_info']


class Ds0_Identity(IanaInterfaceType_Identity):
    """
    Digital Signal Level 0.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ds0_Identity']['meta_info']


class Ds1Fdl_Identity(IanaInterfaceType_Identity):
    """
    Facility Data Link (4Kbps) on a DS1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ds1Fdl_Identity']['meta_info']


class Ds1_Identity(IanaInterfaceType_Identity):
    """
    DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ds1_Identity']['meta_info']


class Ds3_Identity(IanaInterfaceType_Identity):
    """
    DS3\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ds3_Identity']['meta_info']


class Dtm_Identity(IanaInterfaceType_Identity):
    """
    Dynamic synchronous Transfer Mode.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dtm_Identity']['meta_info']


class Dvbasiin_Identity(IanaInterfaceType_Identity):
    """
    DVB\-ASI Input.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dvbasiin_Identity']['meta_info']


class Dvbasiout_Identity(IanaInterfaceType_Identity):
    """
    DVB\-ASI Output.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dvbasiout_Identity']['meta_info']


class Dvbrccdownstream_Identity(IanaInterfaceType_Identity):
    """
    DVB\-RCC Downstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dvbrccdownstream_Identity']['meta_info']


class Dvbrccmaclayer_Identity(IanaInterfaceType_Identity):
    """
    DVB\-RCC MAC Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dvbrccmaclayer_Identity']['meta_info']


class Dvbrccupstream_Identity(IanaInterfaceType_Identity):
    """
    DVB\-RCC Upstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dvbrccupstream_Identity']['meta_info']


class Dvbrcsmaclayer_Identity(IanaInterfaceType_Identity):
    """
    DVB\-RCS MAC Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dvbrcsmaclayer_Identity']['meta_info']


class Dvbrcstdma_Identity(IanaInterfaceType_Identity):
    """
    DVB\-RCS TDMA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dvbrcstdma_Identity']['meta_info']


class Dvbtdm_Identity(IanaInterfaceType_Identity):
    """
    DVB Satellite TDM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dvbtdm_Identity']['meta_info']


class E1_Identity(IanaInterfaceType_Identity):
    """
    Obsolete; see DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['E1_Identity']['meta_info']


class Econet_Identity(IanaInterfaceType_Identity):
    """
    Acorn Econet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Econet_Identity']['meta_info']


class Eon_Identity(IanaInterfaceType_Identity):
    """
    CLNP over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Eon_Identity']['meta_info']


class Eplrs_Identity(IanaInterfaceType_Identity):
    """
    Ext Pos Loc Report Sys.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Eplrs_Identity']['meta_info']


class Escon_Identity(IanaInterfaceType_Identity):
    """
    IBM Enterprise Systems Connection.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Escon_Identity']['meta_info']


class Ethernet3Mbit_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ethernet3Mbit_Identity']['meta_info']


class Ethernetcsmacd_Identity(IanaInterfaceType_Identity):
    """
    For all Ethernet\-like interfaces, regardless of speed,
    as per RFC 3635.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ethernetcsmacd_Identity']['meta_info']


class Fast_Identity(IanaInterfaceType_Identity):
    """
    Fast channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Fast_Identity']['meta_info']


class Fastether_Identity(IanaInterfaceType_Identity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Fastether_Identity']['meta_info']


class Fastetherfx_Identity(IanaInterfaceType_Identity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Fastetherfx_Identity']['meta_info']


class Fciplink_Identity(IanaInterfaceType_Identity):
    """
    FCIP Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Fciplink_Identity']['meta_info']


class Fddi_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Fddi_Identity']['meta_info']


class Fibrechannel_Identity(IanaInterfaceType_Identity):
    """
    Fibre Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Fibrechannel_Identity']['meta_info']


class Framerelay_Identity(IanaInterfaceType_Identity):
    """
    DTE only.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Framerelay_Identity']['meta_info']


class Framerelayinterconnect_Identity(IanaInterfaceType_Identity):
    """
    Obsolete; use either
    frameRelay(32) or frameRelayService(44).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Framerelayinterconnect_Identity']['meta_info']


class Framerelaympi_Identity(IanaInterfaceType_Identity):
    """
    Multiproto Interconnect over FR.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Framerelaympi_Identity']['meta_info']


class Framerelayservice_Identity(IanaInterfaceType_Identity):
    """
    FRNETSERV\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Framerelayservice_Identity']['meta_info']


class Frdlciendpt_Identity(IanaInterfaceType_Identity):
    """
    Frame Relay DLCI End Point.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Frdlciendpt_Identity']['meta_info']


class Frf16Mfrbundle_Identity(IanaInterfaceType_Identity):
    """
    FRF.16 Multilink Frame Relay.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Frf16Mfrbundle_Identity']['meta_info']


class Frforward_Identity(IanaInterfaceType_Identity):
    """
    Frame Forward Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Frforward_Identity']['meta_info']


class G703At2Mb_Identity(IanaInterfaceType_Identity):
    """
    Obsolete; see DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['G703At2Mb_Identity']['meta_info']


class G703At64K_Identity(IanaInterfaceType_Identity):
    """
    CCITT G703 at 64Kbps.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['G703At64K_Identity']['meta_info']


class G9981_Identity(IanaInterfaceType_Identity):
    """
    G.998.1 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['G9981_Identity']['meta_info']


class G9982_Identity(IanaInterfaceType_Identity):
    """
    G.998.2 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['G9982_Identity']['meta_info']


class G9983_Identity(IanaInterfaceType_Identity):
    """
    G.998.3 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['G9983_Identity']['meta_info']


class Gfp_Identity(IanaInterfaceType_Identity):
    """
    Generic Framing Procedure (GFP).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Gfp_Identity']['meta_info']


class Gigabitethernet_Identity(IanaInterfaceType_Identity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Gigabitethernet_Identity']['meta_info']


class Gpon_Identity(IanaInterfaceType_Identity):
    """
    Gigabit\-capable passive optical networks (G\-PON) as per
    ITU\-T G.948.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Gpon_Identity']['meta_info']


class Gr303Idt_Identity(IanaInterfaceType_Identity):
    """
    Integrated Digital Terminal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Gr303Idt_Identity']['meta_info']


class Gr303Rdt_Identity(IanaInterfaceType_Identity):
    """
    Remote Digital Terminal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Gr303Rdt_Identity']['meta_info']


class Gtp_Identity(IanaInterfaceType_Identity):
    """
    GTP (GPRS Tunneling Protocol).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Gtp_Identity']['meta_info']


class H323Gatekeeper_Identity(IanaInterfaceType_Identity):
    """
    H323 Gatekeeper.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['H323Gatekeeper_Identity']['meta_info']


class H323Proxy_Identity(IanaInterfaceType_Identity):
    """
    H323 Voice and Video Proxy.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['H323Proxy_Identity']['meta_info']


class Hdh1822_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Hdh1822_Identity']['meta_info']


class Hdlc_Identity(IanaInterfaceType_Identity):
    """
    HDLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Hdlc_Identity']['meta_info']


class Hdsl2_Identity(IanaInterfaceType_Identity):
    """
    High Bit\-Rate DSL \- 2nd generation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Hdsl2_Identity']['meta_info']


class Hiperlan2_Identity(IanaInterfaceType_Identity):
    """
    HIPERLAN Type 2 Radio Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Hiperlan2_Identity']['meta_info']


class Hippi_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Hippi_Identity']['meta_info']


class Hippiinterface_Identity(IanaInterfaceType_Identity):
    """
    HIPPI interfaces.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Hippiinterface_Identity']['meta_info']


class Homepna_Identity(IanaInterfaceType_Identity):
    """
    HomePNA ITU\-T G.989.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Homepna_Identity']['meta_info']


class Hostpad_Identity(IanaInterfaceType_Identity):
    """
    CCITT\-ITU X.29 PAD Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Hostpad_Identity']['meta_info']


class Hssi_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Hssi_Identity']['meta_info']


class Hyperchannel_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Hyperchannel_Identity']['meta_info']


class Ibm370Parchan_Identity(IanaInterfaceType_Identity):
    """
    IBM System 360/370 OEMI Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ibm370Parchan_Identity']['meta_info']


class Idsl_Identity(IanaInterfaceType_Identity):
    """
    Digital Subscriber Loop over ISDN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Idsl_Identity']['meta_info']


class Ieee1394_Identity(IanaInterfaceType_Identity):
    """
    IEEE1394 High Performance Serial Bus.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ieee1394_Identity']['meta_info']


class Ieee80211_Identity(IanaInterfaceType_Identity):
    """
    Radio spread spectrum.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ieee80211_Identity']['meta_info']


class Ieee80212_Identity(IanaInterfaceType_Identity):
    """
    100BaseVG.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ieee80212_Identity']['meta_info']


class Ieee802154_Identity(IanaInterfaceType_Identity):
    """
    IEEE 802.15.4 WPAN interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ieee802154_Identity']['meta_info']


class Ieee80216Wman_Identity(IanaInterfaceType_Identity):
    """
    IEEE 802.16 WMAN interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ieee80216Wman_Identity']['meta_info']


class Ieee8023Adlag_Identity(IanaInterfaceType_Identity):
    """
    IEEE 802.3ad Link Aggregate.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ieee8023Adlag_Identity']['meta_info']


class IfGsn_Identity(IanaInterfaceType_Identity):
    """
    HIPPI\-6400.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['IfGsn_Identity']['meta_info']


class Ifpwtype_Identity(IanaInterfaceType_Identity):
    """
    Pseudowire interface type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ifpwtype_Identity']['meta_info']


class Ifvfitype_Identity(IanaInterfaceType_Identity):
    """
    VPLS Forwarding Instance Interface Type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ifvfitype_Identity']['meta_info']


class Ilan_Identity(IanaInterfaceType_Identity):
    """
    Internal LAN on a bridge per IEEE 802.1ap.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ilan_Identity']['meta_info']


class Imt_Identity(IanaInterfaceType_Identity):
    """
    Inter\-Machine Trunks.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Imt_Identity']['meta_info']


class Infiniband_Identity(IanaInterfaceType_Identity):
    """
    Infiniband.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Infiniband_Identity']['meta_info']


class Interleave_Identity(IanaInterfaceType_Identity):
    """
    Interleave channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Interleave_Identity']['meta_info']


class Ip_Identity(IanaInterfaceType_Identity):
    """
    IP (for APPN HPR in IP networks).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ip_Identity']['meta_info']


class Ipforward_Identity(IanaInterfaceType_Identity):
    """
    IP Forwarding Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ipforward_Identity']['meta_info']


class Ipoveratm_Identity(IanaInterfaceType_Identity):
    """
    IBM ipOverAtm.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ipoveratm_Identity']['meta_info']


class Ipovercdlc_Identity(IanaInterfaceType_Identity):
    """
    IBM ipOverCdlc.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ipovercdlc_Identity']['meta_info']


class Ipoverclaw_Identity(IanaInterfaceType_Identity):
    """
    IBM Common Link Access to Workstn.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ipoverclaw_Identity']['meta_info']


class Ipswitch_Identity(IanaInterfaceType_Identity):
    """
    IP Switching Objects.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ipswitch_Identity']['meta_info']


class Isdn_Identity(IanaInterfaceType_Identity):
    """
    ISDN and X.25.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Isdn_Identity']['meta_info']


class Isdns_Identity(IanaInterfaceType_Identity):
    """
    ISDN S/T interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Isdns_Identity']['meta_info']


class Isdnu_Identity(IanaInterfaceType_Identity):
    """
    ISDN U interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Isdnu_Identity']['meta_info']


class Iso88022Llc_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88022Llc_Identity']['meta_info']


class Iso88023Csmacd_Identity(IanaInterfaceType_Identity):
    """
    Deprecated via RFC 3635.
    Use ethernetCsmacd(6) instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88023Csmacd_Identity']['meta_info']


class Iso88024Tokenbus_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88024Tokenbus_Identity']['meta_info']


class Iso88025Crfpint_Identity(IanaInterfaceType_Identity):
    """
    ISO 802.5 CRFP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88025Crfpint_Identity']['meta_info']


class Iso88025Dtr_Identity(IanaInterfaceType_Identity):
    """
    ISO 802.5r DTR.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88025Dtr_Identity']['meta_info']


class Iso88025Fiber_Identity(IanaInterfaceType_Identity):
    """
    ISO 802.5j Fiber Token Ring.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88025Fiber_Identity']['meta_info']


class Iso88025Tokenring_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88025Tokenring_Identity']['meta_info']


class Iso88026Man_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88026Man_Identity']['meta_info']


class Isup_Identity(IanaInterfaceType_Identity):
    """
    ISUP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Isup_Identity']['meta_info']


class L2Vlan_Identity(IanaInterfaceType_Identity):
    """
    Layer 2 Virtual LAN using 802.1Q.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['L2Vlan_Identity']['meta_info']


class L3Ipvlan_Identity(IanaInterfaceType_Identity):
    """
    Layer 3 Virtual LAN using IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['L3Ipvlan_Identity']['meta_info']


class L3Ipxvlan_Identity(IanaInterfaceType_Identity):
    """
    Layer 3 Virtual LAN using IPX.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['L3Ipxvlan_Identity']['meta_info']


class Lapb_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Lapb_Identity']['meta_info']


class Lapd_Identity(IanaInterfaceType_Identity):
    """
    Link Access Protocol D.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Lapd_Identity']['meta_info']


class Lapf_Identity(IanaInterfaceType_Identity):
    """
    LAP F.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Lapf_Identity']['meta_info']


class Linegroup_Identity(IanaInterfaceType_Identity):
    """
    Interface common to multiple lines.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Linegroup_Identity']['meta_info']


class Lmp_Identity(IanaInterfaceType_Identity):
    """
    Link Management Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Lmp_Identity']['meta_info']


class Localtalk_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Localtalk_Identity']['meta_info']


class Macseccontrolledif_Identity(IanaInterfaceType_Identity):
    """
    MACSecControlled.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Macseccontrolledif_Identity']['meta_info']


class Macsecuncontrolledif_Identity(IanaInterfaceType_Identity):
    """
    MACSecUncontrolled.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Macsecuncontrolledif_Identity']['meta_info']


class Mediamailoverip_Identity(IanaInterfaceType_Identity):
    """
    Multimedia Mail over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Mediamailoverip_Identity']['meta_info']


class Mfsiglink_Identity(IanaInterfaceType_Identity):
    """
    Multi\-frequency signaling link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Mfsiglink_Identity']['meta_info']


class Miox25_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Miox25_Identity']['meta_info']


class Mocaversion1_Identity(IanaInterfaceType_Identity):
    """
    MultiMedia over Coax Alliance (MoCA) Interface
    as documented in information provided privately to IANA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Mocaversion1_Identity']['meta_info']


class Modem_Identity(IanaInterfaceType_Identity):
    """
    Generic modem.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Modem_Identity']['meta_info']


class Mpc_Identity(IanaInterfaceType_Identity):
    """
    IBM multi\-protocol channel support.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Mpc_Identity']['meta_info']


class Mpegtransport_Identity(IanaInterfaceType_Identity):
    """
    MPEG transport interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Mpegtransport_Identity']['meta_info']


class Mpls_Identity(IanaInterfaceType_Identity):
    """
    MPLS.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Mpls_Identity']['meta_info']


class Mplstunnel_Identity(IanaInterfaceType_Identity):
    """
    MPLS Tunnel Virtual Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Mplstunnel_Identity']['meta_info']


class Msdsl_Identity(IanaInterfaceType_Identity):
    """
    Multi\-rate Symmetric DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Msdsl_Identity']['meta_info']


class Mvl_Identity(IanaInterfaceType_Identity):
    """
    Multiple Virtual Lines DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Mvl_Identity']['meta_info']


class Myrinet_Identity(IanaInterfaceType_Identity):
    """
    Myricom Myrinet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Myrinet_Identity']['meta_info']


class Nfas_Identity(IanaInterfaceType_Identity):
    """
    Non\-Facility Associated Signaling.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Nfas_Identity']['meta_info']


class Nsip_Identity(IanaInterfaceType_Identity):
    """
    XNS over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Nsip_Identity']['meta_info']


class Opticalchannel_Identity(IanaInterfaceType_Identity):
    """
    Optical Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Opticalchannel_Identity']['meta_info']


class Opticalchannelgroup_Identity(IanaInterfaceType_Identity):
    """
    Optical Channel Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Opticalchannelgroup_Identity']['meta_info']


class Opticaltransport_Identity(IanaInterfaceType_Identity):
    """
    Optical Transport.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Opticaltransport_Identity']['meta_info']


class Other_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Other_Identity']['meta_info']


class Otnodu_Identity(IanaInterfaceType_Identity):
    """
    OTN Optical Data Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Otnodu_Identity']['meta_info']


class Otnotu_Identity(IanaInterfaceType_Identity):
    """
    OTN Optical channel Transport Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Otnotu_Identity']['meta_info']


class Para_Identity(IanaInterfaceType_Identity):
    """
    Parallel\-port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Para_Identity']['meta_info']


class Pdnetherloop1_Identity(IanaInterfaceType_Identity):
    """
    Paradyne EtherLoop 1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Pdnetherloop1_Identity']['meta_info']


class Pdnetherloop2_Identity(IanaInterfaceType_Identity):
    """
    Paradyne EtherLoop 2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Pdnetherloop2_Identity']['meta_info']


class Pip_Identity(IanaInterfaceType_Identity):
    """
    Provider Instance Port on a bridge per IEEE 802.1ah PBB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Pip_Identity']['meta_info']


class Plc_Identity(IanaInterfaceType_Identity):
    """
    Power Line Communications.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Plc_Identity']['meta_info']


class Pon155_Identity(IanaInterfaceType_Identity):
    """
    FSAN 155Mb Symetrical PON interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Pon155_Identity']['meta_info']


class Pon622_Identity(IanaInterfaceType_Identity):
    """
    FSAN 622Mb Symetrical PON interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Pon622_Identity']['meta_info']


class Pos_Identity(IanaInterfaceType_Identity):
    """
    Packet over SONET/SDH Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Pos_Identity']['meta_info']


class Ppp_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ppp_Identity']['meta_info']


class Pppmultilinkbundle_Identity(IanaInterfaceType_Identity):
    """
    PPP Multilink Bundle.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Pppmultilinkbundle_Identity']['meta_info']


class Primaryisdn_Identity(IanaInterfaceType_Identity):
    """
    No longer used.  See also RFC 2127.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Primaryisdn_Identity']['meta_info']


class Propatm_Identity(IanaInterfaceType_Identity):
    """
    Proprietary ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Propatm_Identity']['meta_info']


class Propbwap2Mp_Identity(IanaInterfaceType_Identity):
    """
    PropBroadbandWirelessAccesspt2Multipt (use of this value
    for IEEE 802.16 WMAN interfaces as per IEEE Std 802.16f
    is deprecated, and ieee80216WMAN(237) should be used
    instead).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Propbwap2Mp_Identity']['meta_info']


class Propcnls_Identity(IanaInterfaceType_Identity):
    """
    Proprietary Connectionless Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Propcnls_Identity']['meta_info']


class Propdocswirelessdownstream_Identity(IanaInterfaceType_Identity):
    """
    Cisco proprietary Downstream.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Propdocswirelessdownstream_Identity']['meta_info']


class Propdocswirelessmaclayer_Identity(IanaInterfaceType_Identity):
    """
    Cisco proprietary Maclayer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Propdocswirelessmaclayer_Identity']['meta_info']


class Propdocswirelessupstream_Identity(IanaInterfaceType_Identity):
    """
    Cisco proprietary Upstream.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Propdocswirelessupstream_Identity']['meta_info']


class Propmultiplexor_Identity(IanaInterfaceType_Identity):
    """
    Proprietary multiplexing.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Propmultiplexor_Identity']['meta_info']


class Proppointtopointserial_Identity(IanaInterfaceType_Identity):
    """
    Proprietary serial.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Proppointtopointserial_Identity']['meta_info']


class Propvirtual_Identity(IanaInterfaceType_Identity):
    """
    Proprietary virtual/internal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Propvirtual_Identity']['meta_info']


class Propwirelessp2P_Identity(IanaInterfaceType_Identity):
    """
    Prop. P2P wireless interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Propwirelessp2P_Identity']['meta_info']


class Proteon10Mbit_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Proteon10Mbit_Identity']['meta_info']


class Proteon80Mbit_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Proteon80Mbit_Identity']['meta_info']


class Q2931_Identity(IanaInterfaceType_Identity):
    """
    Q.2931.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Q2931_Identity']['meta_info']


class Qam_Identity(IanaInterfaceType_Identity):
    """
    RF Qam Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Qam_Identity']['meta_info']


class Qllc_Identity(IanaInterfaceType_Identity):
    """
    SNA QLLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Qllc_Identity']['meta_info']


class Radiomac_Identity(IanaInterfaceType_Identity):
    """
    MAC layer over radio links.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Radiomac_Identity']['meta_info']


class Radsl_Identity(IanaInterfaceType_Identity):
    """
    Rate\-Adapt. Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Radsl_Identity']['meta_info']


class Reachdsl_Identity(IanaInterfaceType_Identity):
    """
    Long Reach DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Reachdsl_Identity']['meta_info']


class Regular1822_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Regular1822_Identity']['meta_info']


class Rfc1483_Identity(IanaInterfaceType_Identity):
    """
    Multiprotocol over ATM AAL5.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Rfc1483_Identity']['meta_info']


class Rfc877X25_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Rfc877X25_Identity']['meta_info']


class Rpr_Identity(IanaInterfaceType_Identity):
    """
    Resilient Packet Ring Interface Type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Rpr_Identity']['meta_info']


class Rs232_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Rs232_Identity']['meta_info']


class Rsrb_Identity(IanaInterfaceType_Identity):
    """
    Remote Source Route Bridging.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Rsrb_Identity']['meta_info']


class Sdlc_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Sdlc_Identity']['meta_info']


class Sdsl_Identity(IanaInterfaceType_Identity):
    """
    Symmetric Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Sdsl_Identity']['meta_info']


class Shdsl_Identity(IanaInterfaceType_Identity):
    """
    Multirate HDSL2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Shdsl_Identity']['meta_info']


class Sip_Identity(IanaInterfaceType_Identity):
    """
    SMDS, coffee.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Sip_Identity']['meta_info']


class Sipsig_Identity(IanaInterfaceType_Identity):
    """
    SIP Signaling.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Sipsig_Identity']['meta_info']


class Siptg_Identity(IanaInterfaceType_Identity):
    """
    SIP Trunk Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Siptg_Identity']['meta_info']


class Sixtofour_Identity(IanaInterfaceType_Identity):
    """
    6to4 interface (DEPRECATED).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Sixtofour_Identity']['meta_info']


class Slip_Identity(IanaInterfaceType_Identity):
    """
    Generic SLIP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Slip_Identity']['meta_info']


class Smdsdxi_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Smdsdxi_Identity']['meta_info']


class Smdsicip_Identity(IanaInterfaceType_Identity):
    """
    SMDS InterCarrier Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Smdsicip_Identity']['meta_info']


class Softwareloopback_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Softwareloopback_Identity']['meta_info']


class Sonet_Identity(IanaInterfaceType_Identity):
    """
    SONET or SDH.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Sonet_Identity']['meta_info']


class Sonetoverheadchannel_Identity(IanaInterfaceType_Identity):
    """
    SONET Overhead Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Sonetoverheadchannel_Identity']['meta_info']


class Sonetpath_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Sonetpath_Identity']['meta_info']


class Sonetvt_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Sonetvt_Identity']['meta_info']


class Srp_Identity(IanaInterfaceType_Identity):
    """
    Spatial Reuse Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Srp_Identity']['meta_info']


class Ss7Siglink_Identity(IanaInterfaceType_Identity):
    """
    SS7 Signaling Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ss7Siglink_Identity']['meta_info']


class Stacktostack_Identity(IanaInterfaceType_Identity):
    """
    IBM stackToStack.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Stacktostack_Identity']['meta_info']


class Starlan_Identity(IanaInterfaceType_Identity):
    """
    Deprecated via RFC 3635.
    Use ethernetCsmacd(6) instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Starlan_Identity']['meta_info']


class Tdlc_Identity(IanaInterfaceType_Identity):
    """
    IBM twinaxial data link control.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Tdlc_Identity']['meta_info']


class Telink_Identity(IanaInterfaceType_Identity):
    """
    TE Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Telink_Identity']['meta_info']


class Termpad_Identity(IanaInterfaceType_Identity):
    """
    CCITT\-ITU X.3 PAD Facility.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Termpad_Identity']['meta_info']


class Tr008_Identity(IanaInterfaceType_Identity):
    """
    TR008.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Tr008_Identity']['meta_info']


class Transphdlc_Identity(IanaInterfaceType_Identity):
    """
    Transp HDLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Transphdlc_Identity']['meta_info']


class Tunnel_Identity(IanaInterfaceType_Identity):
    """
    Encapsulation interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Tunnel_Identity']['meta_info']


class Ultra_Identity(IanaInterfaceType_Identity):
    """
    Ultra Technologies.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ultra_Identity']['meta_info']


class Usb_Identity(IanaInterfaceType_Identity):
    """
    USB Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Usb_Identity']['meta_info']


class V11_Identity(IanaInterfaceType_Identity):
    """
    CCITT V.11/X.21.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['V11_Identity']['meta_info']


class V35_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['V35_Identity']['meta_info']


class V36_Identity(IanaInterfaceType_Identity):
    """
    CCITT V.36.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['V36_Identity']['meta_info']


class V37_Identity(IanaInterfaceType_Identity):
    """
    V.37.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['V37_Identity']['meta_info']


class Vdsl2_Identity(IanaInterfaceType_Identity):
    """
    Very high speed digital subscriber line Version 2
    (as per ITU\-T Recommendation G.993.2).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Vdsl2_Identity']['meta_info']


class Vdsl_Identity(IanaInterfaceType_Identity):
    """
    Very H\-Speed Digital Subscrib. Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Vdsl_Identity']['meta_info']


class Virtualipaddress_Identity(IanaInterfaceType_Identity):
    """
    IBM VIPA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Virtualipaddress_Identity']['meta_info']


class Virtualtg_Identity(IanaInterfaceType_Identity):
    """
    Virtual Trunk Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Virtualtg_Identity']['meta_info']


class Vmwarenicteam_Identity(IanaInterfaceType_Identity):
    """
    VMware NIC Team.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Vmwarenicteam_Identity']['meta_info']


class Vmwarevirtualnic_Identity(IanaInterfaceType_Identity):
    """
    VMware Virtual Network Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Vmwarevirtualnic_Identity']['meta_info']


class Voicedid_Identity(IanaInterfaceType_Identity):
    """
    Voice Direct Inward Dialing.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voicedid_Identity']['meta_info']


class Voiceebs_Identity(IanaInterfaceType_Identity):
    """
    Voice P\-phone EBS physical interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voiceebs_Identity']['meta_info']


class Voiceem_Identity(IanaInterfaceType_Identity):
    """
    Voice recEive and transMit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voiceem_Identity']['meta_info']


class Voiceemfgd_Identity(IanaInterfaceType_Identity):
    """
    Voice E&M Feature Group D.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voiceemfgd_Identity']['meta_info']


class Voiceencap_Identity(IanaInterfaceType_Identity):
    """
    Voice encapsulation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voiceencap_Identity']['meta_info']


class Voicefgdeana_Identity(IanaInterfaceType_Identity):
    """
    Voice FGD Exchange Access North American.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voicefgdeana_Identity']['meta_info']


class Voicefgdos_Identity(IanaInterfaceType_Identity):
    """
    Voice FGD Operator Services.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voicefgdos_Identity']['meta_info']


class Voicefxo_Identity(IanaInterfaceType_Identity):
    """
    Voice Foreign Exchange Office.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voicefxo_Identity']['meta_info']


class Voicefxs_Identity(IanaInterfaceType_Identity):
    """
    Voice Foreign Exchange Station.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voicefxs_Identity']['meta_info']


class Voiceoveratm_Identity(IanaInterfaceType_Identity):
    """
    Voice over ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voiceoveratm_Identity']['meta_info']


class Voiceovercable_Identity(IanaInterfaceType_Identity):
    """
    Voice Over Cable Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voiceovercable_Identity']['meta_info']


class Voiceoverframerelay_Identity(IanaInterfaceType_Identity):
    """
    Voice Over Frame Relay.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voiceoverframerelay_Identity']['meta_info']


class Voiceoverip_Identity(IanaInterfaceType_Identity):
    """
    Voice over IP encapsulation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Voiceoverip_Identity']['meta_info']


class Wwanpp2_Identity(IanaInterfaceType_Identity):
    """
    3GPP2 WWAN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Wwanpp2_Identity']['meta_info']


class Wwanpp_Identity(IanaInterfaceType_Identity):
    """
    3GPP WWAN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Wwanpp_Identity']['meta_info']


class X213_Identity(IanaInterfaceType_Identity):
    """
    CCITT\-ITU X213.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['X213_Identity']['meta_info']


class X25Huntgroup_Identity(IanaInterfaceType_Identity):
    """
    X25 Hunt Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['X25Huntgroup_Identity']['meta_info']


class X25Mlp_Identity(IanaInterfaceType_Identity):
    """
    Multi\-Link Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['X25Mlp_Identity']['meta_info']


class X25Ple_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['X25Ple_Identity']['meta_info']


class X86Laps_Identity(IanaInterfaceType_Identity):
    """
    LAPS based on ITU\-T X.86/Y.1323.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['X86Laps_Identity']['meta_info']


