""" openconfig_inventory_types 

This module defines data types (e.g., YANG identities)
to support the OpenConfig component inventory model.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class OpenconfigHardwareComponent_Identity(object):
    """
    Base identity for hardware related components in a managed
    device.  Derived identities are partially based on contents
    of the IANA Entity MIB.
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['OpenconfigHardwareComponent_Identity']['meta_info']


class OpenconfigSoftwareComponent_Identity(object):
    """
    Base identity for software\-related components in a managed
    device
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['OpenconfigSoftwareComponent_Identity']['meta_info']


class BACKPLANE_Identity(OpenconfigHardwareComponent_Identity):
    """
    Backplane component for aggregating traffic, typically
    contained in a chassis component
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponent_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['BACKPLANE_Identity']['meta_info']


class CHASSIS_Identity(OpenconfigHardwareComponent_Identity):
    """
    Chassis component, typically with multiple slots / shelves
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponent_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['CHASSIS_Identity']['meta_info']


class CPU_Identity(OpenconfigHardwareComponent_Identity):
    """
    Processing unit, e.g., a management processor
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponent_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['CPU_Identity']['meta_info']


class FAN_Identity(OpenconfigHardwareComponent_Identity):
    """
    Cooling fan, or could be some other heat\-reduction component
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponent_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['FAN_Identity']['meta_info']


class LINECARD_Identity(OpenconfigHardwareComponent_Identity):
    """
    Linecard component, typically inserted into a chassis slot
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponent_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['LINECARD_Identity']['meta_info']


class MODULE_Identity(OpenconfigHardwareComponent_Identity):
    """
    Replaceable hardware module, e.g., a daughtercard
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponent_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['MODULE_Identity']['meta_info']


class OPERATINGSYSTEM_Identity(OpenconfigSoftwareComponent_Identity):
    """
    Operating system running on a component
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigSoftwareComponent_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['OPERATINGSYSTEM_Identity']['meta_info']


class PORT_Identity(OpenconfigHardwareComponent_Identity):
    """
    Physical port, e.g., for attaching pluggables and networking
    cables
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponent_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['PORT_Identity']['meta_info']


class POWERSUPPLY_Identity(OpenconfigHardwareComponent_Identity):
    """
    Component that is supplying power to the device
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponent_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['POWERSUPPLY_Identity']['meta_info']


class SENSOR_Identity(OpenconfigHardwareComponent_Identity):
    """
    Physical sensor, e.g., a temperature sensor in a chassis
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponent_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['SENSOR_Identity']['meta_info']


class TRANSCEIVER_Identity(OpenconfigHardwareComponent_Identity):
    """
    Pluggable module present in a port
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponent_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['TRANSCEIVER_Identity']['meta_info']


