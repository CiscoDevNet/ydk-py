""" Cisco_IOS_XR_ipv6_io_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-io package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-pmtu\-time\-out\: Configure IPv6 Path MTU timeout value in
    minutes
  ipv6\-source\-route\: TRUE if enabled, FALSE if disabled
  ipv6\-assembler\: ipv6 assembler
  ipv6\-pmtu\-enable\: TRUE if enabled, FALSE if disabled
  ipv6\-hop\-limit\: Specify hop limit
  ipv6icmp\: ipv6icmp

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class Ipv6Assembler(object):
    """
    ipv6 assembler
    
    .. attribute:: timeout
    
    	Number of seconds an assembly queue will hold before timeout
    	**type**\: int
    
    	**range:** 1..120
    
    .. attribute:: max_packets
    
    	Maxinum packets allowed in assembly queues (in percent)
    	**type**\: int
    
    	**range:** 1..50
    
    

    """

    _prefix = 'ipv6-io-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.timeout = None
        self.max_packets = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-io-cfg:ipv6-assembler'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.timeout is not None:
            return True

        if self.max_packets is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_io_cfg as meta
        return meta._meta_table['Ipv6Assembler']['meta_info']


class Ipv6Icmp(object):
    """
    ipv6icmp
    
    .. attribute:: error_interval
    
    	Interval between tokens in milliseconds
    	**type**\: int
    
    	**range:** 0..2147483647
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    .. attribute:: bucket_size
    
    	Bucket size
    	**type**\: int
    
    	**range:** 1..200
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv6-io-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.error_interval = None
        self.bucket_size = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-io-cfg:ipv6icmp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.error_interval is not None:
            return True

        if self.bucket_size is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_io_cfg as meta
        return meta._meta_table['Ipv6Icmp']['meta_info']


