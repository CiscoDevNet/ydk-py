""" cisco_routing_ext 

This YANG module is an extention to 'ietf\-routing'
module and describes addtional operational
data for route list

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_routing import RoutingProtocolIdentity


class RipIdentity(RoutingProtocolIdentity):
    """
    RIP.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self):
        RoutingProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_routing_ext as meta
        return meta._meta_table['RipIdentity']['meta_info']


class BgpIdentity(RoutingProtocolIdentity):
    """
    BGP.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self):
        RoutingProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_routing_ext as meta
        return meta._meta_table['BgpIdentity']['meta_info']


class IsIsIdentity(RoutingProtocolIdentity):
    """
    IS\-IS.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self):
        RoutingProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_routing_ext as meta
        return meta._meta_table['IsIsIdentity']['meta_info']


class EigrpIdentity(RoutingProtocolIdentity):
    """
    Eigrp.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self):
        RoutingProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_routing_ext as meta
        return meta._meta_table['EigrpIdentity']['meta_info']


class MobileIdentity(RoutingProtocolIdentity):
    """
    Mobile.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self):
        RoutingProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_routing_ext as meta
        return meta._meta_table['MobileIdentity']['meta_info']


