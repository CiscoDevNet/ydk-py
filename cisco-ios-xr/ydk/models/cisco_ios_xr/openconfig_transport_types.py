""" openconfig_transport_types 

This module contains general type definitions and identities
for optical transport models.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AdminStateType(Enum):
    """
    AdminStateType

    Administrative state modes for

    logical channels in the transponder model.

    .. data:: ENABLED = 0

    	Sets the channel admin state to enabled

    .. data:: DISABLED = 1

    	Sets the channel admin state to disabled

    .. data:: MAINT = 2

    	Sets the channel to maintenance / diagnostic mode

    """

    ENABLED = Enum.YLeaf(0, "ENABLED")

    DISABLED = Enum.YLeaf(1, "DISABLED")

    MAINT = Enum.YLeaf(2, "MAINT")


class LoopbackModeType(Enum):
    """
    LoopbackModeType

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

    NONE = Enum.YLeaf(0, "NONE")

    FACILITY = Enum.YLeaf(1, "FACILITY")

    TERMINAL = Enum.YLeaf(2, "TERMINAL")



class Fiber_Connector_Type(Identity):
    """
    Type of optical fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Fiber_Connector_Type, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:FIBER_CONNECTOR_TYPE")


class Otn_Application_Code(Identity):
    """
    Supported OTN application codes
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Otn_Application_Code, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:OTN_APPLICATION_CODE")


class Optical_Channel(Identity):
    """
    Optical channels act as carriers for transport traffic
    directed over a line system.  They are represented as
    physical components in the physical inventory model.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Optical_Channel, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:OPTICAL_CHANNEL")


class Transceiver_Form_Factor_Type(Identity):
    """
    Base identity for identifying the type of pluggable optic
    transceiver (i.e,. form factor) used in a port.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Transceiver_Form_Factor_Type, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRANSCEIVER_FORM_FACTOR_TYPE")


class Tributary_Rate_Class_Type(Identity):
    """
    Rate of tributary signal \_\- identities will typically reflect
    rounded bit rate.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Tributary_Rate_Class_Type, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIBUTARY_RATE_CLASS_TYPE")


class Ethernet_Pmd_Type(Identity):
    """
    Ethernet compliance codes (PMD) supported by transceivers
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Ethernet_Pmd_Type, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETHERNET_PMD_TYPE")


class Logical_Element_Protocol_Type(Identity):
    """
    Type of protocol framing used on the logical channel or
    tributary
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Logical_Element_Protocol_Type, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:LOGICAL_ELEMENT_PROTOCOL_TYPE")


class Tributary_Protocol_Type(Identity):
    """
    Base identity for protocol framing used by tributary
    signals.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Tributary_Protocol_Type, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIBUTARY_PROTOCOL_TYPE")


class Sonet_Application_Code(Identity):
    """
    Supported SONET/SDH application codes
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Sonet_Application_Code, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:SONET_APPLICATION_CODE")


class Eth_40Gbase_Psm4(Identity):
    """
    Ethernet compliance code\: 40GBASE\_PSM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_40Gbase_Psm4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_40GBASE_PSM4")


class Mpo_Connector(Identity):
    """
    MPO (multi\-fiber push\-on/pull\-off) type fiber connector
    1x12 fibers
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Mpo_Connector, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:MPO_CONNECTOR")


class Prot_Odu2(Identity):
    """
    ODU 2 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Odu2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_ODU2")


class X2(Identity):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE using a XAUI inerface and 4 data channels.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(X2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:X2")


class P1L1_2D1(Identity):
    """
    OTN application code\: P1L1\_2D1
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(P1L1_2D1, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:P1L1_2D1")


class Prot_1Ge(Identity):
    """
    1G Ethernet protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_1Ge, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_1GE")


class Prot_Otu3(Identity):
    """
    OTU 3 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Otu3, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTU3")


class Prot_Otn(Identity):
    """
    OTN protocol framing
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Otn, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTN")


class Eth_100Gbase_Lr4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_LR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_100Gbase_Lr4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_LR4")


class Qsfp(Identity):
    """
    Quad Small Form\-factor Pluggable transceiver that can support
    up to 4x10G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Qsfp, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:QSFP")


class Eth_100Gbase_Cr4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_CR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_100Gbase_Cr4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_CR4")


class Prot_100Ge(Identity):
    """
    100G Ethernet protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_100Ge, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_100GE")


class Eth_100G_Aoc(Identity):
    """
    Ethernet compliance code\: 100G\_AOC
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_100G_Aoc, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100G_AOC")


class Eth_100Gbase_Clr4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_CLR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_100Gbase_Clr4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_CLR4")


class Eth_100Gbase_Cwdm4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_CWDM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_100Gbase_Cwdm4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_CWDM4")


class Qsfp28(Identity):
    """
    QSFP pluggable optic with support for up to 4x28G physical
    channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Qsfp28, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:QSFP28")


class Prot_100G_Mlg(Identity):
    """
    100G MLG protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_100G_Mlg, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_100G_MLG")


class Prot_Oc768(Identity):
    """
    OC 768 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Oc768, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OC768")


class Prot_Otucn(Identity):
    """
    OTU Cn protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Otucn, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTUCN")


class Non_Pluggable(Identity):
    """
    Represents a port that does not require a pluggable optic,
    e.g., with on\-board optics like COBO
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Non_Pluggable, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:NON_PLUGGABLE")


class Eth_10Gbase_Er(Identity):
    """
    Ethernet compliance code\: 10GBASE\_ER
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_10Gbase_Er, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_10GBASE_ER")


class Trib_Rate_10G(Identity):
    """
    10G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Trib_Rate_10G, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIB_RATE_10G")


class Prot_Odu3(Identity):
    """
    ODU 3 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Odu3, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_ODU3")


class Trib_Rate_2__Dot__5G(Identity):
    """
    2.5G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Trib_Rate_2__Dot__5G, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIB_RATE_2.5G")


class Trib_Rate_1G(Identity):
    """
    1G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Trib_Rate_1G, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIB_RATE_1G")


class Eth_4X10Gbase_Lr(Identity):
    """
    Ethernet compliance code\: 4x10GBASE\_LR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_4X10Gbase_Lr, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_4X10GBASE_LR")


class Eth_4X10Gbase_Sr(Identity):
    """
    Ethernet compliance code\: 4x10GBASE\_SR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_4X10Gbase_Sr, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_4X10GBASE_SR")


class Eth_10Gbase_Zr(Identity):
    """
    Ethernet compliance code\: 10GBASE\_ZR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_10Gbase_Zr, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_10GBASE_ZR")


class Prot_Stm16(Identity):
    """
    STM 16 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Stm16, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_STM16")


class Vsr2000_3R3(Identity):
    """
    SONET/SDH application code\: VSR2000\_3R3
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Vsr2000_3R3, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:VSR2000_3R3")


class Prot_Odu2E(Identity):
    """
    ODU 2e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Odu2E, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_ODU2E")


class Eth_100Gbase_Er4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_ER4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_100Gbase_Er4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_ER4")


class Eth_40Gbase_Sr4(Identity):
    """
    Ethernet compliance code\: 40GBASE\_SR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_40Gbase_Sr4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_40GBASE_SR4")


class Prot_Stm64(Identity):
    """
    STM 64 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Stm64, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_STM64")


class Prot_Oc48(Identity):
    """
    OC48 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Oc48, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OC48")


class Xfp(Identity):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE and OTU2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Xfp, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:XFP")


class Eth_10Gbase_Sr(Identity):
    """
    Ethernet compliance code\: 10GBASE\_SR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_10Gbase_Sr, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_10GBASE_SR")


class Cfp2_Aco(Identity):
    """
    CFP2 analog coherent optics transceiver, supporting
    100 Gb, 200Gb, and 250 Gb/s signal.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Cfp2_Aco, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:CFP2_ACO")


class Prot_Oc192(Identity):
    """
    OC 192 (9.6GB) port protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Oc192, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OC192")


class Eth_100Gbase_Psm4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_PSM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_100Gbase_Psm4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_PSM4")


class Prot_10Ge_Wan(Identity):
    """
    10G Ethernet WAN protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_10Ge_Wan, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_10GE_WAN")


class Eth_10Gbase_Lr(Identity):
    """
    Ethernet compliance code\: 10GBASE\_LR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_10Gbase_Lr, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_10GBASE_LR")


class Eth_40Gbase_Cr4(Identity):
    """
    Ethernet compliance code\: 40GBASE\_CR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_40Gbase_Cr4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_40GBASE_CR4")


class Other(Identity):
    """
    Represents a transceiver form factor not otherwise listed
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Other, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:OTHER")


class Sc_Connector(Identity):
    """
    SC type fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Sc_Connector, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:SC_CONNECTOR")


class Lc_Connector(Identity):
    """
    LC type fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Lc_Connector, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:LC_CONNECTOR")


class Eth_10Gbase_Lrm(Identity):
    """
    Ethernet compliance code\: 10GBASE\_LRM
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_10Gbase_Lrm, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_10GBASE_LRM")


class Otn_Undefined(Identity):
    """
    OTN application code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Otn_Undefined, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:OTN_UNDEFINED")


class Vsr2000_3R5(Identity):
    """
    SONET/SDH application code\: VSR2000\_3R5
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Vsr2000_3R5, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:VSR2000_3R5")


class Prot_10Ge_Lan(Identity):
    """
    10G Ethernet LAN protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_10Ge_Lan, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_10GE_LAN")


class Cfp(Identity):
    """
    C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Cfp, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:CFP")


class Vsr2000_3R2(Identity):
    """
    SONET/SDH application code\: VSR2000\_3R2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Vsr2000_3R2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:VSR2000_3R2")


class Prot_Otu2(Identity):
    """
    OTU 2 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Otu2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTU2")


class Cfp2(Identity):
    """
    1/2 C form\-factor pluggable, that can support up to a
    200 Gb/s signal with 10x10G, 4x25G, or 8x25G physical
    channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Cfp2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:CFP2")


class Prot_Ethernet(Identity):
    """
    Ethernet protocol framing
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Ethernet, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_ETHERNET")


class Prot_Otu4(Identity):
    """
    OTU4 signal protocol (112G) for transporting
    100GE signal
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Otu4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTU4")


class Cfp4(Identity):
    """
    1/4 C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Cfp4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:CFP4")


class Sonet_Undefined(Identity):
    """
    SONET/SDH application code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Sonet_Undefined, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:SONET_UNDEFINED")


class Eth_100Gbase_Sr10(Identity):
    """
    Ethernet compliance code\: 100GBASE\_SR10
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_100Gbase_Sr10, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_SR10")


class Prot_Odu4(Identity):
    """
    ODU 4 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Odu4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_ODU4")


class Eth_100G_Acc(Identity):
    """
    Ethernet compliance code\: 100G\_ACC
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_100G_Acc, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100G_ACC")


class Eth_40Gbase_Er4(Identity):
    """
    Ethernet compliance code\: 40GBASE\_ER4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_40Gbase_Er4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_40GBASE_ER4")


class Eth_Undefined(Identity):
    """
    Ethernet compliance code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_Undefined, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_UNDEFINED")


class Trib_Rate_100G(Identity):
    """
    100G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Trib_Rate_100G, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIB_RATE_100G")


class Prot_Otu2E(Identity):
    """
    OTU 2e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Otu2E, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTU2E")


class Eth_40Gbase_Lr4(Identity):
    """
    Ethernet compliance code\: 40GBASE\_LR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_40Gbase_Lr4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_40GBASE_LR4")


class Prot_Otu1E(Identity):
    """
    OTU 1e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Otu1E, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTU1E")


class Eth_100Gbase_Sr4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_SR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Eth_100Gbase_Sr4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_SR4")


class Trib_Rate_40G(Identity):
    """
    40G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Trib_Rate_40G, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIB_RATE_40G")


class Prot_40Ge(Identity):
    """
    40G Ethernet port protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_40Ge, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_40GE")


class Prot_Stm256(Identity):
    """
    STM 256 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Prot_Stm256, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_STM256")


class Sfp(Identity):
    """
    Small form\-factor pluggable transceiver supporting up to
    10 Gb/s signal
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Sfp, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:SFP")


class Sfp_Plus(Identity):
    """
    Enhanced small form\-factor pluggable transceiver supporting
    up to 16 Gb/s signals, including 10 GbE and OTU2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(Sfp_Plus, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:SFP_PLUS")


class P1L1_2D2(Identity):
    """
    OTN application code\: P1L1\_2D2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(P1L1_2D2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:P1L1_2D2")


class P1S1_2D2(Identity):
    """
    OTN application code\: P1S1\_2D2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(P1S1_2D2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:P1S1_2D2")


