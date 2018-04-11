""" openconfig_lldp_types 

This module defines types related to the LLDP protocol model.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ChassisIdType(Enum):
    """
    ChassisIdType (Enum Class)

    Type definition with enumerations describing the source of

    the chassis identifier

    .. data:: CHASSIS_COMPONENT = 0

    	Chassis identifier based on the value of entPhysicalAlias

    	object defined in IETF RFC 2737

    .. data:: INTERFACE_ALIAS = 1

    	Chassis identifier based on the value of ifAlias object

    	defined in IETF RFC 2863

    .. data:: PORT_COMPONENT = 2

    	Chassis identifier based on the value of entPhysicalAlias

    	object defined in IETF RFC 2737 for a port or backplane

    	component

    .. data:: MAC_ADDRESS = 3

    	Chassis identifier based on the value of a unicast source

    	address (encoded in network byte order and IEEE 802.3

    	canonical bit order), of a port on the containing chassis

    	as defined in IEEE Std 802-2001

    .. data:: NETWORK_ADDRESS = 4

    	Chassis identifier based on a network address,

    	associated with a particular chassis.  The encoded address

    	is composed of two fields.  The first field is a single

    	octet, representing the IANA AddressFamilyNumbers value

    	for the specific address type, and the second field is the

    	network address value

    .. data:: INTERFACE_NAME = 5

    	Chassis identifier based on the name of the interface,

    	e.g., the value of ifName object defined in IETF RFC 2863

    .. data:: LOCAL = 6

    	Chassis identifier based on a locally defined value

    """

    CHASSIS_COMPONENT = Enum.YLeaf(0, "CHASSIS_COMPONENT")

    INTERFACE_ALIAS = Enum.YLeaf(1, "INTERFACE_ALIAS")

    PORT_COMPONENT = Enum.YLeaf(2, "PORT_COMPONENT")

    MAC_ADDRESS = Enum.YLeaf(3, "MAC_ADDRESS")

    NETWORK_ADDRESS = Enum.YLeaf(4, "NETWORK_ADDRESS")

    INTERFACE_NAME = Enum.YLeaf(5, "INTERFACE_NAME")

    LOCAL = Enum.YLeaf(6, "LOCAL")


class PortIdType(Enum):
    """
    PortIdType (Enum Class)

    Type definition with enumerations describing the basis of

    the port identifier

    .. data:: INTERFACE_ALIAS = 0

    	Chassis identifier based on the value of ifAlias object

    	defined in IETF RFC 2863

    .. data:: PORT_COMPONENT = 1

    	Port identifier based on the value of entPhysicalAlias

    	object defined in IETF RFC 2737 for a port component

    .. data:: MAC_ADDRESS = 2

    	Port identifier based on the value of a unicast source

    	address (encoded in network byte order and IEEE 802.3

    	canonical bit order) associated with a port

    .. data:: NETWORK_ADDRESS = 3

    	Port identifier based on a network address,

    	associated with a particular port

    .. data:: INTERFACE_NAME = 4

    	Port identifier based on the name of the interface,

    	e.g., the value of ifName object defined in IETF RFC 2863

    .. data:: AGENT_CIRCUIT_ID = 5

    	Port identifer based on the circuit id in the DHCP

    	relay agent information option as defined in IETF

    	RFC 3046

    .. data:: LOCAL = 6

    	Port identifier based on a locally defined alphanumeric

    	string

    """

    INTERFACE_ALIAS = Enum.YLeaf(0, "INTERFACE_ALIAS")

    PORT_COMPONENT = Enum.YLeaf(1, "PORT_COMPONENT")

    MAC_ADDRESS = Enum.YLeaf(2, "MAC_ADDRESS")

    NETWORK_ADDRESS = Enum.YLeaf(3, "NETWORK_ADDRESS")

    INTERFACE_NAME = Enum.YLeaf(4, "INTERFACE_NAME")

    AGENT_CIRCUIT_ID = Enum.YLeaf(5, "AGENT_CIRCUIT_ID")

    LOCAL = Enum.YLeaf(6, "LOCAL")



class LLDPSYSTEMCAPABILITY(Identity):
    """
    Base identity for standard LLDP system capabilities.
    The system capabilities field contains a bit\-map of the
    capabilities that define the primary function(s) of
    the system. A system may advertise more than one capability.
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(LLDPSYSTEMCAPABILITY, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:LLDP_SYSTEM_CAPABILITY")


class LLDPTLV(Identity):
    """
    A base identity which describes the TLVs in LLDP
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(LLDPTLV, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:LLDP_TLV")


class OTHER(Identity):
    """
    Other capability not specified; bit position 1
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(OTHER, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:OTHER")


class REPEATER(Identity):
    """
    Repeater capability; bit position 2
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(REPEATER, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:REPEATER")


class MACBRIDGE(Identity):
    """
    MAC bridge capability; bit position 3
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(MACBRIDGE, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:MAC_BRIDGE")


class WLANACCESSPOINT(Identity):
    """
    WLAN access point capability; bit position 4
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(WLANACCESSPOINT, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:WLAN_ACCESS_POINT")


class ROUTER(Identity):
    """
    Router; bit position 5
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(ROUTER, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:ROUTER")


class TELEPHONE(Identity):
    """
    Telephone capability; bit position 6
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(TELEPHONE, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:TELEPHONE")


class DOCSISCABLEDEVICE(Identity):
    """
    DOCSIS cable device; bit position 7
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(DOCSISCABLEDEVICE, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:DOCSIS_CABLE_DEVICE")


class STATIONONLY(Identity):
    """
    Station only capability, for devices that implement only an
    end station capability, and for which none of the other
    capabilities apply; bit position 8
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(STATIONONLY, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:STATION_ONLY")


class CVLAN(Identity):
    """
    C\-VLAN component of a VLAN Bridge; bit position 9
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(CVLAN, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:C_VLAN")


class SVLAN(Identity):
    """
    S\-VLAN component of a VLAN Bridge; bit position 10
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(SVLAN, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:S_VLAN")


class TWOPORTMACRELAY(Identity):
    """
    Two\-port MAC Relay (TPMR) capability; bit position 11
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(TWOPORTMACRELAY, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:TWO_PORT_MAC_RELAY")


class CHASSISID(Identity):
    """
    The chassis identifier of the device associated with
    the transmitting LLDP agent
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(CHASSISID, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:CHASSIS_ID")


class PORTID(Identity):
    """
    The port identifier associated with the interface
    on with the LLDP agent is transmitting
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(PORTID, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:PORT_ID")


class PORTDESCRIPTION(Identity):
    """
    The description of the port that is associated with
    the interface on which the LLDP agent is transmitting
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(PORTDESCRIPTION, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:PORT_DESCRIPTION")


class SYSTEMNAME(Identity):
    """
    The assigned name (sysName or hostname) of the device
    which is transmitting the LLDP PDU
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(SYSTEMNAME, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:SYSTEM_NAME")


class SYSTEMDESCRIPTION(Identity):
    """
    The description (sysDescr) of the device which is
    transmitting the LLDP PDU
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(SYSTEMDESCRIPTION, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:SYSTEM_DESCRIPTION")


class SYSTEMCAPABILITIES(Identity):
    """
    The primary functions of the device transmitting the
    LLDP PDU and their administrative status
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(SYSTEMCAPABILITIES, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:SYSTEM_CAPABILITIES")


class MANAGEMENTADDRESS(Identity):
    """
    The address associated with the device transmitting the
    LLDP PDU which can be used for higher\-layer network
    management
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self):
        super(MANAGEMENTADDRESS, self).__init__("http://openconfig.net/yang/lldp/types", "openconfig-lldp-types", "openconfig-lldp-types:MANAGEMENT_ADDRESS")


