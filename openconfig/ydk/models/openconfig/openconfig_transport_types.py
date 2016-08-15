""" openconfig_transport_types 

This module contains general type definitions and identities
for optical transport models.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class EthernetPmdTypeIdentity(object):
    """
    Ethernet compliance codes (PMD) supported by transceivers
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['EthernetPmdTypeIdentity']['meta_info']


class OtnApplicationCodeIdentity(object):
    """
    Supported OTN application codes
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['OtnApplicationCodeIdentity']['meta_info']


class SonetApplicationCodeIdentity(object):
    """
    Supported SONET/SDH application codes
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['SonetApplicationCodeIdentity']['meta_info']


class TransceiverFormFactorTypeIdentity(object):
    """
    Base identity for identifying the type of pluggable optic
    transceiver (i.e,. form factor) used in a port.
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TransceiverFormFactorTypeIdentity']['meta_info']


class LogicalElementProtocolTypeIdentity(object):
    """
    Type of protocol framing used on the logical channel or
    tributary
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['LogicalElementProtocolTypeIdentity']['meta_info']


class TributaryProtocolTypeIdentity(object):
    """
    Base identity for protocol framing used by tributary
    signals.
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TributaryProtocolTypeIdentity']['meta_info']


class TributaryRateClassTypeIdentity(object):
    """
    Rate of tributary signal \-\- identities will typically reflect
    rounded bit rate.
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TributaryRateClassTypeIdentity']['meta_info']


class FiberConnectorTypeIdentity(object):
    """
    Type of optical fiber connector
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['FiberConnectorTypeIdentity']['meta_info']


class ProtOc192Identity(TributaryProtocolTypeIdentity):
    """
    OC 192 (9.6GB) port protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOc192Identity']['meta_info']


class Cfp2Identity(TransceiverFormFactorTypeIdentity):
    """
    1/2 C form\-factor pluggable, that can support up to a
    200 Gb/s signal with 10x10G, 4x25G, or 8x25G physical
    channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Cfp2Identity']['meta_info']


class Prot100G_MlgIdentity(TributaryProtocolTypeIdentity):
    """
    100G MLG protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot100G_MlgIdentity']['meta_info']


class Eth100GbaseEr4Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\-ER4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseEr4Identity']['meta_info']


class Cfp4Identity(TransceiverFormFactorTypeIdentity):
    """
    1/4 C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Cfp4Identity']['meta_info']


class Eth100G_AocIdentity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 100G\_AOC
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100G_AocIdentity']['meta_info']


class Eth10GbaseLrmIdentity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 10GBASE\-LRM
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GbaseLrmIdentity']['meta_info']


class ProtOdu4Identity(TributaryProtocolTypeIdentity):
    """
    ODU 4 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOdu4Identity']['meta_info']


class P1L12D2Identity(OtnApplicationCodeIdentity):
    """
    OTN application code\: P1L1\-2D2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        OtnApplicationCodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['P1L12D2Identity']['meta_info']


class Qsfp28Identity(TransceiverFormFactorTypeIdentity):
    """
    QSFP pluggable optic with support for up to 4x28G physical
    channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Qsfp28Identity']['meta_info']


class Prot10Ge_LanIdentity(TributaryProtocolTypeIdentity):
    """
    10G Ethernet LAN protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot10Ge_LanIdentity']['meta_info']


class Eth10GbaseErIdentity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 10GBASE\-ER
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GbaseErIdentity']['meta_info']


class Sfp_PlusIdentity(TransceiverFormFactorTypeIdentity):
    """
    Enhanced small form\-factor pluggable transceiver supporting
    up to 16 Gb/s signals, including 10 GbE and OTU2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Sfp_PlusIdentity']['meta_info']


class Eth100GbaseCr4Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\-CR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseCr4Identity']['meta_info']


class P1L12D1Identity(OtnApplicationCodeIdentity):
    """
    OTN application code\: P1L1\-2D1
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        OtnApplicationCodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['P1L12D1Identity']['meta_info']


class SfpIdentity(TransceiverFormFactorTypeIdentity):
    """
    Small form\-factor pluggable transceiver supporting up to
    10 Gb/s signal
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['SfpIdentity']['meta_info']


class ProtOtu4Identity(TributaryProtocolTypeIdentity):
    """
    OTU4 signal protocol (112G) for transporting
    100GE signal
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtu4Identity']['meta_info']


class Eth40GbaseEr4Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 40GBASE\-ER4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GbaseEr4Identity']['meta_info']


class Eth100GbasePsm4Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\-PSM4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbasePsm4Identity']['meta_info']


class Eth40GbaseCr4Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 40GBASE\-CR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GbaseCr4Identity']['meta_info']


class SonetUndefinedIdentity(SonetApplicationCodeIdentity):
    """
    SONET/SDH application code\: undefined
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        SonetApplicationCodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['SonetUndefinedIdentity']['meta_info']


class Eth100GbaseClr4Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\-CLR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseClr4Identity']['meta_info']


class Prot10Ge_WanIdentity(TributaryProtocolTypeIdentity):
    """
    10G Ethernet WAN protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot10Ge_WanIdentity']['meta_info']


class ProtStm64Identity(TributaryProtocolTypeIdentity):
    """
    STM 64 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtStm64Identity']['meta_info']


class Eth100GbaseCwdm4Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\-CWDM4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseCwdm4Identity']['meta_info']


class ProtOc48Identity(TributaryProtocolTypeIdentity):
    """
    OC48 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOc48Identity']['meta_info']


class NonPluggableIdentity(TransceiverFormFactorTypeIdentity):
    """
    Represents a port that does not require a pluggable optic,
    e.g., with on\-board optics like COBO
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['NonPluggableIdentity']['meta_info']


class Eth100G_AccIdentity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 100G\_ACC
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100G_AccIdentity']['meta_info']


class Prot1GeIdentity(TributaryProtocolTypeIdentity):
    """
    1G Ethernet protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot1GeIdentity']['meta_info']


class Eth40GbaseSr4Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 40GBASE\-SR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GbaseSr4Identity']['meta_info']


class Eth40GbasePsm4Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 40GBASE\-PSM4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GbasePsm4Identity']['meta_info']


class OtherIdentity(TransceiverFormFactorTypeIdentity):
    """
    Represents a transceiver form factor not otherwise listed
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['OtherIdentity']['meta_info']


class TribRate40GIdentity(TributaryRateClassTypeIdentity):
    """
    40G tributary signal rate
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryRateClassTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate40GIdentity']['meta_info']


class X2Identity(TransceiverFormFactorTypeIdentity):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE using a XAUI inerface and 4 data channels.
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['X2Identity']['meta_info']


class XfpIdentity(TransceiverFormFactorTypeIdentity):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE and OTU2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['XfpIdentity']['meta_info']


class Eth10GbaseSrIdentity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 10GBASE\-SR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GbaseSrIdentity']['meta_info']


class EthUndefinedIdentity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: undefined
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['EthUndefinedIdentity']['meta_info']


class TribRate10GIdentity(TributaryRateClassTypeIdentity):
    """
    10G tributary signal rate
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryRateClassTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate10GIdentity']['meta_info']


class Eth100GbaseSr4Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\-SR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseSr4Identity']['meta_info']


class OtnUndefinedIdentity(OtnApplicationCodeIdentity):
    """
    OTN application code\: undefined
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        OtnApplicationCodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['OtnUndefinedIdentity']['meta_info']


class TribRate1GIdentity(TributaryRateClassTypeIdentity):
    """
    1G tributary signal rate
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryRateClassTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate1GIdentity']['meta_info']


class Eth100GbaseLr4Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\-LR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseLr4Identity']['meta_info']


class TribRate2__Dot__5GIdentity(TributaryRateClassTypeIdentity):
    """
    2.5G tributary signal rate
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryRateClassTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate2__Dot__5GIdentity']['meta_info']


class Prot100GeIdentity(TributaryProtocolTypeIdentity):
    """
    100G Ethernet protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot100GeIdentity']['meta_info']


class ProtStm256Identity(TributaryProtocolTypeIdentity):
    """
    STM 256 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtStm256Identity']['meta_info']


class LcConnectorIdentity(FiberConnectorTypeIdentity):
    """
    LC type fiber connector
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        FiberConnectorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['LcConnectorIdentity']['meta_info']


class ProtOdu3Identity(TributaryProtocolTypeIdentity):
    """
    ODU 3 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOdu3Identity']['meta_info']


class ProtOc768Identity(TributaryProtocolTypeIdentity):
    """
    OC 768 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOc768Identity']['meta_info']


class Eth4X10GbaseSrIdentity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 4x10GBASE\-SR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth4X10GbaseSrIdentity']['meta_info']


class Eth4X10GbaseLrIdentity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 4x10GBASE\-LR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth4X10GbaseLrIdentity']['meta_info']


class Eth10GbaseZrIdentity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 10GBASE\-ZR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GbaseZrIdentity']['meta_info']


class ProtOtu2EIdentity(TributaryProtocolTypeIdentity):
    """
    OTU 2e protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtu2EIdentity']['meta_info']


class ScConnectorIdentity(FiberConnectorTypeIdentity):
    """
    SC type fiber connector
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        FiberConnectorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ScConnectorIdentity']['meta_info']


class Vsr20003R2Identity(SonetApplicationCodeIdentity):
    """
    SONET/SDH application code\: VSR2000\-3R2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        SonetApplicationCodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Vsr20003R2Identity']['meta_info']


class ProtOdu2Identity(TributaryProtocolTypeIdentity):
    """
    ODU 2 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOdu2Identity']['meta_info']


class ProtEthernetIdentity(LogicalElementProtocolTypeIdentity):
    """
    Ethernet protocol framing
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        LogicalElementProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtEthernetIdentity']['meta_info']


class Prot40GeIdentity(TributaryProtocolTypeIdentity):
    """
    40G Ethernet port protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot40GeIdentity']['meta_info']


class ProtOtu3Identity(TributaryProtocolTypeIdentity):
    """
    OTU 3 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtu3Identity']['meta_info']


class ProtOtu2Identity(TributaryProtocolTypeIdentity):
    """
    OTU 2 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtu2Identity']['meta_info']


class Vsr20003R5Identity(SonetApplicationCodeIdentity):
    """
    SONET/SDH application code\: VSR2000\-3R5
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        SonetApplicationCodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Vsr20003R5Identity']['meta_info']


class QsfpIdentity(TransceiverFormFactorTypeIdentity):
    """
    Quad Small Form\-factor Pluggable transceiver that can support
    up to 4x10G physical channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['QsfpIdentity']['meta_info']


class ProtStm16Identity(TributaryProtocolTypeIdentity):
    """
    STM 16 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtStm16Identity']['meta_info']


class ProtOtnIdentity(LogicalElementProtocolTypeIdentity):
    """
    OTN protocol framing
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        LogicalElementProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtnIdentity']['meta_info']


class ProtOdu2EIdentity(TributaryProtocolTypeIdentity):
    """
    ODU 2e protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOdu2EIdentity']['meta_info']


class Eth40GbaseLr4Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 40GBASE\-LR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GbaseLr4Identity']['meta_info']


class Vsr20003R3Identity(SonetApplicationCodeIdentity):
    """
    SONET/SDH application code\: VSR2000\-3R3
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        SonetApplicationCodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Vsr20003R3Identity']['meta_info']


class ProtOtu1EIdentity(TributaryProtocolTypeIdentity):
    """
    OTU 1e protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtu1EIdentity']['meta_info']


class ProtOtucnIdentity(TributaryProtocolTypeIdentity):
    """
    OTU Cn protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtucnIdentity']['meta_info']


class Eth100GbaseSr10Identity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\-SR10
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseSr10Identity']['meta_info']


class Eth10GbaseLrIdentity(EthernetPmdTypeIdentity):
    """
    Ethernet compliance code\: 10GBASE\-LR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GbaseLrIdentity']['meta_info']


class P1S12D2Identity(OtnApplicationCodeIdentity):
    """
    OTN application code\: P1S1\-2D2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        OtnApplicationCodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['P1S12D2Identity']['meta_info']


class MpoConnectorIdentity(FiberConnectorTypeIdentity):
    """
    MPO (multi\-fiber push\-on/pull\-off) type fiber connector
    1x12 fibers
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        FiberConnectorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['MpoConnectorIdentity']['meta_info']


class TribRate100GIdentity(TributaryRateClassTypeIdentity):
    """
    100G tributary signal rate
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryRateClassTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate100GIdentity']['meta_info']


class CfpIdentity(TransceiverFormFactorTypeIdentity):
    """
    C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['CfpIdentity']['meta_info']


