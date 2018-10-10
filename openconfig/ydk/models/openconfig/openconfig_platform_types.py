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

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:OPENCONFIG_HARDWARE_COMPONENT"):
        super(OPENCONFIGHARDWARECOMPONENT, self).__init__(ns, pref, tag)


class OPENCONFIGSOFTWARECOMPONENT(Identity):
    """
    Base identity for software\-related components in a managed
    device
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:OPENCONFIG_SOFTWARE_COMPONENT"):
        super(OPENCONFIGSOFTWARECOMPONENT, self).__init__(ns, pref, tag)


class OPERATINGSYSTEM(OPENCONFIGSOFTWARECOMPONENT):
    """
    Operating system running on a component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:OPERATING_SYSTEM"):
        super(OPERATINGSYSTEM, self).__init__(ns, pref, tag)


class LINECARD(OPENCONFIGHARDWARECOMPONENT):
    """
    Linecard component, typically inserted into a chassis slot
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:LINECARD"):
        super(LINECARD, self).__init__(ns, pref, tag)


class MODULE(OPENCONFIGHARDWARECOMPONENT):
    """
    Replaceable hardware module, e.g., a daughtercard
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:MODULE"):
        super(MODULE, self).__init__(ns, pref, tag)


class CPU(OPENCONFIGHARDWARECOMPONENT):
    """
    Processing unit, e.g., a management processor
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:CPU"):
        super(CPU, self).__init__(ns, pref, tag)


class TRANSCEIVER(OPENCONFIGHARDWARECOMPONENT):
    """
    Pluggable module present in a port
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:TRANSCEIVER"):
        super(TRANSCEIVER, self).__init__(ns, pref, tag)


class CHASSIS(OPENCONFIGHARDWARECOMPONENT):
    """
    Chassis component, typically with multiple slots / shelves
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:CHASSIS"):
        super(CHASSIS, self).__init__(ns, pref, tag)


class FAN(OPENCONFIGHARDWARECOMPONENT):
    """
    Cooling fan, or could be some other heat\-reduction component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:FAN"):
        super(FAN, self).__init__(ns, pref, tag)


class BACKPLANE(OPENCONFIGHARDWARECOMPONENT):
    """
    Backplane component for aggregating traffic, typically
    contained in a chassis component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:BACKPLANE"):
        super(BACKPLANE, self).__init__(ns, pref, tag)


class SENSOR(OPENCONFIGHARDWARECOMPONENT):
    """
    Physical sensor, e.g., a temperature sensor in a chassis
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:SENSOR"):
        super(SENSOR, self).__init__(ns, pref, tag)


class PORT(OPENCONFIGHARDWARECOMPONENT):
    """
    Physical port, e.g., for attaching pluggables and networking
    cables
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:PORT"):
        super(PORT, self).__init__(ns, pref, tag)


class POWERSUPPLY(OPENCONFIGHARDWARECOMPONENT):
    """
    Component that is supplying power to the device
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:POWER_SUPPLY"):
        super(POWERSUPPLY, self).__init__(ns, pref, tag)


