""" cisco_storm_control 

This module defines data model for strom control feature.

Traffic storm occurs when packets flood a bridge, creating
excessive traffic and degrading network performance. Traffic
storm control prevents bridge disruption by suppressing traffic
when the number of packets reaches configured threshold
levels.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class StormControlActionIdentity(object):
    """
    Actions to be taken once storm control limit threshold is
    exceeded for a traffic class.
    
    

    """

    _prefix = 'cisco-stormctrl'
    _revision = '2016-12-14'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_storm_control as meta
        return meta._meta_table['StormControlActionIdentity']['meta_info']


class ActionShutdownIdentity(StormControlActionIdentity):
    """
    Shutdown service.
    
    

    """

    _prefix = 'cisco-stormctrl'
    _revision = '2016-12-14'

    def __init__(self):
        StormControlActionIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_storm_control as meta
        return meta._meta_table['ActionShutdownIdentity']['meta_info']


class ActionDropIdentity(StormControlActionIdentity):
    """
    Drop packets.
    
    

    """

    _prefix = 'cisco-stormctrl'
    _revision = '2016-12-14'

    def __init__(self):
        StormControlActionIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_storm_control as meta
        return meta._meta_table['ActionDropIdentity']['meta_info']


class ActionSnmpTrapIdentity(StormControlActionIdentity):
    """
    Generate SNMP traps.
    
    

    """

    _prefix = 'cisco-stormctrl'
    _revision = '2016-12-14'

    def __init__(self):
        StormControlActionIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_storm_control as meta
        return meta._meta_table['ActionSnmpTrapIdentity']['meta_info']


