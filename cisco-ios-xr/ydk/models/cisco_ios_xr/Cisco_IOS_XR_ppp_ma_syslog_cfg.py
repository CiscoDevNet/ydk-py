""" Cisco_IOS_XR_ppp_ma_syslog_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ma\-syslog package configuration.

This module contains definitions
for the following management objects\:
  ppp\: PPP configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Ppp(object):
    """
    PPP configuration
    
    .. attribute:: syslog
    
    	syslog option for session status
    	**type**\:   :py:class:`Syslog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_syslog_cfg.Ppp.Syslog>`
    
    

    """

    _prefix = 'ppp-ma-syslog-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.syslog = Ppp.Syslog()
        self.syslog.parent = self


    class Syslog(object):
        """
        syslog option for session status
        
        .. attribute:: enable_session_status
        
        	Enable syslog for ppp session status
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ppp-ma-syslog-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.enable_session_status = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ppp-ma-syslog-cfg:ppp/Cisco-IOS-XR-ppp-ma-syslog-cfg:syslog'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.enable_session_status is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_syslog_cfg as meta
            return meta._meta_table['Ppp.Syslog']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ppp-ma-syslog-cfg:ppp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.syslog is not None and self.syslog._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_syslog_cfg as meta
        return meta._meta_table['Ppp']['meta_info']


