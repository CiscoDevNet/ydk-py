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

    def __init__(self, ns="http://openconfig.net/yang/interfaces/ethernet", pref="openconfig-if-ethernet", tag="openconfig-if-ethernet:ETHERNET_SPEED"):
        super(ETHERNETSPEED, self).__init__(ns, pref, tag)


class SPEED100GB(ETHERNETSPEED):
    """
    100 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self, ns="http://openconfig.net/yang/interfaces/ethernet", pref="openconfig-if-ethernet", tag="openconfig-if-ethernet:SPEED_100GB"):
        super(SPEED100GB, self).__init__(ns, pref, tag)


class SPEED1GB(ETHERNETSPEED):
    """
    1 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self, ns="http://openconfig.net/yang/interfaces/ethernet", pref="openconfig-if-ethernet", tag="openconfig-if-ethernet:SPEED_1GB"):
        super(SPEED1GB, self).__init__(ns, pref, tag)


class SPEED25GB(ETHERNETSPEED):
    """
    25 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self, ns="http://openconfig.net/yang/interfaces/ethernet", pref="openconfig-if-ethernet", tag="openconfig-if-ethernet:SPEED_25GB"):
        super(SPEED25GB, self).__init__(ns, pref, tag)


class SPEED10GB(ETHERNETSPEED):
    """
    10 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self, ns="http://openconfig.net/yang/interfaces/ethernet", pref="openconfig-if-ethernet", tag="openconfig-if-ethernet:SPEED_10GB"):
        super(SPEED10GB, self).__init__(ns, pref, tag)


class SPEED10MB(ETHERNETSPEED):
    """
    10 Mbps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self, ns="http://openconfig.net/yang/interfaces/ethernet", pref="openconfig-if-ethernet", tag="openconfig-if-ethernet:SPEED_10MB"):
        super(SPEED10MB, self).__init__(ns, pref, tag)


class SPEED40GB(ETHERNETSPEED):
    """
    40 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self, ns="http://openconfig.net/yang/interfaces/ethernet", pref="openconfig-if-ethernet", tag="openconfig-if-ethernet:SPEED_40GB"):
        super(SPEED40GB, self).__init__(ns, pref, tag)


class SPEEDUNKNOWN(ETHERNETSPEED):
    """
    Interface speed is unknown.  Systems may report
    speed UNKNOWN when an interface is down or unpopuplated (e.g.,
    pluggable not present).
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self, ns="http://openconfig.net/yang/interfaces/ethernet", pref="openconfig-if-ethernet", tag="openconfig-if-ethernet:SPEED_UNKNOWN"):
        super(SPEEDUNKNOWN, self).__init__(ns, pref, tag)


class SPEED50GB(ETHERNETSPEED):
    """
    50 GBps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self, ns="http://openconfig.net/yang/interfaces/ethernet", pref="openconfig-if-ethernet", tag="openconfig-if-ethernet:SPEED_50GB"):
        super(SPEED50GB, self).__init__(ns, pref, tag)


class SPEED100MB(ETHERNETSPEED):
    """
    100 Mbps Ethernet
    
    

    """

    _prefix = 'oc-eth'
    _revision = '2016-05-26'

    def __init__(self, ns="http://openconfig.net/yang/interfaces/ethernet", pref="openconfig-if-ethernet", tag="openconfig-if-ethernet:SPEED_100MB"):
        super(SPEED100MB, self).__init__(ns, pref, tag)


