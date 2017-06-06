""" cisco_ethernet 

This module contains a collection of YANG definitions for
configuring Ethernet Interfaces.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class EthIfSpeedIdentity(object):
    """
    Representing the speed of the ethernet interface
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ethernet as meta
        return meta._meta_table['EthIfSpeedIdentity']['meta_info']


class EthIfSpeed10GbIdentity(EthIfSpeedIdentity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        EthIfSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ethernet as meta
        return meta._meta_table['EthIfSpeed10GbIdentity']['meta_info']


class EthIfSpeed100GbIdentity(EthIfSpeedIdentity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        EthIfSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ethernet as meta
        return meta._meta_table['EthIfSpeed100GbIdentity']['meta_info']


class EthIfSpeed10MbIdentity(EthIfSpeedIdentity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        EthIfSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ethernet as meta
        return meta._meta_table['EthIfSpeed10MbIdentity']['meta_info']


class EthIfSpeed100MbIdentity(EthIfSpeedIdentity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        EthIfSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ethernet as meta
        return meta._meta_table['EthIfSpeed100MbIdentity']['meta_info']


class EthIfSpeed40GbIdentity(EthIfSpeedIdentity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        EthIfSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ethernet as meta
        return meta._meta_table['EthIfSpeed40GbIdentity']['meta_info']


class EthIfSpeed1GbIdentity(EthIfSpeedIdentity):
    """
    
    
    

    """

    _prefix = 'eth'
    _revision = '2016-05-10'

    def __init__(self):
        EthIfSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ethernet as meta
        return meta._meta_table['EthIfSpeed1GbIdentity']['meta_info']


