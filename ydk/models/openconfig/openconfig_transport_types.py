""" openconfig_transport_types 

This module contains general type definitions and identities
for optical transport models.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class EthernetPmdType_Identity(object):
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
        return meta._meta_table['EthernetPmdType_Identity']['meta_info']


class FiberConnectorType_Identity(object):
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
        return meta._meta_table['FiberConnectorType_Identity']['meta_info']


class LogicalElementProtocolType_Identity(object):
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
        return meta._meta_table['LogicalElementProtocolType_Identity']['meta_info']


class OtnApplicationCode_Identity(object):
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
        return meta._meta_table['OtnApplicationCode_Identity']['meta_info']


class SonetApplicationCode_Identity(object):
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
        return meta._meta_table['SonetApplicationCode_Identity']['meta_info']


class TransceiverFormFactorType_Identity(object):
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
        return meta._meta_table['TransceiverFormFactorType_Identity']['meta_info']


class TributaryProtocolType_Identity(object):
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
        return meta._meta_table['TributaryProtocolType_Identity']['meta_info']


class TributaryRateClassType_Identity(object):
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
        return meta._meta_table['TributaryRateClassType_Identity']['meta_info']


class Cfp2_Identity(TransceiverFormFactorType_Identity):
    """
    1/2 C form\-factor pluggable, that can support up to a
    200 Gb/s signal with 10x10G, 4x25G, or 8x25G physical
    channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Cfp2_Identity']['meta_info']


class Cfp4_Identity(TransceiverFormFactorType_Identity):
    """
    1/4 C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Cfp4_Identity']['meta_info']


class Cfp_Identity(TransceiverFormFactorType_Identity):
    """
    C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Cfp_Identity']['meta_info']


class Eth100G_Acc_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100G\_ACC
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100G_Acc_Identity']['meta_info']


class Eth100G_Aoc_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100G\_AOC
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100G_Aoc_Identity']['meta_info']


class Eth100GbaseClr4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-CLR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseClr4_Identity']['meta_info']


class Eth100GbaseCr4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-CR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseCr4_Identity']['meta_info']


class Eth100GbaseCwdm4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-CWDM4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseCwdm4_Identity']['meta_info']


class Eth100GbaseEr4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-ER4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseEr4_Identity']['meta_info']


class Eth100GbaseLr4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-LR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseLr4_Identity']['meta_info']


class Eth100GbasePsm4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-PSM4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbasePsm4_Identity']['meta_info']


class Eth100GbaseSr10_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-SR10
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseSr10_Identity']['meta_info']


class Eth100GbaseSr4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-SR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GbaseSr4_Identity']['meta_info']


class Eth10GbaseEr_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 10GBASE\-ER
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GbaseEr_Identity']['meta_info']


class Eth10GbaseLr_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 10GBASE\-LR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GbaseLr_Identity']['meta_info']


class Eth10GbaseLrm_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 10GBASE\-LRM
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GbaseLrm_Identity']['meta_info']


class Eth10GbaseSr_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 10GBASE\-SR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GbaseSr_Identity']['meta_info']


class Eth10GbaseZr_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 10GBASE\-ZR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GbaseZr_Identity']['meta_info']


class Eth40GbaseCr4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 40GBASE\-CR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GbaseCr4_Identity']['meta_info']


class Eth40GbaseEr4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 40GBASE\-ER4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GbaseEr4_Identity']['meta_info']


class Eth40GbaseLr4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 40GBASE\-LR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GbaseLr4_Identity']['meta_info']


class Eth40GbasePsm4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 40GBASE\-PSM4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GbasePsm4_Identity']['meta_info']


class Eth40GbaseSr4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 40GBASE\-SR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GbaseSr4_Identity']['meta_info']


class Eth4X10GbaseLr_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 4x10GBASE\-LR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth4X10GbaseLr_Identity']['meta_info']


class Eth4X10GbaseSr_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 4x10GBASE\-SR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth4X10GbaseSr_Identity']['meta_info']


class EthUndefined_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: undefined
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['EthUndefined_Identity']['meta_info']


class LcConnector_Identity(FiberConnectorType_Identity):
    """
    LC type fiber connector
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        FiberConnectorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['LcConnector_Identity']['meta_info']


class MpoConnector_Identity(FiberConnectorType_Identity):
    """
    MPO (multi\-fiber push\-on/pull\-off) type fiber connector
    1x12 fibers
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        FiberConnectorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['MpoConnector_Identity']['meta_info']


class NonPluggable_Identity(TransceiverFormFactorType_Identity):
    """
    Represents a port that does not require a pluggable optic,
    e.g., with on\-board optics like COBO
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['NonPluggable_Identity']['meta_info']


class Other_Identity(TransceiverFormFactorType_Identity):
    """
    Represents a transceiver form factor not otherwise listed
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Other_Identity']['meta_info']


class OtnUndefined_Identity(OtnApplicationCode_Identity):
    """
    OTN application code\: undefined
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        OtnApplicationCode_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['OtnUndefined_Identity']['meta_info']


class P1L12D1_Identity(OtnApplicationCode_Identity):
    """
    OTN application code\: P1L1\-2D1
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        OtnApplicationCode_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['P1L12D1_Identity']['meta_info']


class P1L12D2_Identity(OtnApplicationCode_Identity):
    """
    OTN application code\: P1L1\-2D2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        OtnApplicationCode_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['P1L12D2_Identity']['meta_info']


class P1S12D2_Identity(OtnApplicationCode_Identity):
    """
    OTN application code\: P1S1\-2D2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        OtnApplicationCode_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['P1S12D2_Identity']['meta_info']


class Prot100G_Mlg_Identity(TributaryProtocolType_Identity):
    """
    100G MLG protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot100G_Mlg_Identity']['meta_info']


class Prot100Ge_Identity(TributaryProtocolType_Identity):
    """
    100G Ethernet protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot100Ge_Identity']['meta_info']


class Prot10Ge_Lan_Identity(TributaryProtocolType_Identity):
    """
    10G Ethernet LAN protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot10Ge_Lan_Identity']['meta_info']


class Prot10Ge_Wan_Identity(TributaryProtocolType_Identity):
    """
    10G Ethernet WAN protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot10Ge_Wan_Identity']['meta_info']


class Prot1Ge_Identity(TributaryProtocolType_Identity):
    """
    1G Ethernet protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot1Ge_Identity']['meta_info']


class Prot40Ge_Identity(TributaryProtocolType_Identity):
    """
    40G Ethernet port protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot40Ge_Identity']['meta_info']


class ProtEthernet_Identity(LogicalElementProtocolType_Identity):
    """
    Ethernet protocol framing
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        LogicalElementProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtEthernet_Identity']['meta_info']


class ProtOc192_Identity(TributaryProtocolType_Identity):
    """
    OC 192 (9.6GB) port protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOc192_Identity']['meta_info']


class ProtOc48_Identity(TributaryProtocolType_Identity):
    """
    OC48 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOc48_Identity']['meta_info']


class ProtOc768_Identity(TributaryProtocolType_Identity):
    """
    OC 768 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOc768_Identity']['meta_info']


class ProtOdu2E_Identity(TributaryProtocolType_Identity):
    """
    ODU 2e protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOdu2E_Identity']['meta_info']


class ProtOdu2_Identity(TributaryProtocolType_Identity):
    """
    ODU 2 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOdu2_Identity']['meta_info']


class ProtOdu3_Identity(TributaryProtocolType_Identity):
    """
    ODU 3 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOdu3_Identity']['meta_info']


class ProtOdu4_Identity(TributaryProtocolType_Identity):
    """
    ODU 4 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOdu4_Identity']['meta_info']


class ProtOtn_Identity(LogicalElementProtocolType_Identity):
    """
    OTN protocol framing
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        LogicalElementProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtn_Identity']['meta_info']


class ProtOtu1E_Identity(TributaryProtocolType_Identity):
    """
    OTU 1e protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtu1E_Identity']['meta_info']


class ProtOtu2E_Identity(TributaryProtocolType_Identity):
    """
    OTU 2e protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtu2E_Identity']['meta_info']


class ProtOtu2_Identity(TributaryProtocolType_Identity):
    """
    OTU 2 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtu2_Identity']['meta_info']


class ProtOtu3_Identity(TributaryProtocolType_Identity):
    """
    OTU 3 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtu3_Identity']['meta_info']


class ProtOtu4_Identity(TributaryProtocolType_Identity):
    """
    OTU4 signal protocol (112G) for transporting
    100GE signal
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtu4_Identity']['meta_info']


class ProtOtucn_Identity(TributaryProtocolType_Identity):
    """
    OTU Cn protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtucn_Identity']['meta_info']


class ProtStm16_Identity(TributaryProtocolType_Identity):
    """
    STM 16 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtStm16_Identity']['meta_info']


class ProtStm256_Identity(TributaryProtocolType_Identity):
    """
    STM 256 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtStm256_Identity']['meta_info']


class ProtStm64_Identity(TributaryProtocolType_Identity):
    """
    STM 64 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtStm64_Identity']['meta_info']


class Qsfp28_Identity(TransceiverFormFactorType_Identity):
    """
    QSFP pluggable optic with support for up to 4x28G physical
    channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Qsfp28_Identity']['meta_info']


class Qsfp_Identity(TransceiverFormFactorType_Identity):
    """
    Quad Small Form\-factor Pluggable transceiver that can support
    up to 4x10G physical channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Qsfp_Identity']['meta_info']


class ScConnector_Identity(FiberConnectorType_Identity):
    """
    SC type fiber connector
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        FiberConnectorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ScConnector_Identity']['meta_info']


class Sfp_Identity(TransceiverFormFactorType_Identity):
    """
    Small form\-factor pluggable transceiver supporting up to
    10 Gb/s signal
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Sfp_Identity']['meta_info']


class Sfp_Plus_Identity(TransceiverFormFactorType_Identity):
    """
    Enhanced small form\-factor pluggable transceiver supporting
    up to 16 Gb/s signals, including 10 GbE and OTU2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Sfp_Plus_Identity']['meta_info']


class SonetUndefined_Identity(SonetApplicationCode_Identity):
    """
    SONET/SDH application code\: undefined
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        SonetApplicationCode_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['SonetUndefined_Identity']['meta_info']


class TribRate100G_Identity(TributaryRateClassType_Identity):
    """
    100G tributary signal rate
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryRateClassType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate100G_Identity']['meta_info']


class TribRate10G_Identity(TributaryRateClassType_Identity):
    """
    10G tributary signal rate
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryRateClassType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate10G_Identity']['meta_info']


class TribRate1G_Identity(TributaryRateClassType_Identity):
    """
    1G tributary signal rate
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryRateClassType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate1G_Identity']['meta_info']


class TribRate2__Dot__5G_Identity(TributaryRateClassType_Identity):
    """
    2.5G tributary signal rate
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryRateClassType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate2__Dot__5G_Identity']['meta_info']


class TribRate40G_Identity(TributaryRateClassType_Identity):
    """
    40G tributary signal rate
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryRateClassType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate40G_Identity']['meta_info']


class Vsr20003R2_Identity(SonetApplicationCode_Identity):
    """
    SONET/SDH application code\: VSR2000\-3R2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        SonetApplicationCode_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Vsr20003R2_Identity']['meta_info']


class Vsr20003R3_Identity(SonetApplicationCode_Identity):
    """
    SONET/SDH application code\: VSR2000\-3R3
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        SonetApplicationCode_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Vsr20003R3_Identity']['meta_info']


class Vsr20003R5_Identity(SonetApplicationCode_Identity):
    """
    SONET/SDH application code\: VSR2000\-3R5
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        SonetApplicationCode_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Vsr20003R5_Identity']['meta_info']


class X2_Identity(TransceiverFormFactorType_Identity):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE using a XAUI inerface and 4 data channels.
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['X2_Identity']['meta_info']


class Xfp_Identity(TransceiverFormFactorType_Identity):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE and OTU2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Xfp_Identity']['meta_info']


