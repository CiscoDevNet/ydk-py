""" openconfig_lldp_types 

This module defines types related to the LLDP protocol model.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:LLDP_SYSTEM_CAPABILITY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LLDPSYSTEMCAPABILITY, self).__init__(ns, pref, tag)



class LLDPTLV(Identity):
    """
    A base identity which describes the TLVs in LLDP
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:LLDP_TLV"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LLDPTLV, self).__init__(ns, pref, tag)



class OTHER(LLDPSYSTEMCAPABILITY):
    """
    Other capability not specified; bit position 1
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:OTHER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OTHER, self).__init__(ns, pref, tag)



class REPEATER(LLDPSYSTEMCAPABILITY):
    """
    Repeater capability; bit position 2
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:REPEATER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(REPEATER, self).__init__(ns, pref, tag)



class MACBRIDGE(LLDPSYSTEMCAPABILITY):
    """
    MAC bridge capability; bit position 3
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:MAC_BRIDGE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MACBRIDGE, self).__init__(ns, pref, tag)



class WLANACCESSPOINT(LLDPSYSTEMCAPABILITY):
    """
    WLAN access point capability; bit position 4
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:WLAN_ACCESS_POINT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(WLANACCESSPOINT, self).__init__(ns, pref, tag)



class ROUTER(LLDPSYSTEMCAPABILITY):
    """
    Router; bit position 5
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:ROUTER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ROUTER, self).__init__(ns, pref, tag)



class TELEPHONE(LLDPSYSTEMCAPABILITY):
    """
    Telephone capability; bit position 6
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:TELEPHONE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TELEPHONE, self).__init__(ns, pref, tag)



class DOCSISCABLEDEVICE(LLDPSYSTEMCAPABILITY):
    """
    DOCSIS cable device; bit position 7
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:DOCSIS_CABLE_DEVICE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DOCSISCABLEDEVICE, self).__init__(ns, pref, tag)



class STATIONONLY(LLDPSYSTEMCAPABILITY):
    """
    Station only capability, for devices that implement only an
    end station capability, and for which none of the other
    capabilities apply; bit position 8
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:STATION_ONLY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(STATIONONLY, self).__init__(ns, pref, tag)



class CVLAN(LLDPSYSTEMCAPABILITY):
    """
    C\-VLAN component of a VLAN Bridge; bit position 9
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:C_VLAN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CVLAN, self).__init__(ns, pref, tag)



class SVLAN(LLDPSYSTEMCAPABILITY):
    """
    S\-VLAN component of a VLAN Bridge; bit position 10
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:S_VLAN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SVLAN, self).__init__(ns, pref, tag)



class TWOPORTMACRELAY(LLDPSYSTEMCAPABILITY):
    """
    Two\-port MAC Relay (TPMR) capability; bit position 11
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:TWO_PORT_MAC_RELAY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TWOPORTMACRELAY, self).__init__(ns, pref, tag)



class CHASSISID(LLDPTLV):
    """
    The chassis identifier of the device associated with
    the transmitting LLDP agent
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:CHASSIS_ID"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CHASSISID, self).__init__(ns, pref, tag)



class PORTID(LLDPTLV):
    """
    The port identifier associated with the interface
    on with the LLDP agent is transmitting
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:PORT_ID"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PORTID, self).__init__(ns, pref, tag)



class PORTDESCRIPTION(LLDPTLV):
    """
    The description of the port that is associated with
    the interface on which the LLDP agent is transmitting
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:PORT_DESCRIPTION"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PORTDESCRIPTION, self).__init__(ns, pref, tag)



class SYSTEMNAME(LLDPTLV):
    """
    The assigned name (sysName or hostname) of the device
    which is transmitting the LLDP PDU
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:SYSTEM_NAME"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SYSTEMNAME, self).__init__(ns, pref, tag)



class SYSTEMDESCRIPTION(LLDPTLV):
    """
    The description (sysDescr) of the device which is
    transmitting the LLDP PDU
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:SYSTEM_DESCRIPTION"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SYSTEMDESCRIPTION, self).__init__(ns, pref, tag)



class SYSTEMCAPABILITIES(LLDPTLV):
    """
    The primary functions of the device transmitting the
    LLDP PDU and their administrative status
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:SYSTEM_CAPABILITIES"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SYSTEMCAPABILITIES, self).__init__(ns, pref, tag)



class MANAGEMENTADDRESS(LLDPTLV):
    """
    The address associated with the device transmitting the
    LLDP PDU which can be used for higher\-layer network
    management
    
    

    """

    _prefix = 'oc-lldp-types'
    _revision = '2016-05-16'

    def __init__(self, ns="http://openconfig.net/yang/lldp/types", pref="openconfig-lldp-types", tag="openconfig-lldp-types:MANAGEMENT_ADDRESS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MANAGEMENTADDRESS, self).__init__(ns, pref, tag)



