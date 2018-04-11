""" openconfig_platform_types 

This module defines data types (e.g., YANG identities)
to support the OpenConfig component inventory model.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class OPENCONFIGHARDWARECOMPONENT(Identity):
    """
    Base identity for hardware related components in a managed
    device.  Derived identities are partially based on contents
    of the IANA Entity MIB.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(OPENCONFIGHARDWARECOMPONENT, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:OPENCONFIG_HARDWARE_COMPONENT")


class OPENCONFIGSOFTWARECOMPONENT(Identity):
    """
    Base identity for software\-related components in a managed
    device
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(OPENCONFIGSOFTWARECOMPONENT, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:OPENCONFIG_SOFTWARE_COMPONENT")


class CHASSIS(Identity):
    """
    Chassis component, typically with multiple slots / shelves
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(CHASSIS, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:CHASSIS")


class BACKPLANE(Identity):
    """
    Backplane component for aggregating traffic, typically
    contained in a chassis component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(BACKPLANE, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:BACKPLANE")


class POWERSUPPLY(Identity):
    """
    Component that is supplying power to the device
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(POWERSUPPLY, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:POWER_SUPPLY")


class FAN(Identity):
    """
    Cooling fan, or could be some other heat\-reduction component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(FAN, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:FAN")


class SENSOR(Identity):
    """
    Physical sensor, e.g., a temperature sensor in a chassis
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(SENSOR, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:SENSOR")


class MODULE(Identity):
    """
    Replaceable hardware module, e.g., a daughtercard
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(MODULE, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:MODULE")


class LINECARD(Identity):
    """
    Linecard component, typically inserted into a chassis slot
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(LINECARD, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:LINECARD")


class PORT(Identity):
    """
    Physical port, e.g., for attaching pluggables and networking
    cables
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(PORT, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:PORT")


class TRANSCEIVER(Identity):
    """
    Pluggable module present in a port
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(TRANSCEIVER, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:TRANSCEIVER")


class CPU(Identity):
    """
    Processing unit, e.g., a management processor
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(CPU, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:CPU")


class OPERATINGSYSTEM(Identity):
    """
    Operating system running on a component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        super(OPERATINGSYSTEM, self).__init__("http://openconfig.net/yang/platform-types", "openconfig-platform-types", "openconfig-platform-types:OPERATING_SYSTEM")


