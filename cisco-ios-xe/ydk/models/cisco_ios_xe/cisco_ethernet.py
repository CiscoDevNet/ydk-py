""" cisco_ethernet 

This module contains a collection of YANG definitions for
configuring Ethernet Interfaces.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class EthIfSpeed(Identity):
    """
    Representing the speed of the ethernet interface
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-ethernet", pref="cisco-ethernet", tag="cisco-ethernet:eth-if-speed"):
        super(EthIfSpeed, self).__init__(ns, pref, tag)


class EthIfSpeed1gb(EthIfSpeed):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-ethernet", pref="cisco-ethernet", tag="cisco-ethernet:eth-if-speed-1gb"):
        super(EthIfSpeed1gb, self).__init__(ns, pref, tag)


class EthIfSpeed40gb(EthIfSpeed):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-ethernet", pref="cisco-ethernet", tag="cisco-ethernet:eth-if-speed-40gb"):
        super(EthIfSpeed40gb, self).__init__(ns, pref, tag)


class EthIfSpeed10mb(EthIfSpeed):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-ethernet", pref="cisco-ethernet", tag="cisco-ethernet:eth-if-speed-10mb"):
        super(EthIfSpeed10mb, self).__init__(ns, pref, tag)


class EthIfSpeed10gb(EthIfSpeed):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-ethernet", pref="cisco-ethernet", tag="cisco-ethernet:eth-if-speed-10gb"):
        super(EthIfSpeed10gb, self).__init__(ns, pref, tag)


class EthIfSpeed100gb(EthIfSpeed):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-ethernet", pref="cisco-ethernet", tag="cisco-ethernet:eth-if-speed-100gb"):
        super(EthIfSpeed100gb, self).__init__(ns, pref, tag)


class EthIfSpeed100mb(EthIfSpeed):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-ethernet", pref="cisco-ethernet", tag="cisco-ethernet:eth-if-speed-100mb"):
        super(EthIfSpeed100mb, self).__init__(ns, pref, tag)


