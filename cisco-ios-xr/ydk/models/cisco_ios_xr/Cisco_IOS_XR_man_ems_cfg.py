""" Cisco_IOS_XR_man_ems_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-ems package configuration.

This module contains definitions
for the following management objects\:
  grpc\: GRPC configruation

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Grpc(object):
    """
    GRPC configruation
    
    .. attribute:: address_family
    
    	Address family identifier type
    	**type**\:  str
    
    .. attribute:: enable
    
    	Enable GRPC
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: max_request_per_user
    
    	Maximum concurrent requests per user
    	**type**\:  int
    
    	**range:** 1..32
    
    .. attribute:: max_request_total
    
    	Maximum concurrent requests in total
    	**type**\:  int
    
    	**range:** 1..256
    
    .. attribute:: port
    
    	Server listening port
    	**type**\:  int
    
    	**range:** 10000..57999
    
    .. attribute:: tls
    
    	Transport Layer Security (TLS)
    	**type**\:   :py:class:`Tls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg.Grpc.Tls>`
    
    

    """

    _prefix = 'man-ems-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.address_family = None
        self.enable = None
        self.max_request_per_user = None
        self.max_request_total = None
        self.port = None
        self.tls = Grpc.Tls()
        self.tls.parent = self


    class Tls(object):
        """
        Transport Layer Security (TLS)
        
        .. attribute:: enable
        
        	Enable TLS
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: trustpoint
        
        	Trustpoint Name
        	**type**\:  str
        
        

        """

        _prefix = 'man-ems-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.enable = None
            self.trustpoint = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-man-ems-cfg:grpc/Cisco-IOS-XR-man-ems-cfg:tls'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.enable is not None:
                return True

            if self.trustpoint is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_ems_cfg as meta
            return meta._meta_table['Grpc.Tls']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-man-ems-cfg:grpc'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.address_family is not None:
            return True

        if self.enable is not None:
            return True

        if self.max_request_per_user is not None:
            return True

        if self.max_request_total is not None:
            return True

        if self.port is not None:
            return True

        if self.tls is not None and self.tls._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_ems_cfg as meta
        return meta._meta_table['Grpc']['meta_info']


