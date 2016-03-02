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


class CFP2_Identity(TransceiverFormFactorType_Identity):
    """
    1/2 C form\-factor pluggable, that can support up to a
    200 Gb/s signal with 10x10G, 4x25G, or 8x25G physical
    channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['CFP2_Identity']['meta_info']


class CFP4_Identity(TransceiverFormFactorType_Identity):
    """
    1/4 C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['CFP4_Identity']['meta_info']


class CFP_Identity(TransceiverFormFactorType_Identity):
    """
    C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['CFP_Identity']['meta_info']


class Eth100GBASECLR4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-CLR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GBASECLR4_Identity']['meta_info']


class Eth100GBASECR4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-CR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GBASECR4_Identity']['meta_info']


class Eth100GBASECWDM4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-CWDM4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GBASECWDM4_Identity']['meta_info']


class Eth100GBASEER4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-ER4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GBASEER4_Identity']['meta_info']


class Eth100GBASELR4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-LR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GBASELR4_Identity']['meta_info']


class Eth100GBASEPSM4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-PSM4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GBASEPSM4_Identity']['meta_info']


class Eth100GBASESR10_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-SR10
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GBASESR10_Identity']['meta_info']


class Eth100GBASESR4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100GBASE\-SR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100GBASESR4_Identity']['meta_info']


class Eth100G_ACC_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100G\_ACC
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100G_ACC_Identity']['meta_info']


class Eth100G_AOC_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 100G\_AOC
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth100G_AOC_Identity']['meta_info']


class Eth10GBASEER_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 10GBASE\-ER
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GBASEER_Identity']['meta_info']


class Eth10GBASELRM_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 10GBASE\-LRM
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GBASELRM_Identity']['meta_info']


class Eth10GBASELR_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 10GBASE\-LR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GBASELR_Identity']['meta_info']


class Eth10GBASESR_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 10GBASE\-SR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GBASESR_Identity']['meta_info']


class Eth10GBASEZR_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 10GBASE\-ZR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth10GBASEZR_Identity']['meta_info']


class Eth40GBASECR4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 40GBASE\-CR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GBASECR4_Identity']['meta_info']


class Eth40GBASEER4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 40GBASE\-ER4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GBASEER4_Identity']['meta_info']


class Eth40GBASELR4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 40GBASE\-LR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GBASELR4_Identity']['meta_info']


class Eth40GBASEPSM4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 40GBASE\-PSM4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GBASEPSM4_Identity']['meta_info']


class Eth40GBASESR4_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 40GBASE\-SR4
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth40GBASESR4_Identity']['meta_info']


class Eth4x10GBASELR_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 4x10GBASE\-LR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth4x10GBASELR_Identity']['meta_info']


class Eth4x10GBASESR_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: 4x10GBASE\-SR
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth4x10GBASESR_Identity']['meta_info']


class EthUndefined_Identity(EthernetPmdType_Identity):
    """
    Ethernet compliance code\: undefined
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        EthernetPmdType_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['P1S12D2_Identity']['meta_info']


class Prot100GE_Identity(TributaryProtocolType_Identity):
    """
    100G Ethernet protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot100GE_Identity']['meta_info']


class Prot100G_MLG_Identity(TributaryProtocolType_Identity):
    """
    100G MLG protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot100G_MLG_Identity']['meta_info']


class Prot10GE_LAN_Identity(TributaryProtocolType_Identity):
    """
    10G Ethernet LAN protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot10GE_LAN_Identity']['meta_info']


class Prot10GE_WAN_Identity(TributaryProtocolType_Identity):
    """
    10G Ethernet WAN protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot10GE_WAN_Identity']['meta_info']


class Prot1GE_Identity(TributaryProtocolType_Identity):
    """
    1G Ethernet protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot1GE_Identity']['meta_info']


class Prot40GE_Identity(TributaryProtocolType_Identity):
    """
    40G Ethernet port protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot40GE_Identity']['meta_info']


class ProtEthernet_Identity(LogicalElementProtocolType_Identity):
    """
    Ethernet protocol framing
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        LogicalElementProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtEthernet_Identity']['meta_info']


class ProtOC192_Identity(TributaryProtocolType_Identity):
    """
    OC 192 (9.6GB) port protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOC192_Identity']['meta_info']


class ProtOC48_Identity(TributaryProtocolType_Identity):
    """
    OC48 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOC48_Identity']['meta_info']


class ProtOC768_Identity(TributaryProtocolType_Identity):
    """
    OC 768 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOC768_Identity']['meta_info']


class ProtODU2_Identity(TributaryProtocolType_Identity):
    """
    ODU 2 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtODU2_Identity']['meta_info']


class ProtODU2e_Identity(TributaryProtocolType_Identity):
    """
    ODU 2e protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtODU2e_Identity']['meta_info']


class ProtODU3_Identity(TributaryProtocolType_Identity):
    """
    ODU 3 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtODU3_Identity']['meta_info']


class ProtODU4_Identity(TributaryProtocolType_Identity):
    """
    ODU 4 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtODU4_Identity']['meta_info']


class ProtOTU1e_Identity(TributaryProtocolType_Identity):
    """
    OTU 1e protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOTU1e_Identity']['meta_info']


class ProtOTU2_Identity(TributaryProtocolType_Identity):
    """
    OTU 2 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOTU2_Identity']['meta_info']


class ProtOTU2e_Identity(TributaryProtocolType_Identity):
    """
    OTU 2e protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOTU2e_Identity']['meta_info']


class ProtOTU3_Identity(TributaryProtocolType_Identity):
    """
    OTU 3 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOTU3_Identity']['meta_info']


class ProtOTU4_Identity(TributaryProtocolType_Identity):
    """
    OTU4 signal protocol (112G) for transporting
    100GE signal
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOTU4_Identity']['meta_info']


class ProtOTUCn_Identity(TributaryProtocolType_Identity):
    """
    OTU Cn protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOTUCn_Identity']['meta_info']


class ProtOtn_Identity(LogicalElementProtocolType_Identity):
    """
    OTN protocol framing
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        LogicalElementProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtOtn_Identity']['meta_info']


class ProtSTM16_Identity(TributaryProtocolType_Identity):
    """
    STM 16 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtSTM16_Identity']['meta_info']


class ProtSTM256_Identity(TributaryProtocolType_Identity):
    """
    STM 256 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtSTM256_Identity']['meta_info']


class ProtSTM64_Identity(TributaryProtocolType_Identity):
    """
    STM 64 protocol
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryProtocolType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ProtSTM64_Identity']['meta_info']


class QSFP28_Identity(TransceiverFormFactorType_Identity):
    """
    QSFP pluggable optic with support for up to 4x28G physical
    channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['QSFP28_Identity']['meta_info']


class QSFP_Identity(TransceiverFormFactorType_Identity):
    """
    Quad Small Form\-factor Pluggable transceiver that can support
    up to 4x10G physical channels
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['QSFP_Identity']['meta_info']


class SFP_Identity(TransceiverFormFactorType_Identity):
    """
    Small form\-factor pluggable transceiver supporting up to
    10 Gb/s signal
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['SFP_Identity']['meta_info']


class SFP_plus_Identity(TransceiverFormFactorType_Identity):
    """
    Enhanced small form\-factor pluggable transceiver supporting
    up to 16 Gb/s signals, including 10 GbE and OTU2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['SFP_plus_Identity']['meta_info']


class ScConnector_Identity(FiberConnectorType_Identity):
    """
    SC type fiber connector
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        FiberConnectorType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['ScConnector_Identity']['meta_info']


class SonetUndefined_Identity(SonetApplicationCode_Identity):
    """
    SONET/SDH application code\: undefined
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        SonetApplicationCode_Identity.__init__(self)
        pass

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
        pass

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
        pass

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
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate1G_Identity']['meta_info']


class TribRate2__DOT__5G_Identity(TributaryRateClassType_Identity):
    """
    2.5G tributary signal rate
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryRateClassType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate2__DOT__5G_Identity']['meta_info']


class TribRate40G_Identity(TributaryRateClassType_Identity):
    """
    40G tributary signal rate
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TributaryRateClassType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['TribRate40G_Identity']['meta_info']


class VSR20003R2_Identity(SonetApplicationCode_Identity):
    """
    SONET/SDH application code\: VSR2000\-3R2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        SonetApplicationCode_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['VSR20003R2_Identity']['meta_info']


class VSR20003R3_Identity(SonetApplicationCode_Identity):
    """
    SONET/SDH application code\: VSR2000\-3R3
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        SonetApplicationCode_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['VSR20003R3_Identity']['meta_info']


class VSR20003R5_Identity(SonetApplicationCode_Identity):
    """
    SONET/SDH application code\: VSR2000\-3R5
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        SonetApplicationCode_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['VSR20003R5_Identity']['meta_info']


class X2_Identity(TransceiverFormFactorType_Identity):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE using a XAUI inerface and 4 data channels.
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['X2_Identity']['meta_info']


class XFP_Identity(TransceiverFormFactorType_Identity):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE and OTU2
    
    

    """

    _prefix = 'opt-types'
    _revision = '2015-11-25'

    def __init__(self):
        TransceiverFormFactorType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['XFP_Identity']['meta_info']


