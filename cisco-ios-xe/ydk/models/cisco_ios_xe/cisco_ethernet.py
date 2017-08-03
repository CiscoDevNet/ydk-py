""" cisco_ethernet 

This module contains a collection of YANG definitions for
configuring Ethernet Interfaces.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EthIfSpeed(Identity):
    """
    Representing the speed of the ethernet interface
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed")


class EthIfSpeed100Mb(Identity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed100Mb, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed-100mb")


class EthIfSpeed10Mb(Identity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed10Mb, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed-10mb")


class EthIfSpeed100Gb(Identity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed100Gb, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed-100gb")


class EthIfSpeed40Gb(Identity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed40Gb, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed-40gb")


class EthIfSpeed10Gb(Identity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed10Gb, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed-10gb")


class EthIfSpeed1Gb(Identity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        super(EthIfSpeed1Gb, self).__init__("urn:cisco:params:xml:ns:yang:cisco-ethernet", "cisco-ethernet", "cisco-ethernet:eth-if-speed-1gb")


