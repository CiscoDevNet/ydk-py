""" Cisco_IOS_XR_man_netconf_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-netconf package configuration.

This module contains definitions
for the following management objects\:
  netconf\-yang\: NETCONF YANG configuration commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class NetconfYang(object):
    """
    NETCONF YANG configuration commands
    
    .. attribute:: agent
    
    	NETCONF YANG agent configuration commands
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg.NetconfYang.Agent>`
    
    

    """

    _prefix = 'man-netconf-cfg'
    _revision = '2016-03-15'

    def __init__(self):
        self.agent = NetconfYang.Agent()
        self.agent.parent = self


    class Agent(object):
        """
        NETCONF YANG agent configuration commands
        
        .. attribute:: rate_limit
        
        	Number of bytes to process per sec
        	**type**\:  int
        
        	**range:** 4096..4294967295
        
        	**units**\: byte
        
        .. attribute:: session
        
        	Session settings
        	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg.NetconfYang.Agent.Session>`
        
        .. attribute:: ssh
        
        	NETCONF YANG agent over SSH connection
        	**type**\:   :py:class:`Ssh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg.NetconfYang.Agent.Ssh>`
        
        

        """

        _prefix = 'man-netconf-cfg'
        _revision = '2016-03-15'

        def __init__(self):
            self.parent = None
            self.rate_limit = None
            self.session = NetconfYang.Agent.Session()
            self.session.parent = self
            self.ssh = NetconfYang.Agent.Ssh()
            self.ssh.parent = self


        class Ssh(object):
            """
            NETCONF YANG agent over SSH connection
            
            .. attribute:: enable
            
            	Enable NETCONF YANG agent over SSH connection
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'man-netconf-cfg'
            _revision = '2016-03-15'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-man-netconf-cfg:netconf-yang/Cisco-IOS-XR-man-netconf-cfg:agent/Cisco-IOS-XR-man-netconf-cfg:ssh'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_netconf_cfg as meta
                return meta._meta_table['NetconfYang.Agent.Ssh']['meta_info']


        class Session(object):
            """
            Session settings
            
            .. attribute:: absolute_timeout
            
            	Absolute timeout in minutes
            	**type**\:  int
            
            	**range:** 1..1440
            
            	**units**\: minute
            
            .. attribute:: idle_timeout
            
            	Non\-active session lifetime
            	**type**\:  int
            
            	**range:** 1..1440
            
            	**units**\: minute
            
            .. attribute:: limit
            
            	Count of allowable concurrent netconf\-yang sessions
            	**type**\:  int
            
            	**range:** 1..50
            
            	**default value**\: 50
            
            

            """

            _prefix = 'man-netconf-cfg'
            _revision = '2016-03-15'

            def __init__(self):
                self.parent = None
                self.absolute_timeout = None
                self.idle_timeout = None
                self.limit = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-man-netconf-cfg:netconf-yang/Cisco-IOS-XR-man-netconf-cfg:agent/Cisco-IOS-XR-man-netconf-cfg:session'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.absolute_timeout is not None:
                    return True

                if self.idle_timeout is not None:
                    return True

                if self.limit is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_netconf_cfg as meta
                return meta._meta_table['NetconfYang.Agent.Session']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-man-netconf-cfg:netconf-yang/Cisco-IOS-XR-man-netconf-cfg:agent'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.rate_limit is not None:
                return True

            if self.session is not None and self.session._has_data():
                return True

            if self.ssh is not None and self.ssh._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_netconf_cfg as meta
            return meta._meta_table['NetconfYang.Agent']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-man-netconf-cfg:netconf-yang'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.agent is not None and self.agent._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_netconf_cfg as meta
        return meta._meta_table['NetconfYang']['meta_info']


