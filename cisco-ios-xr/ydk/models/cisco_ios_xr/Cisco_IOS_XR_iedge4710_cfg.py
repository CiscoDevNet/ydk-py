""" Cisco_IOS_XR_iedge4710_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR iedge4710 package configuration.

This module contains definitions
for the following management objects\:
  subscriber\-manager\: iEdge subscriber manager configuration
  iedge\-license\-manager\: iedge license manager

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class SubscriberManager(object):
    """
    iEdge subscriber manager configuration
    
    .. attribute:: accounting
    
    	iEdge accounting feature
    	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Accounting>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.accounting = SubscriberManager.Accounting()
        self.accounting.parent = self


    class Accounting(object):
        """
        iEdge accounting feature
        
        .. attribute:: send_stop
        
        	Accounting send stop feature
        	**type**\:   :py:class:`SendStop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Accounting.SendStop>`
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.send_stop = SubscriberManager.Accounting.SendStop()
            self.send_stop.parent = self


        class SendStop(object):
            """
            Accounting send stop feature
            
            .. attribute:: setup_failure
            
            	Set up failure feature
            	**type**\:  str
            
            

            """

            _prefix = 'iedge4710-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.setup_failure = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/Cisco-IOS-XR-iedge4710-cfg:accounting/Cisco-IOS-XR-iedge4710-cfg:send-stop'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.setup_failure is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
                return meta._meta_table['SubscriberManager.Accounting.SendStop']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/Cisco-IOS-XR-iedge4710-cfg:accounting'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.send_stop is not None and self.send_stop._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
            return meta._meta_table['SubscriberManager.Accounting']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-iedge4710-cfg:subscriber-manager'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.accounting is not None and self.accounting._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
        return meta._meta_table['SubscriberManager']['meta_info']


class IedgeLicenseManager(object):
    """
    iedge license manager
    
    .. attribute:: node
    
    	Location. For eg., 0/1/CPU0
    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.IedgeLicenseManager.Node>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.node = YList()
        self.node.parent = self
        self.node.name = 'node'


    class Node(object):
        """
        Location. For eg., 0/1/CPU0
        
        .. attribute:: node_name  <key>
        
        	The node id to filter on. For eg., 0/1/CPU0
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: session_limit
        
        	Session limit configured on linecard
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: session_threshold
        
        	Session threshold configured on linecard
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node_name = None
            self.session_limit = None
            self.session_threshold = None

        @property
        def _common_path(self):
            if self.node_name is None:
                raise YPYModelError('Key property node_name is None')

            return '/Cisco-IOS-XR-iedge4710-cfg:iedge-license-manager/Cisco-IOS-XR-iedge4710-cfg:node[Cisco-IOS-XR-iedge4710-cfg:node-name = ' + str(self.node_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.node_name is not None:
                return True

            if self.session_limit is not None:
                return True

            if self.session_threshold is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
            return meta._meta_table['IedgeLicenseManager.Node']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-iedge4710-cfg:iedge-license-manager'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.node is not None:
            for child_ref in self.node:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
        return meta._meta_table['IedgeLicenseManager']['meta_info']


