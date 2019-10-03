""" openconfig_platform_types 

This module defines data types (e.g., YANG identities)
to support the OpenConfig component inventory model.

"""
import sys
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
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OPENCONFIGHARDWARECOMPONENT, self).__init__(ns, pref, tag)



class OPENCONFIGSOFTWARECOMPONENT(Identity):
    """
    Base identity for software\-related components in a managed
    device
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:OPENCONFIG_SOFTWARE_COMPONENT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OPENCONFIGSOFTWARECOMPONENT, self).__init__(ns, pref, tag)



class OPERATINGSYSTEM(OPENCONFIGSOFTWARECOMPONENT):
    """
    Operating system running on a component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:OPERATING_SYSTEM"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OPERATINGSYSTEM, self).__init__(ns, pref, tag)



class LINECARD(OPENCONFIGHARDWARECOMPONENT):
    """
    Linecard component, typically inserted into a chassis slot
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:LINECARD"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LINECARD, self).__init__(ns, pref, tag)



class MODULE(OPENCONFIGHARDWARECOMPONENT):
    """
    Replaceable hardware module, e.g., a daughtercard
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:MODULE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MODULE, self).__init__(ns, pref, tag)



class CPU(OPENCONFIGHARDWARECOMPONENT):
    """
    Processing unit, e.g., a management processor
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:CPU"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CPU, self).__init__(ns, pref, tag)



class TRANSCEIVER(OPENCONFIGHARDWARECOMPONENT):
    """
    Pluggable module present in a port
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:TRANSCEIVER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRANSCEIVER, self).__init__(ns, pref, tag)



class CHASSIS(OPENCONFIGHARDWARECOMPONENT):
    """
    Chassis component, typically with multiple slots / shelves
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:CHASSIS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CHASSIS, self).__init__(ns, pref, tag)



class FAN(OPENCONFIGHARDWARECOMPONENT):
    """
    Cooling fan, or could be some other heat\-reduction component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:FAN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FAN, self).__init__(ns, pref, tag)



class BACKPLANE(OPENCONFIGHARDWARECOMPONENT):
    """
    Backplane component for aggregating traffic, typically
    contained in a chassis component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:BACKPLANE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(BACKPLANE, self).__init__(ns, pref, tag)



class SENSOR(OPENCONFIGHARDWARECOMPONENT):
    """
    Physical sensor, e.g., a temperature sensor in a chassis
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:SENSOR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SENSOR, self).__init__(ns, pref, tag)



class PORT(OPENCONFIGHARDWARECOMPONENT):
    """
    Physical port, e.g., for attaching pluggables and networking
    cables
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:PORT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PORT, self).__init__(ns, pref, tag)



class POWERSUPPLY(OPENCONFIGHARDWARECOMPONENT):
    """
    Component that is supplying power to the device
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:POWER_SUPPLY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(POWERSUPPLY, self).__init__(ns, pref, tag)



