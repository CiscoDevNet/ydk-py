""" openconfig_if_ethernet 

Model for managing Ethernet interfaces \-\- augments the IETF YANG
model for interfaces described by RFC 7223

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class EthernetSpeed_Identity(object):
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
        return meta._meta_table['EthernetSpeed_Identity']['meta_info']


class Speed_100Gb_Identity(EthernetSpeed_Identity):
    """
    100 Gbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeed_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_100Gb_Identity']['meta_info']


class Speed_100Mb_Identity(EthernetSpeed_Identity):
    """
    100 Mbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeed_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_100Mb_Identity']['meta_info']


class Speed_10Gb_Identity(EthernetSpeed_Identity):
    """
    10 Gbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeed_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_10Gb_Identity']['meta_info']


class Speed_10Mb_Identity(EthernetSpeed_Identity):
    """
    10 Mbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeed_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_10Mb_Identity']['meta_info']


class Speed_1Gb_Identity(EthernetSpeed_Identity):
    """
    1 Gbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeed_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_1Gb_Identity']['meta_info']


class Speed_25Gb_Identity(EthernetSpeed_Identity):
    """
    25 Gbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeed_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_25Gb_Identity']['meta_info']


class Speed_40Gb_Identity(EthernetSpeed_Identity):
    """
    40 Gbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeed_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_40Gb_Identity']['meta_info']


class Speed_50Gb_Identity(EthernetSpeed_Identity):
    """
    50 Gbps Ethernet
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeed_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_50Gb_Identity']['meta_info']


class Speed_Unknown_Identity(EthernetSpeed_Identity):
    """
    Interface speed is unknown.  Systems may report
    speed UNKNOWN when an interface is down or unpopuplated (e.g.,
    pluggable not present).
    
    

    """

    _prefix = 'eth'
    _revision = '2015-11-20'

    def __init__(self):
        EthernetSpeed_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ethernet as meta
        return meta._meta_table['Speed_Unknown_Identity']['meta_info']


