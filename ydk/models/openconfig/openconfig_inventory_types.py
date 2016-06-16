""" openconfig_inventory_types 

This module defines data types (e.g., YANG identities)
to support the OpenConfig component inventory model.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class OpenconfigSoftwareComponentIdentity(object):
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
        return meta._meta_table['OpenconfigSoftwareComponentIdentity']['meta_info']


class OpenconfigHardwareComponentIdentity(object):
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
        return meta._meta_table['OpenconfigHardwareComponentIdentity']['meta_info']


class TransceiverIdentity(OpenconfigHardwareComponentIdentity):
    """
    Pluggable module present in a port
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['TransceiverIdentity']['meta_info']


class LinecardIdentity(OpenconfigHardwareComponentIdentity):
    """
    Linecard component, typically inserted into a chassis slot
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['LinecardIdentity']['meta_info']


class PowerSupplyIdentity(OpenconfigHardwareComponentIdentity):
    """
    Component that is supplying power to the device
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['PowerSupplyIdentity']['meta_info']


class CpuIdentity(OpenconfigHardwareComponentIdentity):
    """
    Processing unit, e.g., a management processor
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['CpuIdentity']['meta_info']


class ModuleIdentity(OpenconfigHardwareComponentIdentity):
    """
    Replaceable hardware module, e.g., a daughtercard
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['ModuleIdentity']['meta_info']


class BackplaneIdentity(OpenconfigHardwareComponentIdentity):
    """
    Backplane component for aggregating traffic, typically
    contained in a chassis component
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['BackplaneIdentity']['meta_info']


class ChassisIdentity(OpenconfigHardwareComponentIdentity):
    """
    Chassis component, typically with multiple slots / shelves
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['ChassisIdentity']['meta_info']


class FanIdentity(OpenconfigHardwareComponentIdentity):
    """
    Cooling fan, or could be some other heat\-reduction component
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['FanIdentity']['meta_info']


class OperatingSystemIdentity(OpenconfigSoftwareComponentIdentity):
    """
    Operating system running on a component
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigSoftwareComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['OperatingSystemIdentity']['meta_info']


class SensorIdentity(OpenconfigHardwareComponentIdentity):
    """
    Physical sensor, e.g., a temperature sensor in a chassis
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['SensorIdentity']['meta_info']


class PortIdentity(OpenconfigHardwareComponentIdentity):
    """
    Physical port, e.g., for attaching pluggables and networking
    cables
    
    

    """

    _prefix = 'oc-inv-types'
    _revision = '2015-12-18'

    def __init__(self):
        OpenconfigHardwareComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory_types as meta
        return meta._meta_table['PortIdentity']['meta_info']


