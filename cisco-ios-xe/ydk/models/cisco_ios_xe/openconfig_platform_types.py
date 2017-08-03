""" openconfig_platform_types 

This module defines data types (e.g., YANG identities)
to support the OpenConfig component inventory model.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Openconfig_Software_Component(Identity):
    """
    Base identity for software\-related components in a managed
    device
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Openconfig_Software_Component, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:OPENCONFIG_SOFTWARE_COMPONENT")


class Openconfig_Hardware_Component(Identity):
    """
    Base identity for hardware related components in a managed
    device.  Derived identities are partially based on contents
    of the IANA Entity MIB.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Openconfig_Hardware_Component, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:OPENCONFIG_HARDWARE_COMPONENT")


class Linecard(Identity):
    """
    Linecard component, typically inserted into a chassis slot
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Linecard, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:LINECARD")


class Port(Identity):
    """
    Physical port, e.g., for attaching pluggables and networking
    cables
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Port, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:PORT")


class Backplane(Identity):
    """
    Backplane component for aggregating traffic, typically
    contained in a chassis component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Backplane, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:BACKPLANE")


class Chassis(Identity):
    """
    Chassis component, typically with multiple slots / shelves
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Chassis, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:CHASSIS")


class Operating_System(Identity):
    """
    Operating system running on a component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Operating_System, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:OPERATING_SYSTEM")


class Transceiver(Identity):
    """
    Pluggable module present in a port
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Transceiver, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:TRANSCEIVER")


class Module(Identity):
    """
    Replaceable hardware module, e.g., a daughtercard
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Module, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:MODULE")


class Fan(Identity):
    """
    Cooling fan, or could be some other heat\-reduction component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Fan, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:FAN")


class Power_Supply(Identity):
    """
    Component that is supplying power to the device
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Power_Supply, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:POWER_SUPPLY")


class Sensor(Identity):
    """
    Physical sensor, e.g., a temperature sensor in a chassis
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Sensor, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:SENSOR")


class Cpu(Identity):
    """
    Processing unit, e.g., a management processor
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(Cpu, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:CPU")


