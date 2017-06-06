""" openconfig_if_ethernet 

Model for managing Ethernet interfaces \-\- augments the IETF YANG
model for interfaces described by RFC 7223

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class EthernetSpeedIdentity(object):
    """
    base type to specify available Ethernet link
    speeds
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['EthernetSpeedIdentity']['meta_info']


class Speed_40GbIdentity(EthernetSpeedIdentity):
    """
    40 Gbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_40GbIdentity']['meta_info']


class Speed_10MbIdentity(EthernetSpeedIdentity):
    """
    10 Mbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_10MbIdentity']['meta_info']


class Speed_25GbIdentity(EthernetSpeedIdentity):
    """
    25 Gbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_25GbIdentity']['meta_info']


class Speed_1GbIdentity(EthernetSpeedIdentity):
    """
    1 Gbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_1GbIdentity']['meta_info']


class Speed_UnknownIdentity(EthernetSpeedIdentity):
    """
    Interface speed is unknown.  Systems may report
    speed UNKNOWN when an interface is down or unpopuplated (e.g.,
    pluggable not present).
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_UnknownIdentity']['meta_info']


class Speed_10GbIdentity(EthernetSpeedIdentity):
    """
    10 Gbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_10GbIdentity']['meta_info']


class Speed_100GbIdentity(EthernetSpeedIdentity):
    """
    100 Gbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_100GbIdentity']['meta_info']


class Speed_100MbIdentity(EthernetSpeedIdentity):
    """
    100 Mbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_100MbIdentity']['meta_info']


class Speed_50GbIdentity(EthernetSpeedIdentity):
    """
    50 Gbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_50GbIdentity']['meta_info']


