""" openconfig_transport_types 

This module contains general type definitions and identities
for optical transport models.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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



class FRAMEMAPPINGPROTOCOL(Identity):
    """
    Base identity for frame mapping protocols that can be used
    when mapping Ethernet, OTN or other client signals to OTN
    logical channels.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:FRAME_MAPPING_PROTOCOL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FRAMEMAPPINGPROTOCOL, self).__init__(ns, pref, tag)



class TRIBUTARYSLOTGRANULARITY(Identity):
    """
    Base identity for tributary slot granularity for OTN
    logical channels.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIBUTARY_SLOT_GRANULARITY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBUTARYSLOTGRANULARITY, self).__init__(ns, pref, tag)



class TRIBUTARYPROTOCOLTYPE(Identity):
    """
    Base identity for protocol framing used by tributary
    signals.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIBUTARY_PROTOCOL_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBUTARYPROTOCOLTYPE, self).__init__(ns, pref, tag)



class TRANSCEIVERFORMFACTORTYPE(Identity):
    """
    Base identity for identifying the type of pluggable optic
    transceiver (i.e,. form factor) used in a port.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRANSCEIVER_FORM_FACTOR_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRANSCEIVERFORMFACTORTYPE, self).__init__(ns, pref, tag)



class FIBERCONNECTORTYPE(Identity):
    """
    Type of optical fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:FIBER_CONNECTOR_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FIBERCONNECTORTYPE, self).__init__(ns, pref, tag)



class ETHERNETPMDTYPE(Identity):
    """
    Ethernet compliance codes (PMD) supported by transceivers
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETHERNET_PMD_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETHERNETPMDTYPE, self).__init__(ns, pref, tag)



class SONETAPPLICATIONCODE(Identity):
    """
    Supported SONET/SDH application codes
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:SONET_APPLICATION_CODE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SONETAPPLICATIONCODE, self).__init__(ns, pref, tag)



class OTNAPPLICATIONCODE(Identity):
    """
    Supported OTN application codes
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:OTN_APPLICATION_CODE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OTNAPPLICATIONCODE, self).__init__(ns, pref, tag)



class TRIBUTARYRATECLASSTYPE(Identity):
    """
    Rate of tributary signal \_\- identities will typically reflect
    rounded bit rate.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIBUTARY_RATE_CLASS_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBUTARYRATECLASSTYPE, self).__init__(ns, pref, tag)



class LOGICALELEMENTPROTOCOLTYPE(Identity):
    """
    Type of protocol framing used on the logical channel or
    tributary
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:LOGICAL_ELEMENT_PROTOCOL_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LOGICALELEMENTPROTOCOLTYPE, self).__init__(ns, pref, tag)



class OPTICALCHANNEL(OPENCONFIGHARDWARECOMPONENT):
    """
    Optical channels act as carriers for transport traffic
    directed over a line system.  They are represented as
    physical components in the physical inventory model.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:OPTICAL_CHANNEL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OPTICALCHANNEL, self).__init__(ns, pref, tag)



class FIBERJUMPERTYPE(Identity):
    """
    Types of fiber jumpers used for connecting device ports
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:FIBER_JUMPER_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FIBERJUMPERTYPE, self).__init__(ns, pref, tag)



class OPTICALPORTTYPE(Identity):
    """
    Type definition for optical transport port types
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:OPTICAL_PORT_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OPTICALPORTTYPE, self).__init__(ns, pref, tag)



class AMP(FRAMEMAPPINGPROTOCOL):
    """
    Asynchronous Mapping Procedure
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:AMP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AMP, self).__init__(ns, pref, tag)



class GMP(FRAMEMAPPINGPROTOCOL):
    """
    Generic Mapping Procedure
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:GMP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(GMP, self).__init__(ns, pref, tag)



class BMP(FRAMEMAPPINGPROTOCOL):
    """
    Bit\-synchronous Mapping Procedure
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:BMP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(BMP, self).__init__(ns, pref, tag)



class CBR(FRAMEMAPPINGPROTOCOL):
    """
    Constant Bit Rate Mapping Procedure
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:CBR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CBR, self).__init__(ns, pref, tag)



class GFPT(FRAMEMAPPINGPROTOCOL):
    """
    Transparent Generic Framing Protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:GFP_T"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(GFPT, self).__init__(ns, pref, tag)



class GFPF(FRAMEMAPPINGPROTOCOL):
    """
    Framed\-Mapped Generic Framing Protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:GFP_F"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(GFPF, self).__init__(ns, pref, tag)



class TRIBSLOT1DOT25G(TRIBUTARYSLOTGRANULARITY):
    """
    The tributary slot with a bandwidth of approximately 1.25 Gb/s
    as defined in ITU\-T G.709 standard.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_SLOT_1.25G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBSLOT1DOT25G, self).__init__(ns, pref, tag)



class TRIBSLOT2DOT5G(TRIBUTARYSLOTGRANULARITY):
    """
    The tributary slot with a bandwidth of approximately 2.5 Gb/s
    as defined in ITU\-T G.709 standard.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_SLOT_2.5G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBSLOT2DOT5G, self).__init__(ns, pref, tag)



class TRIBSLOT5G(TRIBUTARYSLOTGRANULARITY):
    """
    The tributary slot with a bandwidth of approximately 5 Gb/s
    as defined in ITU\-T G.709 standard.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_SLOT_5G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBSLOT5G, self).__init__(ns, pref, tag)



class PROT1GE(TRIBUTARYPROTOCOLTYPE):
    """
    1G Ethernet protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_1GE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROT1GE, self).__init__(ns, pref, tag)



class PROTOC48(TRIBUTARYPROTOCOLTYPE):
    """
    OC48 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OC48"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTOC48, self).__init__(ns, pref, tag)



class PROTSTM16(TRIBUTARYPROTOCOLTYPE):
    """
    STM 16 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_STM16"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTSTM16, self).__init__(ns, pref, tag)



class PROT10GELAN(TRIBUTARYPROTOCOLTYPE):
    """
    10G Ethernet LAN protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_10GE_LAN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROT10GELAN, self).__init__(ns, pref, tag)



class PROT10GEWAN(TRIBUTARYPROTOCOLTYPE):
    """
    10G Ethernet WAN protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_10GE_WAN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROT10GEWAN, self).__init__(ns, pref, tag)



class PROTOC192(TRIBUTARYPROTOCOLTYPE):
    """
    OC 192 (9.6GB) port protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OC192"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTOC192, self).__init__(ns, pref, tag)



class PROTSTM64(TRIBUTARYPROTOCOLTYPE):
    """
    STM 64 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_STM64"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTSTM64, self).__init__(ns, pref, tag)



class PROTOTU2(TRIBUTARYPROTOCOLTYPE):
    """
    OTU 2 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTU2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTOTU2, self).__init__(ns, pref, tag)



class PROTOTU2E(TRIBUTARYPROTOCOLTYPE):
    """
    OTU 2e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTU2E"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTOTU2E, self).__init__(ns, pref, tag)



class PROTOTU1E(TRIBUTARYPROTOCOLTYPE):
    """
    OTU 1e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTU1E"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTOTU1E, self).__init__(ns, pref, tag)



class PROTODU2(TRIBUTARYPROTOCOLTYPE):
    """
    ODU 2 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_ODU2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTODU2, self).__init__(ns, pref, tag)



class PROTODU2E(TRIBUTARYPROTOCOLTYPE):
    """
    ODU 2e protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_ODU2E"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTODU2E, self).__init__(ns, pref, tag)



class PROT40GE(TRIBUTARYPROTOCOLTYPE):
    """
    40G Ethernet port protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_40GE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROT40GE, self).__init__(ns, pref, tag)



class PROTOC768(TRIBUTARYPROTOCOLTYPE):
    """
    OC 768 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OC768"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTOC768, self).__init__(ns, pref, tag)



class PROTSTM256(TRIBUTARYPROTOCOLTYPE):
    """
    STM 256 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_STM256"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTSTM256, self).__init__(ns, pref, tag)



class PROTOTU3(TRIBUTARYPROTOCOLTYPE):
    """
    OTU 3 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTU3"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTOTU3, self).__init__(ns, pref, tag)



class PROTODU3(TRIBUTARYPROTOCOLTYPE):
    """
    ODU 3 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_ODU3"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTODU3, self).__init__(ns, pref, tag)



class PROT100GE(TRIBUTARYPROTOCOLTYPE):
    """
    100G Ethernet protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_100GE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROT100GE, self).__init__(ns, pref, tag)



class PROT100GMLG(TRIBUTARYPROTOCOLTYPE):
    """
    100G MLG protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_100G_MLG"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROT100GMLG, self).__init__(ns, pref, tag)



class PROTOTU4(TRIBUTARYPROTOCOLTYPE):
    """
    OTU4 signal protocol (112G) for transporting
    100GE signal
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTU4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTOTU4, self).__init__(ns, pref, tag)



class PROTOTUCN(TRIBUTARYPROTOCOLTYPE):
    """
    OTU Cn protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTUCN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTOTUCN, self).__init__(ns, pref, tag)



class PROTODUCN(TRIBUTARYPROTOCOLTYPE):
    """
    ODU Cn protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_ODUCN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTODUCN, self).__init__(ns, pref, tag)



class PROTODU4(TRIBUTARYPROTOCOLTYPE):
    """
    ODU 4 protocol
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_ODU4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTODU4, self).__init__(ns, pref, tag)



class CFP(TRANSCEIVERFORMFACTORTYPE):
    """
    C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:CFP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CFP, self).__init__(ns, pref, tag)



class CFP2(TRANSCEIVERFORMFACTORTYPE):
    """
    1/2 C form\-factor pluggable, that can support up to a
    200 Gb/s signal with 10x10G, 4x25G, or 8x25G physical
    channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:CFP2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CFP2, self).__init__(ns, pref, tag)



class CFP2ACO(TRANSCEIVERFORMFACTORTYPE):
    """
    CFP2 analog coherent optics transceiver, supporting
    100 Gb, 200Gb, and 250 Gb/s signal.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:CFP2_ACO"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CFP2ACO, self).__init__(ns, pref, tag)



class CFP4(TRANSCEIVERFORMFACTORTYPE):
    """
    1/4 C form\-factor pluggable, that can support up to a
    100 Gb/s signal with 10x10G or 4x25G physical channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:CFP4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CFP4, self).__init__(ns, pref, tag)



class QSFP(TRANSCEIVERFORMFACTORTYPE):
    """
    OriginalQuad Small Form\-factor Pluggable transceiver that can
    support 4x1G physical channels.  Not commonly used.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:QSFP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(QSFP, self).__init__(ns, pref, tag)



class QSFPPLUS(TRANSCEIVERFORMFACTORTYPE):
    """
    Quad Small Form\-factor Pluggable transceiver that can support
    up to 4x10G physical channels.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:QSFP_PLUS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(QSFPPLUS, self).__init__(ns, pref, tag)



class QSFP28(TRANSCEIVERFORMFACTORTYPE):
    """
    QSFP pluggable optic with support for up to 4x28G physical
    channels
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:QSFP28"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(QSFP28, self).__init__(ns, pref, tag)



class CPAK(TRANSCEIVERFORMFACTORTYPE):
    """
    Cisco CPAK transceiver supporting 100 Gb/s.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:CPAK"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CPAK, self).__init__(ns, pref, tag)



class SFP(TRANSCEIVERFORMFACTORTYPE):
    """
    Small form\-factor pluggable transceiver supporting up to
    10 Gb/s signal
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:SFP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SFP, self).__init__(ns, pref, tag)



class SFPPLUS(TRANSCEIVERFORMFACTORTYPE):
    """
    Enhanced small form\-factor pluggable transceiver supporting
    up to 16 Gb/s signals, including 10 GbE and OTU2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:SFP_PLUS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SFPPLUS, self).__init__(ns, pref, tag)



class XFP(TRANSCEIVERFORMFACTORTYPE):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE and OTU2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:XFP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(XFP, self).__init__(ns, pref, tag)



class X2(TRANSCEIVERFORMFACTORTYPE):
    """
    10 Gigabit small form factor pluggable transceiver supporting
    10 GbE using a XAUI inerface and 4 data channels.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:X2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(X2, self).__init__(ns, pref, tag)



class NONPLUGGABLE(TRANSCEIVERFORMFACTORTYPE):
    """
    Represents a port that does not require a pluggable optic,
    e.g., with on\-board optics like COBO
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:NON_PLUGGABLE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(NONPLUGGABLE, self).__init__(ns, pref, tag)



class OTHER(TRANSCEIVERFORMFACTORTYPE):
    """
    Represents a transceiver form factor not otherwise listed
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:OTHER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OTHER, self).__init__(ns, pref, tag)



class SCCONNECTOR(FIBERCONNECTORTYPE):
    """
    SC type fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:SC_CONNECTOR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SCCONNECTOR, self).__init__(ns, pref, tag)



class LCCONNECTOR(FIBERCONNECTORTYPE):
    """
    LC type fiber connector
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:LC_CONNECTOR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LCCONNECTOR, self).__init__(ns, pref, tag)



class MPOCONNECTOR(FIBERCONNECTORTYPE):
    """
    MPO (multi\-fiber push\-on/pull\-off) type fiber connector
    1x12 fibers
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:MPO_CONNECTOR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MPOCONNECTOR, self).__init__(ns, pref, tag)



class ETH10GBASELRM(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 10GBASE\_LRM
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_10GBASE_LRM"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH10GBASELRM, self).__init__(ns, pref, tag)



class ETH10GBASELR(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 10GBASE\_LR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_10GBASE_LR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH10GBASELR, self).__init__(ns, pref, tag)



class ETH10GBASEZR(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 10GBASE\_ZR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_10GBASE_ZR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH10GBASEZR, self).__init__(ns, pref, tag)



class ETH10GBASEER(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 10GBASE\_ER
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_10GBASE_ER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH10GBASEER, self).__init__(ns, pref, tag)



class ETH10GBASESR(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 10GBASE\_SR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_10GBASE_SR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH10GBASESR, self).__init__(ns, pref, tag)



class ETH40GBASECR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 40GBASE\_CR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_40GBASE_CR4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH40GBASECR4, self).__init__(ns, pref, tag)



class ETH40GBASESR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 40GBASE\_SR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_40GBASE_SR4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH40GBASESR4, self).__init__(ns, pref, tag)



class ETH40GBASELR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 40GBASE\_LR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_40GBASE_LR4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH40GBASELR4, self).__init__(ns, pref, tag)



class ETH40GBASEER4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 40GBASE\_ER4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_40GBASE_ER4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH40GBASEER4, self).__init__(ns, pref, tag)



class ETH40GBASEPSM4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 40GBASE\_PSM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_40GBASE_PSM4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH40GBASEPSM4, self).__init__(ns, pref, tag)



class ETH4X10GBASELR(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 4x10GBASE\_LR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_4X10GBASE_LR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH4X10GBASELR, self).__init__(ns, pref, tag)



class ETH4X10GBASESR(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 4x10GBASE\_SR
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_4X10GBASE_SR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH4X10GBASESR, self).__init__(ns, pref, tag)



class ETH100GAOC(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100G\_AOC
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100G_AOC"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH100GAOC, self).__init__(ns, pref, tag)



class ETH100GACC(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100G\_ACC
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100G_ACC"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH100GACC, self).__init__(ns, pref, tag)



class ETH100GBASESR10(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_SR10
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_SR10"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH100GBASESR10, self).__init__(ns, pref, tag)



class ETH100GBASESR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_SR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_SR4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH100GBASESR4, self).__init__(ns, pref, tag)



class ETH100GBASELR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_LR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_LR4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH100GBASELR4, self).__init__(ns, pref, tag)



class ETH100GBASEER4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_ER4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_ER4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH100GBASEER4, self).__init__(ns, pref, tag)



class ETH100GBASECWDM4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_CWDM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_CWDM4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH100GBASECWDM4, self).__init__(ns, pref, tag)



class ETH100GBASECLR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_CLR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_CLR4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH100GBASECLR4, self).__init__(ns, pref, tag)



class ETH100GBASEPSM4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_PSM4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_PSM4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH100GBASEPSM4, self).__init__(ns, pref, tag)



class ETH100GBASECR4(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: 100GBASE\_CR4
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_100GBASE_CR4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETH100GBASECR4, self).__init__(ns, pref, tag)



class ETHUNDEFINED(ETHERNETPMDTYPE):
    """
    Ethernet compliance code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ETH_UNDEFINED"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETHUNDEFINED, self).__init__(ns, pref, tag)



class VSR20003R2(SONETAPPLICATIONCODE):
    """
    SONET/SDH application code\: VSR2000\_3R2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:VSR2000_3R2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VSR20003R2, self).__init__(ns, pref, tag)



class VSR20003R3(SONETAPPLICATIONCODE):
    """
    SONET/SDH application code\: VSR2000\_3R3
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:VSR2000_3R3"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VSR20003R3, self).__init__(ns, pref, tag)



class VSR20003R5(SONETAPPLICATIONCODE):
    """
    SONET/SDH application code\: VSR2000\_3R5
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:VSR2000_3R5"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VSR20003R5, self).__init__(ns, pref, tag)



class SONETUNDEFINED(SONETAPPLICATIONCODE):
    """
    SONET/SDH application code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:SONET_UNDEFINED"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SONETUNDEFINED, self).__init__(ns, pref, tag)



class P1L12D1(OTNAPPLICATIONCODE):
    """
    OTN application code\: P1L1\_2D1
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:P1L1_2D1"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(P1L12D1, self).__init__(ns, pref, tag)



class P1S12D2(OTNAPPLICATIONCODE):
    """
    OTN application code\: P1S1\_2D2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:P1S1_2D2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(P1S12D2, self).__init__(ns, pref, tag)



class P1L12D2(OTNAPPLICATIONCODE):
    """
    OTN application code\: P1L1\_2D2
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:P1L1_2D2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(P1L12D2, self).__init__(ns, pref, tag)



class OTNUNDEFINED(OTNAPPLICATIONCODE):
    """
    OTN application code\: undefined
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:OTN_UNDEFINED"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OTNUNDEFINED, self).__init__(ns, pref, tag)



class TRIBRATE1G(TRIBUTARYRATECLASSTYPE):
    """
    1G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_1G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE1G, self).__init__(ns, pref, tag)



class TRIBRATE2DOT5G(TRIBUTARYRATECLASSTYPE):
    """
    2.5G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_2.5G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE2DOT5G, self).__init__(ns, pref, tag)



class TRIBRATE10G(TRIBUTARYRATECLASSTYPE):
    """
    10G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_10G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE10G, self).__init__(ns, pref, tag)



class TRIBRATE40G(TRIBUTARYRATECLASSTYPE):
    """
    40G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_40G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE40G, self).__init__(ns, pref, tag)



class TRIBRATE100G(TRIBUTARYRATECLASSTYPE):
    """
    100G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_100G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE100G, self).__init__(ns, pref, tag)



class TRIBRATE150G(TRIBUTARYRATECLASSTYPE):
    """
    150G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_150G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE150G, self).__init__(ns, pref, tag)



class TRIBRATE200G(TRIBUTARYRATECLASSTYPE):
    """
    200G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_200G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE200G, self).__init__(ns, pref, tag)



class TRIBRATE250G(TRIBUTARYRATECLASSTYPE):
    """
    250G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_250G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE250G, self).__init__(ns, pref, tag)



class TRIBRATE300G(TRIBUTARYRATECLASSTYPE):
    """
    300G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_300G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE300G, self).__init__(ns, pref, tag)



class TRIBRATE400G(TRIBUTARYRATECLASSTYPE):
    """
    400G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_400G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE400G, self).__init__(ns, pref, tag)



class TRIBRATE500G(TRIBUTARYRATECLASSTYPE):
    """
    500G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_500G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE500G, self).__init__(ns, pref, tag)



class TRIBRATE600G(TRIBUTARYRATECLASSTYPE):
    """
    600G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_600G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE600G, self).__init__(ns, pref, tag)



class TRIBRATE700G(TRIBUTARYRATECLASSTYPE):
    """
    700G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_700G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE700G, self).__init__(ns, pref, tag)



class TRIBRATE800G(TRIBUTARYRATECLASSTYPE):
    """
    800G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_800G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE800G, self).__init__(ns, pref, tag)



class TRIBRATE900G(TRIBUTARYRATECLASSTYPE):
    """
    900G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_900G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE900G, self).__init__(ns, pref, tag)



class TRIBRATE1000G(TRIBUTARYRATECLASSTYPE):
    """
    1000G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_1000G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE1000G, self).__init__(ns, pref, tag)



class TRIBRATE1100G(TRIBUTARYRATECLASSTYPE):
    """
    1100G tributary signal rate
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TRIB_RATE_1100G"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRIBRATE1100G, self).__init__(ns, pref, tag)



class PROTETHERNET(LOGICALELEMENTPROTOCOLTYPE):
    """
    Ethernet protocol framing
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_ETHERNET"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTETHERNET, self).__init__(ns, pref, tag)



class PROTOTN(LOGICALELEMENTPROTOCOLTYPE):
    """
    OTN protocol framing
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:PROT_OTN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PROTOTN, self).__init__(ns, pref, tag)



class FIBERJUMPERSIMPLEX(FIBERJUMPERTYPE):
    """
    Simplex fiber jumper
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:FIBER_JUMPER_SIMPLEX"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FIBERJUMPERSIMPLEX, self).__init__(ns, pref, tag)



class FIBERJUMPERMULTIFIBERSTRAND(FIBERJUMPERTYPE):
    """
    One strand of a fiber jumper which contains multiple fibers
    within it, such as an MPO based fiber jumper
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:FIBER_JUMPER_MULTI_FIBER_STRAND"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FIBERJUMPERMULTIFIBERSTRAND, self).__init__(ns, pref, tag)



class INGRESS(OPTICALPORTTYPE):
    """
    Ingress port, corresponding to a signal entering
    a line system device such as an amplifier or wavelength
    router.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:INGRESS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INGRESS, self).__init__(ns, pref, tag)



class EGRESS(OPTICALPORTTYPE):
    """
    Egress port, corresponding to a signal exiting
    a line system device such as an amplifier or wavelength
    router.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:EGRESS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(EGRESS, self).__init__(ns, pref, tag)



class ADD(OPTICALPORTTYPE):
    """
    Add port, corresponding to a signal injected
    at a wavelength router.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:ADD"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ADD, self).__init__(ns, pref, tag)



class DROP(OPTICALPORTTYPE):
    """
    Drop port, corresponding to a signal dropped
    at a wavelength router.
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:DROP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DROP, self).__init__(ns, pref, tag)



class MONITOR(OPTICALPORTTYPE):
    """
    Monitor port, corresponding to a signal used by an optical
    channel monitor. This is used to represent the connection
    that a channel monitor port is connected to, typically on a
    line system device. This  connection may be via physical cable
    and faceplate ports or internal to the device
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:MONITOR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MONITOR, self).__init__(ns, pref, tag)



class TERMINALCLIENT(OPTICALPORTTYPE):
    """
    Client\-facing port on a terminal optics device (e.g.,
    transponder or muxponder).
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TERMINAL_CLIENT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TERMINALCLIENT, self).__init__(ns, pref, tag)



class TERMINALLINE(OPTICALPORTTYPE):
    """
    Line\-facing port on a terminal optics device (e.g.,
    transponder or muxponder).
    
    

    """

    _prefix = 'oc-opt-types'
    _revision = '2019-06-27'

    def __init__(self, ns="http://openconfig.net/yang/transport-types", pref="openconfig-transport-types", tag="openconfig-transport-types:TERMINAL_LINE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TERMINALLINE, self).__init__(ns, pref, tag)



