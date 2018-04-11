""" openconfig_if_ethernet 

Model for managing Ethernet interfaces \-\- augments the IETF YANG
model for interfaces described by RFC 7223

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ETHERNETSPEED(Identity):
    """
    base type to specify available Ethernet link
    speeds
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(ETHERNETSPEED, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:ETHERNET_SPEED")


class SPEED10MB(Identity):
    """
    10 Mbps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(SPEED10MB, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_10MB")


class SPEED100MB(Identity):
    """
    100 Mbps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(SPEED100MB, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_100MB")


class SPEED1GB(Identity):
    """
    1 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(SPEED1GB, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_1GB")


class SPEED10GB(Identity):
    """
    10 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(SPEED10GB, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_10GB")


class SPEED25GB(Identity):
    """
    25 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(SPEED25GB, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_25GB")


class SPEED40GB(Identity):
    """
    40 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(SPEED40GB, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_40GB")


class SPEED50GB(Identity):
    """
    50 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(SPEED50GB, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_50GB")


class SPEED100GB(Identity):
    """
    100 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(SPEED100GB, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_100GB")


class SPEEDUNKNOWN(Identity):
    """
    Interface speed is unknown.  Systems may report
    speed UNKNOWN when an interface is down or unpopuplated (e.g.,
    pluggable not present).
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self):
        super(SPEEDUNKNOWN, self).__init__("http://openconfig.net/yang/interfaces/ethernet", "openconfig-if-ethernet", "openconfig-if-ethernet:SPEED_UNKNOWN")


