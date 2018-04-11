""" openconfig_isis_types 

This module contains general data definitions for use in ISIS YANG
model.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AdaptiveTimerType(Enum):
    """
    AdaptiveTimerType (Enum Class)

    This type defines ISIS adaptive timer types

    .. data:: LINEAR = 0

    	This enum describes linear algorithm timer

    .. data:: EXPONENTIAL = 1

    	This enum describes exponential algorithm timer

    """

    LINEAR = Enum.YLeaf(0, "LINEAR")

    EXPONENTIAL = Enum.YLeaf(1, "EXPONENTIAL")


class CircuitType(Enum):
    """
    CircuitType (Enum Class)

    This type defines ISIS interface types 

    .. data:: POINT_TO_POINT = 0

    	This enum describes a point-to-point interface

    .. data:: BROADCAST = 1

    	This enum describes a broadcast interface

    """

    POINT_TO_POINT = Enum.YLeaf(0, "POINT_TO_POINT")

    BROADCAST = Enum.YLeaf(1, "BROADCAST")


class HelloPaddingType(Enum):
    """
    HelloPaddingType (Enum Class)

    This type defines ISIS hello padding type

    .. data:: STRICT = 0

    	This enum describes strict padding

    .. data:: LOOSE = 1

    	This enum describes loose padding

    .. data:: ADAPTIVE = 2

    	This enum describes adaptive padding

    .. data:: DISABLE = 3

    	This enum disables padding

    """

    STRICT = Enum.YLeaf(0, "STRICT")

    LOOSE = Enum.YLeaf(1, "LOOSE")

    ADAPTIVE = Enum.YLeaf(2, "ADAPTIVE")

    DISABLE = Enum.YLeaf(3, "DISABLE")


class IsisInterfaceAdjState(Enum):
    """
    IsisInterfaceAdjState (Enum Class)

    This type defines the state of the interface.

    .. data:: UP = 0

    	This state describes that adjacency is established.

    .. data:: DOWN = 1

    	This state describes that adjacency is NOT established.

    .. data:: INIT = 2

    	This state describes that adjacency is establishing.

    .. data:: FAILED = 3

    	This state describes that adjacency is failed.

    """

    UP = Enum.YLeaf(0, "UP")

    DOWN = Enum.YLeaf(1, "DOWN")

    INIT = Enum.YLeaf(2, "INIT")

    FAILED = Enum.YLeaf(3, "FAILED")


class LevelType(Enum):
    """
    LevelType (Enum Class)

    This type defines ISIS level types

    .. data:: LEVEL_1 = 0

    	This enum describes ISIS level 1

    .. data:: LEVEL_2 = 1

    	This enum describes ISIS level 2

    .. data:: LEVEL_1_2 = 2

    	This enum describes ISIS level 1-2

    """

    LEVEL_1 = Enum.YLeaf(0, "LEVEL_1")

    LEVEL_2 = Enum.YLeaf(1, "LEVEL_2")

    LEVEL_1_2 = Enum.YLeaf(2, "LEVEL_1_2")


class MetricStyle(Enum):
    """
    MetricStyle (Enum Class)

    This type defines ISIS metric styles

    .. data:: NARROW_METRIC = 0

    	This enum describes narrow metric style

    .. data:: WIDE_METRIC = 1

    	This enum describes wide metric style

    """

    NARROW_METRIC = Enum.YLeaf(0, "NARROW_METRIC")

    WIDE_METRIC = Enum.YLeaf(1, "WIDE_METRIC")


class MetricType(Enum):
    """
    MetricType (Enum Class)

    This type defines ISIS metric type

    .. data:: INTERNAL = 0

    	This enum describes internal route type

    .. data:: EXTERNAL = 1

    	This enum describes external route type

    """

    INTERNAL = Enum.YLeaf(0, "INTERNAL")

    EXTERNAL = Enum.YLeaf(1, "EXTERNAL")



class OVERLOADRESETTRIGGERTYPE(Identity):
    """
    Base identify type for triggers that reset Overload Bit
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(OVERLOADRESETTRIGGERTYPE, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:OVERLOAD_RESET_TRIGGER_TYPE")


class MTTYPE(Identity):
    """
    Base identify type for multi\-topology
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(MTTYPE, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:MT_TYPE")


class SAFITYPE(Identity):
    """
    Base identify type for SAFI
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(SAFITYPE, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:SAFI_TYPE")


class AFITYPE(Identity):
    """
    Base identify type for AFI
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(AFITYPE, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:AFI_TYPE")


class AFISAFITYPE(Identity):
    """
    Base identify type for AFI/SAFI
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(AFISAFITYPE, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:AFI_SAFI_TYPE")


class WAITFORBGP(Identity):
    """
    Base identity type for resetting Overload Bit when BGP has converged. 
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(WAITFORBGP, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:WAIT_FOR_BGP")


class WAITFORSYSTEM(Identity):
    """
    Base identity type for resetting Overload Bit when system resources have
    been restored. 
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(WAITFORSYSTEM, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:WAIT_FOR_SYSTEM")


class IPV4UNICAST(Identity):
    """
    Base identify type for IPv4 Unicast address family
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV4UNICAST, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:IPV4_UNICAST")


class IPV6MULTICAST(Identity):
    """
    Base identify type for IPv6 multicast address family
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV6MULTICAST, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:IPV6_MULTICAST")


class IPV4MULTICAST(Identity):
    """
    Base identify type for IPv4 multicast address family
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV4MULTICAST, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:IPV4_MULTICAST")


class IPV6UNICAST(Identity):
    """
    Base identify type for IPv6 unicast address family
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV6UNICAST, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:IPV6_UNICAST")


class UNICAST(Identity):
    """
    Base identify type for IPv4 Unicast address family
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(UNICAST, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:UNICAST")


class MULTICAST(Identity):
    """
    Base identify type for IPv6 multicast address family
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(MULTICAST, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:MULTICAST")


class IPV4(Identity):
    """
    Base identify type for IPv4 address family
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV4, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:IPV4")


class IPV6(Identity):
    """
    Base identify type for IPv6 address family
    
    

    """

    _prefix = 'oc-isis-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV6, self).__init__("http://openconfig.net/yang/isis-types", "openconfig-isis-types", "openconfig-isis-types:IPV6")


