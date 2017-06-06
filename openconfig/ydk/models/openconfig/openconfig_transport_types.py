""" openconfig_transport_types 

This module contains general type definitions and identities
for optical transport models.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.openconfig.openconfig_platform_types import Openconfig_Hardware_ComponentIdentity

class AdminStateTypeEnum(Enum):
    """
    AdminStateTypeEnum

    Administrative state modes for

    logical channels in the transponder model.

    .. data:: ENABLED = 0

    	Sets the channel admin state to enabled

    .. data:: DISABLED = 1

    	Sets the channel admin state to disabled

    .. data:: MAINT = 2

    	Sets the channel to maintenance / diagnostic mode

    """

    ENABLED = 0

    DISABLED = 1

    MAINT = 2


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['AdminStateTypeEnum']


class LoopbackModeTypeEnum(Enum):
    """
    LoopbackModeTypeEnum

    Loopback modes for transponder logical channels

    .. data:: NONE = 0

    	No loopback is applied

    .. data:: FACILITY = 1

    	A loopback which directs traffic normally transmitted

    	on the port back to the device as if received on the same

    	port from an external source.

    .. data:: TERMINAL = 2

    	A loopback which directs traffic received from an external

    	source on the port back out the transmit side of the same

    	port.

    """

    NONE = 0

    FACILITY = 1

    TERMINAL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['LoopbackModeTypeEnum']



class Tributary_Rate_Class_TypeIdentity(object):
    """
    Rate of tributary signal \_\- identities will typically reflect
    rounded bit rate.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Tributary_Rate_Class_TypeIdentity']['meta_info']


class Tributary_Protocol_TypeIdentity(object):
    """
    Base identity for protocol framing used by tributary
    signals.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Tributary_Protocol_TypeIdentity']['meta_info']


class Ethernet_Pmd_TypeIdentity(object):
    """
    Ethernet compliance codes (PMD) supported by transceivers
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Ethernet_Pmd_TypeIdentity']['meta_info']


class Fiber_Connector_TypeIdentity(object):
    """
    Type of optical fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Fiber_Connector_TypeIdentity']['meta_info']


class Otn_Application_CodeIdentity(object):
    """
    Supported OTN application codes
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Otn_Application_CodeIdentity']['meta_info']


class Optical_ChannelIdentity(Openconfig_Hardware_ComponentIdentity):
    """
    Optical channels act as carriers for transport traffic
    directed over a line system.  They are represented as
    physical components in the physical inventory model.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Openconfig_Hardware_ComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Optical_ChannelIdentity']['meta_info']


class Transceiver_Form_Factor_TypeIdentity(object):
    """
    Base identity for identifying the type of pluggable optic
    transceiver (i.e,. form factor) used in a port.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Transceiver_Form_Factor_TypeIdentity']['meta_info']


class Logical_Element_Protocol_TypeIdentity(object):
    """
    Type of protocol framing used on the logical channel or
    tributary
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Logical_Element_Protocol_TypeIdentity']['meta_info']


class Sonet_Application_CodeIdentity(object):
    """
    Supported SONET/SDH application codes
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Sonet_Application_CodeIdentity']['meta_info']


class Eth_4X10Gbase_LrIdentity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 4x10GBASE\_LR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_4X10Gbase_LrIdentity']['meta_info']


class Eth_10Gbase_SrIdentity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 10GBASE\_SR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_10Gbase_SrIdentity']['meta_info']


class Prot_Otu3Identity(Tributary_Protocol_TypeIdentity):
    """
    OTU 3 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Otu3Identity']['meta_info']


class Prot_Otu4Identity(Tributary_Protocol_TypeIdentity):
    """
    OTU4 signal protocol (112G) for transporting
    100GE signal
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Otu4Identity']['meta_info']


class Eth_100Gbase_Sr4Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\_SR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_100Gbase_Sr4Identity']['meta_info']


class Prot_Oc768Identity(Tributary_Protocol_TypeIdentity):
    """
    OC 768 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Oc768Identity']['meta_info']


class Prot_Oc48Identity(Tributary_Protocol_TypeIdentity):
    """
    OC48 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Oc48Identity']['meta_info']


class Prot_10Ge_WanIdentity(Tributary_Protocol_TypeIdentity):
    """
    10G Ethernet WAN protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_10Ge_WanIdentity']['meta_info']


class SfpIdentity(Transceiver_Form_Factor_TypeIdentity):
    """
    Small form\-factor pluggable transceiver supporting up to
    10 Gb/s signal
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Transceiver_Form_Factor_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['SfpIdentity']['meta_info']


class Eth_100Gbase_Sr10Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\_SR10
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_100Gbase_Sr10Identity']['meta_info']


class Prot_1GeIdentity(Tributary_Protocol_TypeIdentity):
    """
    1G Ethernet protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_1GeIdentity']['meta_info']


class Otn_UndefinedIdentity(Otn_Application_CodeIdentity):
    """
    OTN application code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Otn_Application_CodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Otn_UndefinedIdentity']['meta_info']


class Eth_100Gbase_Lr4Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\_LR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_100Gbase_Lr4Identity']['meta_info']


class XfpIdentity(Transceiver_Form_Factor_TypeIdentity):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE and OTU2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Transceiver_Form_Factor_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['XfpIdentity']['meta_info']


class Prot_Odu4Identity(Tributary_Protocol_TypeIdentity):
    """
    ODU 4 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Odu4Identity']['meta_info']


class Prot_Stm256Identity(Tributary_Protocol_TypeIdentity):
    """
    STM 256 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Stm256Identity']['meta_info']


class Prot_10Ge_LanIdentity(Tributary_Protocol_TypeIdentity):
    """
    10G Ethernet LAN protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_10Ge_LanIdentity']['meta_info']


class Cfp4Identity(Transceiver_Form_Factor_TypeIdentity):
    """
    1/4 C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Transceiver_Form_Factor_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Cfp4Identity']['meta_info']


class Eth_100Gbase_Clr4Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\_CLR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_100Gbase_Clr4Identity']['meta_info']


class Eth_40Gbase_Lr4Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 40GBASE\_LR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_40Gbase_Lr4Identity']['meta_info']


class Eth_10Gbase_ZrIdentity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 10GBASE\_ZR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_10Gbase_ZrIdentity']['meta_info']


class X2Identity(Transceiver_Form_Factor_TypeIdentity):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE using a XAUI inerface and 4 data channels.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Transceiver_Form_Factor_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['X2Identity']['meta_info']


class Qsfp28Identity(Transceiver_Form_Factor_TypeIdentity):
    """
    QSFP pluggable optic with support for up to 4x28G physical
    channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Transceiver_Form_Factor_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Qsfp28Identity']['meta_info']


class Eth_4X10Gbase_SrIdentity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 4x10GBASE\_SR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_4X10Gbase_SrIdentity']['meta_info']


class Eth_100Gbase_Cr4Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\_CR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_100Gbase_Cr4Identity']['meta_info']


class Vsr2000_3R5Identity(Sonet_Application_CodeIdentity):
    """
    SONET/SDH application code\: VSR2000\_3R5
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Sonet_Application_CodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Vsr2000_3R5Identity']['meta_info']


class Prot_100G_MlgIdentity(Tributary_Protocol_TypeIdentity):
    """
    100G MLG protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_100G_MlgIdentity']['meta_info']


class Prot_Odu3Identity(Tributary_Protocol_TypeIdentity):
    """
    ODU 3 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Odu3Identity']['meta_info']


class Trib_Rate_2__Dot__5GIdentity(Tributary_Rate_Class_TypeIdentity):
    """
    2.5G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Rate_Class_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Trib_Rate_2__Dot__5GIdentity']['meta_info']


class Eth_40Gbase_Cr4Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 40GBASE\_CR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_40Gbase_Cr4Identity']['meta_info']


class Lc_ConnectorIdentity(Fiber_Connector_TypeIdentity):
    """
    LC type fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Fiber_Connector_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Lc_ConnectorIdentity']['meta_info']


class Eth_100G_AocIdentity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 100G\_AOC
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_100G_AocIdentity']['meta_info']


class Prot_Oc192Identity(Tributary_Protocol_TypeIdentity):
    """
    OC 192 (9.6GB) port protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Oc192Identity']['meta_info']


class CfpIdentity(Transceiver_Form_Factor_TypeIdentity):
    """
    C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Transceiver_Form_Factor_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['CfpIdentity']['meta_info']


class Trib_Rate_10GIdentity(Tributary_Rate_Class_TypeIdentity):
    """
    10G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Rate_Class_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Trib_Rate_10GIdentity']['meta_info']


class Eth_100G_AccIdentity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 100G\_ACC
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_100G_AccIdentity']['meta_info']


class Eth_40Gbase_Sr4Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 40GBASE\_SR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_40Gbase_Sr4Identity']['meta_info']


class Prot_OtucnIdentity(Tributary_Protocol_TypeIdentity):
    """
    OTU Cn protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_OtucnIdentity']['meta_info']


class Sfp_PlusIdentity(Transceiver_Form_Factor_TypeIdentity):
    """
    Enhanced small form\-factor pluggable transceiver supporting
    up to 16 Gb/s signals, including 10 GbE and OTU2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Transceiver_Form_Factor_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Sfp_PlusIdentity']['meta_info']


class Trib_Rate_40GIdentity(Tributary_Rate_Class_TypeIdentity):
    """
    40G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Rate_Class_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Trib_Rate_40GIdentity']['meta_info']


class Trib_Rate_1GIdentity(Tributary_Rate_Class_TypeIdentity):
    """
    1G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Rate_Class_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Trib_Rate_1GIdentity']['meta_info']


class Prot_OtnIdentity(Logical_Element_Protocol_TypeIdentity):
    """
    OTN protocol framing
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Logical_Element_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_OtnIdentity']['meta_info']


class Eth_100Gbase_Er4Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\_ER4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_100Gbase_Er4Identity']['meta_info']


class Eth_100Gbase_Psm4Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\_PSM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_100Gbase_Psm4Identity']['meta_info']


class Eth_100Gbase_Cwdm4Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 100GBASE\_CWDM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_100Gbase_Cwdm4Identity']['meta_info']


class P1S1_2D2Identity(Otn_Application_CodeIdentity):
    """
    OTN application code\: P1S1\_2D2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Otn_Application_CodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['P1S1_2D2Identity']['meta_info']


class Prot_40GeIdentity(Tributary_Protocol_TypeIdentity):
    """
    40G Ethernet port protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_40GeIdentity']['meta_info']


class Prot_Odu2EIdentity(Tributary_Protocol_TypeIdentity):
    """
    ODU 2e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Odu2EIdentity']['meta_info']


class Prot_Otu1EIdentity(Tributary_Protocol_TypeIdentity):
    """
    OTU 1e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Otu1EIdentity']['meta_info']


class P1L1_2D1Identity(Otn_Application_CodeIdentity):
    """
    OTN application code\: P1L1\_2D1
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Otn_Application_CodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['P1L1_2D1Identity']['meta_info']


class Eth_40Gbase_Psm4Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 40GBASE\_PSM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_40Gbase_Psm4Identity']['meta_info']


class Vsr2000_3R3Identity(Sonet_Application_CodeIdentity):
    """
    SONET/SDH application code\: VSR2000\_3R3
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Sonet_Application_CodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Vsr2000_3R3Identity']['meta_info']


class P1L1_2D2Identity(Otn_Application_CodeIdentity):
    """
    OTN application code\: P1L1\_2D2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Otn_Application_CodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['P1L1_2D2Identity']['meta_info']


class QsfpIdentity(Transceiver_Form_Factor_TypeIdentity):
    """
    Quad Small Form\-factor Pluggable transceiver that can support
    up to 4x10G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Transceiver_Form_Factor_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['QsfpIdentity']['meta_info']


class Trib_Rate_100GIdentity(Tributary_Rate_Class_TypeIdentity):
    """
    100G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Rate_Class_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Trib_Rate_100GIdentity']['meta_info']


class Prot_EthernetIdentity(Logical_Element_Protocol_TypeIdentity):
    """
    Ethernet protocol framing
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Logical_Element_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_EthernetIdentity']['meta_info']


class Eth_10Gbase_LrIdentity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 10GBASE\_LR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_10Gbase_LrIdentity']['meta_info']


class Vsr2000_3R2Identity(Sonet_Application_CodeIdentity):
    """
    SONET/SDH application code\: VSR2000\_3R2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Sonet_Application_CodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Vsr2000_3R2Identity']['meta_info']


class Prot_Stm64Identity(Tributary_Protocol_TypeIdentity):
    """
    STM 64 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Stm64Identity']['meta_info']


class Cfp2Identity(Transceiver_Form_Factor_TypeIdentity):
    """
    1/2 C form\-factor pluggable, that can support up to a
    200 Gb/s signal with 10x10G, 4x25G, or 8x25G physical
    channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Transceiver_Form_Factor_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Cfp2Identity']['meta_info']


class Eth_40Gbase_Er4Identity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 40GBASE\_ER4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_40Gbase_Er4Identity']['meta_info']


class Prot_100GeIdentity(Tributary_Protocol_TypeIdentity):
    """
    100G Ethernet protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_100GeIdentity']['meta_info']


class OtherIdentity(Transceiver_Form_Factor_TypeIdentity):
    """
    Represents a transceiver form factor not otherwise listed
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Transceiver_Form_Factor_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['OtherIdentity']['meta_info']


class Prot_Stm16Identity(Tributary_Protocol_TypeIdentity):
    """
    STM 16 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Stm16Identity']['meta_info']


class Mpo_ConnectorIdentity(Fiber_Connector_TypeIdentity):
    """
    MPO (multi\-fiber push\-on/pull\-off) type fiber connector
    1x12 fibers
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Fiber_Connector_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Mpo_ConnectorIdentity']['meta_info']


class Eth_10Gbase_LrmIdentity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 10GBASE\_LRM
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_10Gbase_LrmIdentity']['meta_info']


class Eth_10Gbase_ErIdentity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: 10GBASE\_ER
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_10Gbase_ErIdentity']['meta_info']


class Sonet_UndefinedIdentity(Sonet_Application_CodeIdentity):
    """
    SONET/SDH application code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Sonet_Application_CodeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Sonet_UndefinedIdentity']['meta_info']


class Prot_Otu2EIdentity(Tributary_Protocol_TypeIdentity):
    """
    OTU 2e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Otu2EIdentity']['meta_info']


class Prot_Otu2Identity(Tributary_Protocol_TypeIdentity):
    """
    OTU 2 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Otu2Identity']['meta_info']


class Prot_Odu2Identity(Tributary_Protocol_TypeIdentity):
    """
    ODU 2 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Tributary_Protocol_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Prot_Odu2Identity']['meta_info']


class Non_PluggableIdentity(Transceiver_Form_Factor_TypeIdentity):
    """
    Represents a port that does not require a pluggable optic,
    e.g., with on\-board optics like COBO
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Transceiver_Form_Factor_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Non_PluggableIdentity']['meta_info']


class Sc_ConnectorIdentity(Fiber_Connector_TypeIdentity):
    """
    SC type fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Fiber_Connector_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Sc_ConnectorIdentity']['meta_info']


class Cfp2_AcoIdentity(Transceiver_Form_Factor_TypeIdentity):
    """
    CFP2 analog coherent optics transceiver, supporting
    100 Gb, 200Gb, and 250 Gb/s signal.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Transceiver_Form_Factor_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Cfp2_AcoIdentity']['meta_info']


class Eth_UndefinedIdentity(Ethernet_Pmd_TypeIdentity):
    """
    Ethernet compliance code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        Ethernet_Pmd_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_transport_types as meta
        return meta._meta_table['Eth_UndefinedIdentity']['meta_info']


