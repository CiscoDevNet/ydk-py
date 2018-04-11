""" openconfig_transport_types 

This module contains general type definitions and identities
for optical transport models.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AdminStateType(Enum):
    """
    AdminStateType (Enum Class)

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
    LoopbackModeType (Enum Class)

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



class TRIBUTARYPROTOCOLTYPE(Identity):
    """
    Base identity for protocol framing used by tributary
    signals.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(TRIBUTARYPROTOCOLTYPE, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIBUTARY_PROTOCOL_TYPE")


class TRANSCEIVERFORMFACTORTYPE(Identity):
    """
    Base identity for identifying the type of pluggable optic
    transceiver (i.e,. form factor) used in a port.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(TRANSCEIVERFORMFACTORTYPE, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRANSCEIVER_FORM_FACTOR_TYPE")


class FIBERCONNECTORTYPE(Identity):
    """
    Type of optical fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(FIBERCONNECTORTYPE, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:FIBER_CONNECTOR_TYPE")


class ETHERNETPMDTYPE(Identity):
    """
    Ethernet compliance codes (PMD) supported by transceivers
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETHERNETPMDTYPE, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETHERNET_PMD_TYPE")


class SONETAPPLICATIONCODE(Identity):
    """
    Supported SONET/SDH application codes
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(SONETAPPLICATIONCODE, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:SONET_APPLICATION_CODE")


class OTNAPPLICATIONCODE(Identity):
    """
    Supported OTN application codes
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(OTNAPPLICATIONCODE, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:OTN_APPLICATION_CODE")


class TRIBUTARYRATECLASSTYPE(Identity):
    """
    Rate of tributary signal \_\- identities will typically reflect
    rounded bit rate.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(TRIBUTARYRATECLASSTYPE, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIBUTARY_RATE_CLASS_TYPE")


class LOGICALELEMENTPROTOCOLTYPE(Identity):
    """
    Type of protocol framing used on the logical channel or
    tributary
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(LOGICALELEMENTPROTOCOLTYPE, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:LOGICAL_ELEMENT_PROTOCOL_TYPE")


class OPTICALCHANNEL(Identity):
    """
    Optical channels act as carriers for transport traffic
    directed over a line system.  They are represented as
    physical components in the physical inventory model.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(OPTICALCHANNEL, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:OPTICAL_CHANNEL")


class PROT1GE(Identity):
    """
    1G Ethernet protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROT1GE, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_1GE")


class PROTOC48(Identity):
    """
    OC48 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTOC48, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OC48")


class PROTSTM16(Identity):
    """
    STM 16 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTSTM16, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_STM16")


class PROT10GELAN(Identity):
    """
    10G Ethernet LAN protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROT10GELAN, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_10GE_LAN")


class PROT10GEWAN(Identity):
    """
    10G Ethernet WAN protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROT10GEWAN, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_10GE_WAN")


class PROTOC192(Identity):
    """
    OC 192 (9.6GB) port protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTOC192, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OC192")


class PROTSTM64(Identity):
    """
    STM 64 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTSTM64, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_STM64")


class PROTOTU2(Identity):
    """
    OTU 2 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTOTU2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTU2")


class PROTOTU2E(Identity):
    """
    OTU 2e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTOTU2E, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTU2E")


class PROTOTU1E(Identity):
    """
    OTU 1e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTOTU1E, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTU1E")


class PROTODU2(Identity):
    """
    ODU 2 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTODU2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_ODU2")


class PROTODU2E(Identity):
    """
    ODU 2e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTODU2E, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_ODU2E")


class PROT40GE(Identity):
    """
    40G Ethernet port protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROT40GE, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_40GE")


class PROTOC768(Identity):
    """
    OC 768 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTOC768, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OC768")


class PROTSTM256(Identity):
    """
    STM 256 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTSTM256, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_STM256")


class PROTOTU3(Identity):
    """
    OTU 3 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTOTU3, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTU3")


class PROTODU3(Identity):
    """
    ODU 3 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTODU3, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_ODU3")


class PROT100GE(Identity):
    """
    100G Ethernet protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROT100GE, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_100GE")


class PROT100GMLG(Identity):
    """
    100G MLG protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROT100GMLG, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_100G_MLG")


class PROTOTU4(Identity):
    """
    OTU4 signal protocol (112G) for transporting
    100GE signal
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTOTU4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTU4")


class PROTOTUCN(Identity):
    """
    OTU Cn protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTOTUCN, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTUCN")


class PROTODU4(Identity):
    """
    ODU 4 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTODU4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_ODU4")


class CFP(Identity):
    """
    C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(CFP, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:CFP")


class CFP2(Identity):
    """
    1/2 C form\-factor pluggable, that can support up to a
    200 Gb/s signal with 10x10G, 4x25G, or 8x25G physical
    channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(CFP2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:CFP2")


class CFP2ACO(Identity):
    """
    CFP2 analog coherent optics transceiver, supporting
    100 Gb, 200Gb, and 250 Gb/s signal.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(CFP2ACO, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:CFP2_ACO")


class CFP4(Identity):
    """
    1/4 C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(CFP4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:CFP4")


class QSFP(Identity):
    """
    Quad Small Form\-factor Pluggable transceiver that can support
    up to 4x10G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(QSFP, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:QSFP")


class QSFP28(Identity):
    """
    QSFP pluggable optic with support for up to 4x28G physical
    channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(QSFP28, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:QSFP28")


class SFP(Identity):
    """
    Small form\-factor pluggable transceiver supporting up to
    10 Gb/s signal
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(SFP, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:SFP")


class SFPPLUS(Identity):
    """
    Enhanced small form\-factor pluggable transceiver supporting
    up to 16 Gb/s signals, including 10 GbE and OTU2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(SFPPLUS, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:SFP_PLUS")


class XFP(Identity):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE and OTU2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(XFP, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:XFP")


class X2(Identity):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE using a XAUI inerface and 4 data channels.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(X2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:X2")


class NONPLUGGABLE(Identity):
    """
    Represents a port that does not require a pluggable optic,
    e.g., with on\-board optics like COBO
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(NONPLUGGABLE, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:NON_PLUGGABLE")


class OTHER(Identity):
    """
    Represents a transceiver form factor not otherwise listed
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(OTHER, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:OTHER")


class SCCONNECTOR(Identity):
    """
    SC type fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(SCCONNECTOR, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:SC_CONNECTOR")


class LCCONNECTOR(Identity):
    """
    LC type fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(LCCONNECTOR, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:LC_CONNECTOR")


class MPOCONNECTOR(Identity):
    """
    MPO (multi\-fiber push\-on/pull\-off) type fiber connector
    1x12 fibers
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(MPOCONNECTOR, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:MPO_CONNECTOR")


class ETH10GBASELRM(Identity):
    """
    Ethernet compliance code\: 10GBASE\_LRM
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH10GBASELRM, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_10GBASE_LRM")


class ETH10GBASELR(Identity):
    """
    Ethernet compliance code\: 10GBASE\_LR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH10GBASELR, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_10GBASE_LR")


class ETH10GBASEZR(Identity):
    """
    Ethernet compliance code\: 10GBASE\_ZR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH10GBASEZR, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_10GBASE_ZR")


class ETH10GBASEER(Identity):
    """
    Ethernet compliance code\: 10GBASE\_ER
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH10GBASEER, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_10GBASE_ER")


class ETH10GBASESR(Identity):
    """
    Ethernet compliance code\: 10GBASE\_SR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH10GBASESR, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_10GBASE_SR")


class ETH40GBASECR4(Identity):
    """
    Ethernet compliance code\: 40GBASE\_CR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH40GBASECR4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_40GBASE_CR4")


class ETH40GBASESR4(Identity):
    """
    Ethernet compliance code\: 40GBASE\_SR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH40GBASESR4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_40GBASE_SR4")


class ETH40GBASELR4(Identity):
    """
    Ethernet compliance code\: 40GBASE\_LR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH40GBASELR4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_40GBASE_LR4")


class ETH40GBASEER4(Identity):
    """
    Ethernet compliance code\: 40GBASE\_ER4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH40GBASEER4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_40GBASE_ER4")


class ETH40GBASEPSM4(Identity):
    """
    Ethernet compliance code\: 40GBASE\_PSM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH40GBASEPSM4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_40GBASE_PSM4")


class ETH4X10GBASELR(Identity):
    """
    Ethernet compliance code\: 4x10GBASE\_LR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH4X10GBASELR, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_4X10GBASE_LR")


class ETH4X10GBASESR(Identity):
    """
    Ethernet compliance code\: 4x10GBASE\_SR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH4X10GBASESR, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_4X10GBASE_SR")


class ETH100GAOC(Identity):
    """
    Ethernet compliance code\: 100G\_AOC
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH100GAOC, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100G_AOC")


class ETH100GACC(Identity):
    """
    Ethernet compliance code\: 100G\_ACC
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH100GACC, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100G_ACC")


class ETH100GBASESR10(Identity):
    """
    Ethernet compliance code\: 100GBASE\_SR10
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH100GBASESR10, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_SR10")


class ETH100GBASESR4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_SR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH100GBASESR4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_SR4")


class ETH100GBASELR4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_LR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH100GBASELR4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_LR4")


class ETH100GBASEER4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_ER4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH100GBASEER4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_ER4")


class ETH100GBASECWDM4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_CWDM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH100GBASECWDM4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_CWDM4")


class ETH100GBASECLR4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_CLR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH100GBASECLR4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_CLR4")


class ETH100GBASEPSM4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_PSM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH100GBASEPSM4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_PSM4")


class ETH100GBASECR4(Identity):
    """
    Ethernet compliance code\: 100GBASE\_CR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETH100GBASECR4, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_100GBASE_CR4")


class ETHUNDEFINED(Identity):
    """
    Ethernet compliance code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(ETHUNDEFINED, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:ETH_UNDEFINED")


class VSR20003R2(Identity):
    """
    SONET/SDH application code\: VSR2000\_3R2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(VSR20003R2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:VSR2000_3R2")


class VSR20003R3(Identity):
    """
    SONET/SDH application code\: VSR2000\_3R3
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(VSR20003R3, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:VSR2000_3R3")


class VSR20003R5(Identity):
    """
    SONET/SDH application code\: VSR2000\_3R5
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(VSR20003R5, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:VSR2000_3R5")


class SONETUNDEFINED(Identity):
    """
    SONET/SDH application code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(SONETUNDEFINED, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:SONET_UNDEFINED")


class P1L12D1(Identity):
    """
    OTN application code\: P1L1\_2D1
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(P1L12D1, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:P1L1_2D1")


class P1S12D2(Identity):
    """
    OTN application code\: P1S1\_2D2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(P1S12D2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:P1S1_2D2")


class P1L12D2(Identity):
    """
    OTN application code\: P1L1\_2D2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(P1L12D2, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:P1L1_2D2")


class OTNUNDEFINED(Identity):
    """
    OTN application code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(OTNUNDEFINED, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:OTN_UNDEFINED")


class TRIBRATE1G(Identity):
    """
    1G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(TRIBRATE1G, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIB_RATE_1G")


class TRIBRATE2DOT5G(Identity):
    """
    2.5G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(TRIBRATE2DOT5G, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIB_RATE_2.5G")


class TRIBRATE10G(Identity):
    """
    10G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(TRIBRATE10G, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIB_RATE_10G")


class TRIBRATE40G(Identity):
    """
    40G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(TRIBRATE40G, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIB_RATE_40G")


class TRIBRATE100G(Identity):
    """
    100G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(TRIBRATE100G, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:TRIB_RATE_100G")


class PROTETHERNET(Identity):
    """
    Ethernet protocol framing
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTETHERNET, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_ETHERNET")


class PROTOTN(Identity):
    """
    OTN protocol framing
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self):
        super(PROTOTN, self).__init__("http://openconfig.net/yang/transport-types", "openconfig-transport-types", "openconfig-transport-types:PROT_OTN")


