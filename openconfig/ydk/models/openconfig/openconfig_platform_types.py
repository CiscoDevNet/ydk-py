""" openconfig_platform_types 

This module defines data types (e.g., YANG identities)
to support the OpenConfig component inventory model.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ComponentPowerType(Enum):
    """
    ComponentPowerType (Enum Class)

    A generic type reflecting whether a hardware component

    is powered on or off

    .. data:: POWER_ENABLED = 0

    	Enable power on the component

    .. data:: POWER_DISABLED = 1

    	Disable power on the component

    """

    POWER_ENABLED = Enum.YLeaf(0, "POWER_ENABLED")

    POWER_DISABLED = Enum.YLeaf(1, "POWER_DISABLED")



class OPENCONFIGHARDWARECOMPONENT(Identity):
    """
    Base identity for hardware related components in a managed
    device.  Derived identities are partially based on contents
    of the IANA Entity MIB.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

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
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:OPENCONFIG_SOFTWARE_COMPONENT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OPENCONFIGSOFTWARECOMPONENT, self).__init__(ns, pref, tag)



class COMPONENTOPERSTATUS(Identity):
    """
    Current operational status of a platform component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:COMPONENT_OPER_STATUS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(COMPONENTOPERSTATUS, self).__init__(ns, pref, tag)



class FECMODETYPE(Identity):
    """
    Base identity for FEC operational modes.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:FEC_MODE_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FECMODETYPE, self).__init__(ns, pref, tag)



class FECSTATUSTYPE(Identity):
    """
    Base identity for FEC operational statuses.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:FEC_STATUS_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FECSTATUSTYPE, self).__init__(ns, pref, tag)



class CHASSIS(OPENCONFIGHARDWARECOMPONENT):
    """
    Chassis component, typically with multiple slots / shelves
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:CHASSIS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CHASSIS, self).__init__(ns, pref, tag)



class BACKPLANE(OPENCONFIGHARDWARECOMPONENT):
    """
    Backplane component for aggregating traffic, typically
    contained in a chassis component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:BACKPLANE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(BACKPLANE, self).__init__(ns, pref, tag)



class FABRIC(OPENCONFIGHARDWARECOMPONENT):
    """
    Interconnect between ingress and egress ports on the
    device (e.g., a crossbar switch).
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:FABRIC"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FABRIC, self).__init__(ns, pref, tag)



class POWERSUPPLY(OPENCONFIGHARDWARECOMPONENT):
    """
    Component that is supplying power to the device
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:POWER_SUPPLY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(POWERSUPPLY, self).__init__(ns, pref, tag)



class FAN(OPENCONFIGHARDWARECOMPONENT):
    """
    Cooling fan, or could be some other heat\-reduction component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:FAN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FAN, self).__init__(ns, pref, tag)



class SENSOR(OPENCONFIGHARDWARECOMPONENT):
    """
    Physical sensor, e.g., a temperature sensor in a chassis
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:SENSOR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SENSOR, self).__init__(ns, pref, tag)



class FRU(OPENCONFIGHARDWARECOMPONENT):
    """
    Replaceable hardware component that does not have a more
    specific defined schema.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:FRU"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FRU, self).__init__(ns, pref, tag)



class LINECARD(OPENCONFIGHARDWARECOMPONENT):
    """
    Linecard component, typically inserted into a chassis slot
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:LINECARD"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LINECARD, self).__init__(ns, pref, tag)



class CONTROLLERCARD(OPENCONFIGHARDWARECOMPONENT):
    """
    A type of linecard whose primary role is management or control
    rather than data forwarding.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:CONTROLLER_CARD"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CONTROLLERCARD, self).__init__(ns, pref, tag)



class PORT(OPENCONFIGHARDWARECOMPONENT):
    """
    Physical port, e.g., for attaching pluggables and networking
    cables
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:PORT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PORT, self).__init__(ns, pref, tag)



class TRANSCEIVER(OPENCONFIGHARDWARECOMPONENT):
    """
    Pluggable module present in a port
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:TRANSCEIVER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TRANSCEIVER, self).__init__(ns, pref, tag)



class CPU(OPENCONFIGHARDWARECOMPONENT):
    """
    Processing unit, e.g., a management processor
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:CPU"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CPU, self).__init__(ns, pref, tag)



class STORAGE(OPENCONFIGHARDWARECOMPONENT):
    """
    A storage subsystem on the device (disk, SSD, etc.)
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:STORAGE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(STORAGE, self).__init__(ns, pref, tag)



class INTEGRATEDCIRCUIT(OPENCONFIGHARDWARECOMPONENT):
    """
    A special purpose processing unit, typically for traffic
    switching/forwarding (e.g., switching ASIC, NPU, forwarding
    chip, etc.)
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:INTEGRATED_CIRCUIT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INTEGRATEDCIRCUIT, self).__init__(ns, pref, tag)



class OPERATINGSYSTEM(OPENCONFIGSOFTWARECOMPONENT):
    """
    Operating system running on a component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:OPERATING_SYSTEM"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OPERATINGSYSTEM, self).__init__(ns, pref, tag)



class ACTIVE(COMPONENTOPERSTATUS):
    """
    Component is enabled and active (i.e., up)
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:ACTIVE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ACTIVE, self).__init__(ns, pref, tag)



class INACTIVE(COMPONENTOPERSTATUS):
    """
    Component is enabled but inactive (i.e., down)
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:INACTIVE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INACTIVE, self).__init__(ns, pref, tag)



class DISABLED(COMPONENTOPERSTATUS):
    """
    Component is administratively disabled.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:DISABLED"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DISABLED, self).__init__(ns, pref, tag)



class FECENABLED(FECMODETYPE):
    """
    FEC is administratively enabled.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:FEC_ENABLED"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FECENABLED, self).__init__(ns, pref, tag)



class FECDISABLED(FECMODETYPE):
    """
    FEC is administratively disabled.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:FEC_DISABLED"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FECDISABLED, self).__init__(ns, pref, tag)



class FECAUTO(FECMODETYPE):
    """
    System will determine whether to enable or disable
    FEC on a transceiver.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:FEC_AUTO"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FECAUTO, self).__init__(ns, pref, tag)



class FECSTATUSLOCKED(FECSTATUSTYPE):
    """
    FEC is operationally locked.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:FEC_STATUS_LOCKED"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FECSTATUSLOCKED, self).__init__(ns, pref, tag)



class FECSTATUSUNLOCKED(FECSTATUSTYPE):
    """
    FEC is operationally unlocked.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/platform-types", pref="openconfig-platform-types", tag="openconfig-platform-types:FEC_STATUS_UNLOCKED"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FECSTATUSUNLOCKED, self).__init__(ns, pref, tag)



