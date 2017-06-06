""" Cisco_IOS_XR_syslog_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

This module contains definitions
for the following management objects\:
syslog\: Global Syslog messaging data

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class LogmsgRpc(object):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syslog_act.LogmsgRpc.Input>`
    
    

    """

    _prefix = 'syslog-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = LogmsgRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: message
        
        	Message body
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: severity
        
        	Set serverity level
        	**type**\:   :py:class:`SeverityEnum <ydk.models.ietf.ietf_syslog_types.SeverityEnum>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'syslog-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.message = None
            self.severity = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-syslog-act:logmsg/Cisco-IOS-XR-syslog-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.message is not None:
                return True

            if self.severity is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_syslog_act as meta
            return meta._meta_table['LogmsgRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-syslog-act:logmsg'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_syslog_act as meta
        return meta._meta_table['LogmsgRpc']['meta_info']


