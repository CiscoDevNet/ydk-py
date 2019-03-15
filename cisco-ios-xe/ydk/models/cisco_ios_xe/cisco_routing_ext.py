""" cisco_routing_ext 

This YANG module is an extention to 'ietf\-routing'
module and describes addtional operational
data for route list.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.ietf.ietf_routing import RoutingProtocol



class Igrp(RoutingProtocol):
    """
    IGRP
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-routing-ext", pref="cisco-routing-ext", tag="cisco-routing-ext:igrp"):
        super(Igrp, self).__init__(ns, pref, tag)



class Nhrp(RoutingProtocol):
    """
    NHRP
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-routing-ext", pref="cisco-routing-ext", tag="cisco-routing-ext:nhrp"):
        super(Nhrp, self).__init__(ns, pref, tag)



class Hsrp(RoutingProtocol):
    """
    HSRP
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-routing-ext", pref="cisco-routing-ext", tag="cisco-routing-ext:hsrp"):
        super(Hsrp, self).__init__(ns, pref, tag)



class Rip(RoutingProtocol):
    """
    RIP.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-routing-ext", pref="cisco-routing-ext", tag="cisco-routing-ext:rip"):
        super(Rip, self).__init__(ns, pref, tag)



class Bgp(RoutingProtocol):
    """
    BGP.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-routing-ext", pref="cisco-routing-ext", tag="cisco-routing-ext:bgp"):
        super(Bgp, self).__init__(ns, pref, tag)



class Lisp(RoutingProtocol):
    """
    LISP
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-routing-ext", pref="cisco-routing-ext", tag="cisco-routing-ext:lisp"):
        super(Lisp, self).__init__(ns, pref, tag)



class Eigrp(RoutingProtocol):
    """
    Eigrp.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-routing-ext", pref="cisco-routing-ext", tag="cisco-routing-ext:eigrp"):
        super(Eigrp, self).__init__(ns, pref, tag)



class IsIs(RoutingProtocol):
    """
    IS\-IS.
    
    

    """

    _prefix = 'rt-ext'
    _revision = '2016-07-09'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-routing-ext", pref="cisco-routing-ext", tag="cisco-routing-ext:is-is"):
        super(IsIs, self).__init__(ns, pref, tag)



