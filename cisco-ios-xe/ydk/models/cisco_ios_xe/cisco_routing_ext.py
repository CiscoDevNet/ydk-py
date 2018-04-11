""" cisco_routing_ext 

This YANG module is an extention to 'ietf\-routing'
module and describes addtional operational
data for route list

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Rip(Identity):
    """
    RIP.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self):
        super(Rip, self).__init__("urn:cisco:params:xml:ns:yang:cisco-routing-ext", "cisco-routing-ext", "cisco-routing-ext:rip")


class IsIs(Identity):
    """
    IS\-IS.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self):
        super(IsIs, self).__init__("urn:cisco:params:xml:ns:yang:cisco-routing-ext", "cisco-routing-ext", "cisco-routing-ext:is-is")


class Bgp(Identity):
    """
    BGP.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self):
        super(Bgp, self).__init__("urn:cisco:params:xml:ns:yang:cisco-routing-ext", "cisco-routing-ext", "cisco-routing-ext:bgp")


class Eigrp(Identity):
    """
    Eigrp.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self):
        super(Eigrp, self).__init__("urn:cisco:params:xml:ns:yang:cisco-routing-ext", "cisco-routing-ext", "cisco-routing-ext:eigrp")


class Mobile(Identity):
    """
    Mobile.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self):
        super(Mobile, self).__init__("urn:cisco:params:xml:ns:yang:cisco-routing-ext", "cisco-routing-ext", "cisco-routing-ext:mobile")


