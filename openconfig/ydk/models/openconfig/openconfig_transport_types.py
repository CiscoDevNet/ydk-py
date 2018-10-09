""" openconfig_transport_types 

This module contains general type definitions and identities
for optical transport models.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.openconfig.openconfig_platform_types import OPENCONFIGHARDWARECOMPONENT


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



class SONETAPPLICATIONCODE(Identity):
    """
    Supported SONET/SDH application codes
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:SONET_APPLICATION_CODE"):
        super(SONETAPPLICATIONCODE, self).__init__(ns, pref, tag)


class OTNAPPLICATIONCODE(Identity):
    """
    Supported OTN application codes
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:OTN_APPLICATION_CODE"):
        super(OTNAPPLICATIONCODE, self).__init__(ns, pref, tag)


class TRANSCEIVERFORMFACTORTYPE(Identity):
    """
    Base identity for identifying the type of pluggable optic
    transceiver (i.e,. form factor) used in a port.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRANSCEIVER_FORM_FACTOR_TYPE"):
        super(TRANSCEIVERFORMFACTORTYPE, self).__init__(ns, pref, tag)


class LOGICALELEMENTPROTOCOLTYPE(Identity):
    """
    Type of protocol framing used on the logical channel or
    tributary
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:LOGICAL_ELEMENT_PROTOCOL_TYPE"):
        super(LOGICALELEMENTPROTOCOLTYPE, self).__init__(ns, pref, tag)


class TRIBUTARYRATECLASSTYPE(Identity):
    """
    Rate of tributary signal \_\- identities will typically reflect
    rounded bit rate.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIBUTARY_RATE_CLASS_TYPE"):
        super(TRIBUTARYRATECLASSTYPE, self).__init__(ns, pref, tag)


class ETHERNETPMDTYPE(Identity):
    """
    Ethernet compliance codes (PMD) supported by transceivers
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETHERNET_PMD_TYPE"):
        super(ETHERNETPMDTYPE, self).__init__(ns, pref, tag)


class FIBERCONNECTORTYPE(Identity):
    """
    Type of optical fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:FIBER_CONNECTOR_TYPE"):
        super(FIBERCONNECTORTYPE, self).__init__(ns, pref, tag)


class OPTICALCHANNEL(OPENCONFIGHARDWARECOMPONENT):
    """
    Optical channels act as carriers for transport traffic
    directed over a line system.  They are represented as
    physical components in the physical inventory model.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:OPTICAL_CHANNEL"):
        super(OPTICALCHANNEL, self).__init__(ns, pref, tag)


class TRIBUTARYPROTOCOLTYPE(Identity):
    """
    Base identity for protocol framing used by tributary
    signals.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIBUTARY_PROTOCOL_TYPE"):
        super(TRIBUTARYPROTOCOLTYPE, self).__init__(ns, pref, tag)


class CFP2(TRANSCEIVERFORMFACTORTYPE):
    """
    1/2 C form\-factor pluggable, that can support up to a
    200 Gb/s signal with 10x10G, 4x25G, or 8x25G physical
    channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:CFP2"):
        super(CFP2, self).__init__(ns, pref, tag)


class QSFP28(TRANSCEIVERFORMFACTORTYPE):
    """
    QSFP pluggable optic with support for up to 4x28G physical
    channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:QSFP28"):
        super(QSFP28, self).__init__(ns, pref, tag)


class ETH40GBASESR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 40GBASE\_SR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_40GBASE_SR4"):
        super(ETH40GBASESR4, self).__init__(ns, pref, tag)


class ETH10GBASELRM(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 10GBASE\_LRM
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_10GBASE_LRM"):
        super(ETH10GBASELRM, self).__init__(ns, pref, tag)


class ETH4X10GBASESR(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 4x10GBASE\_SR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_4X10GBASE_SR"):
        super(ETH4X10GBASESR, self).__init__(ns, pref, tag)


class ETH100GAOC(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100G\_AOC
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100G_AOC"):
        super(ETH100GAOC, self).__init__(ns, pref, tag)


class CFP4(TRANSCEIVERFORMFACTORTYPE):
    """
    1/4 C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:CFP4"):
        super(CFP4, self).__init__(ns, pref, tag)


class SONETUNDEFINED(SONETAPPLICATIONCODE):
    """
    SONET/SDH application code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:SONET_UNDEFINED"):
        super(SONETUNDEFINED, self).__init__(ns, pref, tag)


class P1L12D2(OTNAPPLICATIONCODE):
    """
    OTN application code\: P1L1\_2D2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:P1L1_2D2"):
        super(P1L12D2, self).__init__(ns, pref, tag)


class P1L12D1(OTNAPPLICATIONCODE):
    """
    OTN application code\: P1L1\_2D1
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:P1L1_2D1"):
        super(P1L12D1, self).__init__(ns, pref, tag)


class TRIBRATE10G(TRIBUTARYRATECLASSTYPE):
    """
    10G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_10G"):
        super(TRIBRATE10G, self).__init__(ns, pref, tag)


class PROTOTU2E(TRIBUTARYPROTOCOLTYPE):
    """
    OTU 2e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTU2E"):
        super(PROTOTU2E, self).__init__(ns, pref, tag)


class ETH100GBASESR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_SR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_SR4"):
        super(ETH100GBASESR4, self).__init__(ns, pref, tag)


class ETH10GBASEZR(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 10GBASE\_ZR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_10GBASE_ZR"):
        super(ETH10GBASEZR, self).__init__(ns, pref, tag)


class SCCONNECTOR(FIBERCONNECTORTYPE):
    """
    SC type fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:SC_CONNECTOR"):
        super(SCCONNECTOR, self).__init__(ns, pref, tag)


class VSR20003R3(SONETAPPLICATIONCODE):
    """
    SONET/SDH application code\: VSR2000\_3R3
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:VSR2000_3R3"):
        super(VSR20003R3, self).__init__(ns, pref, tag)


class ETH100GBASEER4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_ER4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_ER4"):
        super(ETH100GBASEER4, self).__init__(ns, pref, tag)


class OTNUNDEFINED(OTNAPPLICATIONCODE):
    """
    OTN application code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:OTN_UNDEFINED"):
        super(OTNUNDEFINED, self).__init__(ns, pref, tag)


class ETH40GBASEER4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 40GBASE\_ER4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_40GBASE_ER4"):
        super(ETH40GBASEER4, self).__init__(ns, pref, tag)


class PROTODU2E(TRIBUTARYPROTOCOLTYPE):
    """
    ODU 2e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_ODU2E"):
        super(PROTODU2E, self).__init__(ns, pref, tag)


class ETH100GACC(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100G\_ACC
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100G_ACC"):
        super(ETH100GACC, self).__init__(ns, pref, tag)


class PROTOC768(TRIBUTARYPROTOCOLTYPE):
    """
    OC 768 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OC768"):
        super(PROTOC768, self).__init__(ns, pref, tag)


class ETHUNDEFINED(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_UNDEFINED"):
        super(ETHUNDEFINED, self).__init__(ns, pref, tag)


class PROT10GEWAN(TRIBUTARYPROTOCOLTYPE):
    """
    10G Ethernet WAN protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_10GE_WAN"):
        super(PROT10GEWAN, self).__init__(ns, pref, tag)


class ETH40GBASELR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 40GBASE\_LR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_40GBASE_LR4"):
        super(ETH40GBASELR4, self).__init__(ns, pref, tag)


class ETH40GBASEPSM4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 40GBASE\_PSM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_40GBASE_PSM4"):
        super(ETH40GBASEPSM4, self).__init__(ns, pref, tag)


class TRIBRATE40G(TRIBUTARYRATECLASSTYPE):
    """
    40G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_40G"):
        super(TRIBRATE40G, self).__init__(ns, pref, tag)


class VSR20003R2(SONETAPPLICATIONCODE):
    """
    SONET/SDH application code\: VSR2000\_3R2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:VSR2000_3R2"):
        super(VSR20003R2, self).__init__(ns, pref, tag)


class PROTSTM16(TRIBUTARYPROTOCOLTYPE):
    """
    STM 16 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_STM16"):
        super(PROTSTM16, self).__init__(ns, pref, tag)


class PROTOTUCN(TRIBUTARYPROTOCOLTYPE):
    """
    OTU Cn protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTUCN"):
        super(PROTOTUCN, self).__init__(ns, pref, tag)


class CFP2ACO(TRANSCEIVERFORMFACTORTYPE):
    """
    CFP2 analog coherent optics transceiver, supporting
    100 Gb, 200Gb, and 250 Gb/s signal.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:CFP2_ACO"):
        super(CFP2ACO, self).__init__(ns, pref, tag)


class X2(TRANSCEIVERFORMFACTORTYPE):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE using a XAUI inerface and 4 data channels.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:X2"):
        super(X2, self).__init__(ns, pref, tag)


class XFP(TRANSCEIVERFORMFACTORTYPE):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE and OTU2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:XFP"):
        super(XFP, self).__init__(ns, pref, tag)


class PROT1GE(TRIBUTARYPROTOCOLTYPE):
    """
    1G Ethernet protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_1GE"):
        super(PROT1GE, self).__init__(ns, pref, tag)


class VSR20003R5(SONETAPPLICATIONCODE):
    """
    SONET/SDH application code\: VSR2000\_3R5
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:VSR2000_3R5"):
        super(VSR20003R5, self).__init__(ns, pref, tag)


class PROT100GE(TRIBUTARYPROTOCOLTYPE):
    """
    100G Ethernet protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_100GE"):
        super(PROT100GE, self).__init__(ns, pref, tag)


class PROTOTU3(TRIBUTARYPROTOCOLTYPE):
    """
    OTU 3 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTU3"):
        super(PROTOTU3, self).__init__(ns, pref, tag)


class PROTOTU2(TRIBUTARYPROTOCOLTYPE):
    """
    OTU 2 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTU2"):
        super(PROTOTU2, self).__init__(ns, pref, tag)


class PROTOTU4(TRIBUTARYPROTOCOLTYPE):
    """
    OTU4 signal protocol (112G) for transporting
    100GE signal
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTU4"):
        super(PROTOTU4, self).__init__(ns, pref, tag)


class PROTETHERNET(LOGICALELEMENTPROTOCOLTYPE):
    """
    Ethernet protocol framing
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_ETHERNET"):
        super(PROTETHERNET, self).__init__(ns, pref, tag)


class TRIBRATE100G(TRIBUTARYRATECLASSTYPE):
    """
    100G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_100G"):
        super(TRIBRATE100G, self).__init__(ns, pref, tag)


class PROTSTM256(TRIBUTARYPROTOCOLTYPE):
    """
    STM 256 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_STM256"):
        super(PROTSTM256, self).__init__(ns, pref, tag)


class PROTOTN(LOGICALELEMENTPROTOCOLTYPE):
    """
    OTN protocol framing
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTN"):
        super(PROTOTN, self).__init__(ns, pref, tag)


class ETH10GBASELR(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 10GBASE\_LR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_10GBASE_LR"):
        super(ETH10GBASELR, self).__init__(ns, pref, tag)


class ETH100GBASESR10(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_SR10
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_SR10"):
        super(ETH100GBASESR10, self).__init__(ns, pref, tag)


class ETH4X10GBASELR(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 4x10GBASE\_LR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_4X10GBASE_LR"):
        super(ETH4X10GBASELR, self).__init__(ns, pref, tag)


class SFPPLUS(TRANSCEIVERFORMFACTORTYPE):
    """
    Enhanced small form\-factor pluggable transceiver supporting
    up to 16 Gb/s signals, including 10 GbE and OTU2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:SFP_PLUS"):
        super(SFPPLUS, self).__init__(ns, pref, tag)


class NONPLUGGABLE(TRANSCEIVERFORMFACTORTYPE):
    """
    Represents a port that does not require a pluggable optic,
    e.g., with on\-board optics like COBO
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:NON_PLUGGABLE"):
        super(NONPLUGGABLE, self).__init__(ns, pref, tag)


class OTHER(TRANSCEIVERFORMFACTORTYPE):
    """
    Represents a transceiver form factor not otherwise listed
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:OTHER"):
        super(OTHER, self).__init__(ns, pref, tag)


class PROT10GELAN(TRIBUTARYPROTOCOLTYPE):
    """
    10G Ethernet LAN protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_10GE_LAN"):
        super(PROT10GELAN, self).__init__(ns, pref, tag)


class PROTOC48(TRIBUTARYPROTOCOLTYPE):
    """
    OC48 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OC48"):
        super(PROTOC48, self).__init__(ns, pref, tag)


class P1S12D2(OTNAPPLICATIONCODE):
    """
    OTN application code\: P1S1\_2D2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:P1S1_2D2"):
        super(P1S12D2, self).__init__(ns, pref, tag)


class PROTOC192(TRIBUTARYPROTOCOLTYPE):
    """
    OC 192 (9.6GB) port protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OC192"):
        super(PROTOC192, self).__init__(ns, pref, tag)


class ETH100GBASELR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_LR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_LR4"):
        super(ETH100GBASELR4, self).__init__(ns, pref, tag)


class TRIBRATE1G(TRIBUTARYRATECLASSTYPE):
    """
    1G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_1G"):
        super(TRIBRATE1G, self).__init__(ns, pref, tag)


class PROT40GE(TRIBUTARYPROTOCOLTYPE):
    """
    40G Ethernet port protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_40GE"):
        super(PROT40GE, self).__init__(ns, pref, tag)


class ETH100GBASECLR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_CLR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_CLR4"):
        super(ETH100GBASECLR4, self).__init__(ns, pref, tag)


class QSFP(TRANSCEIVERFORMFACTORTYPE):
    """
    Quad Small Form\-factor Pluggable transceiver that can support
    up to 4x10G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:QSFP"):
        super(QSFP, self).__init__(ns, pref, tag)


class MPOCONNECTOR(FIBERCONNECTORTYPE):
    """
    MPO (multi\-fiber push\-on/pull\-off) type fiber connector
    1x12 fibers
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:MPO_CONNECTOR"):
        super(MPOCONNECTOR, self).__init__(ns, pref, tag)


class PROT100GMLG(TRIBUTARYPROTOCOLTYPE):
    """
    100G MLG protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_100G_MLG"):
        super(PROT100GMLG, self).__init__(ns, pref, tag)


class TRIBRATE2DOT5G(TRIBUTARYRATECLASSTYPE):
    """
    2.5G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_2.5G"):
        super(TRIBRATE2DOT5G, self).__init__(ns, pref, tag)


class ETH10GBASESR(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 10GBASE\_SR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_10GBASE_SR"):
        super(ETH10GBASESR, self).__init__(ns, pref, tag)


class ETH100GBASECWDM4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_CWDM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_CWDM4"):
        super(ETH100GBASECWDM4, self).__init__(ns, pref, tag)


class SFP(TRANSCEIVERFORMFACTORTYPE):
    """
    Small form\-factor pluggable transceiver supporting up to
    10 Gb/s signal
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:SFP"):
        super(SFP, self).__init__(ns, pref, tag)


class ETH100GBASEPSM4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_PSM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_PSM4"):
        super(ETH100GBASEPSM4, self).__init__(ns, pref, tag)


class ETH40GBASECR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 40GBASE\_CR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_40GBASE_CR4"):
        super(ETH40GBASECR4, self).__init__(ns, pref, tag)


class PROTODU3(TRIBUTARYPROTOCOLTYPE):
    """
    ODU 3 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_ODU3"):
        super(PROTODU3, self).__init__(ns, pref, tag)


class PROTODU2(TRIBUTARYPROTOCOLTYPE):
    """
    ODU 2 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_ODU2"):
        super(PROTODU2, self).__init__(ns, pref, tag)


class PROTODU4(TRIBUTARYPROTOCOLTYPE):
    """
    ODU 4 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_ODU4"):
        super(PROTODU4, self).__init__(ns, pref, tag)


class ETH100GBASECR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_CR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_CR4"):
        super(ETH100GBASECR4, self).__init__(ns, pref, tag)


class LCCONNECTOR(FIBERCONNECTORTYPE):
    """
    LC type fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:LC_CONNECTOR"):
        super(LCCONNECTOR, self).__init__(ns, pref, tag)


class PROTSTM64(TRIBUTARYPROTOCOLTYPE):
    """
    STM 64 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_STM64"):
        super(PROTSTM64, self).__init__(ns, pref, tag)


class PROTOTU1E(TRIBUTARYPROTOCOLTYPE):
    """
    OTU 1e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTU1E"):
        super(PROTOTU1E, self).__init__(ns, pref, tag)


class ETH10GBASEER(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 10GBASE\_ER
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_10GBASE_ER"):
        super(ETH10GBASEER, self).__init__(ns, pref, tag)


class CFP(TRANSCEIVERFORMFACTORTYPE):
    """
    C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2016-06-17'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:CFP"):
        super(CFP, self).__init__(ns, pref, tag)


