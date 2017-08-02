""" openconfig_if_ethernet 

Model for managing Ethernet interfaces \-\- augments the IETF YANG
model for interfaces described by RFC 7223

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ethernet_Speed(Identity):
    """
    base type to specify available Ethernet link
    speeds
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(Ethernet_Speed, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:ETHERNET_SPEED")


class Speed_40Gb(Identity):
    """
    40 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(Speed_40Gb, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_40GB")


class Speed_25Gb(Identity):
    """
    25 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(Speed_25Gb, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_25GB")


class Speed_Unknown(Identity):
    """
    Interface speed is unknown.  Systems may report
    speed UNKNOWN when an interface is down or unpopuplated (e.g.,
    pluggable not present).
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(Speed_Unknown, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_UNKNOWN")


class Speed_100Gb(Identity):
    """
    100 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(Speed_100Gb, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_100GB")


class Speed_1Gb(Identity):
    """
    1 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(Speed_1Gb, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_1GB")


class Speed_50Gb(Identity):
    """
    50 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(Speed_50Gb, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_50GB")


class Speed_10Gb(Identity):
    """
    10 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(Speed_10Gb, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_10GB")


class Speed_10Mb(Identity):
    """
    10 Mbps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(Speed_10Mb, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_10MB")


class Speed_100Mb(Identity):
    """
    100 Mbps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(Speed_100Mb, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_100MB")


