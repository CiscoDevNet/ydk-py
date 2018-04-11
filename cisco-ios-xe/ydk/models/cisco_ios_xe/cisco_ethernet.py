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

    def __init__(self):
        super(EthIfSpeed, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed")


class EthIfSpeed10mb(Identity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed10mb, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed-10mb")


class EthIfSpeed100mb(Identity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed100mb, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed-100mb")


class EthIfSpeed1gb(Identity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed1gb, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed-1gb")


class EthIfSpeed10gb(Identity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed10gb, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed-10gb")


class EthIfSpeed40gb(Identity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed40gb, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed-40gb")


class EthIfSpeed100gb(Identity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed100gb, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed-100gb")


