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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['IanaInterfaceType_Identity']['meta_info']


class A12MppSwitch_Identity(IanaInterfaceType_Identity):
    """
    Avalon Parallel Processor.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['A12MppSwitch_Identity']['meta_info']


class Aal2_Identity(IanaInterfaceType_Identity):
    """
    ATM adaptation layer 2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Aal5_Identity']['meta_info']


class ActelisMetaLOOP_Identity(IanaInterfaceType_Identity):
    """
    Acteleis proprietary MetaLOOP High Speed Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['ActelisMetaLOOP_Identity']['meta_info']


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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Adsl2_Identity']['meta_info']


class Adsl2plus_Identity(IanaInterfaceType_Identity):
    """
    Asymmetric Digital Subscriber Loop Version 2 \-
    Version 2 Plus and all variants.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Adsl2plus_Identity']['meta_info']


class Adsl_Identity(IanaInterfaceType_Identity):
    """
    Asymmetric Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Aflane8025_Identity']['meta_info']


class AluELP_Identity(IanaInterfaceType_Identity):
    """
    Alcatel\-Lucent Ethernet Link Protection.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AluELP_Identity']['meta_info']


class AluEponLogicalLink_Identity(IanaInterfaceType_Identity):
    """
    The emulation of a point\-to\-point link over the EPON
    layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AluEponLogicalLink_Identity']['meta_info']


class AluEponOnu_Identity(IanaInterfaceType_Identity):
    """
    EPON Optical Network Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AluEponOnu_Identity']['meta_info']


class AluEponPhysicalUni_Identity(IanaInterfaceType_Identity):
    """
    EPON physical User to Network interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AluEponPhysicalUni_Identity']['meta_info']


class AluEpon_Identity(IanaInterfaceType_Identity):
    """
    Ethernet Passive Optical Networks (E\-PON).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AluEpon_Identity']['meta_info']


class AluGponOnu_Identity(IanaInterfaceType_Identity):
    """
    GPON Optical Network Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AluGponOnu_Identity']['meta_info']


class AluGponPhysicalUni_Identity(IanaInterfaceType_Identity):
    """
    GPON physical User to Network interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AluGponPhysicalUni_Identity']['meta_info']


class Arap_Identity(IanaInterfaceType_Identity):
    """
    Appletalk Remote Access Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Arap_Identity']['meta_info']


class ArcnetPlus_Identity(IanaInterfaceType_Identity):
    """
    ARCnet Plus.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['ArcnetPlus_Identity']['meta_info']


class Arcnet_Identity(IanaInterfaceType_Identity):
    """
    ARCnet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Arcnet_Identity']['meta_info']


class Async_Identity(IanaInterfaceType_Identity):
    """
    Asynchronous Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Async_Identity']['meta_info']


class AtmDxi_Identity(IanaInterfaceType_Identity):
    """
    ATM DXI.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AtmDxi_Identity']['meta_info']


class AtmFuni_Identity(IanaInterfaceType_Identity):
    """
    ATM FUNI.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AtmFuni_Identity']['meta_info']


class AtmIma_Identity(IanaInterfaceType_Identity):
    """
    ATM IMA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AtmIma_Identity']['meta_info']


class AtmLogical_Identity(IanaInterfaceType_Identity):
    """
    ATM Logical Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AtmLogical_Identity']['meta_info']


class AtmRadio_Identity(IanaInterfaceType_Identity):
    """
    ATM over radio links.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AtmRadio_Identity']['meta_info']


class AtmSubInterface_Identity(IanaInterfaceType_Identity):
    """
    ATM Sub Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AtmSubInterface_Identity']['meta_info']


class AtmVciEndPt_Identity(IanaInterfaceType_Identity):
    """
    ATM VCI End Point.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AtmVciEndPt_Identity']['meta_info']


class AtmVirtual_Identity(IanaInterfaceType_Identity):
    """
    ATM Virtual Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AtmVirtual_Identity']['meta_info']


class Atm_Identity(IanaInterfaceType_Identity):
    """
    ATM cells.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Atmbond_Identity']['meta_info']


class AviciOpticalEther_Identity(IanaInterfaceType_Identity):
    """
    Avici Optical Ethernet Aggregate.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['AviciOpticalEther_Identity']['meta_info']


class BasicISDN_Identity(IanaInterfaceType_Identity):
    """
    No longer used.  See also RFC 2127.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['BasicISDN_Identity']['meta_info']


class Bgppolicyaccounting_Identity(IanaInterfaceType_Identity):
    """
    BGP Policy Accounting.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Bsc_Identity']['meta_info']


class CableDownstreamRfPort_Identity(IanaInterfaceType_Identity):
    """
    CATV downstream RF Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['CableDownstreamRfPort_Identity']['meta_info']


class CapwapDot11Bss_Identity(IanaInterfaceType_Identity):
    """
    WLAN BSS Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['CapwapDot11Bss_Identity']['meta_info']


class CapwapDot11Profile_Identity(IanaInterfaceType_Identity):
    """
    WLAN Profile Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['CapwapDot11Profile_Identity']['meta_info']


class CapwapWtpVirtualRadio_Identity(IanaInterfaceType_Identity):
    """
    WTP Virtual Radio Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['CapwapWtpVirtualRadio_Identity']['meta_info']


class CblVectaStar_Identity(IanaInterfaceType_Identity):
    """
    Cambridge Broadband Networks Limited VectaStar.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['CblVectaStar_Identity']['meta_info']


class CctEmul_Identity(IanaInterfaceType_Identity):
    """
    ATM Emulated circuit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['CctEmul_Identity']['meta_info']


class Ces_Identity(IanaInterfaceType_Identity):
    """
    Circuit Emulation Service.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Channel_Identity']['meta_info']


class CiscoISLvlan_Identity(IanaInterfaceType_Identity):
    """
    Layer 2 Virtual LAN using Cisco ISL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['CiscoISLvlan_Identity']['meta_info']


class Cnr_Identity(IanaInterfaceType_Identity):
    """
    Combat Net Radio.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Coffee_Identity']['meta_info']


class CompositeLink_Identity(IanaInterfaceType_Identity):
    """
    Avici Composite Link Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['CompositeLink_Identity']['meta_info']


class Dcn_Identity(IanaInterfaceType_Identity):
    """
    Data Communications Network.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dcn_Identity']['meta_info']


class DdnX25_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DdnX25_Identity']['meta_info']


class DigitalPowerline_Identity(IanaInterfaceType_Identity):
    """
    IP over Power Lines.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DigitalPowerline_Identity']['meta_info']


class DigitalWrapperOverheadChannel_Identity(IanaInterfaceType_Identity):
    """
    Digital Wrapper.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DigitalWrapperOverheadChannel_Identity']['meta_info']


class Dlsw_Identity(IanaInterfaceType_Identity):
    """
    Data Link Switching.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dlsw_Identity']['meta_info']


class DocsCableDownstream_Identity(IanaInterfaceType_Identity):
    """
    CATV Downstream interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DocsCableDownstream_Identity']['meta_info']


class DocsCableMCmtsDownstream_Identity(IanaInterfaceType_Identity):
    """
    CATV Modular CMTS Downstream Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DocsCableMCmtsDownstream_Identity']['meta_info']


class DocsCableMaclayer_Identity(IanaInterfaceType_Identity):
    """
    CATV Mac Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DocsCableMaclayer_Identity']['meta_info']


class DocsCableUpstreamChannel_Identity(IanaInterfaceType_Identity):
    """
    CATV Upstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DocsCableUpstreamChannel_Identity']['meta_info']


class DocsCableUpstreamRfPort_Identity(IanaInterfaceType_Identity):
    """
    DOCSIS CATV Upstream RF Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DocsCableUpstreamRfPort_Identity']['meta_info']


class DocsCableUpstream_Identity(IanaInterfaceType_Identity):
    """
    CATV Upstream interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DocsCableUpstream_Identity']['meta_info']


class Ds0Bundle_Identity(IanaInterfaceType_Identity):
    """
    Group of ds0s on the same ds1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ds0_Identity']['meta_info']


class Ds1FDL_Identity(IanaInterfaceType_Identity):
    """
    Facility Data Link (4Kbps) on a DS1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ds1FDL_Identity']['meta_info']


class Ds1_Identity(IanaInterfaceType_Identity):
    """
    DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Dtm_Identity']['meta_info']


class DvbAsiIn_Identity(IanaInterfaceType_Identity):
    """
    DVB\-ASI Input.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DvbAsiIn_Identity']['meta_info']


class DvbAsiOut_Identity(IanaInterfaceType_Identity):
    """
    DVB\-ASI Output.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DvbAsiOut_Identity']['meta_info']


class DvbRccDownstream_Identity(IanaInterfaceType_Identity):
    """
    DVB\-RCC Downstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DvbRccDownstream_Identity']['meta_info']


class DvbRccMacLayer_Identity(IanaInterfaceType_Identity):
    """
    DVB\-RCC MAC Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DvbRccMacLayer_Identity']['meta_info']


class DvbRccUpstream_Identity(IanaInterfaceType_Identity):
    """
    DVB\-RCC Upstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DvbRccUpstream_Identity']['meta_info']


class DvbRcsMacLayer_Identity(IanaInterfaceType_Identity):
    """
    DVB\-RCS MAC Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DvbRcsMacLayer_Identity']['meta_info']


class DvbRcsTdma_Identity(IanaInterfaceType_Identity):
    """
    DVB\-RCS TDMA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DvbRcsTdma_Identity']['meta_info']


class DvbTdm_Identity(IanaInterfaceType_Identity):
    """
    DVB Satellite TDM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['DvbTdm_Identity']['meta_info']


class E1_Identity(IanaInterfaceType_Identity):
    """
    Obsolete; see DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ethernet3Mbit_Identity']['meta_info']


class EthernetCsmacd_Identity(IanaInterfaceType_Identity):
    """
    For all Ethernet\-like interfaces, regardless of speed,
    as per RFC 3635.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['EthernetCsmacd_Identity']['meta_info']


class FastEtherFX_Identity(IanaInterfaceType_Identity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['FastEtherFX_Identity']['meta_info']


class FastEther_Identity(IanaInterfaceType_Identity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['FastEther_Identity']['meta_info']


class Fast_Identity(IanaInterfaceType_Identity):
    """
    Fast channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Fast_Identity']['meta_info']


class FcipLink_Identity(IanaInterfaceType_Identity):
    """
    FCIP Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['FcipLink_Identity']['meta_info']


class Fddi_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Fddi_Identity']['meta_info']


class FibreChannel_Identity(IanaInterfaceType_Identity):
    """
    Fibre Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['FibreChannel_Identity']['meta_info']


class FrDlciEndPt_Identity(IanaInterfaceType_Identity):
    """
    Frame Relay DLCI End Point.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['FrDlciEndPt_Identity']['meta_info']


class FrForward_Identity(IanaInterfaceType_Identity):
    """
    Frame Forward Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['FrForward_Identity']['meta_info']


class FrameRelayInterconnect_Identity(IanaInterfaceType_Identity):
    """
    Obsolete; use either
    frameRelay(32) or frameRelayService(44).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['FrameRelayInterconnect_Identity']['meta_info']


class FrameRelayMPI_Identity(IanaInterfaceType_Identity):
    """
    Multiproto Interconnect over FR.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['FrameRelayMPI_Identity']['meta_info']


class FrameRelayService_Identity(IanaInterfaceType_Identity):
    """
    FRNETSERV\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['FrameRelayService_Identity']['meta_info']


class FrameRelay_Identity(IanaInterfaceType_Identity):
    """
    DTE only.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['FrameRelay_Identity']['meta_info']


class Frf16MfrBundle_Identity(IanaInterfaceType_Identity):
    """
    FRF.16 Multilink Frame Relay.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Frf16MfrBundle_Identity']['meta_info']


class G703at2mb_Identity(IanaInterfaceType_Identity):
    """
    Obsolete; see DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['G703at2mb_Identity']['meta_info']


class G703at64k_Identity(IanaInterfaceType_Identity):
    """
    CCITT G703 at 64Kbps.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['G703at64k_Identity']['meta_info']


class G9981_Identity(IanaInterfaceType_Identity):
    """
    G.998.1 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Gfp_Identity']['meta_info']


class GigabitEthernet_Identity(IanaInterfaceType_Identity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['GigabitEthernet_Identity']['meta_info']


class Gpon_Identity(IanaInterfaceType_Identity):
    """
    Gigabit\-capable passive optical networks (G\-PON) as per
    ITU\-T G.948.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Gpon_Identity']['meta_info']


class Gr303IDT_Identity(IanaInterfaceType_Identity):
    """
    Integrated Digital Terminal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Gr303IDT_Identity']['meta_info']


class Gr303RDT_Identity(IanaInterfaceType_Identity):
    """
    Remote Digital Terminal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Gr303RDT_Identity']['meta_info']


class Gtp_Identity(IanaInterfaceType_Identity):
    """
    GTP (GPRS Tunneling Protocol).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Hiperlan2_Identity']['meta_info']


class HippiInterface_Identity(IanaInterfaceType_Identity):
    """
    HIPPI interfaces.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['HippiInterface_Identity']['meta_info']


class Hippi_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Hippi_Identity']['meta_info']


class Homepna_Identity(IanaInterfaceType_Identity):
    """
    HomePNA ITU\-T G.989.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Homepna_Identity']['meta_info']


class HostPad_Identity(IanaInterfaceType_Identity):
    """
    CCITT\-ITU X.29 PAD Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['HostPad_Identity']['meta_info']


class Hssi_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Hyperchannel_Identity']['meta_info']


class Ibm370parChan_Identity(IanaInterfaceType_Identity):
    """
    IBM System 360/370 OEMI Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ibm370parChan_Identity']['meta_info']


class Idsl_Identity(IanaInterfaceType_Identity):
    """
    Digital Subscriber Loop over ISDN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ieee802154_Identity']['meta_info']


class Ieee80216WMAN_Identity(IanaInterfaceType_Identity):
    """
    IEEE 802.16 WMAN interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ieee80216WMAN_Identity']['meta_info']


class Ieee8023adLag_Identity(IanaInterfaceType_Identity):
    """
    IEEE 802.3ad Link Aggregate.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ieee8023adLag_Identity']['meta_info']


class IfGsn_Identity(IanaInterfaceType_Identity):
    """
    HIPPI\-6400.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['IfGsn_Identity']['meta_info']


class IfPwType_Identity(IanaInterfaceType_Identity):
    """
    Pseudowire interface type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['IfPwType_Identity']['meta_info']


class IfVfiType_Identity(IanaInterfaceType_Identity):
    """
    VPLS Forwarding Instance Interface Type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['IfVfiType_Identity']['meta_info']


class Ilan_Identity(IanaInterfaceType_Identity):
    """
    Internal LAN on a bridge per IEEE 802.1ap.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Interleave_Identity']['meta_info']


class IpForward_Identity(IanaInterfaceType_Identity):
    """
    IP Forwarding Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['IpForward_Identity']['meta_info']


class IpOverAtm_Identity(IanaInterfaceType_Identity):
    """
    IBM ipOverAtm.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['IpOverAtm_Identity']['meta_info']


class IpOverCdlc_Identity(IanaInterfaceType_Identity):
    """
    IBM ipOverCdlc.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['IpOverCdlc_Identity']['meta_info']


class IpOverClaw_Identity(IanaInterfaceType_Identity):
    """
    IBM Common Link Access to Workstn.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['IpOverClaw_Identity']['meta_info']


class IpSwitch_Identity(IanaInterfaceType_Identity):
    """
    IP Switching Objects.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['IpSwitch_Identity']['meta_info']


class Ip_Identity(IanaInterfaceType_Identity):
    """
    IP (for APPN HPR in IP networks).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ip_Identity']['meta_info']


class Isdn_Identity(IanaInterfaceType_Identity):
    """
    ISDN and X.25.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Isdnu_Identity']['meta_info']


class Iso88022llc_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88022llc_Identity']['meta_info']


class Iso88023Csmacd_Identity(IanaInterfaceType_Identity):
    """
    Deprecated via RFC 3635.
    Use ethernetCsmacd(6) instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88023Csmacd_Identity']['meta_info']


class Iso88024TokenBus_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88024TokenBus_Identity']['meta_info']


class Iso88025CRFPInt_Identity(IanaInterfaceType_Identity):
    """
    ISO 802.5 CRFP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88025CRFPInt_Identity']['meta_info']


class Iso88025Dtr_Identity(IanaInterfaceType_Identity):
    """
    ISO 802.5r DTR.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88025Fiber_Identity']['meta_info']


class Iso88025TokenRing_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Iso88025TokenRing_Identity']['meta_info']


class Iso88026Man_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Isup_Identity']['meta_info']


class L2vlan_Identity(IanaInterfaceType_Identity):
    """
    Layer 2 Virtual LAN using 802.1Q.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['L2vlan_Identity']['meta_info']


class L3ipvlan_Identity(IanaInterfaceType_Identity):
    """
    Layer 3 Virtual LAN using IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['L3ipvlan_Identity']['meta_info']


class L3ipxvlan_Identity(IanaInterfaceType_Identity):
    """
    Layer 3 Virtual LAN using IPX.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['L3ipxvlan_Identity']['meta_info']


class Lapb_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Lmp_Identity']['meta_info']


class LocalTalk_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['LocalTalk_Identity']['meta_info']


class MacSecControlledIF_Identity(IanaInterfaceType_Identity):
    """
    MACSecControlled.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['MacSecControlledIF_Identity']['meta_info']


class MacSecUncontrolledIF_Identity(IanaInterfaceType_Identity):
    """
    MACSecUncontrolled.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['MacSecUncontrolledIF_Identity']['meta_info']


class MediaMailOverIp_Identity(IanaInterfaceType_Identity):
    """
    Multimedia Mail over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['MediaMailOverIp_Identity']['meta_info']


class MfSigLink_Identity(IanaInterfaceType_Identity):
    """
    Multi\-frequency signaling link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['MfSigLink_Identity']['meta_info']


class Miox25_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Miox25_Identity']['meta_info']


class MocaVersion1_Identity(IanaInterfaceType_Identity):
    """
    MultiMedia over Coax Alliance (MoCA) Interface
    as documented in information provided privately to IANA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['MocaVersion1_Identity']['meta_info']


class Modem_Identity(IanaInterfaceType_Identity):
    """
    Generic modem.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Mpc_Identity']['meta_info']


class MpegTransport_Identity(IanaInterfaceType_Identity):
    """
    MPEG transport interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['MpegTransport_Identity']['meta_info']


class MplsTunnel_Identity(IanaInterfaceType_Identity):
    """
    MPLS Tunnel Virtual Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['MplsTunnel_Identity']['meta_info']


class Mpls_Identity(IanaInterfaceType_Identity):
    """
    MPLS.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Mpls_Identity']['meta_info']


class Msdsl_Identity(IanaInterfaceType_Identity):
    """
    Multi\-rate Symmetric DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Nsip_Identity']['meta_info']


class OpticalChannelGroup_Identity(IanaInterfaceType_Identity):
    """
    Optical Channel Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['OpticalChannelGroup_Identity']['meta_info']


class OpticalChannel_Identity(IanaInterfaceType_Identity):
    """
    Optical Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['OpticalChannel_Identity']['meta_info']


class OpticalTransport_Identity(IanaInterfaceType_Identity):
    """
    Optical Transport.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['OpticalTransport_Identity']['meta_info']


class Other_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Other_Identity']['meta_info']


class OtnOdu_Identity(IanaInterfaceType_Identity):
    """
    OTN Optical Data Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['OtnOdu_Identity']['meta_info']


class OtnOtu_Identity(IanaInterfaceType_Identity):
    """
    OTN Optical channel Transport Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['OtnOtu_Identity']['meta_info']


class Para_Identity(IanaInterfaceType_Identity):
    """
    Parallel\-port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Para_Identity']['meta_info']


class PdnEtherLoop1_Identity(IanaInterfaceType_Identity):
    """
    Paradyne EtherLoop 1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PdnEtherLoop1_Identity']['meta_info']


class PdnEtherLoop2_Identity(IanaInterfaceType_Identity):
    """
    Paradyne EtherLoop 2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PdnEtherLoop2_Identity']['meta_info']


class Pip_Identity(IanaInterfaceType_Identity):
    """
    Provider Instance Port on a bridge per IEEE 802.1ah PBB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Pos_Identity']['meta_info']


class PppMultilinkBundle_Identity(IanaInterfaceType_Identity):
    """
    PPP Multilink Bundle.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PppMultilinkBundle_Identity']['meta_info']


class Ppp_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ppp_Identity']['meta_info']


class PrimaryISDN_Identity(IanaInterfaceType_Identity):
    """
    No longer used.  See also RFC 2127.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PrimaryISDN_Identity']['meta_info']


class PropAtm_Identity(IanaInterfaceType_Identity):
    """
    Proprietary ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PropAtm_Identity']['meta_info']


class PropBWAp2Mp_Identity(IanaInterfaceType_Identity):
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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PropBWAp2Mp_Identity']['meta_info']


class PropCnls_Identity(IanaInterfaceType_Identity):
    """
    Proprietary Connectionless Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PropCnls_Identity']['meta_info']


class PropDocsWirelessDownstream_Identity(IanaInterfaceType_Identity):
    """
    Cisco proprietary Downstream.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PropDocsWirelessDownstream_Identity']['meta_info']


class PropDocsWirelessMaclayer_Identity(IanaInterfaceType_Identity):
    """
    Cisco proprietary Maclayer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PropDocsWirelessMaclayer_Identity']['meta_info']


class PropDocsWirelessUpstream_Identity(IanaInterfaceType_Identity):
    """
    Cisco proprietary Upstream.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PropDocsWirelessUpstream_Identity']['meta_info']


class PropMultiplexor_Identity(IanaInterfaceType_Identity):
    """
    Proprietary multiplexing.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PropMultiplexor_Identity']['meta_info']


class PropPointToPointSerial_Identity(IanaInterfaceType_Identity):
    """
    Proprietary serial.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PropPointToPointSerial_Identity']['meta_info']


class PropVirtual_Identity(IanaInterfaceType_Identity):
    """
    Proprietary virtual/internal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PropVirtual_Identity']['meta_info']


class PropWirelessP2P_Identity(IanaInterfaceType_Identity):
    """
    Prop. P2P wireless interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['PropWirelessP2P_Identity']['meta_info']


class Proteon10Mbit_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Qllc_Identity']['meta_info']


class RadioMAC_Identity(IanaInterfaceType_Identity):
    """
    MAC layer over radio links.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['RadioMAC_Identity']['meta_info']


class Radsl_Identity(IanaInterfaceType_Identity):
    """
    Rate\-Adapt. Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Radsl_Identity']['meta_info']


class ReachDSL_Identity(IanaInterfaceType_Identity):
    """
    Long Reach DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['ReachDSL_Identity']['meta_info']


class Regular1822_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Rfc1483_Identity']['meta_info']


class Rfc877x25_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Rfc877x25_Identity']['meta_info']


class Rpr_Identity(IanaInterfaceType_Identity):
    """
    Resilient Packet Ring Interface Type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Shdsl_Identity']['meta_info']


class SipSig_Identity(IanaInterfaceType_Identity):
    """
    SIP Signaling.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['SipSig_Identity']['meta_info']


class SipTg_Identity(IanaInterfaceType_Identity):
    """
    SIP Trunk Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['SipTg_Identity']['meta_info']


class Sip_Identity(IanaInterfaceType_Identity):
    """
    SMDS, coffee.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Sip_Identity']['meta_info']


class SixToFour_Identity(IanaInterfaceType_Identity):
    """
    6to4 interface (DEPRECATED).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['SixToFour_Identity']['meta_info']


class Slip_Identity(IanaInterfaceType_Identity):
    """
    Generic SLIP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Slip_Identity']['meta_info']


class SmdsDxi_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['SmdsDxi_Identity']['meta_info']


class SmdsIcip_Identity(IanaInterfaceType_Identity):
    """
    SMDS InterCarrier Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['SmdsIcip_Identity']['meta_info']


class SoftwareLoopback_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['SoftwareLoopback_Identity']['meta_info']


class SonetOverheadChannel_Identity(IanaInterfaceType_Identity):
    """
    SONET Overhead Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['SonetOverheadChannel_Identity']['meta_info']


class SonetPath_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['SonetPath_Identity']['meta_info']


class SonetVT_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['SonetVT_Identity']['meta_info']


class Sonet_Identity(IanaInterfaceType_Identity):
    """
    SONET or SDH.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Sonet_Identity']['meta_info']


class Srp_Identity(IanaInterfaceType_Identity):
    """
    Spatial Reuse Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Srp_Identity']['meta_info']


class Ss7SigLink_Identity(IanaInterfaceType_Identity):
    """
    SS7 Signaling Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Ss7SigLink_Identity']['meta_info']


class StackToStack_Identity(IanaInterfaceType_Identity):
    """
    IBM stackToStack.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['StackToStack_Identity']['meta_info']


class StarLan_Identity(IanaInterfaceType_Identity):
    """
    Deprecated via RFC 3635.
    Use ethernetCsmacd(6) instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['StarLan_Identity']['meta_info']


class Tdlc_Identity(IanaInterfaceType_Identity):
    """
    IBM twinaxial data link control.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Tdlc_Identity']['meta_info']


class TeLink_Identity(IanaInterfaceType_Identity):
    """
    TE Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['TeLink_Identity']['meta_info']


class TermPad_Identity(IanaInterfaceType_Identity):
    """
    CCITT\-ITU X.3 PAD Facility.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['TermPad_Identity']['meta_info']


class Tr008_Identity(IanaInterfaceType_Identity):
    """
    TR008.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Tr008_Identity']['meta_info']


class TranspHdlc_Identity(IanaInterfaceType_Identity):
    """
    Transp HDLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['TranspHdlc_Identity']['meta_info']


class Tunnel_Identity(IanaInterfaceType_Identity):
    """
    Encapsulation interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['Vdsl_Identity']['meta_info']


class VirtualIpAddress_Identity(IanaInterfaceType_Identity):
    """
    IBM VIPA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VirtualIpAddress_Identity']['meta_info']


class VirtualTg_Identity(IanaInterfaceType_Identity):
    """
    Virtual Trunk Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VirtualTg_Identity']['meta_info']


class VmwareNicTeam_Identity(IanaInterfaceType_Identity):
    """
    VMware NIC Team.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VmwareNicTeam_Identity']['meta_info']


class VmwareVirtualNic_Identity(IanaInterfaceType_Identity):
    """
    VMware Virtual Network Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VmwareVirtualNic_Identity']['meta_info']


class VoiceDID_Identity(IanaInterfaceType_Identity):
    """
    Voice Direct Inward Dialing.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceDID_Identity']['meta_info']


class VoiceEBS_Identity(IanaInterfaceType_Identity):
    """
    Voice P\-phone EBS physical interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceEBS_Identity']['meta_info']


class VoiceEMFGD_Identity(IanaInterfaceType_Identity):
    """
    Voice E&M Feature Group D.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceEMFGD_Identity']['meta_info']


class VoiceEM_Identity(IanaInterfaceType_Identity):
    """
    Voice recEive and transMit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceEM_Identity']['meta_info']


class VoiceEncap_Identity(IanaInterfaceType_Identity):
    """
    Voice encapsulation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceEncap_Identity']['meta_info']


class VoiceFGDEANA_Identity(IanaInterfaceType_Identity):
    """
    Voice FGD Exchange Access North American.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceFGDEANA_Identity']['meta_info']


class VoiceFGDOS_Identity(IanaInterfaceType_Identity):
    """
    Voice FGD Operator Services.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceFGDOS_Identity']['meta_info']


class VoiceFXO_Identity(IanaInterfaceType_Identity):
    """
    Voice Foreign Exchange Office.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceFXO_Identity']['meta_info']


class VoiceFXS_Identity(IanaInterfaceType_Identity):
    """
    Voice Foreign Exchange Station.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceFXS_Identity']['meta_info']


class VoiceOverAtm_Identity(IanaInterfaceType_Identity):
    """
    Voice over ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceOverAtm_Identity']['meta_info']


class VoiceOverCable_Identity(IanaInterfaceType_Identity):
    """
    Voice Over Cable Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceOverCable_Identity']['meta_info']


class VoiceOverFrameRelay_Identity(IanaInterfaceType_Identity):
    """
    Voice Over Frame Relay.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceOverFrameRelay_Identity']['meta_info']


class VoiceOverIp_Identity(IanaInterfaceType_Identity):
    """
    Voice over IP encapsulation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['VoiceOverIp_Identity']['meta_info']


class WwanPP2_Identity(IanaInterfaceType_Identity):
    """
    3GPP2 WWAN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['WwanPP2_Identity']['meta_info']


class WwanPP_Identity(IanaInterfaceType_Identity):
    """
    3GPP WWAN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['WwanPP_Identity']['meta_info']


class X213_Identity(IanaInterfaceType_Identity):
    """
    CCITT\-ITU X213.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['X213_Identity']['meta_info']


class X25huntGroup_Identity(IanaInterfaceType_Identity):
    """
    X25 Hunt Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['X25huntGroup_Identity']['meta_info']


class X25mlp_Identity(IanaInterfaceType_Identity):
    """
    Multi\-Link Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['X25mlp_Identity']['meta_info']


class X25ple_Identity(IanaInterfaceType_Identity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['X25ple_Identity']['meta_info']


class X86Laps_Identity(IanaInterfaceType_Identity):
    """
    LAPS based on ITU\-T X.86/Y.1323.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _iana_if_type as meta
        return meta._meta_table['X86Laps_Identity']['meta_info']


