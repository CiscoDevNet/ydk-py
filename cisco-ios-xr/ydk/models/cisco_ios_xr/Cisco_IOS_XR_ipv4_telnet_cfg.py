""" Cisco_IOS_XR_ipv4_telnet_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-telnet package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-telnet\: IPv6 telnet configuration
  ipv4\-telnet\: ipv4 telnet

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Ipv6Telnet(object):
    """
    IPv6 telnet configuration
    
    .. attribute:: client
    
    	Telnet client configuration
    	**type**\:   :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_cfg.Ipv6Telnet.Client>`
    
    

    """

    _prefix = 'ipv4-telnet-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.client = Ipv6Telnet.Client()
        self.client.parent = self


    class Client(object):
        """
        Telnet client configuration
        
        .. attribute:: source_interface
        
        	Source interface for telnet sessions
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        

        """

        _prefix = 'ipv4-telnet-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.source_interface = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-telnet-cfg:ipv6-telnet/Cisco-IOS-XR-ipv4-telnet-cfg:client'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.source_interface is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_telnet_cfg as meta
            return meta._meta_table['Ipv6Telnet.Client']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-telnet-cfg:ipv6-telnet'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.client is not None and self.client._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_telnet_cfg as meta
        return meta._meta_table['Ipv6Telnet']['meta_info']


class Ipv4Telnet(object):
    """
    ipv4 telnet
    
    .. attribute:: client
    
    	Telnet client configuration
    	**type**\:   :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_cfg.Ipv4Telnet.Client>`
    
    

    """

    _prefix = 'ipv4-telnet-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.client = Ipv4Telnet.Client()
        self.client.parent = self


    class Client(object):
        """
        Telnet client configuration
        
        .. attribute:: source_interface
        
        	Source interface for telnet sessions
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        

        """

        _prefix = 'ipv4-telnet-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.source_interface = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-telnet-cfg:ipv4-telnet/Cisco-IOS-XR-ipv4-telnet-cfg:client'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.source_interface is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_telnet_cfg as meta
            return meta._meta_table['Ipv4Telnet.Client']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-telnet-cfg:ipv4-telnet'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.client is not None and self.client._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_telnet_cfg as meta
        return meta._meta_table['Ipv4Telnet']['meta_info']


