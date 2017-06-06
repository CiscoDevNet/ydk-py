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

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_interfaces import InterfaceTypeIdentity


class IanaInterfaceTypeIdentity(InterfaceTypeIdentity):
    """
    This identity is used as a base for all interface types
    defined in the 'ifType definitions' registry.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        InterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IanaInterfaceTypeIdentity']['meta_info']


class H323ProxyIdentity(IanaInterfaceTypeIdentity):
    """
    H323 Voice and Video Proxy.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['H323ProxyIdentity']['meta_info']


class SipsigIdentity(IanaInterfaceTypeIdentity):
    """
    SIP Signaling.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SipsigIdentity']['meta_info']


class PropdocswirelessmaclayerIdentity(IanaInterfaceTypeIdentity):
    """
    Cisco proprietary Maclayer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PropdocswirelessmaclayerIdentity']['meta_info']


class VirtualtgIdentity(IanaInterfaceTypeIdentity):
    """
    Virtual Trunk Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VirtualtgIdentity']['meta_info']


class MplsIdentity(IanaInterfaceTypeIdentity):
    """
    MPLS.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['MplsIdentity']['meta_info']


class StarlanIdentity(IanaInterfaceTypeIdentity):
    """
    Deprecated via RFC 3635.
    Use ethernetCsmacd(6) instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['StarlanIdentity']['meta_info']


class DigitalwrapperoverheadchannelIdentity(IanaInterfaceTypeIdentity):
    """
    Digital Wrapper.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DigitalwrapperoverheadchannelIdentity']['meta_info']


class Rs232Identity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Rs232Identity']['meta_info']


class Capwapdot11ProfileIdentity(IanaInterfaceTypeIdentity):
    """
    WLAN Profile Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Capwapdot11ProfileIdentity']['meta_info']


class SmdsicipIdentity(IanaInterfaceTypeIdentity):
    """
    SMDS InterCarrier Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SmdsicipIdentity']['meta_info']


class Ddnx25Identity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ddnx25Identity']['meta_info']


class Proteon80MbitIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Proteon80MbitIdentity']['meta_info']


class AtmlogicalIdentity(IanaInterfaceTypeIdentity):
    """
    ATM Logical Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AtmlogicalIdentity']['meta_info']


class PropcnlsIdentity(IanaInterfaceTypeIdentity):
    """
    Proprietary Connectionless Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PropcnlsIdentity']['meta_info']


class DvbrccdownstreamIdentity(IanaInterfaceTypeIdentity):
    """
    DVB\-RCC Downstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DvbrccdownstreamIdentity']['meta_info']


class Ds0BundleIdentity(IanaInterfaceTypeIdentity):
    """
    Group of ds0s on the same ds1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ds0BundleIdentity']['meta_info']


class AtmbondIdentity(IanaInterfaceTypeIdentity):
    """
    atmbond.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AtmbondIdentity']['meta_info']


class DvbrccmaclayerIdentity(IanaInterfaceTypeIdentity):
    """
    DVB\-RCC MAC Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DvbrccmaclayerIdentity']['meta_info']


class Pon155Identity(IanaInterfaceTypeIdentity):
    """
    FSAN 155Mb Symetrical PON interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Pon155Identity']['meta_info']


class DlswIdentity(IanaInterfaceTypeIdentity):
    """
    Data Link Switching.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DlswIdentity']['meta_info']


class Regular1822Identity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Regular1822Identity']['meta_info']


class TransphdlcIdentity(IanaInterfaceTypeIdentity):
    """
    Transp HDLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['TransphdlcIdentity']['meta_info']


class HostpadIdentity(IanaInterfaceTypeIdentity):
    """
    CCITT\-ITU X.29 PAD Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['HostpadIdentity']['meta_info']


class DvbrcsmaclayerIdentity(IanaInterfaceTypeIdentity):
    """
    DVB\-RCS MAC Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DvbrcsmaclayerIdentity']['meta_info']


class DcnIdentity(IanaInterfaceTypeIdentity):
    """
    Data Communications Network.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DcnIdentity']['meta_info']


class Ieee80212Identity(IanaInterfaceTypeIdentity):
    """
    100BaseVG.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ieee80212Identity']['meta_info']


class SipIdentity(IanaInterfaceTypeIdentity):
    """
    SMDS, coffee.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SipIdentity']['meta_info']


class DvbrcstdmaIdentity(IanaInterfaceTypeIdentity):
    """
    DVB\-RCS TDMA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DvbrcstdmaIdentity']['meta_info']


class QllcIdentity(IanaInterfaceTypeIdentity):
    """
    SNA QLLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['QllcIdentity']['meta_info']


class X25PleIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['X25PleIdentity']['meta_info']


class PipIdentity(IanaInterfaceTypeIdentity):
    """
    Provider Instance Port on a bridge per IEEE 802.1ah PBB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PipIdentity']['meta_info']


class Rfc877X25Identity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Rfc877X25Identity']['meta_info']


class Iso88026ManIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Iso88026ManIdentity']['meta_info']


class TdlcIdentity(IanaInterfaceTypeIdentity):
    """
    IBM twinaxial data link control.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['TdlcIdentity']['meta_info']


class OpticalchannelgroupIdentity(IanaInterfaceTypeIdentity):
    """
    Optical Channel Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['OpticalchannelgroupIdentity']['meta_info']


class FrforwardIdentity(IanaInterfaceTypeIdentity):
    """
    Frame Forward Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['FrforwardIdentity']['meta_info']


class IsupIdentity(IanaInterfaceTypeIdentity):
    """
    ISUP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IsupIdentity']['meta_info']


class SonetpathIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SonetpathIdentity']['meta_info']


class ModemIdentity(IanaInterfaceTypeIdentity):
    """
    Generic modem.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['ModemIdentity']['meta_info']


class PrimaryisdnIdentity(IanaInterfaceTypeIdentity):
    """
    No longer used.  See also RFC 2127.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PrimaryisdnIdentity']['meta_info']


class PropatmIdentity(IanaInterfaceTypeIdentity):
    """
    Proprietary ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PropatmIdentity']['meta_info']


class DocscablemaclayerIdentity(IanaInterfaceTypeIdentity):
    """
    CATV Mac Layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DocscablemaclayerIdentity']['meta_info']


class X25MlpIdentity(IanaInterfaceTypeIdentity):
    """
    Multi\-Link Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['X25MlpIdentity']['meta_info']


class IsdnIdentity(IanaInterfaceTypeIdentity):
    """
    ISDN and X.25.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IsdnIdentity']['meta_info']


class TermpadIdentity(IanaInterfaceTypeIdentity):
    """
    CCITT\-ITU X.3 PAD Facility.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['TermpadIdentity']['meta_info']


class AviciopticaletherIdentity(IanaInterfaceTypeIdentity):
    """
    Avici Optical Ethernet Aggregate.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AviciopticaletherIdentity']['meta_info']


class LapdIdentity(IanaInterfaceTypeIdentity):
    """
    Link Access Protocol D.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['LapdIdentity']['meta_info']


class CnrIdentity(IanaInterfaceTypeIdentity):
    """
    Combat Net Radio.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['CnrIdentity']['meta_info']


class ChannelIdentity(IanaInterfaceTypeIdentity):
    """
    Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['ChannelIdentity']['meta_info']


class IpoveratmIdentity(IanaInterfaceTypeIdentity):
    """
    IBM ipOverAtm.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IpoveratmIdentity']['meta_info']


class NsipIdentity(IanaInterfaceTypeIdentity):
    """
    XNS over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['NsipIdentity']['meta_info']


class Miox25Identity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Miox25Identity']['meta_info']


class LapfIdentity(IanaInterfaceTypeIdentity):
    """
    LAP F.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['LapfIdentity']['meta_info']


class Aflane8023Identity(IanaInterfaceTypeIdentity):
    """
    ATM Emulated LAN for 802.3.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Aflane8023Identity']['meta_info']


class MediamailoveripIdentity(IanaInterfaceTypeIdentity):
    """
    Multimedia Mail over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['MediamailoveripIdentity']['meta_info']


class X213Identity(IanaInterfaceTypeIdentity):
    """
    CCITT\-ITU X213.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['X213Identity']['meta_info']


class EplrsIdentity(IanaInterfaceTypeIdentity):
    """
    Ext Pos Loc Report Sys.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['EplrsIdentity']['meta_info']


class Gr303RdtIdentity(IanaInterfaceTypeIdentity):
    """
    Remote Digital Terminal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Gr303RdtIdentity']['meta_info']


class HdlcIdentity(IanaInterfaceTypeIdentity):
    """
    HDLC.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['HdlcIdentity']['meta_info']


class VoicefgdeanaIdentity(IanaInterfaceTypeIdentity):
    """
    Voice FGD Exchange Access North American.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoicefgdeanaIdentity']['meta_info']


class CiscoislvlanIdentity(IanaInterfaceTypeIdentity):
    """
    Layer 2 Virtual LAN using Cisco ISL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['CiscoislvlanIdentity']['meta_info']


class PppIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PppIdentity']['meta_info']


class VoiceoveratmIdentity(IanaInterfaceTypeIdentity):
    """
    Voice over ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoiceoveratmIdentity']['meta_info']


class Gr303IdtIdentity(IanaInterfaceTypeIdentity):
    """
    Integrated Digital Terminal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Gr303IdtIdentity']['meta_info']


class SoftwareloopbackIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SoftwareloopbackIdentity']['meta_info']


class Ds1Identity(IanaInterfaceTypeIdentity):
    """
    DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ds1Identity']['meta_info']


class Pon622Identity(IanaInterfaceTypeIdentity):
    """
    FSAN 622Mb Symetrical PON interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Pon622Identity']['meta_info']


class PropmultiplexorIdentity(IanaInterfaceTypeIdentity):
    """
    Proprietary multiplexing.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PropmultiplexorIdentity']['meta_info']


class IpoverclawIdentity(IanaInterfaceTypeIdentity):
    """
    IBM Common Link Access to Workstn.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IpoverclawIdentity']['meta_info']


class Ss7SiglinkIdentity(IanaInterfaceTypeIdentity):
    """
    SS7 Signaling Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ss7SiglinkIdentity']['meta_info']


class CctemulIdentity(IanaInterfaceTypeIdentity):
    """
    ATM Emulated circuit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['CctemulIdentity']['meta_info']


class FastIdentity(IanaInterfaceTypeIdentity):
    """
    Fast channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['FastIdentity']['meta_info']


class DvbtdmIdentity(IanaInterfaceTypeIdentity):
    """
    DVB Satellite TDM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DvbtdmIdentity']['meta_info']


class V36Identity(IanaInterfaceTypeIdentity):
    """
    CCITT V.36.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['V36Identity']['meta_info']


class G9983Identity(IanaInterfaceTypeIdentity):
    """
    G.998.3 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['G9983Identity']['meta_info']


class MpcIdentity(IanaInterfaceTypeIdentity):
    """
    IBM multi\-protocol channel support.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['MpcIdentity']['meta_info']


class QamIdentity(IanaInterfaceTypeIdentity):
    """
    RF Qam Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['QamIdentity']['meta_info']


class Ethernet3MbitIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ethernet3MbitIdentity']['meta_info']


class G703At64KIdentity(IanaInterfaceTypeIdentity):
    """
    CCITT G703 at 64Kbps.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['G703At64KIdentity']['meta_info']


class ImtIdentity(IanaInterfaceTypeIdentity):
    """
    Inter\-Machine Trunks.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['ImtIdentity']['meta_info']


class OtnoduIdentity(IanaInterfaceTypeIdentity):
    """
    OTN Optical Data Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['OtnoduIdentity']['meta_info']


class AtmIdentity(IanaInterfaceTypeIdentity):
    """
    ATM cells.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AtmIdentity']['meta_info']


class ArapIdentity(IanaInterfaceTypeIdentity):
    """
    Appletalk Remote Access Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['ArapIdentity']['meta_info']


class FciplinkIdentity(IanaInterfaceTypeIdentity):
    """
    FCIP Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['FciplinkIdentity']['meta_info']


class Ieee8023AdlagIdentity(IanaInterfaceTypeIdentity):
    """
    IEEE 802.3ad Link Aggregate.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ieee8023AdlagIdentity']['meta_info']


class InfinibandIdentity(IanaInterfaceTypeIdentity):
    """
    Infiniband.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['InfinibandIdentity']['meta_info']


class AtmvciendptIdentity(IanaInterfaceTypeIdentity):
    """
    ATM VCI End Point.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AtmvciendptIdentity']['meta_info']


class X25HuntgroupIdentity(IanaInterfaceTypeIdentity):
    """
    X25 Hunt Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['X25HuntgroupIdentity']['meta_info']


class ArcnetplusIdentity(IanaInterfaceTypeIdentity):
    """
    ARCnet Plus.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['ArcnetplusIdentity']['meta_info']


class Ieee1394Identity(IanaInterfaceTypeIdentity):
    """
    IEEE1394 High Performance Serial Bus.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ieee1394Identity']['meta_info']


class AtmvirtualIdentity(IanaInterfaceTypeIdentity):
    """
    ATM Virtual Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AtmvirtualIdentity']['meta_info']


class Vdsl2Identity(IanaInterfaceTypeIdentity):
    """
    Very high speed digital subscriber line Version 2
    (as per ITU\-T Recommendation G.993.2).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Vdsl2Identity']['meta_info']


class RsrbIdentity(IanaInterfaceTypeIdentity):
    """
    Remote Source Route Bridging.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['RsrbIdentity']['meta_info']


class Propbwap2MpIdentity(IanaInterfaceTypeIdentity):
    """
    PropBroadbandWirelessAccesspt2Multipt (use of this value
    for IEEE 802.16 WMAN interfaces as per IEEE Std 802.16f
    is deprecated, and ieee80216WMAN(237) should be used
    instead).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Propbwap2MpIdentity']['meta_info']


class Tr008Identity(IanaInterfaceTypeIdentity):
    """
    TR008.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Tr008Identity']['meta_info']


class SonetvtIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SonetvtIdentity']['meta_info']


class L2VlanIdentity(IanaInterfaceTypeIdentity):
    """
    Layer 2 Virtual LAN using 802.1Q.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['L2VlanIdentity']['meta_info']


class MpegtransportIdentity(IanaInterfaceTypeIdentity):
    """
    MPEG transport interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['MpegtransportIdentity']['meta_info']


class Pdnetherloop1Identity(IanaInterfaceTypeIdentity):
    """
    Paradyne EtherLoop 1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Pdnetherloop1Identity']['meta_info']


class IlanIdentity(IanaInterfaceTypeIdentity):
    """
    Internal LAN on a bridge per IEEE 802.1ap.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IlanIdentity']['meta_info']


class Ds0Identity(IanaInterfaceTypeIdentity):
    """
    Digital Signal Level 0.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ds0Identity']['meta_info']


class ParaIdentity(IanaInterfaceTypeIdentity):
    """
    Parallel\-port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['ParaIdentity']['meta_info']


class Hiperlan2Identity(IanaInterfaceTypeIdentity):
    """
    HIPERLAN Type 2 Radio Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Hiperlan2Identity']['meta_info']


class BscIdentity(IanaInterfaceTypeIdentity):
    """
    Bisynchronous Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['BscIdentity']['meta_info']


class Iso88025CrfpintIdentity(IanaInterfaceTypeIdentity):
    """
    ISO 802.5 CRFP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Iso88025CrfpintIdentity']['meta_info']


class Adsl2Identity(IanaInterfaceTypeIdentity):
    """
    Asymmetric Digital Subscriber Loop Version 2
    (DEPRECATED/OBSOLETED \- please use adsl2plus(238)
    instead).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Adsl2Identity']['meta_info']


class VoiceoveripIdentity(IanaInterfaceTypeIdentity):
    """
    Voice over IP encapsulation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoiceoveripIdentity']['meta_info']


class SonetIdentity(IanaInterfaceTypeIdentity):
    """
    SONET or SDH.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SonetIdentity']['meta_info']


class FibrechannelIdentity(IanaInterfaceTypeIdentity):
    """
    Fibre Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['FibrechannelIdentity']['meta_info']


class G703At2MbIdentity(IanaInterfaceTypeIdentity):
    """
    Obsolete; see DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['G703At2MbIdentity']['meta_info']


class Propwirelessp2PIdentity(IanaInterfaceTypeIdentity):
    """
    Prop. P2P wireless interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Propwirelessp2PIdentity']['meta_info']


class VoiceebsIdentity(IanaInterfaceTypeIdentity):
    """
    Voice P\-phone EBS physical interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoiceebsIdentity']['meta_info']


class Ieee802154Identity(IanaInterfaceTypeIdentity):
    """
    IEEE 802.15.4 WPAN interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ieee802154Identity']['meta_info']


class BitsIdentity(IanaInterfaceTypeIdentity):
    """
    bitsport.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['BitsIdentity']['meta_info']


class CabledownstreamrfportIdentity(IanaInterfaceTypeIdentity):
    """
    CATV downstream RF Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['CabledownstreamrfportIdentity']['meta_info']


class AlugponphysicaluniIdentity(IanaInterfaceTypeIdentity):
    """
    GPON physical User to Network interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AlugponphysicaluniIdentity']['meta_info']


class VdslIdentity(IanaInterfaceTypeIdentity):
    """
    Very H\-Speed Digital Subscrib. Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VdslIdentity']['meta_info']


class IfGsnIdentity(IanaInterfaceTypeIdentity):
    """
    HIPPI\-6400.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IfGsnIdentity']['meta_info']


class L3IpvlanIdentity(IanaInterfaceTypeIdentity):
    """
    Layer 3 Virtual LAN using IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['L3IpvlanIdentity']['meta_info']


class FramerelayIdentity(IanaInterfaceTypeIdentity):
    """
    DTE only.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['FramerelayIdentity']['meta_info']


class HssiIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['HssiIdentity']['meta_info']


class ProppointtopointserialIdentity(IanaInterfaceTypeIdentity):
    """
    Proprietary serial.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['ProppointtopointserialIdentity']['meta_info']


class HomepnaIdentity(IanaInterfaceTypeIdentity):
    """
    HomePNA ITU\-T G.989.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['HomepnaIdentity']['meta_info']


class DocscablemcmtsdownstreamIdentity(IanaInterfaceTypeIdentity):
    """
    CATV Modular CMTS Downstream Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DocscablemcmtsdownstreamIdentity']['meta_info']


class FramerelaympiIdentity(IanaInterfaceTypeIdentity):
    """
    Multiproto Interconnect over FR.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['FramerelaympiIdentity']['meta_info']


class HippiIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['HippiIdentity']['meta_info']


class NfasIdentity(IanaInterfaceTypeIdentity):
    """
    Non\-Facility Associated Signaling.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['NfasIdentity']['meta_info']


class OpticalchannelIdentity(IanaInterfaceTypeIdentity):
    """
    Optical Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['OpticalchannelIdentity']['meta_info']


class RadiomacIdentity(IanaInterfaceTypeIdentity):
    """
    MAC layer over radio links.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['RadiomacIdentity']['meta_info']


class AlueponphysicaluniIdentity(IanaInterfaceTypeIdentity):
    """
    EPON physical User to Network interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AlueponphysicaluniIdentity']['meta_info']


class E1Identity(IanaInterfaceTypeIdentity):
    """
    Obsolete; see DS1\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['E1Identity']['meta_info']


class Proteon10MbitIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Proteon10MbitIdentity']['meta_info']


class PropdocswirelessdownstreamIdentity(IanaInterfaceTypeIdentity):
    """
    Cisco proprietary Downstream.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PropdocswirelessdownstreamIdentity']['meta_info']


class RprIdentity(IanaInterfaceTypeIdentity):
    """
    Resilient Packet Ring Interface Type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['RprIdentity']['meta_info']


class LmpIdentity(IanaInterfaceTypeIdentity):
    """
    Link Management Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['LmpIdentity']['meta_info']


class TelinkIdentity(IanaInterfaceTypeIdentity):
    """
    TE Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['TelinkIdentity']['meta_info']


class DigitalpowerlineIdentity(IanaInterfaceTypeIdentity):
    """
    IP over Power Lines.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DigitalpowerlineIdentity']['meta_info']


class AlueponlogicallinkIdentity(IanaInterfaceTypeIdentity):
    """
    The emulation of a point\-to\-point link over the EPON
    layer.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AlueponlogicallinkIdentity']['meta_info']


class GponIdentity(IanaInterfaceTypeIdentity):
    """
    Gigabit\-capable passive optical networks (G\-PON) as per
    ITU\-T G.948.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['GponIdentity']['meta_info']


class MplstunnelIdentity(IanaInterfaceTypeIdentity):
    """
    MPLS Tunnel Virtual Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['MplstunnelIdentity']['meta_info']


class VoicedidIdentity(IanaInterfaceTypeIdentity):
    """
    Voice Direct Inward Dialing.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoicedidIdentity']['meta_info']


class OtnotuIdentity(IanaInterfaceTypeIdentity):
    """
    OTN Optical channel Transport Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['OtnotuIdentity']['meta_info']


class VoicefxoIdentity(IanaInterfaceTypeIdentity):
    """
    Voice Foreign Exchange Office.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoicefxoIdentity']['meta_info']


class StacktostackIdentity(IanaInterfaceTypeIdentity):
    """
    IBM stackToStack.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['StacktostackIdentity']['meta_info']


class Iso88025DtrIdentity(IanaInterfaceTypeIdentity):
    """
    ISO 802.5r DTR.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Iso88025DtrIdentity']['meta_info']


class Ds3Identity(IanaInterfaceTypeIdentity):
    """
    DS3\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ds3Identity']['meta_info']


class FramerelayserviceIdentity(IanaInterfaceTypeIdentity):
    """
    FRNETSERV\-MIB.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['FramerelayserviceIdentity']['meta_info']


class PropdocswirelessupstreamIdentity(IanaInterfaceTypeIdentity):
    """
    Cisco proprietary Upstream.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PropdocswirelessupstreamIdentity']['meta_info']


class IpswitchIdentity(IanaInterfaceTypeIdentity):
    """
    IP Switching Objects.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IpswitchIdentity']['meta_info']


class BridgeIdentity(IanaInterfaceTypeIdentity):
    """
    Transparent bridge interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['BridgeIdentity']['meta_info']


class FramerelayinterconnectIdentity(IanaInterfaceTypeIdentity):
    """
    Obsolete; use either
    frameRelay(32) or frameRelayService(44).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['FramerelayinterconnectIdentity']['meta_info']


class EthernetcsmacdIdentity(IanaInterfaceTypeIdentity):
    """
    For all Ethernet\-like interfaces, regardless of speed,
    as per RFC 3635.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['EthernetcsmacdIdentity']['meta_info']


class MfsiglinkIdentity(IanaInterfaceTypeIdentity):
    """
    Multi\-frequency signaling link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['MfsiglinkIdentity']['meta_info']


class Iso88024TokenbusIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Iso88024TokenbusIdentity']['meta_info']


class MsdslIdentity(IanaInterfaceTypeIdentity):
    """
    Multi\-rate Symmetric DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['MsdslIdentity']['meta_info']


class PppmultilinkbundleIdentity(IanaInterfaceTypeIdentity):
    """
    PPP Multilink Bundle.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PppmultilinkbundleIdentity']['meta_info']


class X86LapsIdentity(IanaInterfaceTypeIdentity):
    """
    LAPS based on ITU\-T X.86/Y.1323.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['X86LapsIdentity']['meta_info']


class GfpIdentity(IanaInterfaceTypeIdentity):
    """
    Generic Framing Procedure (GFP).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['GfpIdentity']['meta_info']


class BasicisdnIdentity(IanaInterfaceTypeIdentity):
    """
    No longer used.  See also RFC 2127.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['BasicisdnIdentity']['meta_info']


class TunnelIdentity(IanaInterfaceTypeIdentity):
    """
    Encapsulation interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['TunnelIdentity']['meta_info']


class V11Identity(IanaInterfaceTypeIdentity):
    """
    CCITT V.11/X.21.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['V11Identity']['meta_info']


class FastetherIdentity(IanaInterfaceTypeIdentity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['FastetherIdentity']['meta_info']


class PropvirtualIdentity(IanaInterfaceTypeIdentity):
    """
    Proprietary virtual/internal.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PropvirtualIdentity']['meta_info']


class SlipIdentity(IanaInterfaceTypeIdentity):
    """
    Generic SLIP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SlipIdentity']['meta_info']


class L3IpxvlanIdentity(IanaInterfaceTypeIdentity):
    """
    Layer 3 Virtual LAN using IPX.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['L3IpxvlanIdentity']['meta_info']


class CompositelinkIdentity(IanaInterfaceTypeIdentity):
    """
    Avici Composite Link Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['CompositelinkIdentity']['meta_info']


class ShdslIdentity(IanaInterfaceTypeIdentity):
    """
    Multirate HDSL2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['ShdslIdentity']['meta_info']


class SrpIdentity(IanaInterfaceTypeIdentity):
    """
    Spatial Reuse Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SrpIdentity']['meta_info']


class Aal5Identity(IanaInterfaceTypeIdentity):
    """
    AAL5 over ATM.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Aal5Identity']['meta_info']


class SonetoverheadchannelIdentity(IanaInterfaceTypeIdentity):
    """
    SONET Overhead Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SonetoverheadchannelIdentity']['meta_info']


class UsbIdentity(IanaInterfaceTypeIdentity):
    """
    USB Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['UsbIdentity']['meta_info']


class LapbIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['LapbIdentity']['meta_info']


class DtmIdentity(IanaInterfaceTypeIdentity):
    """
    Dynamic synchronous Transfer Mode.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DtmIdentity']['meta_info']


class Pdnetherloop2Identity(IanaInterfaceTypeIdentity):
    """
    Paradyne EtherLoop 2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Pdnetherloop2Identity']['meta_info']


class Ds1FdlIdentity(IanaInterfaceTypeIdentity):
    """
    Facility Data Link (4Kbps) on a DS1.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ds1FdlIdentity']['meta_info']


class LinegroupIdentity(IanaInterfaceTypeIdentity):
    """
    Interface common to multiple lines.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['LinegroupIdentity']['meta_info']


class V35Identity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['V35Identity']['meta_info']


class DocscableupstreamIdentity(IanaInterfaceTypeIdentity):
    """
    CATV Upstream interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DocscableupstreamIdentity']['meta_info']


class Capwapdot11BssIdentity(IanaInterfaceTypeIdentity):
    """
    WLAN BSS Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Capwapdot11BssIdentity']['meta_info']


class UltraIdentity(IanaInterfaceTypeIdentity):
    """
    Ultra Technologies.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['UltraIdentity']['meta_info']


class AdslIdentity(IanaInterfaceTypeIdentity):
    """
    Asymmetric Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AdslIdentity']['meta_info']


class ReachdslIdentity(IanaInterfaceTypeIdentity):
    """
    Long Reach DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['ReachdslIdentity']['meta_info']


class AtmfuniIdentity(IanaInterfaceTypeIdentity):
    """
    ATM FUNI.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AtmfuniIdentity']['meta_info']


class G9981Identity(IanaInterfaceTypeIdentity):
    """
    G.998.1 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['G9981Identity']['meta_info']


class FddiIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['FddiIdentity']['meta_info']


class IfvfitypeIdentity(IanaInterfaceTypeIdentity):
    """
    VPLS Forwarding Instance Interface Type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IfvfitypeIdentity']['meta_info']


class A12MppswitchIdentity(IanaInterfaceTypeIdentity):
    """
    Avalon Parallel Processor.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['A12MppswitchIdentity']['meta_info']


class IpovercdlcIdentity(IanaInterfaceTypeIdentity):
    """
    IBM ipOverCdlc.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IpovercdlcIdentity']['meta_info']


class Hdsl2Identity(IanaInterfaceTypeIdentity):
    """
    High Bit\-Rate DSL \- 2nd generation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Hdsl2Identity']['meta_info']


class AsyncIdentity(IanaInterfaceTypeIdentity):
    """
    Asynchronous Protocol.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AsyncIdentity']['meta_info']


class SixtofourIdentity(IanaInterfaceTypeIdentity):
    """
    6to4 interface (DEPRECATED).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SixtofourIdentity']['meta_info']


class BgppolicyaccountingIdentity(IanaInterfaceTypeIdentity):
    """
    BGP Policy Accounting.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['BgppolicyaccountingIdentity']['meta_info']


class VoiceemIdentity(IanaInterfaceTypeIdentity):
    """
    Voice recEive and transMit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoiceemIdentity']['meta_info']


class IfpwtypeIdentity(IanaInterfaceTypeIdentity):
    """
    Pseudowire interface type.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IfpwtypeIdentity']['meta_info']


class DocscableupstreamrfportIdentity(IanaInterfaceTypeIdentity):
    """
    DOCSIS CATV Upstream RF Port.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DocscableupstreamrfportIdentity']['meta_info']


class VirtualipaddressIdentity(IanaInterfaceTypeIdentity):
    """
    IBM VIPA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VirtualipaddressIdentity']['meta_info']


class VmwarevirtualnicIdentity(IanaInterfaceTypeIdentity):
    """
    VMware Virtual Network Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VmwarevirtualnicIdentity']['meta_info']


class Iso88025FiberIdentity(IanaInterfaceTypeIdentity):
    """
    ISO 802.5j Fiber Token Ring.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Iso88025FiberIdentity']['meta_info']


class RadslIdentity(IanaInterfaceTypeIdentity):
    """
    Rate\-Adapt. Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['RadslIdentity']['meta_info']


class AtmsubinterfaceIdentity(IanaInterfaceTypeIdentity):
    """
    ATM Sub Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AtmsubinterfaceIdentity']['meta_info']


class DocscableupstreamchannelIdentity(IanaInterfaceTypeIdentity):
    """
    CATV Upstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DocscableupstreamchannelIdentity']['meta_info']


class SmdsdxiIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SmdsdxiIdentity']['meta_info']


class VmwarenicteamIdentity(IanaInterfaceTypeIdentity):
    """
    VMware NIC Team.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VmwarenicteamIdentity']['meta_info']


class VoicefgdosIdentity(IanaInterfaceTypeIdentity):
    """
    Voice FGD Operator Services.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoicefgdosIdentity']['meta_info']


class GtpIdentity(IanaInterfaceTypeIdentity):
    """
    GTP (GPRS Tunneling Protocol).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['GtpIdentity']['meta_info']


class MacseccontrolledifIdentity(IanaInterfaceTypeIdentity):
    """
    MACSecControlled.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['MacseccontrolledifIdentity']['meta_info']


class FrdlciendptIdentity(IanaInterfaceTypeIdentity):
    """
    Frame Relay DLCI End Point.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['FrdlciendptIdentity']['meta_info']


class AtmimaIdentity(IanaInterfaceTypeIdentity):
    """
    ATM IMA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AtmimaIdentity']['meta_info']


class DocscabledownstreamIdentity(IanaInterfaceTypeIdentity):
    """
    CATV Downstream interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DocscabledownstreamIdentity']['meta_info']


class ArcnetIdentity(IanaInterfaceTypeIdentity):
    """
    ARCnet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['ArcnetIdentity']['meta_info']


class Frf16MfrbundleIdentity(IanaInterfaceTypeIdentity):
    """
    FRF.16 Multilink Frame Relay.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Frf16MfrbundleIdentity']['meta_info']


class CoffeeIdentity(IanaInterfaceTypeIdentity):
    """
    Coffee pot.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['CoffeeIdentity']['meta_info']


class HippiinterfaceIdentity(IanaInterfaceTypeIdentity):
    """
    HIPPI interfaces.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['HippiinterfaceIdentity']['meta_info']


class Iso88025TokenringIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Iso88025TokenringIdentity']['meta_info']


class Ieee80216WmanIdentity(IanaInterfaceTypeIdentity):
    """
    IEEE 802.16 WMAN interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ieee80216WmanIdentity']['meta_info']


class G9982Identity(IanaInterfaceTypeIdentity):
    """
    G.998.2 bonded interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['G9982Identity']['meta_info']


class OpticaltransportIdentity(IanaInterfaceTypeIdentity):
    """
    Optical Transport.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['OpticaltransportIdentity']['meta_info']


class CesIdentity(IanaInterfaceTypeIdentity):
    """
    Circuit Emulation Service.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['CesIdentity']['meta_info']


class IpforwardIdentity(IanaInterfaceTypeIdentity):
    """
    IP Forwarding Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IpforwardIdentity']['meta_info']


class AtmdxiIdentity(IanaInterfaceTypeIdentity):
    """
    ATM DXI.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AtmdxiIdentity']['meta_info']


class IsdnuIdentity(IanaInterfaceTypeIdentity):
    """
    ISDN U interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IsdnuIdentity']['meta_info']


class Aflane8025Identity(IanaInterfaceTypeIdentity):
    """
    ATM Emulated LAN for 802.5.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Aflane8025Identity']['meta_info']


class AlueponIdentity(IanaInterfaceTypeIdentity):
    """
    Ethernet Passive Optical Networks (E\-PON).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AlueponIdentity']['meta_info']


class MacsecuncontrolledifIdentity(IanaInterfaceTypeIdentity):
    """
    MACSecUncontrolled.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['MacsecuncontrolledifIdentity']['meta_info']


class Hdh1822Identity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Hdh1822Identity']['meta_info']


class WwanppIdentity(IanaInterfaceTypeIdentity):
    """
    3GPP WWAN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['WwanppIdentity']['meta_info']


class VoicefxsIdentity(IanaInterfaceTypeIdentity):
    """
    Voice Foreign Exchange Station.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoicefxsIdentity']['meta_info']


class SdlcIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SdlcIdentity']['meta_info']


class SdslIdentity(IanaInterfaceTypeIdentity):
    """
    Symmetric Digital Subscriber Loop.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SdslIdentity']['meta_info']


class Ibm370ParchanIdentity(IanaInterfaceTypeIdentity):
    """
    IBM System 360/370 OEMI Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ibm370ParchanIdentity']['meta_info']


class AluelpIdentity(IanaInterfaceTypeIdentity):
    """
    Alcatel\-Lucent Ethernet Link Protection.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AluelpIdentity']['meta_info']


class CapwapwtpvirtualradioIdentity(IanaInterfaceTypeIdentity):
    """
    WTP Virtual Radio Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['CapwapwtpvirtualradioIdentity']['meta_info']


class Iso88023CsmacdIdentity(IanaInterfaceTypeIdentity):
    """
    Deprecated via RFC 3635.
    Use ethernetCsmacd(6) instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Iso88023CsmacdIdentity']['meta_info']


class EsconIdentity(IanaInterfaceTypeIdentity):
    """
    IBM Enterprise Systems Connection.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['EsconIdentity']['meta_info']


class Aal2Identity(IanaInterfaceTypeIdentity):
    """
    ATM adaptation layer 2.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Aal2Identity']['meta_info']


class Adsl2PlusIdentity(IanaInterfaceTypeIdentity):
    """
    Asymmetric Digital Subscriber Loop Version 2 \-
    Version 2 Plus and all variants.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Adsl2PlusIdentity']['meta_info']


class HyperchannelIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['HyperchannelIdentity']['meta_info']


class VoiceencapIdentity(IanaInterfaceTypeIdentity):
    """
    Voice encapsulation.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoiceencapIdentity']['meta_info']


class DvbasiinIdentity(IanaInterfaceTypeIdentity):
    """
    DVB\-ASI Input.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DvbasiinIdentity']['meta_info']


class LocaltalkIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['LocaltalkIdentity']['meta_info']


class Rfc1483Identity(IanaInterfaceTypeIdentity):
    """
    Multiprotocol over ATM AAL5.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Rfc1483Identity']['meta_info']


class VoiceovercableIdentity(IanaInterfaceTypeIdentity):
    """
    Voice Over Cable Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoiceovercableIdentity']['meta_info']


class Ieee80211Identity(IanaInterfaceTypeIdentity):
    """
    Radio spread spectrum.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Ieee80211Identity']['meta_info']


class VoiceemfgdIdentity(IanaInterfaceTypeIdentity):
    """
    Voice E&M Feature Group D.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoiceemfgdIdentity']['meta_info']


class Mocaversion1Identity(IanaInterfaceTypeIdentity):
    """
    MultiMedia over Coax Alliance (MoCA) Interface
    as documented in information provided privately to IANA.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Mocaversion1Identity']['meta_info']


class PlcIdentity(IanaInterfaceTypeIdentity):
    """
    Power Line Communications.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PlcIdentity']['meta_info']


class H323GatekeeperIdentity(IanaInterfaceTypeIdentity):
    """
    H323 Gatekeeper.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['H323GatekeeperIdentity']['meta_info']


class IsdnsIdentity(IanaInterfaceTypeIdentity):
    """
    ISDN S/T interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IsdnsIdentity']['meta_info']


class Q2931Identity(IanaInterfaceTypeIdentity):
    """
    Q.2931.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Q2931Identity']['meta_info']


class AluepononuIdentity(IanaInterfaceTypeIdentity):
    """
    EPON Optical Network Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AluepononuIdentity']['meta_info']


class GigabitethernetIdentity(IanaInterfaceTypeIdentity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['GigabitethernetIdentity']['meta_info']


class FastetherfxIdentity(IanaInterfaceTypeIdentity):
    """
    Obsoleted via RFC 3635.
    ethernetCsmacd(6) should be used instead.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['FastetherfxIdentity']['meta_info']


class EconetIdentity(IanaInterfaceTypeIdentity):
    """
    Acorn Econet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['EconetIdentity']['meta_info']


class DvbrccupstreamIdentity(IanaInterfaceTypeIdentity):
    """
    DVB\-RCC Upstream Channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DvbrccupstreamIdentity']['meta_info']


class OtherIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['OtherIdentity']['meta_info']


class CblvectastarIdentity(IanaInterfaceTypeIdentity):
    """
    Cambridge Broadband Networks Limited VectaStar.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['CblvectastarIdentity']['meta_info']


class AtmradioIdentity(IanaInterfaceTypeIdentity):
    """
    ATM over radio links.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AtmradioIdentity']['meta_info']


class ActelismetaloopIdentity(IanaInterfaceTypeIdentity):
    """
    Acteleis proprietary MetaLOOP High Speed Link.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['ActelismetaloopIdentity']['meta_info']


class V37Identity(IanaInterfaceTypeIdentity):
    """
    V.37.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['V37Identity']['meta_info']


class InterleaveIdentity(IanaInterfaceTypeIdentity):
    """
    Interleave channel.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['InterleaveIdentity']['meta_info']


class Wwanpp2Identity(IanaInterfaceTypeIdentity):
    """
    3GPP2 WWAN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Wwanpp2Identity']['meta_info']


class PosIdentity(IanaInterfaceTypeIdentity):
    """
    Packet over SONET/SDH Interface.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['PosIdentity']['meta_info']


class IdslIdentity(IanaInterfaceTypeIdentity):
    """
    Digital Subscriber Loop over ISDN.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IdslIdentity']['meta_info']


class Iso88022LlcIdentity(IanaInterfaceTypeIdentity):
    """
    
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['Iso88022LlcIdentity']['meta_info']


class VoiceoverframerelayIdentity(IanaInterfaceTypeIdentity):
    """
    Voice Over Frame Relay.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['VoiceoverframerelayIdentity']['meta_info']


class IpIdentity(IanaInterfaceTypeIdentity):
    """
    IP (for APPN HPR in IP networks).
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['IpIdentity']['meta_info']


class MvlIdentity(IanaInterfaceTypeIdentity):
    """
    Multiple Virtual Lines DSL.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['MvlIdentity']['meta_info']


class DvbasioutIdentity(IanaInterfaceTypeIdentity):
    """
    DVB\-ASI Output.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['DvbasioutIdentity']['meta_info']


class SiptgIdentity(IanaInterfaceTypeIdentity):
    """
    SIP Trunk Group.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['SiptgIdentity']['meta_info']


class MyrinetIdentity(IanaInterfaceTypeIdentity):
    """
    Myricom Myrinet.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['MyrinetIdentity']['meta_info']


class EonIdentity(IanaInterfaceTypeIdentity):
    """
    CLNP over IP.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['EonIdentity']['meta_info']


class AlugpononuIdentity(IanaInterfaceTypeIdentity):
    """
    GPON Optical Network Unit.
    
    

    """

    _prefix = 'ianaift'
    _revision = '2014-05-08'

    def __init__(self):
        IanaInterfaceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _iana_if_type as meta
        return meta._meta_table['AlugpononuIdentity']['meta_info']


