""" Cisco_IOS_XR_ipv6_io_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-io package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-configuration\: IPv6 Configuration Data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Ipv6Configuration(object):
    """
    IPv6 Configuration Data
    
    .. attribute:: ipv6_assembler
    
    	IPv6 fragmented packet assembler
    	**type**\:   :py:class:`Ipv6Assembler <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg.Ipv6Configuration.Ipv6Assembler>`
    
    .. attribute:: ipv6_hop_limit
    
    	Configure IPv6 hop count limit
    	**type**\:  int
    
    	**range:** 1..255
    
    .. attribute:: ipv6_pmtu_enable
    
    	TRUE if enabled, FALSE if disabled
    	**type**\:  bool
    
    	**default value**\: false
    
    .. attribute:: ipv6_pmtu_time_out
    
    	Configure IPv6 Path MTU timeout value in minutes
    	**type**\:  int
    
    	**range:** 1..15
    
    	**units**\: minute
    
    .. attribute:: ipv6_source_route
    
    	TRUE if enabled, FALSE if disabled
    	**type**\:  bool
    
    	**default value**\: true
    
    .. attribute:: ipv6icmp
    
    	Configure IPv6 ICMP parameters
    	**type**\:   :py:class:`Ipv6Icmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg.Ipv6Configuration.Ipv6Icmp>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ipv6-io-cfg'
    _revision = '2016-05-10'

    def __init__(self):
        self.ipv6_assembler = Ipv6Configuration.Ipv6Assembler()
        self.ipv6_assembler.parent = self
        self.ipv6_hop_limit = None
        self.ipv6_pmtu_enable = None
        self.ipv6_pmtu_time_out = None
        self.ipv6_source_route = None
        self.ipv6icmp = None


    class Ipv6Assembler(object):
        """
        IPv6 fragmented packet assembler
        
        .. attribute:: max_packets
        
        	Maxinum packets allowed in assembly queues (in percent)
        	**type**\:  int
        
        	**range:** 1..50
        
        	**units**\: percentage
        
        .. attribute:: timeout
        
        	Number of seconds an assembly queue will hold before timeout
        	**type**\:  int
        
        	**range:** 1..120
        
        	**units**\: second
        
        

        """

        _prefix = 'ipv6-io-cfg'
        _revision = '2016-05-10'

        def __init__(self):
            self.parent = None
            self.max_packets = None
            self.timeout = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-io-cfg:ipv6-configuration/Cisco-IOS-XR-ipv6-io-cfg:ipv6-assembler'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.max_packets is not None:
                return True

            if self.timeout is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_io_cfg as meta
            return meta._meta_table['Ipv6Configuration.Ipv6Assembler']['meta_info']


    class Ipv6Icmp(object):
        """
        Configure IPv6 ICMP parameters
        
        .. attribute:: bucket_size
        
        	Bucket size
        	**type**\:  int
        
        	**range:** 1..200
        
        	**default value**\: 10
        
        .. attribute:: error_interval
        
        	Interval between tokens in milliseconds
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**mandatory**\: True
        
        	**units**\: millisecond
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv6-io-cfg'
        _revision = '2016-05-10'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.bucket_size = None
            self.error_interval = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-io-cfg:ipv6-configuration/Cisco-IOS-XR-ipv6-io-cfg:ipv6icmp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.bucket_size is not None:
                return True

            if self.error_interval is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_io_cfg as meta
            return meta._meta_table['Ipv6Configuration.Ipv6Icmp']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-io-cfg:ipv6-configuration'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.ipv6_assembler is not None and self.ipv6_assembler._has_data():
            return True

        if self.ipv6_hop_limit is not None:
            return True

        if self.ipv6_pmtu_enable is not None:
            return True

        if self.ipv6_pmtu_time_out is not None:
            return True

        if self.ipv6_source_route is not None:
            return True

        if self.ipv6icmp is not None and self.ipv6icmp._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_io_cfg as meta
        return meta._meta_table['Ipv6Configuration']['meta_info']


