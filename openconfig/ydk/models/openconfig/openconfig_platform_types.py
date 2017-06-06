""" openconfig_platform_types 

This module defines data types (e.g., YANG identities)
to support the OpenConfig component inventory model.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Openconfig_Hardware_ComponentIdentity(object):
    """
    Base identity for hardware related components in a managed
    device.  Derived identities are partially based on contents
    of the IANA Entity MIB.
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['Openconfig_Hardware_ComponentIdentity']['meta_info']


class Openconfig_Software_ComponentIdentity(object):
    """
    Base identity for software\-related components in a managed
    device
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['Openconfig_Software_ComponentIdentity']['meta_info']


class CpuIdentity(Openconfig_Hardware_ComponentIdentity):
    """
    Processing unit, e.g., a management processor
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        Openconfig_Hardware_ComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['CpuIdentity']['meta_info']


class SensorIdentity(Openconfig_Hardware_ComponentIdentity):
    """
    Physical sensor, e.g., a temperature sensor in a chassis
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        Openconfig_Hardware_ComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['SensorIdentity']['meta_info']


class ModuleIdentity(Openconfig_Hardware_ComponentIdentity):
    """
    Replaceable hardware module, e.g., a daughtercard
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        Openconfig_Hardware_ComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['ModuleIdentity']['meta_info']


class TransceiverIdentity(Openconfig_Hardware_ComponentIdentity):
    """
    Pluggable module present in a port
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        Openconfig_Hardware_ComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['TransceiverIdentity']['meta_info']


class FanIdentity(Openconfig_Hardware_ComponentIdentity):
    """
    Cooling fan, or could be some other heat\-reduction component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        Openconfig_Hardware_ComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['FanIdentity']['meta_info']


class Operating_SystemIdentity(Openconfig_Software_ComponentIdentity):
    """
    Operating system running on a component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        Openconfig_Software_ComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['Operating_SystemIdentity']['meta_info']


class Power_SupplyIdentity(Openconfig_Hardware_ComponentIdentity):
    """
    Component that is supplying power to the device
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        Openconfig_Hardware_ComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['Power_SupplyIdentity']['meta_info']


class BackplaneIdentity(Openconfig_Hardware_ComponentIdentity):
    """
    Backplane component for aggregating traffic, typically
    contained in a chassis component
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        Openconfig_Hardware_ComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['BackplaneIdentity']['meta_info']


class LinecardIdentity(Openconfig_Hardware_ComponentIdentity):
    """
    Linecard component, typically inserted into a chassis slot
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        Openconfig_Hardware_ComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['LinecardIdentity']['meta_info']


class ChassisIdentity(Openconfig_Hardware_ComponentIdentity):
    """
    Chassis component, typically with multiple slots / shelves
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        Openconfig_Hardware_ComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['ChassisIdentity']['meta_info']


class PortIdentity(Openconfig_Hardware_ComponentIdentity):
    """
    Physical port, e.g., for attaching pluggables and networking
    cables
    
    

    """

    _prefix = 'oc-platform-types'
    _revision = '2016-06-06'

    def __init__(self):
        Openconfig_Hardware_ComponentIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform_types as meta
        return meta._meta_table['PortIdentity']['meta_info']


